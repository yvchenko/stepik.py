# Вам дано описание пирамиды из кубиков в формате XML.
# Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue).
# Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.
#
# Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML документа имеет ценность 1.
# Кубики, расположенные прямо под ним, имеют ценность 2. Кубики, расположенные прямо под нижележащими кубиками,
# имеют ценность 3. И т. д.
#
# Ценность цвета равна сумме ценностей всех кубиков этого цвета.
#
# Выведите через пробел три числа: ценности красного, зеленого и синего цветов.
from xml.etree import ElementTree

color_values = {"red": 0, "green": 0, "blue": 0}

pyramid = input().strip()


def calculate_color_values(xml_structure, value=0):
    value += 1
    color_values[xml_structure.attrib.get("color")] += value
    for cube in xml_structure:
        calculate_color_values(cube, value)


calculate_color_values(ElementTree.fromstring(pyramid))

print(*list(color_values.values()))
