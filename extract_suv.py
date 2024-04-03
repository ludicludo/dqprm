import re
import argparse

from inout import ouverture_fichier, csv_file

fic = "20200527152905.861802.ig.tum"


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("f")
    parser.add_argument("-o")
    return parser.parse_args()


def extract_infos(chaine, type_info):
    m = re.findall(f"(M.*)(?<!RC){type_info}Value = (\d+(\.\d+)?)", chaine, re.M)
    return m


def sortie_resultat(data):
    return [(el[0], float(el[1])) for el in data]


def do_it(fic, output):
    lines = ouverture_fichier(fic)
    suv = extract_infos(lines, "SUV")
    hu = extract_infos(lines, "HU")
    d = sortie_resultat(suv)
    csv_file(d, output + "_suv.csv")
    e = sortie_resultat(hu)
    csv_file(e, output + "_hu.csv")
    print(d, e)


if __name__ == "__main__":
    p = parse()
    do_it(p.f, p.o)
