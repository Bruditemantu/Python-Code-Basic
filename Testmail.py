
from smtplib import SMTP
import datetime

SMTPserver = 'smtp.gmail.com'
sender =     'mantu.r.brudite@gmail.com'
destination = ['manturaj25122003@gmail.com']

USERNAME = "mantu.r.brudite@gmail.com"
PASSWORD = "pztuxjfmzusyozbw"

# typical values for text_subtype are plain, html, xml
text_subtype = 'plain'


content="""\
Hello Guys
"""

subject="Testing mail code using python"

import sys
import os
import re

from smtplib import SMTP_SSL as SMTP       # this invokes the secure SMTP protocol (port 465, uses SSL)
# from smtplib import SMTP                  # use this for standard SMTP protocol   (port 25, no encryption)

# old version
# from email.MIMEText import MIMEText
from email.mime.text import MIMEText

try:
    msg = MIMEText(content, text_subtype)
    msg['Subject']= subject
    msg['manturaj25122003@gmail.com']   = sender # some SMTP servers will do this automatically, not all

    conn = SMTP(SMTPserver)
    conn.set_debuglevel(False)
    conn.login(USERNAME, PASSWORD)
    try:
        conn.sendmail(sender, destination, msg.as_string())
    finally:
        conn.quit()

except:
    sys.exit( "mail failed; %s" % "CUSTOM_ERROR" ) # give an error message