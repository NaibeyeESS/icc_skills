#!/usr/bin/env python3
"""
budget.py — Consolidation d'un budget prévisionnel ICC à partir d'un CSV.

Usage :
    python3 -I budget.py projet/budget/budget.csv
    python3 -I budget.py projet/budget/budget.csv --eur 655.957 --usd 600
    python3 -I budget.py projet/budget/budget.csv --plafond "Frais administratifs=7" --plafond "Imprévus=10"
    python3 -I budget.py projet/budget/budget.csv --total-attendu 16400000

Format du CSV attendu (séparateur « , » ou « ; », en-tête obligatoire, encodage UTF-8) :
    code,rubrique,designation,unite,quantite,cout_unitaire_fcfa,source,statut,eligible,justificatif

    - code                 : identifiant de la ligne (ex. RH-01). Libre.
    - rubrique             : grande rubrique (ex. Ressources humaines). Sert aux sous-totaux.
    - designation          : libellé de la dépense.
    - unite                : jour, forfait, mois, unité, km…
    - quantite             : nombre (décimales avec « . » ou « , »).
    - cout_unitaire_fcfa   : coût unitaire en FCFA.
    - source               : source de financement (ex. OIF, Apport propre, Valorisation).
                             Vide = ligne non financée (signalée).
    - statut               : acquis | demandé | à chercher (libre, utilisé tel quel).
    - eligible             : oui | non | à vérifier (pour le bailleur principal).
    - justificatif         : pièce attendue (facture, contrat, fiche de paie…).

    Une colonne facultative « total_fcfa » est acceptée : si elle est présente et non vide,
    elle est utilisée telle quelle (sinon total = quantite x cout_unitaire_fcfa).

Sortie : rapport Markdown sur la sortie standard. Bibliothèque standard uniquement.
"""

import argparse
import csv
import sys
from collections import OrderedDict

TAUX_EUR_DEFAUT = 655.957  # parité fixe FCFA (XAF/XOF) / EUR


def nombre(valeur, defaut=0.0):
    """Convertit une chaîne en float, tolère « 1 200,50 », « 1200.50 », vide."""
    if valeur is None:
        return defaut
    v = str(valeur).strip().replace(" ", "").replace("\xa0", "").replace(" ", "")
    if v == "":
        return defaut
    if "," in v and "." in v:
        v = v.replace(".", "").replace(",", ".")
    elif "," in v:
        v = v.replace(",", ".")
    try:
        return float(v)
    except ValueError:
        return defaut


def fmt(montant, decimales=0):
    """Formate un montant avec séparateur de milliers (espace) et virgule décimale."""
    s = f"{montant:,.{decimales}f}"
    return s.replace(",", " ").replace(".", ",")


def pct(valeur, dec=1):
    """Pourcentage au format français : 39,0 %."""
    return f"{valeur:.{dec}f}".replace(".", ",") + " %"


def detecter_separateur(chemin):
    with open(chemin, "r", encoding="utf-8-sig", newline="") as f:
        premiere = f.readline()
    return ";" if premiere.count(";") > premiere.count(",") else ","


def lire_csv(chemin):
    sep = detecter_separateur(chemin)
    lignes = []
    with open(chemin, "r", encoding="utf-8-sig", newline="") as f:
        lecteur = csv.DictReader(f, delimiter=sep)
        if lecteur.fieldnames is None:
            sys.exit("Erreur : le fichier CSV est vide.")
        champs = [c.strip().lower() for c in lecteur.fieldnames]
        obligatoires = ["rubrique", "designation", "quantite", "cout_unitaire_fcfa", "source"]
        manquants = [c for c in obligatoires if c not in champs]
        if manquants:
            sys.exit(
                "Erreur : colonnes manquantes dans l'en-tête : "
                + ", ".join(manquants)
                + "\nEn-tête attendu : code,rubrique,designation,unite,quantite,"
                "cout_unitaire_fcfa,source,statut,eligible,justificatif"
            )
        for num, brut in enumerate(lecteur, start=2):
            ligne = {k.strip().lower(): (v or "").strip() for k, v in brut.items() if k}
            if not any(ligne.values()):
                continue  # ligne vide
            if brut.get(None) or any(v is None for k, v in brut.items() if k):
                sys.stderr.write(
                    f"ATTENTION ligne {num} : nombre de colonnes différent de l'en-tête. "
                    "Une virgule dans un libellé ? Entourez le champ de guillemets \"...\".\n")
                ligne["_colonnes_ko"] = True
            qte = nombre(ligne.get("quantite"))
            cu = nombre(ligne.get("cout_unitaire_fcfa"))
            total = nombre(ligne.get("total_fcfa"), None) if ligne.get("total_fcfa") else None
            if total is None:
                total = qte * cu
            ligne["_num"] = num
            ligne["_qte"] = qte
            ligne["_cu"] = cu
            ligne["_total"] = total
            lignes.append(ligne)
    return lignes


def parser_plafonds(valeurs):
    """« Frais administratifs=7 » -> {"frais administratifs": 7.0}"""
    plafonds = {}
    for v in valeurs or []:
        if "=" not in v:
            sys.exit(f"Erreur : plafond mal formé « {v} » (attendu : Rubrique=pourcentage)")
        rub, pct = v.rsplit("=", 1)
        plafonds[rub.strip().lower()] = nombre(pct)
    return plafonds


def main():
    p = argparse.ArgumentParser(description="Consolide un budget ICC (CSV) en rapport Markdown.")
    p.add_argument("csv", help="chemin du fichier budget.csv")
    p.add_argument("--eur", type=float, default=TAUX_EUR_DEFAUT,
                   help="taux FCFA pour 1 EUR (défaut 655.957, parité fixe)")
    p.add_argument("--usd", type=float, default=None,
                   help="taux FCFA pour 1 USD (variable : indiquez le taux du jour)")
    p.add_argument("--plafond", action="append", metavar="RUBRIQUE=PCT",
                   help="plafond en %% du total pour une rubrique (répétable)")
    p.add_argument("--total-attendu", type=float, default=None,
                   help="total cible en FCFA (ex. montant demandé) pour afficher l'écart")
    p.add_argument("--cofinancement-min", type=float, default=None,
                   help="taux minimal de cofinancement exigé en %% (hors bailleur principal)")
    p.add_argument("--bailleur", default=None,
                   help="nom de la source considérée comme bailleur principal "
                        "(défaut : la source la plus importante)")
    args = p.parse_args()

    lignes = lire_csv(args.csv)
    if not lignes:
        sys.exit("Erreur : aucune ligne budgétaire trouvée.")

    total = sum(l["_total"] for l in lignes)
    taux_eur = args.eur
    taux_usd = args.usd

    def conv(m):
        s = f"{fmt(m)} FCFA | {fmt(m / taux_eur, 2)} EUR"
        if taux_usd:
            s += f" | {fmt(m / taux_usd, 2)} USD"
        return s

    # Sous-totaux par rubrique (ordre d'apparition)
    rubriques = OrderedDict()
    for l in lignes:
        rubriques.setdefault(l["rubrique"] or "(sans rubrique)", 0.0)
        rubriques[l["rubrique"] or "(sans rubrique)"] += l["_total"]

    # Sources de financement
    sources = OrderedDict()
    statuts_par_source = {}
    for l in lignes:
        src = l.get("source") or "(SANS SOURCE)"
        sources.setdefault(src, 0.0)
        sources[src] += l["_total"]
        statuts_par_source.setdefault(src, set()).add(l.get("statut") or "non renseigné")

    # Bailleur principal
    sources_valides = {k: v for k, v in sources.items() if k != "(SANS SOURCE)"}
    if args.bailleur:
        bailleur = args.bailleur
    elif sources_valides:
        bailleur = max(sources_valides, key=sources_valides.get)
    else:
        bailleur = None
    part_bailleur = sources.get(bailleur, 0.0) if bailleur else 0.0
    cofinancement = total - part_bailleur - sources.get("(SANS SOURCE)", 0.0)
    taux_cofi = (cofinancement / total * 100) if total else 0.0

    # Éligibilité
    elig = {"oui": 0.0, "non": 0.0, "à vérifier": 0.0}
    for l in lignes:
        e = (l.get("eligible") or "à vérifier").lower()
        e = e.replace("a vérifier", "à vérifier").replace("a verifier", "à vérifier")
        if e not in elig:
            e = "à vérifier"
        elig[e] += l["_total"]

    # Statuts
    statuts = OrderedDict()
    for l in lignes:
        st = l.get("statut") or "non renseigné"
        statuts.setdefault(st, 0.0)
        statuts[st] += l["_total"]

    out = []
    w = out.append
    w("# Rapport de consolidation budgétaire")
    w("")
    w(f"Fichier : `{args.csv}` — {len(lignes)} lignes budgétaires.")
    w(f"Taux utilisés : 1 EUR = {fmt(taux_eur, 3)} FCFA"
      + (f" ; 1 USD = {fmt(taux_usd, 2)} FCFA" if taux_usd else " ; USD non renseigné (option --usd)") + ".")
    w("")
    w("## 1. Total général")
    w("")
    w(f"**TOTAL : {conv(total)}**")
    if args.total_attendu is not None:
        ecart = total - args.total_attendu
        signe = "+" if ecart >= 0 else "-"
        w("")
        w(f"Total attendu : {conv(args.total_attendu)} — écart : {signe}{fmt(abs(ecart))} FCFA "
          f"({('+' if (ecart / args.total_attendu * 100) >= 0 else '') + pct(ecart / args.total_attendu * 100, 1)}).")
    w("")
    w("## 2. Sous-totaux par rubrique")
    w("")
    w("| Rubrique | Total FCFA | Total EUR | % du total |")
    w("|---|---:|---:|---:|")
    for rub, m in rubriques.items():
        w(f"| {rub} | {fmt(m)} | {fmt(m / taux_eur, 2)} | {pct(m / total * 100, 1)} |")
    w(f"| **TOTAL** | **{fmt(total)}** | **{fmt(total / taux_eur, 2)}** | 100 % |")
    w("")
    w("## 3. Plan de financement par source")
    w("")
    w("| Source | Montant FCFA | Montant EUR | % | Statut(s) des lignes |")
    w("|---|---:|---:|---:|---|")
    for src, m in sources.items():
        marque = " (bailleur principal)" if src == bailleur else ""
        w(f"| {src}{marque} | {fmt(m)} | {fmt(m / taux_eur, 2)} | {pct(m / total * 100, 1)} | "
          f"{', '.join(sorted(statuts_par_source[src]))} |")
    w(f"| **TOTAL** | **{fmt(total)}** | **{fmt(total / taux_eur, 2)}** | 100 % | |")
    w("")
    if bailleur:
        w(f"Part du bailleur principal (« {bailleur} ») : {pct(part_bailleur / total * 100, 1)}.")
        w(f"**Taux de cofinancement** (toutes les autres sources identifiées) : **{pct(taux_cofi, 1)}**.")
        if args.cofinancement_min is not None:
            if taux_cofi + 1e-9 >= args.cofinancement_min:
                w(f"Cofinancement minimal exigé ({pct(args.cofinancement_min, 0)}) : atteint.")
            else:
                manque = args.cofinancement_min / 100 * total - cofinancement
                w(f"ALERTE : cofinancement minimal exigé ({pct(args.cofinancement_min, 0)}) NON atteint — "
                  f"il manque environ {fmt(manque)} FCFA ({fmt(manque / taux_eur, 2)} EUR) de cofinancement.")
    w("")
    w("## 4. Répartition par statut de financement")
    w("")
    w("| Statut | Montant FCFA | Montant EUR | % |")
    w("|---|---:|---:|---:|")
    for st, m in statuts.items():
        w(f"| {st} | {fmt(m)} | {fmt(m / taux_eur, 2)} | {pct(m / total * 100, 1)} |")
    w("")
    w("## 5. Éligibilité des dépenses (bailleur principal)")
    w("")
    w("| Éligibilité | Montant FCFA | Montant EUR | % |")
    w("|---|---:|---:|---:|")
    for e in ("oui", "non", "à vérifier"):
        w(f"| {e} | {fmt(elig[e])} | {fmt(elig[e] / taux_eur, 2)} | {pct(elig[e] / total * 100, 1)} |")
    w("")

    # Alertes
    alertes = []
    sans_source = [l for l in lignes if not l.get("source")]
    for l in sans_source:
        alertes.append(f"Ligne {l['_num']} ({l.get('code') or '-'} — {l['designation']}) : "
                       f"aucune source de financement ({fmt(l['_total'])} FCFA).")
    for l in lignes:
        if l.get("_colonnes_ko"):
            alertes.append(f"Ligne {l['_num']} ({l.get('code') or '-'}) : nombre de colonnes différent de "
                           f"l'en-tête (virgule non protégée dans un libellé ?) — valeurs décalées, à corriger.")
        if l["_total"] <= 0:
            alertes.append(f"Ligne {l['_num']} ({l.get('code') or '-'} — {l['designation']}) : "
                           f"montant nul ou négatif — quantité ou coût unitaire manquant ?")
        if not l.get("justificatif"):
            alertes.append(f"Ligne {l['_num']} ({l.get('code') or '-'} — {l['designation']}) : "
                           f"justificatif attendu non renseigné.")
        if (l.get("eligible") or "").lower() == "non" and l.get("source", "") == bailleur and bailleur:
            alertes.append(f"Ligne {l['_num']} ({l.get('code') or '-'} — {l['designation']}) : "
                           f"dépense marquée NON éligible mais imputée au bailleur principal « {bailleur} ».")
    plafonds = parser_plafonds(args.plafond)
    for rub, m in rubriques.items():
        pct_max = plafonds.get(rub.lower())
        if pct_max is not None:
            part = m / total * 100
            if part > pct_max + 1e-9:
                alertes.append(f"Rubrique « {rub} » : {pct(part, 1)} du total, au-dessus du plafond de "
                               f"{pct(pct_max, 0)} (dépassement de {fmt(m - pct_max / 100 * total)} FCFA).")
    for rub in plafonds:
        if rub not in [r.lower() for r in rubriques]:
            alertes.append(f"Plafond fourni pour « {rub} » mais aucune rubrique de ce nom dans le CSV "
                           f"(vérifiez l'orthographe).")

    w("## 6. Alertes et points à corriger")
    w("")
    if alertes:
        for a in alertes:
            w(f"- {a}")
    else:
        w("- Aucune alerte : toutes les lignes ont une source, un montant positif et un justificatif.")
    w("")
    w("## 7. Détail des lignes")
    w("")
    w("| Code | Rubrique | Désignation | Unité | Qté | CU FCFA | Total FCFA | Total EUR | Source | Statut | Éligible | Justificatif |")
    w("|---|---|---|---|---:|---:|---:|---:|---|---|---|---|")
    for l in lignes:
        w(f"| {l.get('code') or ''} | {l['rubrique']} | {l['designation']} | {l.get('unite') or ''} | "
          f"{fmt(l['_qte'], 2 if l['_qte'] % 1 else 0)} | {fmt(l['_cu'])} | {fmt(l['_total'])} | "
          f"{fmt(l['_total'] / taux_eur, 2)} | {l.get('source') or 'SANS SOURCE'} | {l.get('statut') or ''} | "
          f"{l.get('eligible') or 'à vérifier'} | {l.get('justificatif') or ''} |")
    w("")
    w("_Rapport généré par budget.py — les montants en EUR utilisent la parité fixe ; "
      "les montants en USD dépendent du taux saisi et doivent être datés dans le dossier._")
    print("\n".join(out))


if __name__ == "__main__":
    main()
