from Notification import Notification as Notify
class SmsNotification(Notify):

    def send(self, msg: str):
        print("Sms send: ", msg)