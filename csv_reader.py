import csv



def parserechnung(filename):
    with open(filename) as csvfile:
        csvReader = csv.reader(csvfile, delimiter=';')

        rechnungsdata=dict()

        #Write all into a row

        rechnungsdata["rechnungspos"] = []
        for row in csvReader: #jedes row ein subarray
            #print all rows out
            #print(row)

            if row[0].startswith("Rechnung_"):
                rechnungsdata["rechnungsNr"] = row[0][9:] #von null bis _ zählen dann ab neunter stelle alles nehmen
                #print(rechnungsdata["rechnungsNr"])

                rechnungsdata["auftragsnummer"] = row[1][8:]


                rechnungsdata["ort_datum1"] = row[2]
                rechnungsdata["ort_datum2"] = row[3]


            if row[0] == "Herkunft":

                rechnungsdata["kundennummer"] = row[2]

                rechnungsstellerID = row[1]
                rechnungsstellerkundenNr=row[2]
                rechnungsdata["senderName"] = row[3]
                rechnungsdata["senderAdresse"] = row[4]
                rechnungsdata["senderPLZ"] = row[5]
                rechnungsdata["senderCHE"] = row[6]

            if row[0] == "Endkunde":
                print("")
                rechnungsdata["kundenName"] = row[2]
                rechnungsdata["kundenStrasse"] = row[3]
                rechnungsdata["kundenPLZ"] = row[4]
                # rechnungsdata["rechnungsNr"] = row[2][9:]   alles hinter dran ab der 9 stelle vom Feld null





            rechnArray = []
            if row[0] == "RechnPos":
                rechnArray.append(row)
                text = []
                for element in rechnArray: #Für alli
                    newText = ""
                    newText = newText + "  "
                    newText = newText + element[1]
                    newText = newText + "   "
                    newText = newText + element[2]
                    newText = newText + "      " + element[3]
                    newText = newText + "    " + element[4] + " CHF"
                    newText = newText + "     " + element[5]
                    newText = newText + element[6]
                    text.append(newText)

                    print(text)
                    rechnungsdata["rechnungspos"] = text  #Contains both in one

        return rechnungsdata