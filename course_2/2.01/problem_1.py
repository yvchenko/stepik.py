# Вашей программе будет доступна функция foo, которая может бросать исключения.
#
# Вам необходимо написать код, который запускает эту функцию, затем ловит исключения
# ArithmeticError, AssertionError, ZeroDivisionError и выводит имя пойманного исключения.

def foo():
    pass


try:
    foo()
except (ZeroDivisionError, AssertionError) as e:
    print(e.__class__.__name__)
except ArithmeticError:
    print("ArithmeticError")
