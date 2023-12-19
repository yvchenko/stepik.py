# Вам дана в архиве (ссылка) файловая структура, состоящая из директорий и файлов.
#
# Вам необходимо распаковать этот архив, и затем найти в данной в файловой структуре все директории,
# в которых есть хотя бы один файл с расширением ".py".
#
# Ответом на данную задачу будет являться файл со списком таких директорий,
# отсортированных в лексикографическом порядке.
import os

paths = []

for contents in os.walk("main"):
    for file in contents[2]:
        if ".py" in file:
            paths.append(contents[0].replace("\\", "/"))
            break

paths.sort()

with open("problem_2_processed.txt", "w") as f:
    f.writelines('\n'.join(paths))
