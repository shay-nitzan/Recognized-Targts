import sys
import serial    
import os, time

"""ser = serial.Serial(port = '/dev/serial0',baudrate = 9600,timeout = 1) #ttyS0
ser.write(str.encode('AT'+'\r\n'))
time.sleep(2)
print(ser.readline())
print(ser.readline())
print(ser.readline())

ser.write(str.encode('ATE1'+'\r\n'))
time.sleep(2)
print(ser.readline())
print(ser.readline())
print(ser.readline())


ser.write(str.encode('AT+CMGF=1'+'\r\n'))
time.sleep(2)
print(ser.readline())
print(ser.readline())
print(ser.readline())
print(ser.readline())
print(ser.readline())"""


def send_sms(ser, phone_num, name_user, target_num, bullets_number_percentage): 
    ser.write(str.encode('AT+CMGS='+phone_num+'\r\n'))
    time.sleep(1)
    ser.write(str.encode('Hello '+name_user+','+'\n'+'an email with your shooting results of target '+target_num+ ' has been sent to your mailbox.'+'\r\n' + 'Your shooting accuracy is: '+bullets_number_percentage+'%'+'\r\n'))
    time.sleep(1)
    ser.write(str.encode('\x1A'))
    print(ser.readline())
    print(ser.readline())
    time.sleep(1)
    

def print_smssss(name_user, target_num, bullets_number_percentage):
    print('Hello '+name_user+','+'\n'+'an email with your shooting results of target '+target_num+ ' has been sent to your mailbox.'+'\r\n' + 'Your shooting accuracy is: '+bullets_number_percentage+'%'+'\r\n')


if __name__ == '__main__' :
    bullets_number_from_target = 9
    bullets_number_user = "11"
    bullets_number_percentage = str(round(bullets_number_from_target/int(bullets_number_user)*100, 2))
    print (bullets_number_percentage)

    #print_smssss("shay nitzan","2","86")
