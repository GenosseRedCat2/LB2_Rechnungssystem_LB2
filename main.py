import ftp_connector #Muss ich au no e funktion drus mache
import os
from csv_reader import parserechnung

rechnungsdata=parserechnung("rechnung21003.data")
os.chdir("..") #Mussi no schönner mache gfallt ihm ned so


with open("template.txt") as tplfle:
    tpl = tplfle.read()
    print(tpl % rechnungsdata)

