import csv

with open("rechnung21003.data") as csvfile:
    csvReader = csv.reader(csvfile, delimiter=';')



    #Write all into a row
    rechnungspos = []
    for row in csvReader:
        #print all rows out
        #print(row)

        if row[0].startswith("Rechnung_"):
            rechnungsNr=row[0][9:]
            print(rechnungsNr)
        if row[0] == "Herkunft":
            rechnungsstellerID = row[1]
            rechnungsstellerkundenNr=row[2]
        if row[0] == "Endkunde":
            kundenID = row[1]
            kundenName = row[2]
        if row[0]== "RechnPos":
            print(row[1:])
            rechnungspos.append(row[1:])
    print(rechnungspos)

    with open('rechnung21003.txt', 'a') as f:
        if 'Rechnung_21003' in row:
            #print(row)
            f.write("RECHNUNG INFO")
            f.write("\n")
            Rechnung_Info_string = '\n'.join(map(str, row))
            f.write(Rechnung_Info_string)
            f.write("\n")
            f.write("\n")

        if 'Herkunft' in row:
            #print(row)
            f.write("HERKUNFT INFO")
            f.write("\n")
            Herkunft_string = '\n'.join(map(str, row))
            f.write(Herkunft_string)
            f.write("\n")
            f.write("\n")

        if 'Endkunde' in row:
            #print(row)
            f.write("ENDKUNDE INFO")
            f.write("\n")
            Endkunde_string = '\n                                 '.join(map(str, row))
            f.write(Endkunde_string)
            f.write("\n")
            f.write("\n")

        if 'RechnPos' in row and '1' in row:
            #print(row)
            f.write("RECHNUNGS POSITION INFO EINS")
            f.write("\n")
            RechnPos_string = ''.join(map(str, row))
            f.write(RechnPos_string)
            f.write("\n")
            f.write("\n")

        if 'RechnPos' in row and '2' in row:
            f.write("RECHNUNGS POSITION INFO ZWEI")
            f.write("\n")
            RechnPos_string = '\n'.join(map(str, row))
            f.write(RechnPos_string)
            f.write("\n")
            f.write("\n")
    print(rechnungspos)

