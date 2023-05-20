from abc import ABC, abstractmethod

class Product:
 dough = ["дрожжевое", "слоёное"]
 meat = ['курица', 'колбаса']
 top = ['сыр', 'оливки', 'помидорки', 'огурчики']
 souse = ["томатный", "песто"]

class pizza:
 def __init__(self, name):
  self.name = name
  self.meat = None
  self.topping = []
  self.souse = None
  self.dough = None
 def printer(self):
  print(f'название:{self.name}\n' \
        f'мясо:{self.meat}\n' \
        f'начинка:{[it for it in self.topping]}\n' \
        f'соус:{self.souse}\n' \
        f'тесто:{self.dough}\n')

class Builder(ABC):
 @abstractmethod
 def add_souce(self) -> None: pass
 @abstractmethod
 def add_meat(self) -> None: pass
 @abstractmethod
 def add_topping(self) -> None: pass
 @abstractmethod
 def prepare_dough(self) -> None: pass
 @abstractmethod
 def get_piz(self) -> pizza: pass

class Director:
 def __init__(self):
  self.builder = None
 def set_builder(self, builder: Builder):
  self.builder = builder
 def make_piz(self):
  if not self.builder:
   raise ValueError("Builder didn't set")
  self.builder.add_souce()
  self.builder.add_meat()
  self.builder.add_topping()
  self.builder.prepare_dough()

class HomePiz(Builder):
 def __init__(self):
  self.piz = pizza("Домашняя")
 def add_souce(self) -> None:
  self.piz.souse = Product.souse[0]
 def add_meat(self) -> None:
  self.piz.meat = Product.meat[1]
 def add_topping(self) -> None:
  self.piz.topping.append(Product.top[0])
  self.piz.topping.append(Product.top[1])
  self.piz.topping.append(Product.top[2])
  self.piz.topping.append(Product.top[3])
 def prepare_dough(self) -> None:
  self.piz.dough = Product.dough[0]
 def get_piz(self) -> pizza:
  return self.piz

class PestoPiz(Builder):
 def __init__(self):
  self.piz = pizza("Песто с курицей")
 def add_souce(self) -> None:
  self.piz.souse = Product.souse[1]
 def add_meat(self) -> None:
  self.piz.meat = Product.meat[0]
 def add_topping(self) -> None:
  self.piz.topping.append(Product.top[0])
  self.piz.topping.append(Product.top[1])
 def prepare_dough(self) -> None:
  self.piz.dough = Product.dough[1]
 def get_piz(self) -> pizza:
  return self.piz

director = Director()
print("Домашняя-1, Песто с курицей-2")
a=int(input())
if a==1:
 builder = HomePiz()
else:
 builder = PestoPiz()
director.set_builder(builder)
director.make_piz()
pizza = builder.get_piz()
pizza.printer()
