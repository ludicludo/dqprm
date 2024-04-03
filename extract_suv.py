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


def do_it(fic):
    with open(fic, "r") as f:
        lines = f.read()
    m = extract_SUV(lines)
    d = {el[0]: float(el[1]) for el in m}
    print(d)


if __name__ == "__main__":
    p = parse()
    do_it(p.f)
