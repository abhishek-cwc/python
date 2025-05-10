from SmsNotification import SmsNotification
from EmailNotification import EmailNotification

class NotificationFactory:

    @staticmethod
    def createFactory(channel: str):
        if channel == "sms":
            return SmsNotification()
        elif channel == "email":
            return EmailNotification()
        else:
            raise ValueError("Unknow channle error")     

################### Run Code ##########################

str = "sms"
obj = NotificationFactory.createFactory(str)
obj.send("Sms")

str = "email"
obj = NotificationFactory.createFactory(str)
obj.send("Email")

try:
    str = "push"
    obj = NotificationFactory.createFactory(str)
    obj.send("Push")
except (ValueError) as e:
    print(e)

