import json
import os

for trans_rep in os.listdir("reports"):
    f = os.path.join("reports", trans_rep)
    if os.path.isfile(f):
        print(f)
