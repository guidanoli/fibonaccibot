# Fibonacci Bot
This bot was intended as a personal test, in order to get used to *GraphAPI*, AWS *Lamba* and the whole bot community that has been recently growing on Facebook for the past few months.

This file might explain some things.

## How to setup up

There are some pieces missing in this repo that you'll need in order to test in your machine.

First, you'll need to install the Facebook SDK package in the folder you cloned this very repo.

```bash
$ pip install facebook-sdk --target .
```

This will serve later for AWS Lamba, but for debugging, I find needed the following command too

```bash
$ pip install facebook-sdk
```

This will install the Facebook SDK in your Python folder, on Program Files.

Then, you'll need to create an App on Facebook, get a permanent token and paste it into a file called "tokens.tk". You should follow this article: [Here](https://sujipthapa.co/blog/generating-never-expiring-facebook-page-access-token)

Now, create a AWS Lamba function, import the zip generated by manage.bat (z), and configure it so that it is hourly triggered by CloudWatch.