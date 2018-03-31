import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email import Encoders

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
#Next, log in to the server
server.login("YOUR.EMAIL@gmail.com", "PASSWORD.")

#Send the mail
msg = MIMEMultipart()

msg['Subject'] = "Here is attachment" 
msg['From'] = "YOUR.EMAIL@gmail.com"
msg['To'] = ', '.join("YOUR.FRIEND@gmail.com")

part = MIMEBase('application', "octet-stream")
part.set_payload(open("/home/mitu/Pictures/someIMAGE.png", "rb").read())
Encoders.encode_base64(part)

part.add_header('Content-Disposition', 'attachment; filename="someIMAGE.png"')

msg.attach(part)

server.sendmail("YOUR.EMAIL@gmail.com", "YOUR.FRIEND@gmail.com",msg.as_string())
