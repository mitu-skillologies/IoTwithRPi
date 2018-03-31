import picamera, time
import smtplib, os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders

camera = picamera.PiCamera()
camera.start_preview()
time.sleep(5) # hang for preview for 5 seconds
os.remove('snapshot.jpg')
camera.capture('snapshot.jpg')
camera.stop_preview()

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
#Next, log in to the server
server.login("YOUR.MAILID@gmail.com", "PASSWORD")

#Send the mail
msg = MIMEMultipart()

msg['Subject'] = "New person is coming..." 
msg['From'] = "YOUR.MAILID@gmail.com"
msg['To'] = ', '.join("YOUR.FRIEND@gmail.com")

part = MIMEBase('application', "octet-stream")
part.set_payload(open("snapshot.jpg", "rb").read())
Encoders.encode_base64(part)

part.add_header('Content-Disposition', 'attachment; filename="snapshot.jpg"')

body = "Open lock from here: http://localhost/servo.php"
msg.attach(MIMEText(body, 'plain'))
msg.attach(part)

server.sendmail("YOUR.MAILID@gmail.com", "YOUR.FRIEND@gmail.com",msg.as_string())
