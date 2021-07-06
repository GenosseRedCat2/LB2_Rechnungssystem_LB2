



absender_text = "Adam Adler \nBahnhofstrasse 1 \n8000 Zuerich"
mwst_text = "\nCHE-111.222.333 MWST\n\n\n\n"

ort_datum = "Uster, den 31.07.2020"
empfaenger_text = "Autoleasing AG Gewerbestrasse 100 5000 Aarau"

kundennummer_text="K821"
auftragsnummer_text="A003"
rechnungsnummer_text = "21003"



absender_template="%(absender)0s"%{'absender' : absender_text }

angabe_mwst = "%(mwst)0s"%{'mwst' : mwst_text }

angabe_ort_datum_empfaenger="%(ortunddatum)0s %(empfaenger)50s"%{'ortunddatum' : ort_datum, 'empfaenger' : empfaenger_text }

kundennummer="\n\n\nKundennummer: %(kundennummer)7s"%{'kundennummer' : kundennummer_text }
auftragsnummer="Auftragsnummer: %(auftragsnummer)5s"%{'auftragsnummer' : auftragsnummer_text }
rechnungsnummer="Rechnung Nr %(rechnungsnummer)10s"%{'rechnungsnummer' : rechnungsnummer_text }

sendername = "&(sendername_text)"

print(absender_template)
print(angabe_mwst)
print(angabe_ort_datum_empfaenger)
print(kundennummer)
print(auftragsnummer + "\n")
print(rechnungsnummer)
print("----------------------")