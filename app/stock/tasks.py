import requests
import logging

from django.conf import settings

from app.celery_app import app as celery_app
from stock.bot_rules.request_parcer import stock_parser

log = logging.getLogger("celery")

@celery_app.task
def minute_bot():
    url = "https://stooq.com/q/l/?s=aapl.us&f=sd2t2ohlcv&h&e=csv"
    response = requests.get(url)

    if response.status_code !=200:
        log.error("could not get stock")
        return "ROBOT FAILED"
    response_text = response.text

    stock_string = stock_parser(response_text)
    stocks = stock_string.split(",")
    application_url = settings.STOCK_ROBOT_URL
    application_token = settings.APPLICATION_TOKEN # generated uuid

    for stock in stocks:
        json_data = {
            "token": application_token,
            "stock": stock
        }
        
        application_response = requests.post(application_url+"/stock", json=json_data)
        if application_response.status_code != 200:
            return "ROBOT FAILED"
        
        sleep(1)

