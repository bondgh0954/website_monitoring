import requests
import smtplib
import os
import paramiko

response = requests.get('http://172.104.134.76:8080/')
res = response.status_code
EMAIL = os.environ.get('EMAIL')
PASS = os.environ.get('PASS')

print(res)

if res == 200:
    print('your application or website is running ok')
else:
    print('Website is down please check')

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.ehlo()
        smtp.login(EMAIL, PASS)
        msg = "SUBJECT: website issues \n Please website is down"
        smtp.sendmail(EMAIL, EMAIL, msg)


        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh.connect('', username='root', key_filename='')
        this = ssh.exec_command('docker ps')
        print(this)
