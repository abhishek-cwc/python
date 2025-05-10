from abc import ABC, abstractmethod

class Notification(ABC):

    def send(self, msg: str):
        pass