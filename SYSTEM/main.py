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

        # 解析電子郵件內容
        msg = Parser().parsestr(data)
        print(f"Subject: {msg['Subject']}")
        print(f"Content-Type: {msg.get_content_type()}")
        print(msg.get_payload())

        # 您可以在這裡實現自定義的電子郵件處理邏輯
        # 例如,保存電子郵件到文件,或轉發到其他收件人等

        # 返回 '250 OK' 以表示電子郵件已成功接收
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
