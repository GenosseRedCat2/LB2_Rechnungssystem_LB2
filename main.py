import ftp_connector #Muss ich au no e funktion drus mache
import os

import logger
from csv_reader import parserechnung
from ftp_connector import godate, gohome
from mailsender import sendmail
from uploader import sendnow
from zipper import zipper_go_zip

rechnungsdata=parserechnung("rechnung21003.data")
os.chdir(gohome)

with open("template_full.xml") as tplfle_xml:
    tpl_xml = tplfle_xml.read()
    os.chdir(godate)
    xmlfilename = rechnungsdata["kundennummer"] + "_" + rechnungsdata["rechnungsNr"] + "_invoice" + ".xml"
    template_full_xml = open(xmlfilename, "w")
    template_full_xml.write(tpl_xml % rechnungsdata)
    template_full_xml.close()
    os.chdir(gohome)
    logger.info("(1) erfolgreich XML template generiert")


#Textfile wird mit header generiert und in Ordner mit aktuellem Datum abgespeichert
with open("template_head.txt") as tplfle:
    tpl_header = tplfle.read()
    os.chdir(godate)
    textfilename = rechnungsdata["kundennummer"] + "_" + rechnungsdata["rechnungsNr"] + "_invoice" + ".txt"
    textfilename_full_text = open(textfilename, "w")
    textfilename_full_text.write(tpl_header % rechnungsdata)
    textfilename_full_text.close()
    os.chdir(gohome)
    logger.info("(2) erfolgreich TXT head template generiert")

#Textfile wird mit Rechnungsposition generiert und in Ordner mit aktuellem Datum abgespeichert
with open("template_rechnungspos.txt") as tplfile_rechnungspos:
    tpl_pos = tplfile_rechnungspos.read()
    os.chdir(godate)
    for rechnungspos in rechnungsdata["rechnungspos"]:
        textfilename = rechnungsdata["kundennummer"] + "_" + rechnungsdata["rechnungsNr"] + "_invoice" + ".txt"
        textfilename_full_text = open(textfilename, "a")
        textfilename_full_text.write(tpl_pos % (rechnungspos[1],rechnungspos[2],rechnungspos[3],float(rechnungspos[4]),float(rechnungspos[5])))
        textfilename_full_text.write("\n")
    textfilename_full_text.close()
    os.chdir(gohome)
logger.info("(3) erfolgreich TXT Rechnungsposition template generiert")
#Textfile wird mit footer generiert und in Ordner mit aktuellem Datum abgespeichert
with open("template_footer.txt") as tplfle:
    tpl_footer = tplfle.read()
    os.chdir(godate)
    textfilename = rechnungsdata["kundennummer"] + "_" + rechnungsdata["rechnungsNr"] + "_invoice" + ".txt"
    textfilename_full_text = open(textfilename, "a")
    textfilename_full_text.write(tpl_footer % rechnungsdata)
    textfilename_full_text.close()
    os.chdir(gohome)
logger.info("(4) erfolgreich footer TXT template generiert")
#Die beiden invoice Dateien werden hochgeladen per FTP
sendnow()
#Ein E-Mail wird versendet mit den aktuellen Informationen zu dem vollendeten Prozess.
sendmail()
zipper_go_zip()
logger.info("(8) Prozess erfolgreich beendet.")
ftp_connector.ftp_conn.close()