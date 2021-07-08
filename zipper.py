import os
import shutil

from ftp_connector import gohome, godate
from main import rechnungsdata


def zipper_go_zip():
    os.chdir(godate)
    NameOfDownloadedQuittung = "INSERT QUITTUNG NAME HERE, WHICH I CANT BECAUSE I DON'T HAVE ANY QUITTUNGS"


    shutil.make_archive(NameOfDownloadedQuittung, 'zip', gohome / rechnungsdata["rechnungsNr"])
