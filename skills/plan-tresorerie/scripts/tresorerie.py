#!/usr/bin/env python3
"""
tresorerie.py — Plan de trésorerie mensuel ICC à partir d'un CSV d'encaissements / décaissements.

Usage :
    python3 -I tresorerie.py projet/budget/tresorerie.csv
    python3 -I tresorerie.py projet/budget/tresorerie.csv --solde-initial 500000 --eur 655.957
    python3 -I tresorerie.py projet/budget/tresorerie.csv --seuil-alerte 300000

Format du CSV attendu (séparateur « , » ou « ; », en-tête obligatoire, UTF-8) :
    mois,type,libelle,montant_fcfa,source_ou_rubrique,statut

    - mois                : AAAA-MM (ex. 2027-03). Les mois sont triés par ordre chronologique.
    - type                : E (encaissement = argent qui entre) ou D (décaissement = argent qui sort).
                            Variantes acceptées : encaissement/décaissement, entree/sortie, recette/depense.
    - libelle             : description (ex. « Tranche 1 OIF 40 % », « Cachets artistes »).
    - montant_fcfa        : montant positif en FCFA.
    - source_ou_rubrique  : source de financement (pour E) ou rubrique budgétaire (pour D).
    - statut              : facultatif — confirmé | probable | hypothèse (repris tel quel).

Sortie : rapport Markdown sur la sortie standard (tableau mensuel, solde, cumul, mois négatifs,
besoin de financement maximal). Bibliothèque standard uniquement.
"""

import argparse
import csv
import sys
from collections import OrderedDict

TAUX_EUR_DEFAUT = 655.957

TYPES_E = {"e", "enc", "encaissement", "encaissements", "entree", "entrée", "recette", "recettes", "in", "+"}
TYPES_D = {"d", "dec", "decaissement", "décaissement", "decaissements", "décaissements",
           "sortie", "depense", "dépense", "depenses", "dépenses", "out", "-"}


def nombre(valeur, defaut=0.0):
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


def fmt(m, dec=0):
    s = f"{m:,.{dec}f}"
    return s.replace(",", " ").replace(".", ",")


def pct(valeur, dec=1):
    """Pourcentage au format français : 39,0 %."""
    return f"{valeur:.{dec}f}".replace(".", ",") + " %"


def detecter_separateur(chemin):
    with open(chemin, "r", encoding="utf-8-sig", newline="") as f:
        premiere = f.readline()
    return ";" if premiere.count(";") > premiere.count(",") else ","


def cle_mois(m):
    """« 2027-03 » -> (2027, 3). Accepte aussi « 03/2027 » et « M1 » (ordre numérique)."""
    m = m.strip()
    if "-" in m:
        a, b = m.split("-", 1)
        if a.isdigit() and b.isdigit():
            return (int(a), int(b))
    if "/" in m:
        a, b = m.split("/", 1)
        if a.isdigit() and b.isdigit():
            return (int(b), int(a))
    if m.upper().startswith("M") and m[1:].isdigit():
        return (0, int(m[1:]))
    return (9999, 0)


def lire_csv(chemin):
    sep = detecter_separateur(chemin)
    lignes = []
    with open(chemin, "r", encoding="utf-8-sig", newline="") as f:
        lecteur = csv.DictReader(f, delimiter=sep)
        if lecteur.fieldnames is None:
            sys.exit("Erreur : fichier CSV vide.")
        champs = [c.strip().lower() for c in lecteur.fieldnames]
        for c in ("mois", "type", "libelle", "montant_fcfa"):
            if c not in champs:
                sys.exit(f"Erreur : colonne « {c} » manquante. En-tête attendu : "
                         "mois,type,libelle,montant_fcfa,source_ou_rubrique,statut")
        for num, brut in enumerate(lecteur, start=2):
            l = {k.strip().lower(): (v or "").strip() for k, v in brut.items() if k}
            if not any(l.values()):
                continue
            if brut.get(None) or any(v is None for k, v in brut.items() if k):
                sys.stderr.write(f"ATTENTION ligne {num} : nombre de colonnes différent de l'en-tête "
                                 "(virgule dans un libellé ? entourez-le de guillemets).\n")
            t = l.get("type", "").lower()
            if t in TYPES_E:
                l["_type"] = "E"
            elif t in TYPES_D:
                l["_type"] = "D"
            else:
                sys.exit(f"Erreur ligne {num} : type « {l.get('type')} » inconnu (attendu E ou D).")
            l["_montant"] = abs(nombre(l.get("montant_fcfa")))
            l["_num"] = num
            if not l.get("mois"):
                sys.exit(f"Erreur ligne {num} : mois manquant.")
            lignes.append(l)
    return lignes


def main():
    p = argparse.ArgumentParser(description="Plan de trésorerie mensuel ICC (CSV -> Markdown).")
    p.add_argument("csv", help="chemin du fichier tresorerie.csv")
    p.add_argument("--solde-initial", type=float, default=0.0,
                   help="trésorerie disponible au début du premier mois (FCFA)")
    p.add_argument("--eur", type=float, default=TAUX_EUR_DEFAUT, help="taux FCFA pour 1 EUR")
    p.add_argument("--seuil-alerte", type=float, default=0.0,
                   help="seuil de trésorerie cumulée (FCFA) sous lequel signaler une alerte (défaut 0)")
    args = p.parse_args()

    lignes = lire_csv(args.csv)
    if not lignes:
        sys.exit("Erreur : aucune ligne trouvée.")
    taux = args.eur

    mois_tries = sorted({l["mois"] for l in lignes}, key=cle_mois)
    enc = OrderedDict((m, 0.0) for m in mois_tries)
    dec = OrderedDict((m, 0.0) for m in mois_tries)
    enc_par_source = OrderedDict()
    dec_par_rubrique = OrderedDict()
    for l in lignes:
        cat = l.get("source_ou_rubrique") or "(non renseigné)"
        if l["_type"] == "E":
            enc[l["mois"]] += l["_montant"]
            enc_par_source.setdefault(cat, OrderedDict((m, 0.0) for m in mois_tries))
            enc_par_source[cat][l["mois"]] += l["_montant"]
        else:
            dec[l["mois"]] += l["_montant"]
            dec_par_rubrique.setdefault(cat, OrderedDict((m, 0.0) for m in mois_tries))
            dec_par_rubrique[cat][l["mois"]] += l["_montant"]

    cumul = args.solde_initial
    soldes, cumuls = OrderedDict(), OrderedDict()
    for m in mois_tries:
        soldes[m] = enc[m] - dec[m]
        cumul += soldes[m]
        cumuls[m] = cumul

    total_enc = sum(enc.values())
    total_dec = sum(dec.values())
    mois_negatifs = [m for m in mois_tries if cumuls[m] < 0]
    mois_alerte = [m for m in mois_tries if 0 <= cumuls[m] < args.seuil_alerte] if args.seuil_alerte > 0 else []
    pire_mois = min(mois_tries, key=lambda m: cumuls[m])
    besoin_max = -cumuls[pire_mois] if cumuls[pire_mois] < 0 else 0.0

    out = []
    w = out.append
    w("# Plan de trésorerie mensuel")
    w("")
    w(f"Fichier : `{args.csv}` — {len(lignes)} mouvements sur {len(mois_tries)} mois "
      f"({mois_tries[0]} à {mois_tries[-1]}). Solde initial : {fmt(args.solde_initial)} FCFA. "
      f"1 EUR = {fmt(taux, 3)} FCFA.")
    w("")
    w("## 1. Synthèse")
    w("")
    w(f"- Total encaissements : {fmt(total_enc)} FCFA ({fmt(total_enc / taux, 2)} EUR)")
    w(f"- Total décaissements : {fmt(total_dec)} FCFA ({fmt(total_dec / taux, 2)} EUR)")
    w(f"- Solde final cumulé : {fmt(cumuls[mois_tries[-1]])} FCFA ({fmt(cumuls[mois_tries[-1]] / taux, 2)} EUR)")
    if besoin_max > 0:
        w(f"- **Besoin de financement maximal : {fmt(besoin_max)} FCFA ({fmt(besoin_max / taux, 2)} EUR) "
          f"atteint en {pire_mois}.** C'est le montant minimal de préfinancement (avance, découvert, "
          f"acompte partenaire) à sécuriser pour ne jamais être à découvert.")
    else:
        w(f"- Besoin de financement maximal : aucun — le cumul reste positif ; point le plus bas "
          f"{fmt(cumuls[pire_mois])} FCFA en {pire_mois}.")
    if mois_negatifs:
        w(f"- **Mois en trésorerie négative ({len(mois_negatifs)}) : {', '.join(mois_negatifs)}.**")
    else:
        w("- Aucun mois en trésorerie négative.")
    if args.seuil_alerte > 0:
        if mois_alerte:
            w(f"- Mois sous le seuil d'alerte ({fmt(args.seuil_alerte)} FCFA) : {', '.join(mois_alerte)}.")
        else:
            w(f"- Aucun mois sous le seuil d'alerte ({fmt(args.seuil_alerte)} FCFA) hors mois négatifs.")
    w("")
    w("## 2. Tableau mensuel (FCFA)")
    w("")
    w("| Mois | Encaissements | Décaissements | Solde du mois | Cumul | Situation |")
    w("|---|---:|---:|---:|---:|---|")
    for m in mois_tries:
        if cumuls[m] < 0:
            sit = "NÉGATIF"
        elif args.seuil_alerte > 0 and cumuls[m] < args.seuil_alerte:
            sit = "sous seuil"
        else:
            sit = "ok"
        w(f"| {m} | {fmt(enc[m])} | {fmt(dec[m])} | {fmt(soldes[m])} | {fmt(cumuls[m])} | {sit} |")
    w(f"| **Total** | **{fmt(total_enc)}** | **{fmt(total_dec)}** | **{fmt(total_enc - total_dec)}** | "
      f"**{fmt(cumuls[mois_tries[-1]])}** | |")
    w("")
    w("## 3. Encaissements par source et par mois (FCFA)")
    w("")
    w("| Source | " + " | ".join(mois_tries) + " | Total |")
    w("|---|" + "---:|" * (len(mois_tries) + 1))
    for src, d in enc_par_source.items():
        w(f"| {src} | " + " | ".join(fmt(d[m]) if d[m] else "" for m in mois_tries)
          + f" | {fmt(sum(d.values()))} |")
    w("")
    w("## 4. Décaissements par rubrique et par mois (FCFA)")
    w("")
    w("| Rubrique | " + " | ".join(mois_tries) + " | Total |")
    w("|---|" + "---:|" * (len(mois_tries) + 1))
    for rub, d in dec_par_rubrique.items():
        w(f"| {rub} | " + " | ".join(fmt(d[m]) if d[m] else "" for m in mois_tries)
          + f" | {fmt(sum(d.values()))} |")
    w("")
    w("## 5. Alertes")
    w("")
    alertes = []
    for m in mois_negatifs:
        alertes.append(f"{m} : cumul négatif de {fmt(cumuls[m])} FCFA — décaler des dépenses, "
                       f"avancer un encaissement ou prévoir un relais.")
    for m in mois_alerte:
        alertes.append(f"{m} : cumul {fmt(cumuls[m])} FCFA sous le seuil d'alerte.")
    sans_statut = [l for l in lignes if l["_type"] == "E" and not l.get("statut")]
    if sans_statut:
        alertes.append(f"{len(sans_statut)} encaissement(s) sans statut (confirmé/probable/hypothèse) : "
                       "précisez le degré de certitude de chaque versement.")
    hypo = sum(l["_montant"] for l in lignes if l["_type"] == "E"
               and l.get("statut", "").lower().startswith("hypoth"))
    if hypo:
        alertes.append(f"Encaissements au statut « hypothèse » : {fmt(hypo)} FCFA "
                       f"({pct(hypo / total_enc * 100, 0)} des entrées) — préparez un scénario sans eux.")
    for l in lignes:
        if l["_montant"] == 0:
            alertes.append(f"Ligne {l['_num']} ({l['libelle']}) : montant nul.")
    if alertes:
        for a in alertes:
            w(f"- {a}")
    else:
        w("- Aucune alerte.")
    w("")
    w("_Rapport généré par tresorerie.py. Les dates de versement des bailleurs sont des hypothèses "
      "à confirmer dans la convention de financement._")
    print("\n".join(out))


if __name__ == "__main__":
    main()
