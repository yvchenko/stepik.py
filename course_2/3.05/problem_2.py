# В этой задаче вам необходимо воспользоваться API сайта artsy.net
#
# API проекта Artsy предоставляет информацию о некоторых деятелях искусства, их работах, выставках.
#
# В рамках данной задачи вам понадобятся сведения о деятелях искусства (назовем их, условно, художники).
#
# Вам даны идентификаторы художников в базе Artsy.
# Для каждого идентификатора получите информацию о имени художника и годе рождения.
# Выведите имена художников в порядке неубывания года рождения. В случае если у художников одинаковый год рождения,
# выведите их имена в лексикографическом порядке.
import requests

artist_data = []

client_id = '18d89f38ac2abb898b98'
client_secret = '1197273dd67c42eccd4d1d5a63305053'

with open("problem_2_dataset.txt") as f:
    artists = f.read().strip().split("\n")

token = requests.post(
    "https://api.artsy.net/api/tokens/xapp_token",
    data={"client_id": client_id, "client_secret": client_secret}
).json().get("token")

for artist in artists:
    artist_details = requests.get(
        f"https://api.artsy.net/api/artists/{artist}", headers={"X-Xapp-Token": token}
    ).json()
    artist_data.append((artist_details.get("birthday"), artist_details.get("sortable_name")))

artist_data.sort()

with open("problem_2_dataset_processed.txt", "w", encoding="utf-8") as f:
    [f.write(artist[1] + "\n") for artist in artist_data]
