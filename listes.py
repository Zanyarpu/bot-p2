import telebot
from os import environ
from telebot.types import KeyboardButton, ReplyKeyboardMarkup
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

API_TOKEN = environ.get("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN)

menu_back_BTN_TEXT = "منـــوی اصـــلی  ↪️"
return_back_BTN_TEXT = "مرحلـــه قبلـــی  ➡️"

def K_class1(message):
    bot.send_message(message.chat.id,"class 1")
def K_class2(message):
    bot.send_message(message.chat.id,"class 2")
def K_class3(message):
    bot.send_message(message.chat.id,"class 3")
def K_class4(message):
    bot.send_message(message.chat.id,"class 4")
def K_class5(message):
    bot.send_message(message.chat.id,"class 5")
def K_class6(message):
    bot.send_message(message.chat.id,"class 6")
def K_class7(message):
    bot.send_message(message.chat.id,"class 7")
def K_class8(message):
    bot.send_message(message.chat.id,"class 8")

# #-------------------------------------------------------------------
def K_masid1(message):
    bot.send_message(message.chat.id,"class 1")
def K_masid2(message):
    bot.send_message(message.chat.id,"class 2")
def K_masid3(message):
    bot.send_message(message.chat.id,"class 3")
def K_masid4(message):
    bot.send_message(message.chat.id,"class 4")
def K_masid5(message):
    bot.send_message(message.chat.id,"class 5")
def K_masid6(message):
    bot.send_message(message.chat.id,"class 6")
def K_masid7(message):
    bot.send_message(message.chat.id,"class 7")
def K_masid8(message):
    bot.send_message(message.chat.id,"class 8")





# #-------------------------------------------------------------------
def M_class1(message):
    bot.send_message(message.chat.id,"کلاس های موجود: ")
def M_class2(message):
    bot.send_message(message.chat.id,"هنوز لیستی وارد نشده")
def M_class3(message):
    bot.send_message(message.chat.id,"هنوز لیستی وارد نشده")
def M_class4(message):
    bot.send_message(message.chat.id,"هنوز لیستی وارد نشده")
def M_class5(message):
    bot.send_message(message.chat.id,"هنوز لیستی وارد نشده")
def M_class6(message):
    bot.send_message(message.chat.id,"هنوز لیستی وارد نشده")
def M_class7(message):
    bot.send_message(message.chat.id,"هنوز لیستی وارد نشده")
def M_class8(message):
    bot.send_message(message.chat.id,"هنوز لیستی وارد نشده")


def M_docs1(message):
    bot.send_message(message.chat.id,"class 1")
def M_docs2(message):
    bot.send_message(message.chat.id,"class 2")
def M_docs3(message):
    bot.send_message(message.chat.id,"class 3")
def M_docs4(message):
    bot.send_message(message.chat.id,"class 4")
def M_docs5(message):
    bot.send_message(message.chat.id,"class 5")
def M_docs6(message):
    bot.send_message(message.chat.id,"class 6")
def M_docs7(message):
    bot.send_message(message.chat.id,"class 7")
def M_docs8(message):
    bot.send_message(message.chat.id,"class 8")


def M_masid1(message):
    bot.send_message(message.chat.id,"class 1")
def M_masid2(message):
    bot.send_message(message.chat.id,"class 2")
def M_masid3(message):
    bot.send_message(message.chat.id,"class 3")
def M_masid4(message):
    bot.send_message(message.chat.id,"class 4")
def M_masid5(message):
    bot.send_message(message.chat.id,"class 5")
def M_masid6(message):
    bot.send_message(message.chat.id,"class 6")
def M_masid7(message):
    bot.send_message(message.chat.id,"class 7")
def M_masid8(message):
    bot.send_message(message.chat.id,"class 8")








#-------------------------------------------------------------------
def I_class1(message):
    bot.send_message(message.chat.id,"class 1")
def I_class2(message):
    bot.send_message(message.chat.id,"class 2")
def I_class3(message):
    bot.send_message(message.chat.id,"class 3")
def I_class4(message):
    bot.send_message(message.chat.id,"class 4")
def I_class5(message):
    bot.send_message(message.chat.id,"class 5")
def I_class6(message):
    bot.send_message(message.chat.id,"class 6")
def I_class7(message):
    bot.send_message(message.chat.id,"class 7")
def I_class8(message):
    bot.send_message(message.chat.id,"class 8")


def I_docs1(message):
    bot.send_message(message.chat.id,"class 1")
def I_docs2(message):
    bot.send_message(message.chat.id,"class 2")
def I_docs3(message):
    bot.send_message(message.chat.id,"class 3")
def I_docs4(message):
    bot.send_message(message.chat.id,"class 4")
def I_docs5(message):
    bot.send_message(message.chat.id,"class 5")
def I_docs6(message):
    bot.send_message(message.chat.id,"class 6")
def I_docs7(message):
    bot.send_message(message.chat.id,"class 7")
def I_docs8(message):
    bot.send_message(message.chat.id,"class 8")


def I_masid1(message):
    bot.send_message(message.chat.id,"class 1")
def I_masid2(message):
    bot.send_message(message.chat.id,"class 2")
def I_masid3(message):
    bot.send_message(message.chat.id,"class 3")
def I_masid4(message):
    bot.send_message(message.chat.id,"class 4")
def I_masid5(message):
    bot.send_message(message.chat.id,"class 5")
def I_masid6(message):
    bot.send_message(message.chat.id,"class 6")
def I_masid7(message):
    bot.send_message(message.chat.id,"class 7")
def I_masid8(message):
    bot.send_message(message.chat.id,"class 8")




def Faculty_Call_list(message):
    call_list = """

    📚شماره تلفن بخش های مختلف دانشکده

    ▫️مسئول امورآموزش دانشکده:
    +98444152220131

    ▫️سرکارخانم صفی خانی:
    +989144231822

    ▫️سرکارخانم موسوی:
    +989930684752
    +989145708511

    ▫️مسئول امورمالی وشهریه دانشکده:
    +98444152220399

    ▫️جناب آقای صادقی:
    +989149042361

    ▫️مسئول اموردانشکده:
    +98444152220336

    ▫️جناب آقای رسول زاده:
    +989053303685

    ▫️مسئول امور دانشجویی خواهران وامورفرهنگی دانشکده:
    +98444152220141

    ▫️معاونت دانشکده جناب آقای ابراهیم پور:
    +989370559538

    ▫️حراست دانشکده:
    +98444152220356

    ▫️سرگروه رشته مکانیک جناب آقای ابراهیم پور:
    +989370559538

    ▫️سرگروه رشته راه آهن\صنایع جناب آقای امین محمدی:
    +989141244706

    🔸مسئول اصلی خوابگاه برادران(آقای اسکندرنیا):
    +989144237119

    🔹مسئول خوابگاه برادران (آقای قلی زاده):
    +989141246149

    """
    bot.send_message(message.chat.id, call_list)