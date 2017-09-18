import socket, sys, base64, ssl

MAILRU_SERVER_ADDRESS = ('smtp.mail.ru', 465)
GMAIL_SERVER_ADDRESS = ('smtp.gmail.com', 587)
GMAIL_SERVER_ADDRESS_1 = ('gmail-smtp-in.l.google.com', 25)

LOGIN = "computer_networks_kbtu@mail.ru"
PASSWORD = "Qwerty321"
CRLF = "\r\n"
EHLO_COMMAND = 'EHLO Almat' + CRLF

def extract_server_address(data):
	address = data.split()[1]
	return address + ""


def send_gmail_email(fromaddr, toaddr, subject=None, message=None):
	if subject is None:
		subject = ""
	
	if message is None:
		message = ""

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	s.connect(GMAIL_SERVER_ADDRESS_1)
	print "0: " + s.recv(1024)
	s.send("HELO codebusters.team" + CRLF)
	print "1: " + s.recv(1024)
	s.send("MAIL FROM: <{}>".format(fromaddr) + CRLF)
	print "2: " + s.recv(1024)
	s.send("RCPT TO: <{}>".format(toaddr) + CRLF)
	print "3: " + s.recv(1024)
	s.send("DATA" + CRLF)
	print "4: " + s.recv(1024)
	s.send("From: Almat Kenen <{}>".format(fromaddr) + CRLF)
	print "5: " + ""
	s.send("To: <{}>".format(toaddr) + CRLF)
	print "6: " + ""
	s.send("Subject: <{}>".format(subject) + CRLF)
	print "7: " + ""
	s.send(message + CRLF)
	s.send("." + CRLF)
	print "8: " + s.recv(1024)
	s.send("QUIT" + CRLF)
	print "9: " + s.recv(1024)


def send_mailru_email(fromaddr, toaddr, subject=None, message=None):

	if subject is None:
		subject = ""
	
	if message is None:
		message = ""

	sock = ssl.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM), ssl_version=ssl.PROTOCOL_SSLv23)

	sock.connect(MAILRU_SERVER_ADDRESS)

	print "0: " + sock.recv(1024)
	print "OK1"
	sock.send("EHLO smtp.mail.ru" + CRLF)
	print "1: " + sock.recv(1024)
	sock.send("AUTH LOGIN" + CRLF)
	print "2: " + sock.recv(1024)
	sock.send(base64.b64encode(LOGIN) + CRLF)
	print "3: " + sock.recv(1024)
	sock.send(base64.b64encode(PASSWORD) + CRLF)
	print "4: " + sock.recv(1024)

	sock.send("MAIL FROM: <{}>".format(LOGIN) + CRLF)
	print "5: " + sock.recv(1024) 
	sock.send("RCPT TO: <{}>".format(toaddr) + CRLF)
	print "6: " + sock.recv(1024)
	sock.send("DATA" + CRLF)
	print "7: " + sock.recv(1024)
	sock.send("From: Computer Networks <{}>".format(LOGIN) + CRLF)
	sock.send("To: <{}>".format(toaddr) + CRLF)
	sock.send("Subject: <{}>".format(subject) + CRLF)
	sock.send(message + CRLF)
	print "message: " + message
	sock.send("." + CRLF)
	print "8: " + sock.recv(1024)
	sock.send("QUIT" + CRLF)
	print "9: " + sock.recv(1024)

