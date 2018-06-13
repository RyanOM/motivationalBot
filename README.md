# MotivationalBot
A Telegram bot that gives you some motivation.
Built using Python3, AWS Lambda and [Serverless](https://serverless.com/).

The motivation quotes are stored in the `quote_list.py` file.

## Live Demo

You can contact the bot via Telegram using this link:
[https://web.telegram.org/#/im?p=@ryansMotivationalBot](https://web.telegram.org/#/im?p=@ryansMotivationalBot)


## Requirements

- Python3
- An AWS account
- [Serverless](https://serverless.com/)
- Nodejs

## Setup

Make sure Serverless is installed:
```
npm install -g serverless
```

Install the python dependencies locally:
```
pip install -r requirements.txt -t vendored
```

[Generate AWS access keys](https://serverless.com/framework/docs/providers/aws/guide/credentials/) and export them:
```
export AWS_ACCESS_KEY_ID=<your-key-here>
export AWS_SECRET_ACCESS_KEY=<your-secret-key-here>
# AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY are now available for serverless to use
serverless deploy
```

Keep to the side the url generated (that's your Lambda's endpoint), which should look something like this:
```
endpoints:
  POST - https://egmwgr53.execute-api.us-east-1.amazonaws.com/dev/my-custom-url
```

Set up a Telegram bot by contacting the [@BotFather](https://web.telegram.org/#/im?p=@BotFather).
Once finishing the steps, you will receive a `TELEGRAM_TOKEN` that should look like:
```
se this token to access the HTTP API:
25264639168:geklgnmKLNFJbege-u1oMR3
```

Export the `TELEGRAM_TOKEN`:
```
export TELEGRAM_TOKEN="<YOUR TELEGRAM TOKEN>"
```

Create the webhook to connect your Lambda with the Telegram bot:
```
curl --request POST --url https://api.telegram.org/botA<YOUR TELEGRAM TOKEN>/setWebhook --header 'content-type: application/json' --data '{"url": "<Your Lambda's endpoint url>"}'
```

You should receive the following if everything worked:
```
{"ok":true,"result":true,"description":"Webhook was set"}
```

Update your Lambda's `TELEGRAM_TOKEN` by deploying again:
```
serverless deploy
```

You should now be able to communicate with your bot!

You can customize your bot via the [@BotFather](https://web.telegram.org/#/im?p=@BotFather) by using the `/mybots` command.
