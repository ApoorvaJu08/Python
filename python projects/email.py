import smtplib
server = smtplib.SMTP('imap.gmail.com',587)
server.starttls()
sender_address = "apoorva10339@gmail.com'
password = "2308"
msg = "hello"
reciever_address = ""
server.login(sender_address,password)

