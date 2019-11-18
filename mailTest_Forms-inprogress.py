import smtplib, ssl
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
import getForms

# list of all contacts
contacts = getForms.getContacts()

def messageSetup(email):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "pythontest420420@gmail.com"  # Enter your address
    receiver_email = f"{email}"  # Enter receiver address
    password = 'pyth0nt35t'
    message = MIMEMultipart("alternative")
    message["Subject"] = "Today's Weather!"
    message["From"] = sender_email
    message["To"] = receiver_email

#
imgCount = 0

# add images to message
def addImage(image):
    global imgCount
    with open(f'{image}', 'rb') as f:
        # set attachment mime and file name, the image type is png
        mime = MIMEBase('image', 'png', filename=f'{image}')
        # add required header data:
        mime.add_header('Content-Disposition', 'attachment', filename=f'{image}')
        mime.add_header('X-Attachment-Id', f'{imgCount}')
        mime.add_header('Content-ID', f'<{imgCount}>')
        # read attachment file content into the MIMEBase object
        mime.set_payload(f.read())
        # encode with base64
        encoders.encode_base64(mime)
        # add MIMEBase object to MIMEMultipart object
        message.attach(mime)
    imgCount += 1

images = ('TempZoomedIn.png','TempZoomedOut.png')

def makeMessage(name,date,analytics,interpretation,analyticsHTML,interpretationHTML):
    
    for image in images:
        addImage(image)

    text = f"""\
Good morning, {name}!
{interpretation}

Here are the analytics:
{analytics}
"""
    html=f"""\
<html>
    <body>
        <p>Good morning, {name}!</p>
        <p>Today is {date}</p>
        <p>{interpretationHTML}</p>
        <p>{analyticsHTML}</p>
        <img src="cid:0">
        <img src="cid:1">
    </body>
</html>
    """
    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())