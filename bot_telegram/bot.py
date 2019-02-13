#!/usr/bin/env python
# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import web



# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Database connection
db = web.database(
    dbn = 'mysql',
    host = 'localhost',
    db = 'perros',
    user = 'root',
    pw = '1234',
    port = 3306
    )
 
#Samm17_bot 
token = '774308202:AAHfEbIyuKdQ6_c9hPg5iUiR4-RSNJEvlHg' # numero del token que father

# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update): # tiene que ver con la linea 75
    username = update.message.from_user.username
    update.message.reply_text('Busca la descripcion de acuerdo a la raza de tu perro: \n\n/raza "la_raza"\n'+
                                '/info --> acerca de ')

def info(bot, update): 
    username = update.message.from_user.username
    update.message.reply_text('Busca la  descripcion de acuerdo a la raza de tu perro: \n\n/raza "la_raza"\n'+
                                '/info --> acerca de ')

def search(update):
    text = update.message.text.split() #descompone el  mensaje que mande al usuario 
    username = update.message.from_user.username
    try:
        nombre = text[1] # cast para convertir string a intero
        print "Send info to {}".format(username)
        print "Key search {}".format(nombre)
        result = db.select('raza',where='nombre=$nombre', vars=locals())[0]
        mnsg = "Aqui esta tu informacion amiguito\n"+str(result.mensaje)
        update.message.reply_text(mnsg)
    except Exception as e:
        print "Error search: " + str(e.message)
        print "Error search: " + str(e.args)


def raza(bot, update):
    search(update)

def echo(bot, update):
    update.message.reply_text(update.message.text)
    print update.message.text
    print update.message.date
    print update.message.from_user 
    print update.message.from_user.username
    
def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))

    
def main():
    try:
        print 'Perros init token'

        updater = Updater(token)

        # Get the dispatcher to register handlers
        dp = updater.dispatcher

        print 'Perros init dispatcher'

        # on different commands - answer in Telegram ***comandos que usara nuetro boot***
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("info", info))
        dp.add_handler(CommandHandler("raza", raza))        

        # on noncommand i.e message - echo the message on Telegram
        dp.add_handler(MessageHandler(Filters.text, echo))

        # log all errors --- almacena errores
        dp.add_error_handler(error) 

        # Start the Bot
        updater.start_polling()

        # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT. This should be used most of the time, since
        # start_polling() is non-blocking and will stop the bot gracefully.
        print 'Vamos! ready' #pone el bot en modo de espera 
        updater.idle()
    except Exception as e:
        print "Error 100: ", e.message

if __name__ == '__main__':
    main()
