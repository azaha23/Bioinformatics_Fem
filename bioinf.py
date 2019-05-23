from sys import argv
import urllib.request

url_file = urllib.request.urlopen("https://files.rcsb.org/download/" + argv[1] + ".pdb")
lines = url_file.readlines()
read = []

file_fasta = open(argv[1].lower() + "_nuc.fasta", "w")

for line in lines:
    line = str(line)
    if line[2:6] == "ATOM" and line[15] == "P":
        read.append(line)

url_file.close()

na = []
f = 0

for elem in read:
    if elem[21] == "T":
        f = 1
        na.append(elem)
    elif elem[21] == "A" or elem[21] == "C" or elem[21] == "G":
        na.append(elem)

lst_na = []

for el in na:
    if el[23] not in lst_na:
        lst_na.append(el[23])

for p in lst_na:
    file_fasta.write(">" + argv[1] + "_" + p + " ")
    if f == 1:
        file_fasta.write("DNA\n")
    else:
        file_fasta.write("RNA\n")

    for el in na:
        if el[23] == p:
            file_fasta.write(el[21])
    file_fasta.write("\n")
