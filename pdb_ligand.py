'''
This program gets centers of the ligands.
Please enter the PDB-code and the ligand name
'''


import urllib.request
from sys import argv


def string_on_prev(prev):
    result = str(prev["chain"]) + "\t" + str(prev["number"]) \
             + "\t%.3f\t%.3f\t%.3f\n" % (round(prev["sumX"] / prev["count"], 3),
                                         round(prev["sumY"] / prev["count"], 3),
                                         round(prev["sumZ"] / prev["count"], 3))
    return result


SOURCE = "https://files.rcsb.org/download/"

code = argv[1]
ligand = argv[2]
ref = SOURCE + code + ".pdb"
url_file = None

try:
    url_file = urllib.request.urlopen(ref)
except Exception:
    print("Code does not exist")
    exit(0)

result = ""

prev = {"chain": None, "number": None, "X": None, "Y": None, "Z": None,
        "count": None}

for line in url_file:
    line = str(line)
    if line[2:8] == "HETATM" and line.find(ligand, 19, 22) >= 0:
        chain = line[23]
        number = int(line[24:28].replace(" ", ""))
        x_coor = float(line[32:40].replace(" ", ""))
        y_coor = float(line[40:48].replace(" ", ""))
        z_coor = float(line[48:56].replace(" ", ""))

        if prev["chain"] == chain and prev["number"] == number:
            prev["sumX"] += x_coor
            prev["sumY"] += y_coor
            prev["sumZ"] += z_coor
            prev["count"] += 1
        else:

            if prev["chain"] != None:
                result += string_on_prev(prev)

            prev = {"chain": chain, "number": number,
                    "sumX": x_coor, "sumY": y_coor, "sumZ": z_coor,
                    "count": 1}

if prev["chain"] != None:
    result += string_on_prev(prev)

url_file.close()
print(result[:-1])
