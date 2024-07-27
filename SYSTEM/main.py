import smtpd
import asyncore
import email
from email.parser import Parser
print("givemetocode python stmp server v1.0 beta")
print("IF YOU FOUND THE BUG, PLEASE COMMENT AT GITHUB, THANK YOU.")
class CustomSMTPServer(smtpd.SMTPServer):
    def process_message(self, peer, mailfrom, rcpttos, data, **kwargs):
        print(f"Receiving message from: {mailfrom}")
        print(f"Sending to: {rcpttos}")

        
        msg = Parser().parsestr(data)
        print(f"Subject: {msg['Subject']}")
        print(f"Content-Type: {msg.get_content_type()}")
        print(msg.get_payload())

        

        
        return '250 OK'

print("Starting SMTP server...")
stmpport = input("the stmp server's port: ")
server = CustomSMTPServer(('localhost', stmpport), None)
print("SMTP server is running...")

try:
    asyncore.loop()
except KeyboardInterrupt:
    print("Stopping SMTP server...")
    server.close()
    print("the SMTP server stopped.")
