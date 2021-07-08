import csv
import datetime

def parserechnung(filename):
    with open(filename) as csvfile:
        csvReader = csv.reader(csvfile, delimiter=';')

        rechnungsdata = dict()

        # Write all into a row

        rechnungsdata["rechnungspos"] = []
        rechnungsdata["rechnungstotal"] = 0.0
        for row in csvReader:  # jedes row ein subarray
            # print all rows out
            # print(row)

            if row[0].startswith("Rechnung_"):
                rechnungsdata["rechnungsNr"] = row[0][9:]  # von null bis _ zählen dann ab neunter stelle alles nehmen


                rechnungsdata["auftragsnummer"] = row[1][8:]

                rechnungsdata["ort_datum1"] = row[2]
                rechnungsdata["ort_datum2"] = row[3]

                #Genauere Details für die Zahlungen werden angefragt
                rechnungsdata["paymentperiodtype"] = input("Which payment-period type do you want to use: M, Y or D? \n")
                rechnungsdata["paymentperiodday"] = input("Which payment-period day do you want? Type a number: \n")
                rechnungsdata["paymentperiodreferenceday"] = input("Which payment-period reference day do you want: 30 or 31? \n")
                rechnungsdata["paymentperiodreferencedaybefore"] = int(rechnungsdata["paymentperiodreferenceday"]) -1



            if row[0] == "Herkunft":
                rechnungsdata["kundennummer"] = row[2]

                rechnungsdata["senderPID"] = row[1]
                rechnungsstellerkundenNr = row[2]
                rechnungsdata["senderName"] = row[3]
                rechnungsdata["senderAdresse"] = row[4]
                rechnungsdata["senderPLZ"] = row[5]
                rechnungsdata["senderCHE"] = row[6]
                rechnungsdata["receiverEmail"] = row[7]


            if row[0] == "Endkunde":
                print("")
                rechnungsdata["receiverPID"] = row[1]
                rechnungsdata["kundenName"] = row[2]
                rechnungsdata["kundenStrasse"] = row[3]
                rechnungsdata["kundenPLZ"] = row[4]

            if row[0] == "RechnPos":
                rechnungsdata["rechnungspos"].append(row)
                rechnungsdata["rechnungstotal"] += float(row[5])



        return rechnungsdata
