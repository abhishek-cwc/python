from Notification import Notification as Notify

class EmailNotification(Notify):

    def send(self, msg: str):
        print("Email send: ", msg)