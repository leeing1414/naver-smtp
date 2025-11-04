import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys

# 메일 설정
SMTP_SERVER = "smtp.worksmobile.com"
SMTP_PORT = 465

# 발송자 이메일, 비밀번호 (메일 -> POP3 SMTP 설정에서 앱비밀번호 생성 필수)
SENDER_EMAIL="발송자 이메일"
SENDER_PASSWORD = "생성된 앱비밀번호"
RECIPIENT_EMAILS = ["수신자 이메일1", "수신자 이메일2"]

if not all([SENDER_EMAIL, SENDER_PASSWORD, RECIPIENT_EMAILS]):
    print("발송자 정보 설정이 안되어있습니다.")
    sys.exit(1)

try:
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "메일 제목"
    msg['From'] = SENDER_EMAIL              # 발송자 이메일
    msg['To'] = ", ".join(RECIPIENT_EMAILS) # 수신자 이메일 리스트

    msg.attach(MIMEText("본문 내용", 'html', 'utf-8'))     # 본문이 html 일 경우
    msg.attach(MIMEText("본문 내용", 'plain', 'utf-8'))    # 본문이 plainText 일 경우

    # 네이버는 SSL 연결 필수
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)

    print(f"이메일 발송 완료: {', '.join(RECIPIENT_EMAILS)}")
    sys.exit(0)

except Exception as e:
    print(f"이메일 발송 실패: {e}")
    sys.exit(1)

