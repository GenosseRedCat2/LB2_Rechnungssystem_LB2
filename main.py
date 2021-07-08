import ftp_connector #Muss ich au no e funktion drus mache
import os
from csv_reader import parserechnung
from ftp_connector import godate, goback
from uploader import sendnow



rechnungsdata=parserechnung("rechnung21003.data")
os.chdir(goback)

with open("template_full.xml") as tplfle_xml:
    tpl_xml = tplfle_xml.read()
    os.chdir(godate)
    xmlfilename = "rechnung" + rechnungsdata["rechnungsNr"] + ".xml"
    template_full_xml = open(xmlfilename, "w")
    template_full_xml.write(tpl_xml % rechnungsdata)
    template_full_xml.close()
    os.chdir(goback)


#Textfile wird mit header generiert und in Ordner mit aktuellem Datum abgespeichert
with open("template_head.txt") as tplfle:
    tpl_header = tplfle.read()
    os.chdir(godate)
    textfilename = "rechnung" + rechnungsdata["rechnungsNr"] + ".txt"
    textfilename_full_text = open(textfilename, "w")
    textfilename_full_text.write(tpl_header % rechnungsdata)
    textfilename_full_text.close()
    os.chdir(goback)

#Textfile wird mit Rechnungsposition generiert und in Ordner mit aktuellem Datum abgespeichert
with open("template_rechnungspos.txt") as tplfile_rechnungspos:
    tpl_pos = tplfile_rechnungspos.read()
    os.chdir(godate)
    for rechnungspos in rechnungsdata["rechnungspos"]:
        textfilename = "rechnung" + rechnungsdata["rechnungsNr"] + ".txt"
        textfilename_full_text = open(textfilename, "a")
        textfilename_full_text.write(tpl_pos % (rechnungspos[1],rechnungspos[2],rechnungspos[3],float(rechnungspos[4]),float(rechnungspos[5])))
        textfilename_full_text.write("\n")
    textfilename_full_text.close()
    os.chdir(goback)

#Textfile wird mit footer generiert und in Ordner mit aktuellem Datum abgespeichert
with open("template_footer.txt") as tplfle:
    tpl_footer = tplfle.read()
    os.chdir(godate)
    textfilename = "rechnung" + rechnungsdata["rechnungsNr"] + ".txt"
    textfilename_full_text = open(textfilename, "a")
    textfilename_full_text.write(tpl_footer % rechnungsdata)
    textfilename_full_text.close()
    os.chdir(goback)

sendnow()
