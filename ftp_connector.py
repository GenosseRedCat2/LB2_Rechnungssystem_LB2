import ftplib
from datetime import date
import os
print("Connecting to FTP")
#Connection Informationen hardgecoded
username = "schoolerinvoices"
password = "Berufsschule8005!"
FTP_server = "ftp.haraldmueller.ch"
#Connection wird aufgebaut
ftp_conn = ftplib.FTP(FTP_server)
#print('using %s : %s' % (username, password))
ftp_conn.login(username, password)
#print("Success: %s:%s" % (username, password))
ftp_conn.cwd("/out/AP18cBanyer")

today = date.today()
d1 = today.strftime("%d-%b-%Y")
neuste_rechnungen = "Rechnungen_vom_" + d1

# Fertige Directory Befehle
goback = ".."
godate = neuste_rechnungen
#Incase the folder doesn't exist,
# one is automatically created with the name "Backup_Homepage" and the current date.
if not os.path.exists(neuste_rechnungen):
    os.makedirs(neuste_rechnungen)
os.chdir(neuste_rechnungen)


#Downloads all files, which end with .data and actually are files.
#This gives me all CSV files, which will be used later.
files = ftp_conn.mlsd("")
for file in files:
    if file[1]["type"] == "file" and file[0].endswith(".data"):
        #print(file[1])
        with open(file[0], "wb") as file_2:
            ftp_conn.retrbinary('RETR ' + file[0], file_2.write)


