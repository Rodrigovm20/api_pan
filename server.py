from flask import Flask
app = Flask(__name__)





@app.route("/api/panes")
def panes():
    import csv
    json = {}
    lista_panes = []
    with open('panes.csv', newline='', encoding='utf=8') as csvfile:
        spanreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in spanreader:
            lista_panes.append({"id":row[0], "nombre":row[1]})


    json["panes"] = lista_panes
    return json
