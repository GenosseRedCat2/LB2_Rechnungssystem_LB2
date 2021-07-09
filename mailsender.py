import os

import logger
from ftp_connector import FTP_server, gohome
from main import rechnungsdata


def sendmail():
    import smtplib
    from datetime import date
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    today = date.today()
    date_in_DBY = today.strftime("%d.%b.%Y %H:%M:%S")

    # Information is added into the E-Mail
    msg = MIMEMultipart()
    msg['From'] = "jason.banyer@edu.tbz.ch"
    msg['To'] = rechnungsdata["receiverEmail"]
    msg['Subject'] = "Erfolgte Verarbeitung Rechnung " + rechnungsdata["rechnungsNr"]
    message = "Sehr geehrter "+ rechnungsdata["kundenName"] + "\n\n" + \
        'Am ' + date_in_DBY + " wurde die erfolgreiche Bearbeitung der Rechnung "+ rechnungsdata["rechnungsNr"] \
              + "vom Zahlungssystem " + FTP_server + \
              "gemeldet. \n\n Mit freundlichen Grüssen \n\n Jason Banyer Maxim \n GmbH"
    os.chdir(gohome)
    zipdata = rechnungsdata["rechnungsNr"] + ".zip"

    msg['Content-Disposition'] = 'attachment; filename="%s"' % zipdata
    msg.attach(msg)

    msg.attach(MIMEText(message))

    # Connection to the GMX is established
    smtp_connection = smtplib.SMTP("websitebackupper@gmx.ch", 587)
    smtp_connection.ehlo()
    smtp_connection.starttls()
    smtp_connection.ehlo()
    smtp_connection.login(msg['From'], "SchulePASSWORTFUERFTP2222")


    # E-Mail is sent
    smtp_connection.sendmail(msg['From'], msg['To'], msg.as_string())

    # Connection is ended.
    smtp_connection.quit()
    #logger.info("(7) Email versendet.")