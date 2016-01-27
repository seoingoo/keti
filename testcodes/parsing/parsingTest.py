# -*- coding: cp949 -*-

import urllib
import re


# Web Page Title 
url="https://mail.google.com/mail/u/0/#inbox"
Ga=urllib.urlopen(url).read()
Pur='<title>(.+?)</title>'
To=re.findall(Pur,Ga)
print To
