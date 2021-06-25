import ftplib

print("Connecting to FTP")
#Connection Informationen hardgecoded
username = "schoolerinvoices"
password = "Berufsschule8005!"
FTP_server = "ftp.haraldmueller.ch"
#Connection wird aufgebaut
ftp_conn = ftplib.FTP(FTP_server)
print('using %s : %s' % (username, password))
ftp_conn.login(username, password)
print("Success: %s:%s" % (username, password))
ftp_conn.cwd("/out/AP18cBanyer")

files = ftp_conn.mlsd("")
for file in files:
    if file[1]["type"] == "file" and file[1]["attr_name"] == ".data":
        print(file[1])
