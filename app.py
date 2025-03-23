from pandas import pandas as pd
from bs4 import BeautifulSoup
import requests
import csv
from flask import Flask

app = Flask(__name__)

df = pd.read_csv('data.csv')
html_df= df.to_html()

with open('data.html', 'w') as f:
    f.write(html_df)

@app.route('/')

def index():
    return html_df

if __name__ == '__main__':
    app.run(debug=True)

    app.run()

