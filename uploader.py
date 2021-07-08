import ftplib
import os

from ftp_connector import goback, godate
from main import xmlfilename, textfilename

def sendnow():
    #Connection Informationen hardgecoded
    username = "310721-297-zahlsystem"
    password = "Berufsschule8005!"
    FTP_server = "134.119.225.245"

    ftp_conn = ftplib.FTP(FTP_server)
    ftp_conn.login(username, password)
    ftp_conn.cwd("/in/AP18cBanyer")
    os.chdir(godate)

    file_xml = open(xmlfilename,'rb') #XML File to upload
    file_txt = open(textfilename,'rb') #TXT File to upload

    ftp_conn.storbinary('STOR'+ str(file_xml), file_xml) #uploading XML to FTP
    ftp_conn.storbinary('STOR'+ str(file_txt), file_txt) #uploading TXT to FTP
    file_xml.close()#XML close file
    file_txt.close()#TXT close file
    ftp_conn.quit()#FTP Verbindung geschlossen


    #Ab diesem Punkt funktionierte die Verbindung zum ersten Server nicht mehr
    #TimeoutError: [WinError 10060] Ein Verbindungsversuch ist fehlgeschlagen, da die Gegenstelle nach einer bestimmten Zeitspanne nicht richtig reagiert hat, oder die hergestellte Verbindung war fehlerhaft, da der verbundene Host nicht reagiert hat
