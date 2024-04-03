import re

fic = "data/20200527152905.861802.ig.tum"

with open(fic, "r") as f:
    lines = f.read()

m = re.findall("(M.*)(?<!RC)SUVValue = (\d+\.\d+)", lines, re.M)

d = {el[0]: float(el[1]) for el in m}
print(d)
