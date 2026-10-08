import re

import jiwer

# Insérer entre les guillemets la chaîne de caractères qui sert de démarcation entre vos pages de sorties HTR
# Conserver la même démarcation pour le fichier 'verite_de_terrain'
demarcation = re.compile("inserer_demarcation") 


# Ouverture et lecture des fichiers
with open('fichier_HTR_a_evaluer', mode="r", encoding="utf-8") as HTR_file:
    HTR = HTR_file.read()

with open('verite_de_terrain', mode="r", encoding="utf-8") as VT_file:
    VT = VT_file.read()


# Récupération des pages de HTR et de VT grâce à la démarcation prédéfinie au début du code "inserer_dermarcation"
HTR_findings = demarcation.findall(HTR)

HTR_parts = demarcation.split(HTR)

HTR_parts = HTR_parts[1:]


VT_findings = demarcation.findall(VT)

VT_parts = demarcation.split(VT)

VT_parts = VT_parts[1:]


# Création d'un fichier contenant les résultats de CER et WER
with open("resultats.txt", mode="w", encoding="utf-8") as f:
    for HTR_part, VT_part, title in zip(HTR_parts, VT_parts, HTR_findings):
        print(title, file=f)
        WER = jiwer.wer(HTR_part,VT_part)
        print("WER : ", WER, file=f)
        CER = jiwer.cer(HTR_part, VT_part)
        print("CER : ", CER, file=f)
