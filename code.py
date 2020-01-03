# At line 52 of the code, please enter you bot's api token

from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re


url = "https://api.github.com/orgs/fedora-infra/repos"


data = requests.get(url)
data = data.json()


def get_fork_count(update, bot, args):
    abc = ""
    for arg in args:
        abc.append(arg)
    name = arg
    for i in data:
        if name in i['name']:
            return i['forks']
        else:
            return str("not found")
            break

def available_repos(bot, update,):
    chat_id = update.message.chat_id
    name = []
    for i in data:
        name.append(i['name'])
    ltr = ("\n".join(name))
    

    bot.sendMessage(chat_id=chat_id, text=ltr)

def count(bot, update, args):
    chat_id = update.message.chat_id
    alpha = []
    abcde = "Please pass repository name as an argument with the command"
    for arg in args:
        a = arg
        for x in data:
            if a == x['name']:
                alpha.append(x['forks'])
                abcde = str(alpha).replace('[','').replace(']','')
            

    bot.sendMessage(chat_id=chat_id, text=abcde)

def main():
    updater = Updater('984743753:AAH5eQx4k4E6KEhMjIGua_pmplwkV7U6klo')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('repo',available_repos))
    dp.add_handler(CommandHandler('count',count, pass_args=True))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()