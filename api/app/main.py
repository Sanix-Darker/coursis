import json
import time
from api.app.utils import *

print("[+] Coursis started...")

search = input("[+] search: ")
pages = input("[+] pages: ")

fetched_items = process(search, pages)

with open("results.json", "w") as frr:
    json.dump(fetched_items, frr, indent=4)

print("[+] results: ", len(fetched_items))
print("[+] Done !")

