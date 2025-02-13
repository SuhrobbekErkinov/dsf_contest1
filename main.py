from task1 import kwargsAcceptFun
from task2 import typeBasedTransformer
import random
from task3 import decorator_1

@decorator_1
def func():
    print("I am ready to Start")
    result = 0
    n = random.randint(10, 751)
    for i in range(n):
        result += (i**2)

@decorator_1
def funx(n=2, m=5):
    print("I am ready to do serious stuff")
    max_val = float('-inf')
    n = random.randint(10, 751)
    res = [pow(i, 2) for i in range(n)]
    for i in res:
        if i > max_val:
            max_val = i

if __name__ == "__main__":
    """------TASK 1------"""
    print("Hi, I am Python! Please enter your info:")
    name =  input("Name: ")
    age = input("Age: ")
    city = input("City: ")
    profession = input("Profession: ")
    kwargsAcceptFun(name = name, age = age, city = city, profession = profession)
    print("")

    """------TASK 2------"""
    print("Now, it is time for task 2!")
    data = typeBasedTransformer(
        num=4,
        pi=3.14,
        text="Hello",
        is_active= False,
        items=[1, 2, 3],
        dict={"a": 1, "b": 2},
        unknown=None
    )
    print("Data that has been changed: ", data)
    print("")

    """------TASK 3-------"""
    func()
    funx()
    func()
    funx()
    func()