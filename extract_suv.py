import re
import argparse

fic = "20200527152905.861802.ig.tum"


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("f")
    return parser.parse_args()


def extract_SUV(chaine):
    m = re.findall("(M.*)(?<!RC)SUVValue = (\d+\.\d+)", chaine, re.M)
    return m


def extract_HU(chaine):
    m = re.findall("(M.*)HUValue = (\d+(\.\d+)?)", chaine, re.M)
    return m


def ouverture_fichier(fic):
    with open(fic, "r") as f:
        lines = f.read()
    return lines


def sortie_resultat(data):
    return {el[0]: float(el[1]) for el in data}


def do_it(fic):
    lines = ouverture_fichier(fic)
    suv = extract_SUV(lines)
    hu = extract_HU(lines)
    d = sortie_resultat(suv)
    e = sortie_resultat(hu)
    print(d, e)


if __name__ == "__main__":
    p = parse()
    do_it(p.f)
