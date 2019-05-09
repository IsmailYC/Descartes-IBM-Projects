##from Bio.Affy import CelFile
##with open("Affy/affy_v4_example.CEL", "rb") as handle:
##    c = CelFile.read(handle)

from Bio.Affy import CelFile
with open("Data/GSE58661_RAW/GSM1416528_LUNG3-01.CEL", "rb") as handle:
     c = CelFile.read_v3(handle)
