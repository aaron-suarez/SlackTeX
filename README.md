# SlackTeX

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






