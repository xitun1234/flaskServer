from imap_tools import MailBox, AND
import imaplib
import email
import re

host = 'imap-mail.outlook.com'



def apiOTPLZD(mail, passMail):
    host = 'imap-mail.outlook.com'
    print("Mail: " + mail + "|pass: "+ passMail)
    with MailBox(host).login(mail, passMail ,'INBOX') as mailbox:
        result = []
        # get unseen emails from INBOX folder
        for msg in mailbox.fetch('Text "Lazada"'):
            resultHTML  = msg.html
            numbers = re.findall(r"\b\d{6}\b", resultHTML)
            result.append(numbers[0])

        lengthOTP = len(result)
        return result[lengthOTP-1]

def apiOTPFacebook(mail,passMail):
    host = 'imap-mail.outlook.com'
    with MailBox(host).login(mail, passMail, 'INBOX') as mailbox:
        result = []
        # get unseen emails from INBOX folder
        for msg in mailbox.fetch('Text "Facebook"'):
            #resultHTML  = msg.html
            numbers = re.findall(r"\b\d{5}\b", msg.subject)
            if (len(numbers) != 0):
                result.append(numbers[0])
    lengthOTP = len(result)
    return result[lengthOTP-1]

# otpLZD = apiOTPLZD("peltolbzehrerz@hotmail.com","9MyzOc39")
# print(otpLZD)
