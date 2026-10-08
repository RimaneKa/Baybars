import re

import jiwer
demarcation = re.compile("=== .+? ===")

with open('HTR_3_pages.txt', mode="r", encoding="utf-8") as HTR_file:
    HTR = HTR_file.read()

with open('verite_de_terrain', mode="r", encoding="utf-8") as VT_file:
    VT = VT_file.read()

HTR_findings = demarcation.findall(HTR)
# print(HTR_findings)
HTR_parts = demarcation.split(HTR)
# print(HTR_parts)
HTR_parts = HTR_parts[1:]
# print(HTR_parts)

VT_findings = demarcation.findall(VT)
# print(VT_findings)
VT_parts = demarcation.split(VT)
# print(VT_parts)
VT_parts = VT_parts[1:]
# print(VT_parts)

# for HTR_part in HTR_parts:
#    print(HTR_part)

with open("results.txt", mode="w", encoding="utf-8") as f:
    for HTR_part, VT_part, title in zip(HTR_parts, VT_parts, HTR_findings):
        # print("HTR :")
        # print(HTR_part)
        # print("VT :")
        # print(VT_part)
        print(title, file=f)
        WER = jiwer.wer(HTR_part,VT_part)
        print("WER : ", WER, file=f)
        CER = jiwer.cer(HTR_part, VT_part)
        print("CER : ", CER, file=f)
