from abc import ABC, abstractmethod
from typing import List

class OrderItemVisitor(ABC):
    @abstractmethod
    def visit(self, item) -> float:
        ...

class ItemElement(ABC):
    @abstractmethod
    def accept(self, visitor: OrderItemVisitor) -> float:
        ...

class Bakery(ItemElement):
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def get_price(self) -> float:
        return self.price

    def accept(self, visitor: OrderItemVisitor) -> float:
        return visitor.visit(self)

class Coffee(ItemElement):
    def __init__(self, name: str, price: float, capacity: float):
        self.name = name
        self.price = price
        self.capacity = capacity

    def get_price(self) -> float:
        return self.price

    def get_capacity(self) -> float:
        return self.capacity

    def accept(self, visitor: OrderItemVisitor) -> float:
        return visitor.visit(self)

class WithOutDiscountVisitor(OrderItemVisitor):
    def visit(self, item: ItemElement) -> float:
        cost = 0
        if isinstance(item, Bakery):
            cost = item.get_price()
        elif isinstance(item, Coffee):
            cost = item.get_capacity() * item.get_price()
        return cost

class OnlyBakeryDiscountVisitor(OrderItemVisitor):
    def visit(self, item: ItemElement) -> float:
        cost = 0
        if isinstance(item, Bakery):
            cost = item.get_price()
            cost -= cost * 0.25 #Скидка 25%
        elif isinstance(item, Coffee):
            cost = item.get_capacity() * item.get_price()
        return cost


class OnlyCoffeeDiscountVisitor(OrderItemVisitor):
    def visit(self, item: ItemElement) -> float:
        cost = 0
        if isinstance(item, Bakery):
            cost = item.get_price()
        elif isinstance(item, Coffee):
            cost = item.get_capacity() * item.get_price()
            cost -= cost * 0.30 #Скидка 30% на кофе
        return cost

class AllDiscountVisitor(OrderItemVisitor):
    def visit(self, item: ItemElement) -> float:
        cost = 0
        if isinstance(item, Bakery):
            cost = item.get_price()
        elif isinstance(item, Coffee):
            cost = item.get_capacity() * item.get_price()
        cost -= cost * 0.45 #Скидка 45% на всю продукцию
        return cost

class Waiter:
    def __init__(self, discount: OrderItemVisitor):
        self.order: List[ItemElement] = []
        self.discount_calculator = discount

    def set_order(self, order: List[ItemElement]) -> None:
        self.order = order

    def set_discount(self, discount: OrderItemVisitor) -> None:
        self.discount_calculator = discount

    def calculate_finish_price(self) -> float:
        price = 0
        if self.order:
            for item in self.order:
                price += item.accept(self.discount_calculator)
        return price

order: List[ItemElement] = [Bakery("круассан", 45),
                            Coffee("латте мал", 3, 100),
                            Bakery("улитка с изюмом", 30),
                            Coffee("капучино бол", 5, 80),
                            Bakery("чизкейк", 100)]
discount = WithOutDiscountVisitor()
waiter = Waiter(discount)
waiter.set_order(order)

n=1
while n==1:
    print("Введите скидку: без скидки, выпечка, кофе, все позиции")
    vibor=input()
    while vibor not in ("без скидки", "выпечка", "кофе", "все позиции"):
        print("повторите ввод")
        vibor=input()

    if vibor=="без скидки":
        discount = WithOutDiscountVisitor()
        waiter = Waiter(discount)
        waiter.set_order(order)
        print(f"Сумма заказа без учета скидок: "
              f"{round(waiter.calculate_finish_price(),2)}")

    elif vibor=="выпечка":
        discount = OnlyBakeryDiscountVisitor()
        waiter.set_discount(discount)
        print(f"Сумма заказа c учетом скидки на выпечку: "
              f"{round(waiter.calculate_finish_price(),2)}")

    elif vibor=="кофе":
        discount = OnlyCoffeeDiscountVisitor()
        waiter.set_discount(discount)
        print(f"Сумма заказа c учетом скидки на кофе: "
              f"{round(waiter.calculate_finish_price(),2)}")
    elif vibor=="все позиции":
        discount = AllDiscountVisitor()
        waiter.set_discount(discount)
        print(f"Сумма заказа c учетом скидки на всё: "
              f"{round(waiter.calculate_finish_price(),2)}")
    print("хотите повторить? 1-да")
    n = int(input())
print("спасибо за заказ!")