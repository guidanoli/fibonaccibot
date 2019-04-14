# Fibonacci Bot

This bot is a proof of concept: bots that depend on previous posts to output a new one.

I couldn't think of a better way to demonstrate this than with the famous [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number). a pattern with natural properties found all over nature. It is also ruled by a simple recursive definition, which facilitates the computation a lot.

This project also helped me to get used to [GraphAPI](https://developers.facebook.com/docs/graph-api/), [Amazon Web Services Lamba](https://aws.amazon.com/pt/lambda/) and to the growing Facebook bot community. So I write this documentation focusing on those interested in messing around with these tools by themselves, and, hopefully, create bots of their own.

#### Manager

The manager batch file is there to help you with some basic tasks. The commands and their description follows. The text in brackets means the user will be prompted to input additional parameters for performing the corresponding command.

- c : **cycle** - run the script for n iterations [ #iterations = ... ]
- d : **debug** - run the script once
- g : **generate** the Facebook SDK layer zip file
- r : **remove** from the page feed all posts generated by the bot
- t* : **Token Manager** commands
- z : **zip** fibonacci.py and token.tk to be deployed in AWSλ

Whenever one task is completed, pressing any key will return to the initial idle state.

#### Token Manager

If you are managing more than one page (generally a debug page and a "release" page), you must be really careful not to accidentally start debugging on your release page, like removing all the posts or cycling 100 iterations or uploading a ZIP with the wrong token to your cloud service... That's why I have this handy dandy token manager. It is contained inside the Manager, and you can access its functions through the t* commands. The token manager consists of the following commands:

- tc : prints **current** token
- td : **delete** token from list [ Token index: ... ]
- tr : **register** new token [ Name your token: ... , Paste your token: ... ]
- ts : **select** token from list [ Token index: ... ]

The registered tokens will be located in **tknlist.tk** and, for safety purposes, is ignored by git, just like **token.tk** and any other ***.tk** file.

## Setup

#### Local setup

This setup is intended to run the script locally and let the bot post on a test page.

Clone this repository in an empty folder

```bash
$ git clone https://github.com/guidanoli/fibonaccibot.git .
```

Assuming you've got [Python](https://www.python.org), install the Facebook SDK package through pip:

```bash
$ pip install facebook-sdk
```

Create a Facebook page where the bot will be posting, and also an application on [Facebook for Developers](https://developers.facebook.com/), through which the bot will get access to your page feed. If you'd rather not request a new access token every hour, get a [long-term token](https://sujipthapa.co/blog/generating-never-expiring-facebook-page-access-token) that will last 2 months, or a [permanent token](https://sujipthapa.co/blog/generating-never-expiring-facebook-page-access-token) so not to think about it ever again. Paste it on a new file called "token.tk" or run the Manager and run the command **t**, then paste the token in the prompt, then press Enter.

#### Cloud setup (with AWS Lambda)

After running some tests locally, you may want to upload your bot to the cloud and run it periodically. After some research, I found it rather simple to achieve this task using Amazon Web Services Lambda, or AWSλ for short. It hosts functions and its triggers. For our purpose, we'll make use of CloudWatch Events to trigger the bot hourly.

Be aware that due only to the fact that this bot is triggered discretely, AWSλ makes for the ideal service to the task. But for a bot that operates constantly, e.g. replies to comments, it might be better to look for alternatives. Thus, the instructions that follow are for setting up a platform for said "discrete bots".

First, clone this repository in an empty folder.

```bash
$ git clone https://github.com/guidanoli/fibonaccibot.git .
```

Create a Facebook page, and generate a permanent token to access its feed. For that, use the application developed by [@Maxman013](https://github.com/maxman013) linked [here](https://maxman013.github.io/token/?fbclid=IwAR25te6sYpYW_pbSRUBykdgdwHQBA3MUdhRQJp7Sq02Ok84bWQdUt5ww6v4). Follow the instructions on the website. Now run the Manager, and register the token with the command **t**, then zip both token.tk and fibonacci.py with the command **z**.

Now, create an Amazon account (if you don't have one already) and create your new function on [AWSλ](https://aws.amazon.com/pt/lambda/) (**Disclaimer: you won't be able to change its name later!**). Then, [upload](https://aws.amazon.com/pt/premiumsupport/knowledge-center/build-python-lambda-deployment-package/) the ZIP file you've just generated (don't forget to save it).

Other useful feature AWSλ provides us is the ability to tie layers (in the python context, packages and modules) to AWSλ functions. That way, if you have multiple Facebook bots on AWSλ and want to share the same Facebook SDK packages amongst them, just upload the package as a layer and link it to each bot. Code reuse is always a good programming practice, after all!

In order to create a layer, first, generate the layer ZIP file with command **g** on the Manager. This will contain all of the necessary functions the bot needs to access the GraphAPI.

It should be intuitive where to add layers on the AWSλ Management Console, but if you just can't find it, Medium has a great post on this topic: [here](https://medium.com/@adhorn/getting-started-with-aws-lambda-layers-for-python-6e10b1f9a5d) you can learn more about it (including how to upload and link one to your functions).

Lastly, [setup](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/RunLambdaSchedule.html) the CloudWatch to trigger hourly or in whichever frequency you so desire. The schedule expressions obey [this language](https://docs.aws.amazon.com/lambda/latest/dg/tutorial-scheduled-events-schedule-expressions.html). But beware that AWSλ provides you every month with the first 1,000,000 requests free of cost. After that, you'll be charged for the next million requests and so on.
