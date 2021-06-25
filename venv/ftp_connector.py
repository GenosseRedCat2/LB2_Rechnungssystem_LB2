import ftplib

print("Connecting to FTP")

username = "schoolerinvoices"
password = "Berufsschule8005!"
FTP_server = "ftp.haraldmueller.ch"

ftp_conn = ftplib.FTP(FTP_server)
print('using %s : %s' % (username, password))
ftp_conn.login(username, password)
print("Success: %s:%s" % (username, password))
