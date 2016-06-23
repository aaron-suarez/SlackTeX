from flask import Flask, request
from models import Slack
from urllib import quote

import urllib2


app = Flask(__name__)


@app.route("/")
def index():
    if not request.args:
        message = """
        Welcome to SlackTeX!
        Check me out on <a href="https://github.com/nicolewhite/slacktex">GitHub</a>.
        """

        return message

    slack = Slack()

    token = request.args["token"]
    latex_raw = request.args["text"]
    channel_id = request.args["channel_id"]
    user_id = request.args["user_id"]

    if token != slack.SLASH_COMMAND_TOKEN:
        return "Unauthorized."

    latex = quote(latex_raw)
    latex_url = "http://chart.apis.google.com/chart?cht=tx&chl={latex}".format(latex=latex)

    headrequest = urllib2.Request(latex_url)
    headrequest.get_method = lambda : 'HEAD'
    try:
        response = urllib2.urlopen(headrequest)
    except:
        return "Invalid expression:\n" + latex_raw
    else:
        payload = {"channel": channel_id}
        user = slack.find_user_info(user_id)
        payload.update(user)

        attachments = [{"image_url": latex_url, "fallback": "Oops. Something went wrong."}]
        payload.update({"attachments": attachments})

        slack.post_latex_to_webhook(payload)

        return "", 200
    # return "Success!", 200
