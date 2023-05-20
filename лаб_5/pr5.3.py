class intTime:
 def geti(self):
  return 12345678

class strTime:
 def gets(self):
  return "87654321"

class Adapter(intTime,strTime):
 def get1(self):
  return str(self.geti())
 def get2(self):
  return int(self.gets())


work = Adapter()
intwork=intTime()
strwork=strTime()
#print("результат:" + intwork.geti()) выдаст ошибку
#print(intwork.geti()+strwork.gets()) выдаст ошибку
print("результат:" + work.get1())
print(work.get2()+intwork.geti())