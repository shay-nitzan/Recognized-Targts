
#mail librarys
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_email(email_addr,target_num, num_id):
    # Sending mail
    msg = MIMEMultipart()
    msg['From'] = "ShootingRangeProject@gmail.com"
    msg['To'] = email_addr #change to user email
    msg['Subject'] = 'Shooting results of target ' + target_num
    body = 'Your image result: '
    msg.attach(MIMEText(body, 'plain'))
    
    path_linux = os.getcwd()+"/Users/"+num_id+"/output"+target_num+".jpg"
    attachment = open(path_linux, 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename=image_target"+target_num+".jpg")
    msg.attach(part)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("ShootingRangeProject@gmail.com", "Project2021")
    text = msg.as_string()
    server.sendmail("ShootingRangeProject@gmail.com", email_addr, text) #change to user email
    server.quit()


def send_email_statistics(email_addr, name, num_id):
    # Sending mail
    msg = MIMEMultipart()
    msg['From'] = "ShootingRangeProject@gmail.com"
    msg['To'] = email_addr #change to user email
    msg['Subject'] = 'Shooting results of statistics'
    body = 'Your image result: '
    msg.attach(MIMEText(body, 'plain'))
    
    path_linux = os.getcwd()+"/Users/"+num_id+ "/"+ name +".jpg"
    attachment = open(path_linux, 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename="+name+".jpg")
    msg.attach(part)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("ShootingRangeProject@gmail.com", "Project2021")
    text = msg.as_string()
    server.sendmail("ShootingRangeProject@gmail.com", email_addr, text) #change to user email
    server.quit()

if __name__ == "__main__":
    pass
    #send_email()