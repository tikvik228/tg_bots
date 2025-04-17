'''import sys
from collections import defaultdict


data = list(map(lambda x: int(x.strip()), sys.stdin))
slovar = {}
nums_was = []
for i in data:
    if i in nums_was:
        continue
    else:
        nums_was.append(i)
        slovar[i] = []
    for prov in range(2, i // 2 + 1):
        if prov % 2 == 1 and i % prov == 0:
            slovar[i].append(prov)
    #if i not in slovar.keys():
    #    slovar[i] = []

for k, v in slovar.items():
    slovar[k] = sorted(v)
print(slovar)'''

'''import requests
import sys
import json


data = list(map(str.strip, sys.stdin))
port = data[0]
word = data[1]
giant = int(data[2])

response = requests.get(f'http://127.0.0.1:{port}')
dataa_ = response.json()

otv = {}
for i in dataa_:
    if word in i['built'] and i['giant'] >= giant:
        if i['place'] in otv.keys():
            otv[i['place']].append(i['built'])
        else:
            otv[i['place']] = [i['built']]

otv = dict(sorted(otv.items()))
for k, v in otv.items():
    otv[k] = sorted(v)
    vst = ", ".join(sorted(v))
    print(f"{k}: {vst}")'''


import sqlite3

predmet = input()
db_name = input()
con = sqlite3.connect(db_name)
cur = con.cursor()

epoche = cur.execute(f'''SELECT epoch FROM Epochs WHERE id=(SELECT epoch_id from
Mysterious WHERE thing='{predmet}')''').fetchone()[0]
game_ = cur.execute(f'''SELECT game FROM Games WHERE id=(SELECT game_id from
Mysterious WHERE thing='{predmet}')''').fetchone()[0]
otv = cur.execute(f'''SELECT thing FROM Mysterious WHERE epoch_id=(SELECT id FROM Epochs WHERE epoch='{epoche}')
AND game_id=(SELECT id FROM Games WHERE game='{game_}')''').fetchall()
okonch_otv = []
for i in otv:
    okonch_otv.append(i[0])
okonch_otv = sorted(okonch_otv)
okonch_otv = sorted(okonch_otv, key=lambda x: len(x), reverse=True)
print(*okonch_otv, sep='\n')
con.close()

