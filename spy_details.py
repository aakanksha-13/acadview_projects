
from datetime import datetime
#this contains details of spy
class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None
        

#contains message,time which is sent by user
class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me
#Default spy details
spy = Spy('O Ha Ni', 'Ms.', 21, 4.9)
#spy friend's details
friend_one = Spy('Lee Min Ho', 'Mr.', 4.9, 27)
friend_two = Spy('Jan Di', 'Ms.', 4.39, 21)
friend_three = Spy('Jee Hu', 'Mr.',3.5, 45)

#list of friends
friends = [friend_one, friend_two, friend_three]
