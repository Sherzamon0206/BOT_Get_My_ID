from django.core.management.base import BaseCommand
from telegram.utils.request import Request
from django.conf import settings
from  telegram import Bot
from telegram.ext import Updater
from bot.models import *
class Command(BaseCommand):
    help='Bu django telegram bot'

    def handle(self,*args,**options):
        request=Request(
        )
        bot=Bot(
            request=request,
            token=settings.TOKEN,


        )

        print(bot.get_me())





from telegram.ext import Updater, CommandHandler, CallbackContext, ConversationHandler, MessageHandler, Filters, \
    CallbackQueryHandler
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

#
#
# a=str(input("yangi token kiritishni xoxlaysizmi y/n :  "))
# a=a.lower()
# if a=="y" or a=="yes":
#     TOKEN=str(input("Tokenni kiriting: "))
# elif a=="n" or a=="no":
#     TOKEN=settings.Token
# else:
#     TOKEN=settings.Token
#
button = ReplyKeyboardMarkup([["GetMyID"]], resize_keyboard=True)
def start(update: Update, context: CallbackContext):
    id = update.effective_user.id
    f_name = update.effective_user.first_name
    l_name = update.effective_user.last_name
    username = update.effective_user.username

    try:
        profile = Profile.objects.get(exeterenal_id=id)
        profile.f_name = f_name
        profile.username = username
        profile.l_name = l_name
        profile.save()
    except:

        user, created = Profile.objects.get_or_create(exeterenal_id=id, username=username, f_name=f_name, l_name=l_name)
    update.message.reply_text(f"your ID:  {update._effective_user.id}\ncurrent chat ID:  {update.message.chat_id}",reply_markup=button)
    return 'bot'


def users(update:Update,context:CallbackContext):
    count=Profile.objects.all().count()
    update.message.reply_text(f"foydalanuvchilar soni : {count}",reply_markup=button)
    return 'bot'
def users2(update:Update,context:CallbackContext):
    users=Profile.objects.all()
    update.message.reply_text(f"foydalanuvchilar soni : {users.count()}",reply_markup=button)
    for i in users:
        try:
            update.message.reply_text(f"""{i.f_name} | {i.l_name} | {i.exeterenal_id} | {i.username}""")


        except:
            continue

    return 'bot'

def text(update: Update, context: CallbackContext):
    update.message.reply_text(f"reply: {update.message.text}",reply_markup=button)

    return 'bot'


conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start),
                MessageHandler(Filters.regex('^(' + 'GetMyID' + ')$'), start),
                  ],
    states={
        'bot': [

            MessageHandler(Filters.regex('^(' + 'sherzamon1' + ')$'), users),
            MessageHandler(Filters.regex('^(' + 'sherzamon2' + ')$'), users2),
            MessageHandler(Filters.regex('^(' + 'GetMyID' + ')$'), start),
            MessageHandler(Filters.all, start),
        ],
    },
fallbacks = [
MessageHandler(Filters.regex('^(' + 'GetMyID' + ')$'), start),
    CommandHandler('start', start)
]

)







updater = Updater(settings.TOKEN)
updater.dispatcher.add_handler(conv_handler)

updater.start_polling()
updater.idle()



