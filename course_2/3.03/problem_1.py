# Рассмотрим два HTML-документа A и B.
# Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">,
# возможно с дополнительными параметрами внутри тега.
# Из A можно перейти в B за два перехода если существует такой документ C, что из A в C можно перейти
# за один переход и из C в B можно перейти за один переход.
#
# Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
# Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.
#
# Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML
# документы.
import requests
import re


def fix_stepik(link):
    return link.replace("stepik", "stepic")


doc_a, doc_b = fix_stepik(input()), fix_stepik(input())


def get_links(doc):
    return [link.strip("href=").strip('"') for link in re.findall(r'href=".*"', fix_stepik(doc.text))]


def are_docs_connected(doc_a, doc_b):
    links = get_links(requests.get(doc_a))
    for link in links:
        if doc_b in get_links(requests.get(link)):
            return True
    return False


print("No" if not are_docs_connected(doc_a, doc_b) else "Yes")
