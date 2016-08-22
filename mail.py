# coding: utf-8

from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText  
import smtplib 

   
def send(info):   
   
    msg = MIMEMultipart()
    msg['to'] = ";".join(info['to_addr'])
    msg['cc'] = ";".join(info['cc_addr']) 
    msg['from'] = info['from_addr']   
    msg['Subject'] = info['mail_subject']    
    msg.attach(MIMEText(info['mail_text']))   
   
    smtp = smtplib.SMTP(info['server'], info['server_port'])
    smtp.ehlo()  
    smtp.starttls()  
    smtp.ehlo()   
    smtp.login(info['mail_user'], info['password'])   
    smtp.sendmail(msg['from'], msg['to'], msg.as_string())   
    smtp.close()  

