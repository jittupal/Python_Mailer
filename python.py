import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_mail(workflow_name, repo_name, workflow_run_ID):
    sender_email = os.getenv('Sender_Email')
    sender_password = os.getenv('Sender_Password')
    receiver_email = os.getenv('Receiver_Email')
    
    subject = f"Workflow {workflow_name} failed for repo {repo_name}"
    body = f"workflow  {workflow_name} failed for the repo {repo_name} and runner id {workflow_run_ID}"
    
    msg = MIMEMultipart()
    msg['from'] = sender_email
    msg['to'] = receiver_email
    msg['subject'] = subject
    msg.attach(MIMEMultipart(body, 'plain'))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()
        
    except Exception as e:
        print(f'error: {e}')
        

    