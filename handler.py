import json
import os
import sys
import random
import logging

from quote_list import quote_list

here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "./vendored"))

import requests

TOKEN = os.environ['TELEGRAM_TOKEN']
BASE_URL = "https://api.telegram.org/bot{}".format(TOKEN)


def hello(event, context):
    try:
        data = json.loads(event["body"])
        message = str(data["message"]["text"])
        chat_id = data["message"]["chat"]["id"]

        response = "Hey! Use the /motivate command to get some inspiration!"

        if "/motivate" in message:
            quote = random.choice(quote_list)
            response = '"%s" - %s' % (quote['quote'], quote['author'])

        if "/status" in message:
            response = "Motivating people since June 13th 2018!"

        data = {"text": response.encode("utf8"), "chat_id": chat_id}
        url = BASE_URL + "/sendMessage"
        requests.post(url, data)
        logging.info(response)

    except Exception as e:
        logging.error(e)

    return {"statusCode": 200}
