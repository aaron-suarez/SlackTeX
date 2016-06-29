# SlackTeX

## Disclaimer

The repository and the documentation come **without any warranty**, to the extent permitted by applicable law. For example, it is not guaranteed that the program will function normally or as expected and it is not guaranteed that if you follow the guidelines below correctly, you will have the program function normally or as expected.

Please be advised that you agree to use this repository and this documentation **at your own risk** if you decide to use them.

## How to use SlackTeX

After proper configuration, you can use SlackTeX directly on Slack by typing `/latex [formula]`  in the Slack message inbox box, where `[formula]`  is the formula that you want to render. For example, if you want to redner `\sum_{i=0}^n x_n` , simply type `/latex \sum_{i=0}^n x_n ` . If you want it to be in displayed math, please surround the formula with `$$`  before and after it, e.g., `/latex $$\sum_{i=0}^n x_n$$`.

An example that shows the command and its result on Slack is presented below.

```
/latex \sum_{n=1}^{\infty} 2^{-n} = 1
```

![ss](http://i.imgur.com/usMx4Au.png)

### Slash command

In previous examples, `/latex`  is termed a slash command of Slack. You can choose any available slash command that you want to typeset LaTeX as long as you configure it propoerly.

## Deployment

Please follow the steps below to deploy this project.

1. Fork this repository to your GitHub account.

2. Register a [Heroku account](https://www.heroku.com/) and start a new Heroku app.

3. Go to the *Deploy* tab on your Heroku app dashboard. 

4. Choose GitHub in the *Deployment method* and connect it to your forked repository.

5. In the *Manual deploy*, choose the branch *master* and then click *Deploy branch*.

6. Go to the *Settings* tab on your Heroku app dashboard and click *Reveal Config Vars*.

7. Add three config vars:

   - SLACK_API_TOKEN
   - SLACK_SLASH_COMMAND_TOKEN
   - SLACK_WEBHOOK_URL

   We will show how to set the values of the three config vars in the steps below.

8. Go to the [Slack API](https://api.slack.com/docs/oauth-test-tokens) page, click *issue token* to obtain your API token. SLACK_API_TOKEN should be set to the API token.

9. Go to `https://yourslackteam.slack.com/apps`  and find the app *Incoming WebHooks* via the search box. Click the *Add Configuration* button. This will bring you to a configuration page.

10. On the configuration page, choose a channel of your Slack team. You can choose any channel. The LaTeX integration should be in effect on every channel irrespective of the channel that you choose here.

11. Generate a Webhook URL and the config var SLACK_WEBHOOK_URL should be set to this Webhook URL.

12. After you finishe other configration items on this page, click *Save Settings*.

13. Go back to the page `https://yourslackteam.slack.com/apps` and find the app *Slash Commands* via the search box. Click *Add Configuration* button. This will bring your to another configuration page.

14. On the configuration page that you are brought to, input `/latex` or any available slash command that you like in the *Command* box.

15. In the *URL* box, put `https://yourherokuappname.herokuapp.com`.

16. In the *Method* box, choose *GET*.

17. In the *Token* box, click *generate* to generate a token. The config var SLACK_SLASH_COMMAND_TOKEN should be set to this token.

18. After you finish other configration items on this page, click *Save Integration*.

19. Doublecheck the three config vars on the Heroku dashborad and make sure that they are set correctly.

20. Enjoy using SlackTeX on your Slack!

### Minor reminders

If you use a free account to run your Heroku app, it will sleep after 30 minutes of inactiveness. When your app is sleeping, you can still use the command as usual but there would be a delay of approximately 9 seconds. This delay would occur only once when your app transition from the sleeping state to the awake state.

## Development

This part might be more useful for those interested in further development of this project.

The major part of the code resides in `SlackTeX/slacktex/views.py`. This Python script fine contains one function called `index`. The variable `latex`  is the LaTeX formula that the user inputs.

This project renders LaTeX formulas via [Google Chart API](https://developers.google.com/chart/infographics/docs/formulas). The variable `latex_url` is a concatenation of Google Chart address and the LaTeX formula, which is a link that will bring you to an image. You can replace Google Chart API by other LaTeX rendering services.


