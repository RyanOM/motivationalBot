import json
import os
import sys
import random

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

        response = "Hey! Use the /motivateMe command to get some inspiration!"

        if "/motivateMe" in message:
            quote = random.choice(quote_list)
            response = '"%s" - %s' % (quote['quote'], quote['author'])

        data = {"text": response.encode("utf8"), "chat_id": chat_id}
        url = BASE_URL + "/sendMessage"
        requests.post(url, data)
        print(response)

    except Exception as e:
        print(e)

    return {"statusCode": 200}
