import ftp_connector #Muss ich au no e funktion drus mache
import os
from csv_reader import parserechnung

rechnungsdata=parserechnung("rechnung21003.data")
os.chdir("..") #Mussi no schönner mache gfallt ihm ned so

#speichern als output file name steht in auftrag
with open("template_head.txt") as tplfle:
    tpl = tplfle.read()
    print(tpl % rechnungsdata) #statt print write

with open("template_rechnungspos.txt") as tplfile_rechnungspos:
    tpl_pos = tplfile_rechnungspos.read()
    for rechnungspos in rechnungsdata["rechnungspos"]:
        print(tpl_pos % (rechnungspos[1],rechnungspos[2],rechnungspos[3],float(rechnungspos[4]),float(rechnungspos[5])))

with open("template_footer.txt") as tplfle:
    tpl = tplfle.read()
    print(tpl % rechnungsdata)
