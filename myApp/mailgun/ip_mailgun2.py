import smtplib

from email.mime.text import MIMEText

import time, os
from subprocess import *

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

# print ip_chk(), mac_chk(), wip_chk(), wmac_chk(), stalk_chk()

now = time.localtime()

msg = MIMEText('ip : %s\nmac : %s\nwip : %s\nwmac : %s\nstalk : %s\n\n\n' % (ip_chk(), mac_chk(), wip_chk(), wmac_chk(), stalk_chk()) + '%04d/%02d/%02d %02d:%02d:%02d' % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec))
msg['Subject'] = "Raspberry Pi IP Address Announcement!"
msg['From'] = "raspberry@pi.com"
msg['to'] = "disk012@ajou.ac.kr"

s = smtplib.SMTP('smtp.mailgun.org', 587)

s.login('postmaster@sandboxd13de7857b744ce1872cea0b767eeb12.mailgun.org',
'49dfd47c9017e9e1fe3215c279a70e67')
s.sendmail(msg['From'], msg['To'], msg.as_string())
s.quit()
