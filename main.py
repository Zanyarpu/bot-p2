import telebot
import logging
from listes import *
from Buttons import *
from os import environ
from time import sleep
from telebot.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardRemove

# API Token:
API_TOKEN = environ.get("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN, threaded= True)

# Output logger:
logger = telebot.logger
logger.setLevel(logging.INFO)

# Buttons Message:
menu_back_MSG_TEXT = "بازگـــشت بــــه منــــوی اصـــــلی 👇🏻"
return_back_MSG_TEXT = "بازگـــشت بــــه مرحلــــه قبلــــی 👇🏻"
both_back_MSG_TEXT = "بازگشت به مرحلـه قبلـی یا منـوی اصلـی 👇🏻"

# Buttons Text:
menu_back_BTN_TEXT = "منـــوی اصـــلی  ↪️"
return_back_BTN_TEXT = "مرحلـــه قبلـــی  ➡️"
Return_BTN_LIST = [return_back_BTN_TEXT, menu_back_BTN_TEXT]




#/////////////////////////////////////////////////////////////////////////////////////////////////////
# Main Menu Sections:

def get_section(message, section_list):
    section = message.text
    logger.info("triggred 1: OK ...")

    if section == section_list[0]: Class_list(message, 0)

    elif section == section_list[1]: docs_list(message, 1)

    elif section == section_list[2]: Systems_web(message)

    elif section == section_list[3]: Students_org(message)

    elif section == section_list[4]: Students_form(message)

    elif section == section_list[5]: Educational_file(message)

    elif section == section_list[6]: Masters_id(message, 6)

    elif section == section_list[7]: Faculty_call(message)

    elif section == section_list[8]: Support_id(message)


#/////////////////////////////////////////////////////////////////////////////////////////////////////
# Main Defs:

def Class_list(message, sec_indx):
    logger.info("triggred 2: OK ...")
    send_Field(message, sec_indx)

def docs_list(message, sec_indx):
    logger.info("triggred 2: OK ...")
    send_Field(message, sec_indx)

def Systems_web(message):
    logger.info("triggred 2: OK ...")
    send_webs(message)

def Students_org(message):
    logger.info("triggred 2: OK ...")
    send_orgs(message)

def Students_form(message):
    logger.info("triggred 2: OK ...")
    send_stud_forms(message)

def Educational_file(message):
    logger.info("triggred 2: OK ...")
    send_educat_files(message)

def Masters_id(message, sec_indx):
    logger.info("triggred 2: OK ...")
    send_Field(message, sec_indx)

def Faculty_call(message):
    logger.info("triggred 2: OK ...")
    send_faculty_call(message)

def Support_id(message):
    logger.info("triggred 2: OK ...")
    send_support_id(message, 0)



#/////////////////////////////////////////////////////////////////////////////////////////////////////
# Define return Defs:

def return_check(message, back_step, Field_index, section_index):
    # Check Return BTN (Back Step):
    if message.text == Return_BTN_LIST[0]:
        return_back(message, back_step, Field_index, section_index)
    # Check Return BTN (Menu Back):
    elif message.text == Return_BTN_LIST[1]: 
        return_menu(message)


def return_menu(message):
    logger.info("triggred menu: OK ...")
    send_menu(message)


def return_back(message, back_step, Field_index, section_index):
    logger.info("triggred back: OK ...")
    if back_step == -1: send_Field(message, section_index)
    elif back_step == -2: send_search_type(message, Field_index, section_index)
    elif back_step == -3: send_Semester(message, Field_index, section_index)



#/////////////////////////////////////////////////////////////////////////////////////////////////////
# Define send Defs:

def send_menu(message):
    menu_text = """در چه زمینه ای می تونم کمک تون کنم ؟ 😊👇🏻"""

    markup, section_list = send_welcome_BTN()
    bot.send_message(message.chat.id, menu_text, reply_markup = markup)
    bot.register_next_step_handler(message, get_section, section_list)


#-------------------------------------------------------------------
def send_Field(message, section_index):
    logger.info("triggred 3: OK ...")

    markup, Field_list = send_Field_BTN()

    bot.send_message(message.chat.id, """
    🌟  بسیار خب! چه رشته ای هستی؟""",
    reply_markup = markup )

    bot.register_next_step_handler(message,
    get_Field, Field_list, section_index)


#-------------------------------------------------------------------
def send_search_type(message, Field_index, section_index):
    logger.info("triggred 5: OK ...")

    markup, type_list = send_search_type_BTN(section_index)

    bot.send_message(message.chat.id, """
    🌟  لطفا روش جستجو را انتخاب کنید: 👇🏻""",
    reply_markup = markup )

    bot.register_next_step_handler(message,
    get_search_type, type_list, Field_index, section_index)
    

#-------------------------------------------------------------------
def send_Semester(message, Field_index, section_index):
    logger.info("triggred 7: OK ...")

    markup, semester_list = send_Semester_BTN()

    bot.send_message(message.chat.id,
    "🌟  خیلی عالی! ترم چندی؟", 
    reply_markup = markup )

    # Check Fields (Mechanic):
    if Field_index == 0:
        bot.register_next_step_handler(message,
        M_get_Semester, semester_list, Field_index, section_index)

    # Check Fields (Computer):
    elif Field_index == 1:
        bot.register_next_step_handler(message,
        K_get_Semester, semester_list, Field_index, section_index)
    
    # Check Fields (Industries):
    elif Field_index == 2:
        bot.register_next_step_handler(message,
        I_get_Semester,semester_list, Field_index, section_index)


#-------------------------------------------------------------------
def send_all(message, Field_index, section_index):
    logger.info("triggred 7: OK ...")

    no_list(message, -2, Field_index, section_index)
    pass

    # logger.info("triggred 11: OK ...")
    # # Check Section Index (For Class): 
    # if section_index == 0:
    #     # Mechanic Classes:
    #     if Field_index == 0:
    #         inline_markup_Class = M_all_class_BTN(message)
    #     # Computer Classes:
    #     elif Field_index == 1:
    #         inline_markup_Class = K_all_class_BTN(message)
    #     # Industries Classes:
    #     elif Field_index == 2:
    #         inline_markup_Class = I_all_class_BTN(message)

    #     bot.send_message(message.chat.id,
    #     "لیست کلاس های موجود  🔽",
    #     reply_markup = inline_markup_Class)

    # # Check Section Index (For Docs): 
    # if section_index == 1:
    #     # Mechanic Docs:
    #     if Field_index == 0:
    #         inline_markup_Docs = M_all_Docs_BTN(message)
    #     # Computer Docs:
    #     elif Field_index == 1:
    #         inline_markup_Docs = K_all_Docs_BTN(message)
    #     # Industries Docs:
    #     elif Field_index == 2:
    #         inline_markup_Docs = I_all_Docs_BTN(message)

    #     bot.send_message(message.chat.id,
    #     "لیست دروس موجود  🔽",
    #     reply_markup = inline_markup_Docs)

        
    # bot.send_message(message.chat.id,
    # both_back_MSG_TEXT,
    # reply_markup = both_back_BTN())

    # bot.register_next_step_handler(message, return_check, -1, None, None)

#-------------------------------------------------------------------
def send_webs(message):
    logger.info("triggred 3: OK ...")

    inline_markup = send_webs_BTN()

    bot.send_message(message.chat.id, 
    """ بسیار خب! سامانه های موجود   🔽""",
    reply_markup = inline_markup)

    bot.send_message(message.chat.id,
    menu_back_MSG_TEXT,
    reply_markup = menu_back_BTN())

    bot.register_next_step_handler(message, return_check, None, None, None)


#-------------------------------------------------------------------
def send_orgs(message):
    logger.info("triggred 3: OK ...")

    inline_markup = send_orgs_BTN()

    bot.send_message(message.chat.id,
    """ بسیار خب! تشکل های موجود   🔽""",
    reply_markup = inline_markup)

    bot.send_message(message.chat.id,
    menu_back_MSG_TEXT,
    reply_markup = menu_back_BTN())

    bot.register_next_step_handler(message, return_check, None, None, None)


#-------------------------------------------------------------------
def send_stud_forms(message):
    
    inline_markup = send_stud_forms_BTN()

    bot.send_message(message.chat.id, 
    """ برای دسترسی سریع به فرم مورد نظر از طریق لینک های زیر اقدام نمایید  🔽""",
    reply_markup = inline_markup)

    bot.send_message(message.chat.id,
    menu_back_MSG_TEXT,
    reply_markup = menu_back_BTN())

    bot.register_next_step_handler(message, return_check, None, None, None)


#-------------------------------------------------------------------
def send_educat_files(message):
    
    inline_markup = send_educat_files_BTN()

    bot.send_message(message.chat.id, 
    """ فایل مورد نظر را جهت دریافت انتخاب کنید  🔽""",
    reply_markup = inline_markup)

    bot.send_message(message.chat.id,
    menu_back_MSG_TEXT,
    reply_markup = menu_back_BTN())

    bot.register_next_step_handler(message, return_check, None, None, None)


#-------------------------------------------------------------------
def send_support_id(message, send_it):
    logger.info("triggred 3: OK ...")

    markup, support_list = send_support_id_BTN()

    if send_it == 0:
        bot.send_message(message.chat.id,"""
        🌟  اگر پیشنهادی دارید یا به خطایی برخوردید خوشحال می شیم با ما در میان بزارید 👇🏻""",
        reply_markup = markup)
        
    bot.register_next_step_handler(message,
    get_support_id, support_list)

    
#-------------------------------------------------------------------
def send_faculty_call(message):

    Faculty_Call_list(message)

    bot.send_message(message.chat.id,
    menu_back_MSG_TEXT,
    reply_markup = menu_back_BTN())

    bot.register_next_step_handler(message, return_check, None, None, None)


#/////////////////////////////////////////////////////////////////////////////////////////////////////
# Define  no list  Defs:

def no_list(message, back_step, Field_index, section_index):
    logger.info("triggred no_list: OK ...")
    # logger.info("back_step :", back_step)

    bot.send_message(message.chat.id,
    "هنوز لیستی وارد نشده",
    reply_markup = both_back_BTN())

    if back_step == -1:
        bot.register_next_step_handler(message, return_check, back_step, None, section_index)

    elif back_step == -2:
        bot.register_next_step_handler(message, return_check, back_step, Field_index, section_index)




#/////////////////////////////////////////////////////////////////////////////////////////////////////
# Define  next_step_handeler  Defs:

def get_Field(message, Field_list, section_index):
    logger.info("triggred 4: OK ...")

    Field_index = 0
    Field = message.text

    if Field in Field_list:

        # Check Section Index (For Mass_Id):
        if section_index == 6:
            no_list(message, -1, None, section_index)
        # Check Section Index (For Class and Docs):
        elif section_index == 0 or 1:
            Field_index = (Field_list.index(Field))
            send_search_type(message, Field_index, section_index)
    
    # Check Return Btn:
    else: return_check(message, None, None, None)


#-------------------------------------------------------------------
def get_search_type(message, type_list, Field_index, section_index):
    logger.info("triggred 6: OK ...")

    search_type = message.text

    # Check search type (For all):
    if search_type == type_list[0]:
        send_all(message, Field_index, section_index)

    # Check search type (By Semesters):
    elif search_type == type_list[1]:
        send_Semester(message, Field_index, section_index)

    # Check Return Btn:
    else: return_check(message, -1, None, section_index)


#-------------------------------------------------------------------
def M_get_Semester(message, semester_list, Field_index, section_index):
    logger.info("triggred 8: OK ...")

    def_Class_list = [M_class1, M_class2, M_class3, M_class4,
                      M_class5, M_class6, M_class7, M_class8]

    def_Docs_list = [M_docs1, M_docs2, M_docs3, M_docs4,
                     M_docs5, M_docs6, M_docs7, M_docs8]

    def_list = []
    semester_index = 0
    semester = message.text
    
    # Control:
    if semester in semester_list:
        # Check Section (For Class):
        if section_index == 0:
            def_list = def_Class_list
        # Check Section (For Docs):
        elif section_index == 1:
            def_list = def_Docs_list

        class_to_fun = {i+1: func for i, func in enumerate(def_list)}
        semester_index = (semester_list.index(semester)) + 1
        class_to_fun[semester_index](message)

    # Check Return Btn:
    else: return_check(message, -2, Field_index, section_index)

    
    #-------------------------------------------------------------------
def K_get_Semester(message, semester_list, Field_index, section_index):
    logger.info("triggred 8: OK ...")

    def_Class_list = [K_class1, K_class2, K_class3, K_class4, 
                      K_class5, K_class6, K_class7, K_class8]

    def_Docs_list = [K_docs1, K_docs2, K_docs3, K_docs4,
                     K_docs5, K_docs6, K_docs7, K_docs8]

    def_list = []
    list_index = 0
    semester = message.text

    if semester in semester_list:
        # Check Section (For Class):
        if section_index == 0:
            def_list = def_Class_list
        # Check Section (For Docs):
        elif section_index == 1:
            def_list = def_Docs_list

        class_to_fun = {i+1: func for i, func in enumerate(def_list)}
        list_index = (semester_list.index(semester)) + 1
        class_to_fun[list_index](message, Field_index, section_index)

    # Check Return Btn:
    else: return_check(message, -2, Field_index, section_index)

#-------------------------------------------------------------------
def I_get_Semester(message, semester_list, Field_index, section_index):
    logger.info("triggred 8: OK ...")

    def_Class_list = [I_class1, I_class2, I_class3, I_class4,
                      I_class5, I_class6, I_class7, I_class8]

    def_Docs_list = [I_docs1, I_docs2, I_docs3, I_docs4,
                     I_docs5, I_docs6, I_docs7, I_docs8]

    def_list = []
    list_index = 0
    semester = message.text

    if semester in semester_list:
        # Check Section (For Class):
        if section_index == 0:
            def_list = def_Class_list
        # Check Section (For Docs):
        elif section_index == 1:
            def_list = def_Docs_list

        class_to_fun = {i+1: globals()[func] for i, func in enumerate(def_list)}
        list_index = (semester_list.index(semester)) + 1
        class_to_fun[list_index](message)

    # Check Return Btn:
    else: return_check(message, -2, Field_index, section_index)


#-------------------------------------------------------------------
def get_support_id(message, support_list): #support_list
    logger.info("triggred 4: OK ...")
    
    support = message.text

    if support in support_list:
        bot.send_message(message.chat.id,"""
        🌟  لطفا نظر خود را با ما در میان بزارید👇🏻""",
        reply_markup = get_support_id_BTN(message.text, support_list))
        send_support_id(message, -1)

    else:
        return_check(message, None, None, None)




#/////////////////////////////////////////////////////////////////////////////////////////////////////
# Define Kmputer Docs Defs:

def K_docs1(message, Field_index, section_index):
    # inline_markup = K_docs6_BTN()
    inline_markup = []

    bot.send_message(message.chat.id,
    "هنوز لیستی وارد نشده",
    reply_markup = inline_markup)

    bot.send_message(message.chat.id,
    both_back_MSG_TEXT,
    reply_markup = both_back_BTN())
    
    bot.register_next_step_handler(message, return_check, -3, Field_index, section_index)


def K_docs2(message, Field_index, section_index):
    # inline_markup = K_docs6_BTN()
    inline_markup = []

    bot.send_message(message.chat.id,
    "هنوز لیستی وارد نشده",
    reply_markup = inline_markup)

    bot.send_message(message.chat.id,
    both_back_MSG_TEXT,
    reply_markup = both_back_BTN())
    
    bot.register_next_step_handler(message, return_check, -3, Field_index, section_index)


def K_docs3(message, Field_index, section_index):
    # inline_markup = K_docs6_BTN()
    inline_markup = []

    bot.send_message(message.chat.id,
    "هنوز لیستی وارد نشده",
    reply_markup = inline_markup)

    bot.send_message(message.chat.id,
    both_back_MSG_TEXT,
    reply_markup = both_back_BTN())
    
    bot.register_next_step_handler(message, return_check, -3, Field_index, section_index)


def K_docs4(message, Field_index, section_index):
    # inline_markup = K_docs6_BTN()
    inline_markup = []

    bot.send_message(message.chat.id,
    "هنوز لیستی وارد نشده",
    reply_markup = inline_markup)

    bot.send_message(message.chat.id,
    both_back_MSG_TEXT,
    reply_markup = both_back_BTN())
    
    bot.register_next_step_handler(message, return_check, -3, Field_index, section_index)


def K_docs5(message, Field_index, section_index):
    # inline_markup = K_docs6_BTN()
    inline_markup = []

    bot.send_message(message.chat.id,
    "هنوز لیستی وارد نشده",
    reply_markup = inline_markup)

    bot.send_message(message.chat.id,
    both_back_MSG_TEXT,
    reply_markup = both_back_BTN())
    
    bot.register_next_step_handler(message, return_check, -3, Field_index, section_index)


def K_docs6(message, Field_index, section_index):
    inline_markup = K_docs6_BTN()

    bot.send_message(message.chat.id,
    "لیست دروس تــرم  🔽",
    reply_markup = inline_markup)

    bot.send_message(message.chat.id,
    both_back_MSG_TEXT,
    reply_markup = both_back_BTN())
    
    bot.register_next_step_handler(message, return_check, -3, Field_index, section_index)


def K_docs7(message, Field_index, section_index):
    # inline_markup = K_docs6_BTN()
    inline_markup = []

    bot.send_message(message.chat.id,
    "هنوز لیستی وارد نشده",
    reply_markup = inline_markup)

    bot.send_message(message.chat.id,
    both_back_MSG_TEXT,
    reply_markup = both_back_BTN())
    
    bot.register_next_step_handler(message, return_check, -3, Field_index, section_index)
    

def K_docs8(message, Field_index, section_index):
    # inline_markup = K_docs6_BTN()
    inline_markup = []

    bot.send_message(message.chat.id,
    "هنوز لیستی وارد نشده",
    reply_markup = inline_markup)

    bot.send_message(message.chat.id,
    both_back_MSG_TEXT,
    reply_markup = both_back_BTN())
    
    bot.register_next_step_handler(message, return_check, -3, Field_index, section_index)




#/////////////////////////////////////////////////////////////////////////////////////////////////////
# Define  Main handlers  Decorators:

@bot.message_handler(commands=['start'])
def def_welcome(message):
    welcome_text = """
🌟  سلام!👋🏻 
🌟 به ربات ما خوش اومدی ، 😊
\n🌟  این یک نسخه آزمایشی از ربات است و تیم توسعه همچنان در حال آزمایش و تکمیل ربات هستند، از این رو اگر با اشکالی در عملکرد ربات مواجه شدید یا پیشنهادی در راستای توسعه ربات دارید حتما با ما در میان بگذارید.
\n🌟  از طریق این ربات میتوانید به فایل ها و منابع مورد نیاز تون سریع تر دسترسی داشته باشید.
\n\n🌟  در چه زمینه ای می تونم کمک تون کنم ؟ 👇🏻 """

    markup, section_list = send_welcome_BTN()

    bot.send_message(message.chat.id, welcome_text, reply_markup = markup)
    bot.register_next_step_handler(message, get_section, section_list)


#-------------------------------------------------------------------
@bot.message_handler(commands=['help'])
def def_help(message):
    
    help_text = """
🤖 این ربات توسط تیم برنامه نویسی انجمن علمی کامپیوتر طراحی شده،
\n⭕️ هدف این ربات تسریع دسترسی دانشجو به بخش ها و سامانه های موجود دانشکده و جمع آوری منابع و اسناد آموزشی و بصورت یکجا جهت تسهیل فعالیت‌های دانشجویان گرامی است،
\n⭕️ لذا قابلیت های ربات شامل بخش های زیر است:
<b>1. کلاس های درسی:</b> دسترسی به لیست کلاس های دانشکده یا ترم مربوطه
<b>2. جزوه های درسی:</b> دسترسی به جزوه های درسی اساتید هر درس یا سایر فایل های درسی مربوطه
<b>3. سامانه های دانشجویی:</b> دسترسی به سامانه های موجود دانشکده
<b>4. تشکل های دانشجویی:</b> دسترسی به تشکل های موجود دانشکده
<b>5. فرم های دانشجویی:</b> دسترسی به فرم های دانشجویی مورد نظر
<b>6. فایل های آموزشی:</b> دسترسی به فایل های ارائه شده توسط واحد آموزش
<b>7. ارتباط با اساتید:</b> دسترسی به راه های ارتباطی اساتید جهت تسریع ارتباط دانشجو با استاد مربوطه
<b>8. تماس با واحد های دانشکده:</b> دسترسی به شماره تماس واحد های دانشکده و کارکنان محترم
<b>9. ارتباط با پشتیبانی:</b> ارتباط با تیم پشتیبانی جهت بروزرسانی منابع و فایل ها یا گزارش اشکال و ارسال پیشنهاد به تیم پشتیبانی جهت توسعه و بهبود بیشتر عملکرد ربات.
\n
📑 <b>ارسال فایل ها و منابع آموزشی:</b>
🆔 @Alireza_ktbi

⚠️ <b>گزارش اشکال یا ارسال پیشنهاد:</b>
🆔 @ZNR_KD """

    bot.reply_to(message, help_text, parse_mode='HTML')

#-------------------------------------------------------------------
@bot.message_handler(commands=['menu'])
def def_menu(message):
    send_menu(message)
    bot.register_next_step_handler(message, send_menu)


#-------------------------------------------------------------------
@bot.message_handler(commands=['support'])
def def_menu(message):
    Support_id(message)


#-------------------------------------------------------------------
@bot.message_handler(content_types=["document"])
def Check_id(message):

    bot.send_message(message.chat.id, "فایل دریافت شد. 😊")
    logger.info("triggred get: OK ...")
    logger.info(message.__dict__)


#-------------------------------------------------------------------
@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    # Educational Files Callback:
    if call.data == "Class_and_Exam_schedule":
        bot.send_chat_action(call.message.chat.id, action= "upload_document")
        bot.send_document(call.message.chat.id,
        "BQACAgQAAxkBAAINJ2gKBFGbbR92aMxWDE5YqWNX6IGHAALCFgACYZERUZW3GkWFUXoAATYE")

    if call.data == "M_E_chart":
        bot.send_chat_action(call.message.chat.id, action= "upload_document")
        bot.send_document(call.message.chat.id,
        "BQACAgQAAxkBAAINKWgKBXGYot496qew5Wfu898JLI3qAAI7FwACHwMYUBXNFhwCevERNgQ")

    if call.data == "C_E_chart":
        bot.send_chat_action(call.message.chat.id, action= "upload_document")
        bot.send_document(call.message.chat.id,
        "BQACAgQAAxkBAAINHWgKA6bgnkyuwqYhHlmWxx0uAZuGAAJIEgACY_0ZUoUNa1nmu5B3NgQ")

    if call.data == "I_E_chart":
        bot.send_chat_action(call.message.chat.id, action= "upload_document")
        bot.send_document(call.message.chat.id,
        "BQACAgQAAxkBAAINL2gKBlp0nJLjO7vu006vUnPUYkXFAAIvDgACA9x5UwpYPZ9YWtz1NgQ")

    if call.data == "M_E_code_list":
        bot.send_chat_action(call.message.chat.id, action= "upload_document")
        bot.send_document(call.message.chat.id,
        "BQACAgQAAxkBAAINL2gKBlp0nJLjO7vu006vUnPUYkXFAAIvDgACA9x5UwpYPZ9YWtz1NgQ")

    if call.data == "C_E_code_list":
        bot.send_chat_action(call.message.chat.id, action= "upload_document")
        bot.send_document(call.message.chat.id,
        "BQACAgQAAxkBAAINL2gKBlp0nJLjO7vu006vUnPUYkXFAAIvDgACA9x5UwpYPZ9YWtz1NgQ")

    if call.data == "I_E_code_list":
        bot.send_chat_action(call.message.chat.id, action= "upload_document")
        bot.send_document(call.message.chat.id,
        "BQACAgQAAxkBAAINL2gKBlp0nJLjO7vu006vUnPUYkXFAAIvDgACA9x5UwpYPZ9YWtz1NgQ")

    if call.data == "Unit_selection_guide":
        bot.send_chat_action(call.message.chat.id, action= "upload_document")
        bot.send_document(call.message.chat.id,
        "BQACAgQAAxkBAAINK2gKBd9XRLZan8_AsztN0YChRDwBAAINFAACHDeAUMRACisduv_gNgQ")

    if call.data == "Exam_regulation":
        bot.send_chat_action(call.message.chat.id, action= "upload_document")
        bot.send_document(call.message.chat.id,
        "BQACAgQAAxkBAAINLWgKBhYcJj80qBm9MsZVd6aosK8KAAK1IAAC3YMgUFFGPekzDbUONgQ")


#-------------------------------------------------------------------
bot.polling() 