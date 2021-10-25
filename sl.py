# This app is for educational purpose only. Insights gained is not financial advice. Use at your own risk!
import streamlit as st
from PIL import Image
import pandas as pd
import base64
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import json
import time
import streamlit.components.v1 as components

import json
import random
import statistics
import statistics as stat
import time
import random
from csv import writer

import oandapyV20
import oandapyV20.endpoints.accounts as accounts
import oandapyV20.endpoints.orders as orders
import pandas as pd
import v20
from scipy import stats
from scipy.stats import kendalltau
from scipy.stats import spearmanr
from sklearn import svm
from sklearn import tree
from sklearn.ensemble import RandomForestRegressor

RFEE = []
Euler = 0
ret = 0
her = 0
Sbfx = 0
svmp = []
Quant = 0
Sb = 0
wer = 0
EUL1 = 0
D1 = 0
tg1 = 0
Fs = 0
RF = []
TG = []
TW = []
TQ = []
trade = []
returns = []
TV = []
PV = []
T1 = 0
Sbf = 0
db = []
Speed = 1
Time = 1
t0 = 0
UC = 1
t1 = 0
EurUsd = [1.1800]
Area = 0
Chart = []
Long = 0
Short = 0
Ticks = 0
Distance = 1
D = []
BR = []
EUL = []
AREA = []
LT = []
ST = []
SBFX = []
T = []
S = []
SP = []
ST1 = 0
Exitl = 0
wer1 = 0
r = 0
wer = 0
her = 0
balance = 0
NAV = 0
Exits = 0
AREA1 = 0
SBFX1 = 0
LT1 = 0
EP = [1, 1]
sp = 0
ep = 0
LongTrend = 0
ShortTrend = 0
counter = 0
my_series = 0
last = 1
prev = 1
TP = 100
TickBar = 0

API = 'api-fxtrade.oanda.com'
ACCESS_TOKEN = \
    '65977df04d32049a40a9b64cb802ca6a-80ebe64ef60de9d9cfd787ef204a1966'
ACCOUNT_ID = '001-001-7053810-001'
client = oandapyV20.API(environment='live',
                        access_token='65977df04d32049a40a9b64cb802ca6a-80ebe64ef60de9d9cfd787ef204a1966'
                        )

api = v20.Context(hostname=API, token=ACCESS_TOKEN, port=443, ssl=True)

try:
    USDCHF = api.pricing.get(accountID=ACCOUNT_ID, instruments='EUR_NZD')
    USDCHF = json.loads(USDCHF.body['prices'][0].json())
    UC = USDCHF['closeoutBid']
    CU = USDCHF['closeoutAsk']
    EURUSD = api.pricing.get(accountID=ACCOUNT_ID, instruments='AUD_CAD')
    EURUSD = json.loads(EURUSD.body['prices'][0].json())
    EU = EURUSD['closeoutBid']
    UE = EURUSD['closeoutAsk']
    r = accounts.AccountDetails(ACCOUNT_ID)
    wer1 = client.request(r)
    wer = wer1["account"]["positions"][-13]["unrealizedPL"]
    her = wer1["account"]["openTradeCount"]
    her = float(her)
    wer = float(wer)
    balance = wer1["account"]["balance"]
    balance = float(balance)
    NAV = wer1["account"]["NAV"]
    NAV = float(NAV)
except Exception:
    pass
wer = wer1["account"]["positions"][0]["unrealizedPL"]
her = wer1["account"]["openTradeCount"]
her = float(her)
wer = float(wer)

lunits = wer1["account"]["positions"][0]["long"]["units"]
sunits = wer1["account"]["positions"][0]["short"]["units"]
lunits = float(lunits)
sunits = float(sunits)
units = lunits + sunits
st.metric('Current Units ', units)

balance = wer1["account"]["balance"]
balance = float(balance)
st.metric('The balance is ', balance)

NAV = wer1["account"]["NAV"]
NAV = float(NAV)
st.metric('The NAV is ', NAV)

pl = wer1["account"]["pl"]
pl = float(pl)
st.metric('The pl is ', pl)

mu = wer1["account"]["marginUsed"]
mu = float(mu)
st.metric('The marginUsed is ', mu)

test = random.uniform(1, 100)

st.button('Reload Account Data')

components.html(
    """
    <iframe
  src="https://app.uniswap.org/#/swap?use=v1?outputCurrency=0x89d24a6b4ccb1b6faa2625fe562bdd9a23260359"
  height="666px"
  width="100%"
  style="
    border: 0;
    margin: 0 auto;
    display: block;
    border-radius: auto;
    max-width: 1000px;
    min-width: 300px;
    



    
    
  "
  id="myId"
/>
    
    
    
    
    
    
    
    
<head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }} - My Django Application</title>
    {% load staticfiles %}
    <link rel="stylesheet" type="text/css" href="{% static 'app/content/bootstrap.min.css' %}" />
    <link rel="stylesheet" type="text/css" href="{% static 'app/content/site.css' %}" />
    <script src="{% static 'app/scripts/modernizr-2.6.2.js' %}"></script>
</head>

<body>
<div class="jumbotron">
    <h1>Django</h1>
    <p class="lead">Django is a free web framework for building great Web sites and Web applications using HTML, CSS and JavaScript.</p>
    <p><a href="https://www.djangoproject.com/" class="btn btn-primary btn-large">Learn more &raquo;</a></p>
</div>

<div class="row">
    <div class="col-md-4">
        <h2>Getting started</h2>
        <p>
            Django gives you a powerful, patterns-based way to build dynamic websites that
            enables a clean separation of concerns and gives you full control over markup
            for enjoyable, agile development.
        </p>
        <p><a class="btn btn-default" href="https://djangobook.com/django-tutorials/">Learn more &raquo;</a></p>
    </div>
    <div class="col-md-4">
        <h2>Get more libraries</h2>
        <p>The Python Package Index is a repository of software for the Python programming language.</p>
        <p><a class="btn btn-default" href="https://pypi.org/">Learn more &raquo;</a></p>
    </div>
    <div class="col-md-4">
        <h2>Microsoft Azure</h2>
        <p>You can easily publish to Microsoft Azure using Visual Studio. Find out how you can host your application using a free trial today.</p>
        <p><a class="btn btn-default" href="http://azure.microsoft.com">Learn more &raquo;</a></p>
    </div>
</div>




    <div class="navbar navbar-inverse navbar-fixed-top">
        <div class="container">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a href="/" class="navbar-brand">Application name</a>
            </div>
            <div class="navbar-collapse collapse">
                <ul class="nav navbar-nav">
                    <li><a href="{% url 'home' %}">Home</a></li>
                    <li><a href="{% url 'about' %}">About</a></li>
                    <li><a href="{% url 'contact' %}">Contact</a></li>
                </ul>
                {% include 'app/loginpartial.html' %}
            </div>
        </div>
    </div>

    <div class="container body-content">
{% block content %}{% endblock %}
        <hr/>
        <footer>
            <p>&copy; {{ year }} - My Django Application</p>
        </footer>
    </div>

    <script src="{% static 'app/scripts/jquery-1.10.2.js' %}"></script>
    <script src="{% static 'app/scripts/bootstrap.js' %}"></script>
    <script src="{% static 'app/scripts/respond.js' %}"></script>
{% block scripts %}{% endblock %}

</body>
    
    """,
    height=600,
)
