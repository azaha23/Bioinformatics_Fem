from sys import argv
import urllib.request

url_file = urllib.request.urlopen("https://files.rcsb.org/download/" + argv[1] + ".pdb")
lines = url_file.readlines()
read = []

file_fasta = open(argv[1].lower() + "_nuc.fasta", "w")

for line in lines:
    line = str(line)
    if line[2:6] == "ATOM" and line[15] == "P":
        print(line)
        read.append(line)

url_file.close()

dna = []
rna = []

for elem in read:
    if elem[21] == "A" or elem[21] == "C" or elem[21] == "G" or elem[21] == "U":
        rna.append(elem)
    else:
        dna.append(elem)

lst_dna = []

for el in dna:
    if el[23] not in lst_dna:
        lst_dna.append(el[23])

for p in lst_dna:
    file_fasta.write(">" + argv[1] + "_" + p + " " + "DNA\n")
    for el in dna:
        if el[23] == p:
            file_fasta.write(el[21])
    file_fasta.write("\n")

lst_rna = []

for els in rna:
    if els[23] not in lst_rna:
        lst_rna.append(els[23])

for q in lst_rna:
    file_fasta.write(">" + argv[1] + "_" + q + " " + "RNA\n")
    for els in rna:
        if els[23] == q:
            file_fasta.write(els[21])
    file_fasta.write("\n")

file_fasta.close()

























