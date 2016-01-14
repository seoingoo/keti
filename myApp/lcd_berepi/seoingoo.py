import sys
sys.path.append("./lib")
from lcd import *
sys.path.append("../sht20")
from sht25 import *

def main():
    lcd_init()
    print "ip : %s" % ip_chk(), "wip : %s" % wip_chk(), "mac : %s" % mac_chk(), "wmac : %s" % wmac_chk(), "stalk : %s" % stalk_chk()

    while True:
        LCDoff()
        lcd_clear()
        time.sleep(1)
        lcd_string('Start Testing', LCD_LINE_1, 1)
        lcd_string('Text LCD ...', LCD_LINE_2, 1)
        GPIO.output(LCD_BLUE, False)
        time.sleep(0.5)
        GPIO.output(LCD_BLUE, True)
        GPIO.output(LCD_RED, False)
        time.sleep(0.5)
        GPIO.output(LCD_RED, True)
        GPIO.output(LCD_GREEN, False)
        time.sleep(0.5)
        GPIO.output(LCD_RED, False)
        time.sleep(0.5)
        GPIO.output(LCD_GREEN, True)
        GPIO.output(LCD_BLUE, False)
        time.sleep(0.5)
        GPIO.output(LCD_RED, True)
        GPIO.output(LCD_GREEN, False)
        time.sleep(0.5)
        GPIO.output(LCD_RED, False)
        time.sleep(0.5)
        
        str='18.9254'
        skyeLCDon()
        lcd_string('Temperature', LCD_LINE_1, 2)
        lcd_string('%.5s `C' % (str), LCD_LINE_2, 2)
        time.sleep(1.5)

        str1=ip_chk()
        str1=str1[:-1]
        str2=mac_chk()
        str2=str2[:-1]
        GPIO.output(LCD_RED, True)
        GPIO.output(LCD_BLUE, False)
        GPIO.output(LCD_GREEN, False)
        lcd_string('%s ET' % (str1), LCD_LINE_1, 1)
        lcd_string('%s' % (str2), LCD_LINE_2, 1)
        time.sleep(1.5)
        
        str1=wip_chk()
        str1=str1[:-1]
        str2=wmac_chk()
        str2=str2[:-1]
        pinkLCDon()
        lcd_string('%s WL' % (str1), LCD_LINE_1, 1)
        lcd_string('%s' % (str2), LCD_LINE_2, 1)
        time.sleep(1.5)
        
        str=stalk_chk()
        str=str[:-1]
        whiteLCDon()
        lcd_string('sTalk Channel', LCD_LINE_1, 2)
        lcd_string('%s' % (str), LCD_LINE_2, 2)
        time.sleep(1.5)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        lcd_byte(0x01, LCD_CMD)
        lcd_string("Goodbye!", LCD_LINE_1,2)
        time.sleep(1)
        LCDoff()
        GPIO.cleanup()
