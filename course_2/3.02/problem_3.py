# Вам дана последовательность строк.
# Выведите строки, содержащие две буквы "z", между которыми ровно три символа.

import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    if re.search(r"z.{3}z", line):
        print(line)
