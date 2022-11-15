import time
import sys
import serial

import cv2 as cv
from send_sms import *
from email_fun import send_email, send_email_statistics
from camera_fun import take_picture
from fun_targets import process_image, show_statistics

ser = serial.Serial(port = '/dev/serial0',baudrate = 9600,timeout = 1) #ttyS0
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
print(ser.readline())

def target_image_process(phone_num, name_user, email_addr, num_id, target_num, bullets_number_user):
    take_picture("target"+target_num, num_id)

    #path_windows = os.getcwd()+"\\Users\\"+num_id+"\\target"+target_num+".jpg"
    path_linux = os.getcwd()+"/Users/"+num_id+"/target"+target_num+".jpg"

    img = cv.imread(path_linux)

    bullets_number_from_target = process_image(img, "output"+target_num, num_id) # return bullets_number_from_target from the function
    bullets_number_percentage = str(round(bullets_number_from_target/int(bullets_number_user)*100, 2))
    if (float(bullets_number_percentage) > float(100)):
        bullets_number_percentage = "100"

    send_sms(ser, phone_num, name_user, target_num, bullets_number_percentage)
    send_email(email_addr, target_num, num_id)

def show_the_statistics(email_addr, num_id, num_images):
    name = show_statistics(num_id)
    if (name != -1):
        send_email_statistics(email_addr, name, num_id)
    return name


if __name__ == '__main__' :
    bullets_number_from_target = 17
    bullets_number_user = 16
    bullets_number_percentage = str(round(bullets_number_from_target/int(bullets_number_user)*100, 2))
    if (float(bullets_number_percentage) > float(100)):
        bullets_number_percentage = "100"
    print(bullets_number_percentage)