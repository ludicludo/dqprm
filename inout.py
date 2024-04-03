import csv


def ouverture_fichier(fic):
    with open(fic, "r") as f:
        lines = f.read()
    return lines


def csv_file(rows, fichier_out):
    with open(fichier_out, "w") as csv_out:
        csv_w = csv.writer(csv_out)
        for row in rows:
            csv_w.writerow(row)
