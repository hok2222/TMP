from abc import ABC, abstractmethod

class User():
 def __init__(self, med, name, st):
    self.mediator = med
    self.name = name
    self.statusmember = st

 @abstractmethod
 def send(self, msg):
  pass

 @abstractmethod
 def sendA(self, msg):
  pass

 @abstractmethod
 def sendO(self, msg):
  pass

 @abstractmethod
 def receive(self, msg):
  pass

class ChatMediator:
 def __init__(self):
  self.users = []
 def add_user(self, user):
  self.users.append(user)
 def send_message(self, msg, user):
  for u in self.users:
   if u != user:
    u.receive(msg)
 def send_messageA(self,msg,user):
  for u in self.users:
   if u != user and u.statusmember == "Administration":
    u.receive(msg)
 def send_messageO(self,msg,user):
  for u in self.users:
   if u != user and u.statusmember == "Other":
    u.receive(msg)

class ConcreteUser(User):
 def send(self, msg):
  print(self.name + ": отправил сообщение: " + msg)
  self.mediator.send_message(msg, self)
 def sendA(self, msg):
  print(self.name + ": отправил администрации: " + msg)
  self.mediator.send_messageA(msg, self)
 def sendO(self, msg):
  print(self.name + ": отправил штатным сотрудникам: " + msg)
  self.mediator.send_messageO(msg, self)
 def receive(self, msg):
  print(self.name + ": получено сообщение: " + msg)

def printl():
 print("-" * 50)

mediator = ChatMediator()
user1 = ConcreteUser(mediator, "Олег", "Administration")
user2 = ConcreteUser(mediator, "Маруся", "Administration")
user3 = ConcreteUser(mediator, "Даша", "Other")
user4 = ConcreteUser(mediator, "Глаша", "Other")
user5 = ConcreteUser(mediator, "Иван", "Other")

mediator.add_user(user1)
mediator.add_user(user2)
mediator.add_user(user3)
mediator.add_user(user4)
mediator.add_user(user5)

user1.send("Привет всем")
printl()

user1.sendA("Привет Администрация")
printl()

user1.sendO("Привет ОбычныеСотрудники")
printl()