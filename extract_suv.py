import re
import argparse

fic = "20200527152905.861802.ig.tum"


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument("f")
    return parser.parse_args()


def extract_infos(chaine, type_info):
    m = re.findall(f"(M.*)(?<!RC){type_info}Value = (\d+(\.\d+)?)", chaine, re.M)
    return m


def ouverture_fichier(fic):
    with open(fic, "r") as f:
        lines = f.read()
    return lines


def sortie_resultat(data):
    return {el[0]: float(el[1]) for el in data}


def do_it(fic):
    lines = ouverture_fichier(fic)
    suv = extract_infos(lines, "SUV")
    hu = extract_infos(lines, "HU")
    d = sortie_resultat(suv)
    e = sortie_resultat(hu)
    print(d, e)


if __name__ == "__main__":
    p = parse()
    do_it(p.f)
