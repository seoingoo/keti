#!/usr/bin/python
# -*- coding:utf-8 -*-

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
from email import Utils
from email.header import Header
import os
import time
from subprocess import *


smtp_server = "smtp.mailgun.org"
port = 587
userid = "postmaster@sandboxd13de7857b744ce1872cea0b767eeb12.mailgun.org"
passwd = "49dfd47c9017e9e1fe3215c279a70e67"

def send_mail(from_user, to_user, cc_users, subject, text, attach):
    COMMASPACE = ", "
    msg = MIMEMultipart("alternative")
    msg["From"] = from_user
    msg["To"] = to_user
    msg["Cc"] = COMMASPACE.join(cc_users)
    msg["Subject"] = Header(s=subject, charset="utf-8")
    msg["Date"] = Utils.formatdate(localtime=1)
    msg.attach(MIMEText(text, "html", _charset="utf-8"))

    if (attach != None):
        part = MIMEBase("application", "octet-stream")
        part.set_payload(open(attach, "rb").read())
        Encoders.encode_base64(part)
        part.add_header("Content-Disposition", "attachment; filename=\"%s\"" % os.path.basename(attach))
        msg.attach(part)

    smtp = smtplib.SMTP(smtp_server, port)
    smtp.login(userid, passwd)
    smtp.sendmail(from_user, cc_users, msg.as_string())
    smtp.close()

def run_cmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    output = p.communicate()[0]
    return output

def ip_chk():
    cmd = "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"
    ipAddr = run_cmd(cmd)
    return ipAddr

def wip_chk():
    cmd = "ip addr show wlan0 | grep inet | awk '{print $2}' | cut -d/ -f1"
    wipAddr = run_cmd(cmd)
    return wipAddr

def mac_chk():
    cmd = "ifconfig -a | grep ^eth | awk '{print $5}'"
    macAddr = run_cmd(cmd)
    return macAddr

def wmac_chk():
    cmd = "ifconfig -a | grep ^wlan | awk '{print $5}'"
    wmacAddr = run_cmd(cmd)
    return wmacAddr

def stalk_chk():
    cmd = "hostname"
    return run_cmd(cmd)


if __name__ == "__main__":
    now = time.localtime()
    
    fromU = "raspberry@pi.com"
    toU = "disk012@ajou.ac.kr"
    ccU = ["disk012@ajou.ac.kr", "tjdlsrn012@naver.com"]
    mail_subject = "Raspberry Pi IP Address Announcement!"
    mail_text = "ip: %s\n" % ip_chk() + "mac: %s\n" % mac_chk() + "wip: %s\n" % wip_chk() + "wmac: %s\n" % wmac_chk() + "stalk: %s\n\n\n" % stalk_chk() + "%04d/%02d/%02d %02d:%02d:%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    attach = None
   
    send_mail(fromU, toU, ccU, mail_subject, mail_text, attach)
