# Одним из самых часто используемых классов в Python является класс filter. Он принимает в конструкторе два аргумента
# a и f – последовательность и функцию, и позволяет проитерироваться только по таким элементам x из последовательности
# a, что f(x) равно True. Будем говорить, что в этом случае функция f допускает элемент x, а элемент x
# является допущенным.
#
# В данной задаче мы просим вас реализовать класс multifilter, который будет выполнять ту же функцию, что и стандартный
# класс filter, но будет использовать не одну функцию, а несколько.

class multifilter:
    def judge_half(pos, neg):
        return True if pos >= neg else False

    def judge_any(pos, neg):
        return True if pos >= 1 else False

    def judge_all(pos, neg):
        return True if neg == 0 else False

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge
        self.i = 0
        self.pos = 0
        self.neg = 0

    def __iter__(self):
        for i in self.iterable:
            self.pos = 0
            self.neg = 0
            for func in self.funcs:
                if func(i):
                    self.pos += 1
                else:
                    self.neg += 1
            if self.judge(self.pos, self.neg):
                yield i
        return self
