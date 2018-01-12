from flask import Flask, request
from models import Slack
from urllib import quote, unquote_plus

app = Flask(__name__)


@app.route("/", methods=['POST'])
def index():
    if not request.form:
        message = """
        Welcome to SlackTeX!
        Check me out on <a href="https://github.com/aaron-suarez/slacktex">GitHub</a>.
        """

        return message

    slack = Slack()

    token = request.form["token"]
    latex = request.form["text"]
    channel_id = request.form["channel_id"]
    user_id = request.form["user_id"]

    if token != slack.SLASH_COMMAND_TOKEN:
        return "Unauthorized."

    asciify = {
        u'\u201c': '"',
        u'\u201d': '"',
        u'\u2018': "'",
        u'\u2019': "'",
        u'\u2026': "...",
    }
    for unicodeChar, asciiReplacement in asciify.iteritems():
        latex = latex.replace(unicodeChar, asciiReplacement)
    latex = quote(latex.encode("utf-8"))
    latex_url = "http://chart.apis.google.com/chart?cht=tx&chs=tx&chl={latex}".format(latex=latex)

    payload = {"channel": channel_id, "text": unquote_plus(latex)}
    user = slack.find_user_info(user_id)
    payload.update(user)

    attachments = [{"image_url": latex_url, "fallback": "Oops. Something went wrong."}]
    payload.update({"attachments": attachments})

    slack.post_latex_to_webhook(payload)

    return "", 200
    # return "Success!", 200
