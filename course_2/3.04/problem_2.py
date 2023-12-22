# Вам дано описание наследования классов в формате JSON.
# Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого JSON-объекта есть
# поле name, которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.
#
# Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс не
# наследуется явно от одного класса более одного раза.
#
# Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.
#
# <имя класса> : <количество потомков>
#
# Выводить классы следует в лексикографическом порядке.
import json

classes_info = {}
classes_list = json.loads(input())


def is_parent(parent, child):
    if child == parent:
        return True

    for p in classes_info.get(child):
        if is_parent(parent, p):
            return True

    return False


for class_description in classes_list:
    classes_info[class_description.get("name")] = class_description.get("parents")

classes_info = dict(sorted(classes_info.items()))

for class_name in classes_info.keys():
    children = 0
    for child in classes_info.keys():
        if is_parent(class_name, child):
            children += 1
    print(f"{class_name} : {children}")
