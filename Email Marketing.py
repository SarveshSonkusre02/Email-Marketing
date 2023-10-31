import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email content
subject = "Stylish HTML Email"
sender_email = "ABC@gmail.com"
receiver_email = "abc@gmail.com"

# Create the HTML content
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Resume - Your Name</title>
    <style>
        <!-- your CSS Styles
    </style>
</head>
<body>
    <!--html Body-->
</body>
</html>

"""

# Create the email
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject
msg.attach(MIMEText(html_content, "html"))

# Connect to the SMTP server and send the email
smtp_server = "smtp.gmail.com"  # Update with your SMTP server
smtp_port = 587  # Update with the SMTP port for your email provider

# Initialize the SMTP server and set up a secure connection
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()  # Use TLS for secure connection
    server.login(sender_email, "XXXX XXXX XXXX XXXX")  # Replace with your email's password
    server.sendmail(sender_email, receiver_email, msg.as_string())

print("HTML email sent successfully.")
