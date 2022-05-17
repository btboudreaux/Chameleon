import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64

SEND_EMAIL_ADDRESS = "your_send_email@gmail.com"
SEND_EMAIL_PASSWORD = "your_password"


class Emailer:

    def send_email(self, game_id, topic, code, player_name, player_email, text):
        msg = MIMEMultipart("alternative")
        msg['Subject'] = f"Chameleon Game ID: {game_id}"
        # msg.attach(MIMEText(f"ID: {game_id}\n {text}", "plain", "utf-8"))
        msg.attach(MIMEText(f"<html><body><h1>ID: {game_id}<br>{player_name}: {text}</h1><br>"
                            f"<img src='cid:0'>"
                            f"<br><br><h2>⬇Scroll Down for Topic Card⬇</h2>"
                            f"<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>"
                            f"<img src='cid:1' width='800' height='540'></body></html>", "html", "utf-8"))
        with open(f"{code}", 'rb') as f:
            mime = MIMEBase("image", 'jpg', filename=code)
            mime.add_header("Content-Disposition", "attachment", filename=code)
            mime.add_header("X-Attachment-Id", "0")
            mime.add_header("Content-ID", "<0>")
            mime.set_payload(f.read())
            encode_base64(mime)
            msg.attach(mime)
        with open(f"{topic}", 'rb') as f:
            mime2 = MIMEBase("image", 'jpg', filename=topic)
            mime2.add_header("Content-Disposition", "attachment", filename=topic)
            mime2.add_header("X-Attachment-Id", "1")
            mime2.add_header("Content-ID", "<1>")
            mime2.set_payload(f.read())
            encode_base64(mime2)
            msg.attach(mime2)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=SEND_EMAIL_ADDRESS, password=SEND_EMAIL_PASSWORD)
            connection.sendmail(from_addr=SEND_EMAIL_ADDRESS,
                                to_addrs=player_email,
                                msg=msg.as_string())

    def send_codes(self, game_id, topic, code, player_list):
        for player in player_list[1:]:
            text = "You are NOT the Chameleon. Don't be so sus!"
            self.send_email(game_id, topic, code, player["Name"], player["Email"], text)
            print(f"Game ID: {game_id}: Sent Email...")
        for player in player_list[:1]:
            code = "images_chameleon/chameleon.jpg"
            text = "You ARE the Chameleon... Be Sneaky!"
            self.send_email(game_id, topic, code, player["Name"], player["Email"], text)
            print(f"Game ID: {game_id}: Sent Email... final.")
