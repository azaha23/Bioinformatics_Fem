from sys import argv
import urllib.request

url_file = urllib.request.urlopen("https://files.rcsb.org/download/" + argv[1] + ".pdb")
lines = url_file.readlines()
read = []

file_fasta = open(argv[1].lower() + "_nuc.fasta", "w")

for line in lines:
    if line[0:4] == "ATOM" and line[12:16] == " P  ":
        read.append(line)

url_file.close()

dna = []
rna = []

for elem in read:
    if elem[17:20] == "  A" or elem[17:20] == "  C" or elem[17:20] == "  G" or elem[17:20] == "  U":
        rna.append(elem)
    else:
        dna.append(elem)

lst_dna = []

for el in dna:
    if el[21] not in lst_dna:
        lst_dna.append(el[21])

for p in lst_dna:
    file_fasta.write(">" + argv[1] + "_" + p + " " + "DNA\n")
    for el in dna:
        if el[21] == p:
            file_fasta.write(el[19])
    file_fasta.write("\n")

lst_rna = []

for els in rna:
    if els[21] not in lst_rna:
        lst_rna.append(els[21])

for q in lst_rna:
    file_fasta.write(">" + argv[1] + "_" + q + " " + "RNA\n")
    for els in rna:
        if els[21] == q:
            file_fasta.write(els[19])
    file_fasta.write("\n")

file_fasta.close()
























