import csv
import json
djins = []
was = []
with open('gifts.csv', encoding="utf8") as csvfile:
    reader = list(csv.DictReader(csvfile, delimiter=';', quotechar='"'))
    for i in reader:
        if i['who'] not in was:
            was.append(i['who'])
            djins.append({"name": i['who'], "gift": [i['what']], "whom": [i['whom']], "ave_age": [i['age']]})
        else:
            djins[was.index(i['who'])]['gift'].append(i['what'])
            djins[was.index(i['who'])]['whom'].append(i['whom'])
            djins[was.index(i['who'])]['ave_age'].append(i['age'])

with open('genie.jsonl', 'w') as file:
    for i in djins:
        i['gift'] = sorted(i['gift'])
        i['whom'] = sorted(i['whom'])
        i['ave_age'] = int(sum(list(map(lambda x: int(x), i['ave_age']))) / len(i['ave_age']))
        data = json.dumps(i)
        file.write(data)
        file.write('\n')

