from flask import Flask
import csv
import sqlite3


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ytrewq'

@app.route('/jewelry/<place>/')
def base(place):
    with open('bottoms.csv', encoding="utf8") as csvfile:
        reader = list(csv.DictReader(csvfile, delimiter=';', quotechar='"'))
        print(reader)
        con = sqlite3.connect('finds.db')
        cur = con.cursor()
        id_place = cur.execute(f'''SELECT id FROM Places WHERE place="{place}"''').fetchone()[0]
        maybe_fit = []
        for i in reader:
            if i['place_id'] == str(id_place):
                maybe_fit.append((i['find'], int(i['type_id'])))
        maybe_fit = sorted(maybe_fit, key=lambda x: x[0])
        maybe_fit = sorted(maybe_fit, key=lambda x: x[1], reverse=True)
        otv = []
        for n in range(5):
            if n < len(maybe_fit):
                otv.append(maybe_fit[n])
        return otv


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')