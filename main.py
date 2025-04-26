import telebot
import logging
from listes import *
from os import environ
from time import sleep
from telebot.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardRemove

API_TOKEN = environ.get("API_TOKEN")
bot = telebot.TeleBot(API_TOKEN, threaded= True)

logger = telebot.logger
logger.setLevel(logging.INFO)

# Buttons Text:
menu_back_MSG_TEXT = "بازگـــشت بــــه منــــوی اصـــــلی 👇🏻"
return_back_MSG_TEXT = "بازگـــشت بــــه مرحلــــه قبلــــی 👇🏻"
both_back_MSG_TEXT = "بازگشت به مرحلـه قبلـی یا منـوی اصلـی 👇🏻"

menu_back_BTN_TEXT = "منـــوی اصـــلی  ↪️"
return_back_BTN_TEXT = "مرحلـــه قبلـــی  ➡️"

Return_BTN_LIST = [return_back_BTN_TEXT, menu_back_BTN_TEXT]

#*******************************************************************************
# Main Menu Sections:

def get_section(message, section_list):
    section = message.text
    logger.info("triggred 1: OK ...")

    if section == section_list[0]: Class_list(message, 0)

    elif section == section_list[1]: Class_docs(message, 1)

    elif section == section_list[2]: Systems_web(message)

    elif section == section_list[3]: Students_org(message)

    elif section == section_list[4]: Students_form(message)

    elif section == section_list[5]: Educational_file(message)

    elif section == section_list[6]: Masters_id(message, 6)

    elif section == section_list[7]: Faculty_call(message)

    elif section == section_list[8]: Support_id(message)

def get_return(message, Field_index, section_index): # back_step
    if message.text == Return_BTN_LIST[1]:
        logger.info("triggred menu: OK ...")
        send_welcome(message)

    if message.text == Return_BTN_LIST[0]:
        send_Semester(message, Field_index, section_index)

#*******************************************************************************
# Main Def:

def Class_list(message, sec_indx):
    logger.info("triggred 2: OK ...")
    send_Field(message, sec_indx)

def Class_docs(message, sec_indx):
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


#*******************************************************************************
# Define Defs:

def send_Field(message, section_index):
    logger.info("triggred 3: OK ...")

    markup, Field_list = send_Field_BTN()

    bot.send_message(message.chat.id, """
    🌟  بسیار خب! چه رشته ای هستی؟""",
    reply_markup = markup )

    bot.register_next_step_handler(message, get_Field, Field_list, section_index)


def get_Field(message, Field_list, section_index):
    logger.info("triggred 4: OK ...")

    Field_index = 0
    Field = message.text

    if section_index == 6:
        no_list_MasId(message, section_index)

    else:
        if Field in Field_list:
            Field_index = (Field_list.index(Field))
        send_search_type(message, Field_index, section_index)
    
    if message.text == Field_list[3]: send_welcome(message)
        

#-------------------------------------------------------------------
def send_search_type(message, Field_index, section_index):
    logger.info("triggred 5: OK ...")

    markup, type_list = send_search_type_BTN(section_index)

    bot.send_message(message.chat.id, """
    🌟  لطفا روش جستجو را انتخاب کنید: 👇🏻""",
    reply_markup = markup )

    # bot.register_next_step_handler(message, get_search_type, type_list, Field_index, section_index)
    bot.register_next_step_handler(message, no_list_Class, Field_index, section_index)


def get_search_type(message, type_list, Field_index, section_index):
    logger.info("triggred 6: OK ...")

    search_type = message.text
    if search_type == type_list[0]:
        send_Semester(message, Field_index, section_index)

    elif search_type == type_list[1]:
        send_all(message, Field_index, section_index)

    elif message.text == type_list[2]:
        send_Field(message, section_index)

    elif message.text == type_list[3]:
        send_welcome(message)


def send_all(message, Field_index, section_index):
    logger.info("triggred 7: OK ...")

    no_list_Class()

    # if Field_index == 0:
    #     if section_index == 0:
    #         M_class_all(message)
    #     elif section_index == 1:
    #         M_docs_all(message)
    #     elif section_index == 6:
    #         M_master_all(message)

    # elif Field_index == 1:
    #     if section_index == 0:
    #         K_class_all(message)
    #     elif section_index == 1:
    #         K_docs_all(message)
    #     elif section_index == 6:
    #         K_master_all(message)

    # elif Field_index == 2:
    #     if section_index == 0:
    #         I_class_all(message)
    #     elif section_index == 1:
    #         I_docs_all(message)
    #     elif section_index == 6:
    #         I_master_all(message)

#-------------------------------------------------------------------
def send_Semester(message, Field_index, section_index):
    logger.info("triggred 7: OK ...")

    markup, semester_list = send_Semester_BTN()

    bot.send_message(message.chat.id,
    "🌟  خیلی عالی! ترم چندی؟", 
    reply_markup = markup )

    # Fields:
    if Field_index == 0:
        bot.register_next_step_handler(message, M_get_Semester, semester_list, Field_index, section_index)
    elif Field_index == 1:
        bot.register_next_step_handler(message, K_get_Semester, semester_list, Field_index, section_index)
    elif Field_index == 2:
        bot.register_next_step_handler(message, I_get_Semester, semester_list, Field_index, section_index)


def M_get_Semester(message, semester_list, Field_index, section_index):
    logger.info("triggred 8: OK ...")

    def_Class_list = [M_class1, M_class2, M_class3, M_class4,
                      M_class5, M_class6, M_class7, M_class8]

    def_Docs_list = [M_docs1, M_docs2, M_docs3, M_docs4,
                     M_docs5, M_docs6, M_docs7, M_docs8]

    # def_MasID_list = [M_masid1, M_masid2, M_masid3, M_masid4, 
    #                   M_masid5, M_masid6, M_masid7, M_masid8]
    def_list = []
    list_index = 0
    semester = message.text
    
    # Control:
    if message.text == semester_list[8]:
        send_search_type(message, Field_index, section_index)
    elif message.text == semester_list[9]:
        send_welcome(message)

    # Type ask:
    if section_index == 0:
        def_list = def_Class_list
    elif section_index == 1:
        def_list = def_Docs_list
    # elif section_index == 6:
    #     def_list = def_MasID_list

    class_to_fun = {i+1: func for i, func in enumerate(def_list)}
    if semester in semester_list: list_index = (semester_list.index(semester)) + 1
    action = class_to_fun[list_index](message)

    if action == -1:
        send_Semester(message, Field_index, section_index)
    elif action == -2:
        send_welcome(message)

    


def K_get_Semester(message, semester_list, Field_index, section_index):
    logger.info("triggred 7: OK ...")

    def_Class_list = [K_class1, K_class2, K_class3, K_class4, 
                      K_class5, K_class6, K_class7, K_class8]

    def_Docs_list = [K_docs1, K_docs2, K_docs3, K_docs4,
                     K_docs5, K_docs6, K_docs7, K_docs8]

    # def_MasID_list = [K_masid1, K_masid2, K_masid3, K_masid4,
    #                   K_masid5, K_masid6, K_masid7, K_masid8]
    def_list = []
    list_index = 0
    semester = message.text

    # Control:
    if message.text == semester_list[8]:
        send_search_type(message, Field_index, section_index)
    elif message.text == semester_list[9]:
        send_welcome(message)

    # Type ask:
    if section_index == 0:
        def_list = def_Class_list
    elif section_index == 1:
        def_list = def_Docs_list
    # elif section_index == 6:
    #     def_list = def_MasID_list

    class_to_fun = {i+1: func for i, func in enumerate(def_list)}
    if semester in semester_list: list_index = (semester_list.index(semester)) + 1
    action = class_to_fun[list_index](message, Field_index, section_index)

    if action == -1:
        send_Semester(message, Field_index, section_index)


def I_get_Semester(message, semester_list, Field_index, section_index):
    logger.info("triggred 7: OK ...")

    def_Class_list = [I_clas41, I_class2, I_class3, I_class4,
                      I_class5, I_class6, I_class7, I_class8]

    def_Docs_list = [I_docs1, I_docs2, I_docs3, I_docs4,
                     I_docs5, I_docs6, I_docs7, I_docs8]

    # def_MasID_list = [I_masid1, I_masid2, I_masid3, I_masid4,
    #                   I_masid5, I_masid6, I_masid7, I_masid8]
    def_list = []
    list_index = 0
    semester = message.text

    # Control:
    if message.text == semester_list[8]:
        send_search_type(message, Field_index, section_index)
    elif message.text == semester_list[9]:
        send_welcome(message)

    # Type ask:
    if section_index == 0:
        def_list = def_Class_list
    elif section_index == 1:
        def_list = def_Docs_list
    # elif section_index == 6:
    #     def_list = def_MasID_list

    class_to_fun = {i+1: globals()[func] for i, func in enumerate(def_list)}
    if semester in semester_list: list_index = (semester_list.index(semester)) + 1
    class_to_fun[list_index](message)


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


#-------------------------------------------------------------------
def send_stud_forms(message):
    
    inline_markup = send_stud_forms_BTN()

    bot.send_message(message.chat.id, 
    """ برای دسترسی سریع به فرم مورد نظر از طریق لینک های زیر اقدام نمایید  🔽""",
    reply_markup = inline_markup)

    bot.send_message(message.chat.id,
    menu_back_MSG_TEXT,
    reply_markup = menu_back_BTN())


#-------------------------------------------------------------------
def send_educat_files(message):
    
    inline_markup = send_educat_files_BTN()

    bot.send_message(message.chat.id, 
    """ فایل مورد نظر را جهت دریافت انتخاب کنید  🔽""",
    reply_markup = inline_markup)

    bot.send_message(message.chat.id,
    menu_back_MSG_TEXT,
    reply_markup = menu_back_BTN())


#-------------------------------------------------------------------
def send_support_id(message, send_it):
    logger.info("triggred 3: OK ...")

    markup, support_list = send_support_id_BTN()

    if send_it == 0:
        bot.send_message(message.chat.id,"""
        🌟  لطفا گزینه موردنظرت رو انتخاب کن 👇🏻""",
        reply_markup = markup)
        
    bot.register_next_step_handler(message, get_support_id, support_list)


def get_support_id(message, support_list): #support_list
    logger.info("triggred 4: OK ...")
    
    if message.text == support_list[2]:
        send_welcome(message)
    else:
        bot.send_message(message.chat.id,"""
        🌟  لطفا نظر خود را با ما در میان بزارید👇🏻""",
        reply_markup = get_support_id_BTN(message.text, support_list))
        send_support_id(message, -1)


#-------------------------------------------------------------------
def send_faculty_call(message):

    Faculty_Call_list(message)

    bot.send_message(message.chat.id,
    menu_back_MSG_TEXT,
    reply_markup = menu_back_BTN())


#*******************************************************************************


def K_docs1(message, Field_index, section_index):
    # inline_markup = K_docs6_BTN()
    inline_markup = []

    bot.send_message(message.chat.id,
    "هنوز لیستی وارد نشده",
    reply_markup = inline_markup)

    bot.send_message(message.chat.id,
    both_back_MSG_TEXT,
    reply_markup = both_back_BTN())
    
    bot.register_next_step_handler(message, get_return, Field_index, section_index)


def K_docs2(message, Field_index, section_index):
    # inline_markup = K_docs6_BTN()
    inline_markup = []

    bot.send_message(message.chat.id,
    "هنوز لیستی وارد نشده",
    reply_markup = inline_markup)

    bot.send_message(message.chat.id,
    both_back_MSG_TEXT,
    reply_markup = both_back_BTN())
    
    bot.register_next_step_handler(message, get_return, Field_index, section_index)


def K_docs3(message, Field_index, section_index):
    # inline_markup = K_docs6_BTN()
    inline_markup = []

    bot.send_message(message.chat.id,
    "هنوز لیستی وارد نشده",
    reply_markup = inline_markup)

    bot.send_message(message.chat.id,
    both_back_MSG_TEXT,
    reply_markup = both_back_BTN())
    
    bot.register_next_step_handler(message, get_return, Field_index, section_index)


def K_docs4(message, Field_index, section_index):
    # inline_markup = K_docs6_BTN()
    inline_markup = []

    bot.send_message(message.chat.id,
    "هنوز لیستی وارد نشده",
    reply_markup = inline_markup)

    bot.send_message(message.chat.id,
    both_back_MSG_TEXT,
    reply_markup = both_back_BTN())
    
    bot.register_next_step_handler(message, get_return, Field_index, section_index)


def K_docs5(message, Field_index, section_index):
    # inline_markup = K_docs6_BTN()
    inline_markup = []

    bot.send_message(message.chat.id,
    "هنوز لیستی وارد نشده",
    reply_markup = inline_markup)

    bot.send_message(message.chat.id,
    both_back_MSG_TEXT,
    reply_markup = both_back_BTN())
    
    bot.register_next_step_handler(message, get_return, Field_index, section_index)


def K_docs6(message, Field_index, section_index):
    inline_markup = K_docs6_BTN()

    bot.send_message(message.chat.id,
    "لیست دروس تــرم  🔽",
    reply_markup = inline_markup)

    bot.send_message(message.chat.id,
    both_back_MSG_TEXT,
    reply_markup = both_back_BTN())
    
    bot.register_next_step_handler(message, get_return, Field_index, section_index)


def K_docs7(message, Field_index, section_index):
    # inline_markup = K_docs6_BTN()
    inline_markup = []

    bot.send_message(message.chat.id,
    "هنوز لیستی وارد نشده",
    reply_markup = inline_markup)

    bot.send_message(message.chat.id,
    both_back_MSG_TEXT,
    reply_markup = both_back_BTN())
    
    bot.register_next_step_handler(message, get_return, Field_index, section_index)
    

def K_docs8(message, Field_index, section_index):
    # inline_markup = K_docs6_BTN()
    inline_markup = []

    bot.send_message(message.chat.id,
    "هنوز لیستی وارد نشده",
    reply_markup = inline_markup)

    bot.send_message(message.chat.id,
    both_back_MSG_TEXT,
    reply_markup = both_back_BTN())
    
    bot.register_next_step_handler(message, get_return, Field_index, section_index)


#*******************************************************************************
def no_list_MasId(message, section_index):
    logger.info("triggred 77777: OK ...")

    if message.text == Return_BTN_LIST[0]:
        logger.info("triggred 8888: OK ...")
        send_welcome(message)

    elif message.text == Return_BTN_LIST[1]:
        send_Field(message, section_index)

    bot.send_message(message.chat.id,
    "هنوز لیستی وارد نشده",
    reply_markup = both_back_BTN())


#-------------------------------------------------------------------
def no_list_Class(message, Field_index, section_index):
    
    logger.info("triggred 77777: OK ...")

    if message.text == Return_BTN_LIST[0]:
        logger.info("triggred 8888: OK ...")
        send_search_type(message, Field_index, section_index)

    elif message.text == Return_BTN_LIST[1]:
        send_welcome(message)

    bot.send_message(message.chat.id,
    "هنوز لیستی وارد نشده",
    reply_markup = both_back_BTN())
    



#*******************************************************************************
# Buttons:

def menu_back_BTN():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton(menu_back_BTN_TEXT))
    return markup

def return_back_BTN():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton(return_back_BTN_TEXT))
    return markup

def both_back_BTN():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for return_btn in range(2):
        markup.add(KeyboardButton(Return_BTN_LIST[return_btn]))
    return markup


#-------------------------------------------------------------------
def send_welcome_BTN():

    section_list = [
        "کلاس های درسی",
        "جزوه های درسی",
        "سامانه های دانشجویی",
        "تشکل های دانشجویی",
        "فرم های دانشجویی",
        "فایل های آمورشی",
        "ارتباط با اساتید",
        "تماس با واحدهای دانشکده",
        "ارتباط با پشتیبانی"
    ]

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for sl in range(0, 7, 2):
        markup.add(KeyboardButton(section_list[sl+1]), KeyboardButton(section_list[sl]))
    markup.add(KeyboardButton(section_list[8]))

    return markup, section_list


#-------------------------------------------------------------------
def send_Field_BTN():

    Field_list = [
        'مکانیک 👨🏻‍🔧','کامپیوتر 👨🏻‍💻', 'صنایع 👷🏻‍♂️',
        menu_back_BTN_TEXT
    ]

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for sl in range(3):
        markup.add(KeyboardButton(Field_list[sl]))
    markup.add(KeyboardButton(Field_list[3]))

    return markup, Field_list


#-------------------------------------------------------------------
def send_search_type_BTN(section_index):

    type_class_list = [
        'جستجـــوی هـمـــــــــه کلاس ها 🔠',
        'جستجوی کلاس ها بر اساس ترم 🔢',
        return_back_BTN_TEXT, menu_back_BTN_TEXT
    ]
    type_docs_list = [
        'جستجـــوی هـمـــــــــه جزوه ها 🔠',
        'جستجوی جزوه ها بر اساس ترم 🔢',
        return_back_BTN_TEXT, menu_back_BTN_TEXT
    ]


    type_list = []
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    if section_index == 0:
        for st in range(4):
            markup.add(KeyboardButton(type_class_list[st]))
            type_list = type_class_list

    elif section_index == 1:
        for st in range(4):
            markup.add(KeyboardButton(type_docs_list[st]))
            type_list = type_docs_list
    
    return markup, type_list


#-------------------------------------------------------------------
def send_Semester_BTN():

    semester_list = [
        'تــرم  1⃣', 'تــرم  2⃣',
        'تــرم  3⃣', 'تــرم  4⃣',
        'تــرم  5⃣','تــرم  6⃣',
        'تــرم  7⃣', 'تــرم  8⃣',
        return_back_BTN_TEXT, menu_back_BTN_TEXT
    ]

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for sl in range(0, 7, 2):
        markup.add(KeyboardButton(semester_list[sl+1]), 
                   KeyboardButton(semester_list[sl]))
    markup.add(KeyboardButton(semester_list[8]))
    markup.add(KeyboardButton(semester_list[9]))

    return markup, semester_list

#-------------------------------------------------------------------
def send_webs_BTN():

    web_name = [
        'سایت دانشکده 🌐',
        'سایت کتابخانه 📚' ,
        'سامانه سمــاد 🍔',
        'سمــــــــاد اپ ✅',
        'سامانه نــــــاد 📝',
        'صندوق رفاه دانشجویان 📥'
    ]
    
    web_url = [
        "https://miyanehtech.tabrizu.ac.ir/fa",
        "https://google.com",
        "https://samad-mi.tabrizu.ac.ir/index/index.rose",
        "https://samad.app",
        "http://46.209.208.110:7010/Student/Pages/acmstd/loginPage.jsp",
        "https://refah.swf.ir/Account/Login/?ReturnUrl=%2F"
    ]

    inline_markup = InlineKeyboardMarkup()
    for sw in range(6):
        inline_markup.add(InlineKeyboardButton(text= web_name[sw], url= web_url[sw]))

    return inline_markup


#-------------------------------------------------------------------
def send_orgs_BTN():

    org_name = [
        'شـــورای صنفــــــــی دانشکده  ⭕️',
        'انجمن علمی مهندسی مکـانـیک  ⭕️',
        'انجمن علمی مهندسی کامپیوتر  ⭕️',
        'انجمن علمی مهندسی صنــــایع  ⭕️',
        'بسیــــــج دانشجویی دانشکده  ⭕️',
        'نشـریـــــــه های دانــــشجویی  ⭕️'
    ]
    
    org_url = [
        "https://t.me/senfimiyane",
        "https://t.me/MECH_MSME",
        "https://t.me/Computer_SCM",
        "https://ssss.ss",
        "https://t.me/basij_mianeh",
        "https://ssss.ss"
    ]

    inline_markup = InlineKeyboardMarkup()
    for so in range(6):
        inline_markup.add(InlineKeyboardButton(text= org_name[so], url= org_url[so]))

    return inline_markup


#-------------------------------------------------------------------
def send_stud_forms_BTN():

    forms_name = [
        "فرم درخواست بررسی مشکلات امتحانی دانشجویان",
        "فرم تسویه حساب",
        "فرم درخواست مهمانی و انتقال",
        "گواهی اشتغال به تحصیل",
        "گزارش ارزیابی کارآموزی",
        "فرم درخواست مهمان در ترم تابستانی",
        "فرم درخواست معادل سازی دروس",
        "فرم درخواست مرخصی تحصیلی دانشجویان",
        "فرم درخواست تغییر رشته داخل دانشگاه",
        "فرم درخواست استاد راهنمای پروژه تخصصی",
        "فرم حذف تک درس",
        "فرم حذف اضطراری",
        "فرم تقاضای امتحان معرفی به استاد",
        "فرم پیشنهاد پروژه تخصصی کارشناسی",
        "درخواست کارآموزی",
        "فرم ارزیابی کارآموزی",
        "فرم معرفی به کارآموزی"
    ]

    forms_urls = [
        "https://miyanehtech.tabrizu.ac.ir/file/download/page/1593425151-.docx",
        "https://miyanehtech.tabrizu.ac.ir/file/download/page/1625644738-.docx",
        "https://miyanehtech.tabrizu.ac.ir/file/download/page/1591086925-.doc",
        "https://miyanehtech.tabrizu.ac.ir/file/download/page/1592291479-99-.docx",
        "https://miyanehtech.tabrizu.ac.ir/file/download/page/1572256100-.docx",
        "https://miyanehtech.tabrizu.ac.ir/file/download/page/1594713480-1572255861-.doc",
        "https://miyanehtech.tabrizu.ac.ir/file/download/page/1572255748-.docx",
        "https://miyanehtech.tabrizu.ac.ir/file/download/page/1572255677-.docx",
        "https://miyanehtech.tabrizu.ac.ir/file/download/page/1572255512-.docx",
        "https://miyanehtech.tabrizu.ac.ir/file/download/page/1594713433-1572255428-2-.doc",
        "https://miyanehtech.tabrizu.ac.ir/file/download/page/1572254473-.docx",
        "https://miyanehtech.tabrizu.ac.ir/file/download/page/1572254337-.docx",
        "https://miyanehtech.tabrizu.ac.ir/file/download/page/1572254259-.docx",
        "https://miyanehtech.tabrizu.ac.ir/file/download/page/1572254200-.doc",
        "https://miyanehtech.tabrizu.ac.ir/file/download/page/1591763964-.docx",
        "https://miyanehtech.tabrizu.ac.ir/file/download/page/1594184770-.docx",
        "https://miyanehtech.tabrizu.ac.ir/file/download/page/1593935756-.docx"
    ]

    inline_markup = InlineKeyboardMarkup()
    for sf in range(17):
        inline_markup.add(InlineKeyboardButton(text= forms_name[sf], url= forms_urls[sf]))

    return inline_markup


#-------------------------------------------------------------------
def send_educat_files_BTN():

    doc_name = [
        "برنامه کلاسی و امتحانی ۱۴۰۴ - ۱۴۰۳",
        "چارت درسی مهندسی مکانیک",
        "چارت درسی مهندسی کامپیوتر",
        "چارت درسی مهندسی صنایع",
        "لیست کد دروس مهندسی مکانیک",
        "لیست کد دروس مهندسی کامپیوتر",
        "لیست کد دروس مهندسی صنایع",
        "رهنمای جامع انتخاب واحد",
        "آیین نامه شرکت در امتحانات"
    ]

    doc_callback = [
        "Class_and_Exam_schedule",
        "M_E_chart",
        "C_E_chart",
        "I_E_chart",
        "M_E_code_list",
        "C_E_code_list",
        "I_E_code_list",
        "Unit_selection_guide",
        "Exam_regulation"
    ]

    inline_markup = InlineKeyboardMarkup()
    for ef in range(9):
        inline_markup.add(InlineKeyboardButton(text = doc_name[ef], callback_data = doc_callback[ef]))

    return inline_markup


#-------------------------------------------------------------------
def send_support_id_BTN():

    support_list = [
        "ارسال پیشنهادات",
        "گزارش باگ",
    ]

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for si in range(3):
        markup.add(KeyboardButton(support_list[si]))

    return markup, support_list
    

def get_support_id_BTN(request, support_list):

    supports_name = [
        'ارتباط با ادمین',
        'ارتباط با توسعه دهنده'
    ]
    supports_id = [
        'https://t.me/ZNR_KD',
        'https://t.me/ZNR_KD'
    ]
    
    inline_markup = InlineKeyboardMarkup(row_width=2)
    if request == support_list[0]:
        inline_markup.add(InlineKeyboardButton(text= supports_name[0], url= supports_id[0]))
    elif request == support_list[1]:
        inline_markup.add(InlineKeyboardButton(text= supports_name[1], url= supports_id[1]))

    return inline_markup


#*******************************************************************************
def K_docs6_BTN():

    doc6_name = [
        "اصول علم ربات",
        "مبانی هوش محاسباتی",
        "شبکه های کامپیوتری",
        "آز شبکه های کامپیوتری",
        "اقتصاد مهندسی",
        "اندیشه 2"
    ]

    doc6_callback = ["Class_and_Exam_schedule"]


    inline_markup = InlineKeyboardMarkup(row_width=1)
    for kd in range(6):
        inline_markup.add(InlineKeyboardButton(text = doc6_name[kd], callback_data = doc6_callback[0]))

    return inline_markup


#*******************************************************************************
# handlers:

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_txt = """🌟  سلام!👋🏻 \n🌟 به ربات ما خوش اومدی ، 😊\n\n 🌟  در چه زمینه ای کمک میخای ؟👇🏻"""

    markup, section_list = send_welcome_BTN()
    bot.send_message(message.chat.id, welcome_txt, reply_markup = markup)
    bot.register_next_step_handler(message, get_section, section_list)


#-------------------------------------------------------------------
@bot.message_handler(func=lambda message: True)
def Reback(message):

    if message.text == menu_back_BTN_TEXT:
        logger.info("triggred back: OK ...")
        send_welcome(message)

    # if message.text == return_back_BTN_TEXT:
    #     logger.info("triggred back: OK ...")
    #     send_Semester(message, Field_index, section_index)

#-------------------------------------------------------------------
@bot.message_handler(content_types=["document"])
def Check_id(message):

    logger.info("triggred get: OK ...")
    logger.info(message.__dict__)

#-------------------------------------------------------------------
@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    # Menu Back Callback:
    # if call.data == "return_menu":
    #     logger.info("triggred menu_back: OK ...")
    #     send_welcome(call.message)

    # Educational Files Callback:
    if call.data == "Class_and_Exam_schedule":
        bot.send_chat_action(call.message.chat.id, action= "upload_document")
        bot.send_document(call.message.chat.id, "BQACAgQAAxkBAAII7WgD3VQw65pQ6vKp-ENcfcVEo7SlAALCFgACYZERUZW3GkWFUXoAATYE")

    if call.data == "Unit_selection_guide":
        bot.send_chat_action(call.message.chat.id, action= "upload_document")
        bot.send_document(call.message.chat.id, "BQACAgQAAxkBAAII7WgD3VQw65pQ6vKp-ENcfcVEo7SlAALCFgACYZERUZW3GkWFUXoAATYE")

    if call.data == "M_E_chart":
        bot.send_chat_action(call.message.chat.id, action= "upload_document")
        bot.send_document(call.message.chat.id, "BQACAgQAAxkBAAII7WgD3VQw65pQ6vKp-ENcfcVEo7SlAALCFgACYZERUZW3GkWFUXoAATYE")

    if call.data == "C_E_chart":
        bot.send_chat_action(call.message.chat.id, action= "upload_document")
        bot.send_document(call.message.chat.id, "BQACAgQAAxkBAAII7WgD3VQw65pQ6vKp-ENcfcVEo7SlAALCFgACYZERUZW3GkWFUXoAATYE")

    if call.data == "I_E_chart":
        bot.send_chat_action(call.message.chat.id, action= "upload_document")
        bot.send_document(call.message.chat.id, "BQACAgQAAxkBAAII7WgD3VQw65pQ6vKp-ENcfcVEo7SlAALCFgACYZERUZW3GkWFUXoAATYE")

    if call.data == "M_E_code_list":
        bot.send_chat_action(call.message.chat.id, action= "upload_document")
        bot.send_document(call.message.chat.id, "BQACAgQAAxkBAAII7WgD3VQw65pQ6vKp-ENcfcVEo7SlAALCFgACYZERUZW3GkWFUXoAATYE")

    if call.data == "C_E_code_list":
        bot.send_chat_action(call.message.chat.id, action= "upload_document")
        bot.send_document(call.message.chat.id, "BQACAgQAAxkBAAII7WgD3VQw65pQ6vKp-ENcfcVEo7SlAALCFgACYZERUZW3GkWFUXoAATYE")

    if call.data == "I_E_code_list":
        bot.send_chat_action(call.message.chat.id, action= "upload_document")
        bot.send_document(call.message.chat.id, "BQACAgQAAxkBAAII7WgD3VQw65pQ6vKp-ENcfcVEo7SlAALCFgACYZERUZW3GkWFUXoAATYE")

    if call.data == "Exam_regulation":
        bot.send_chat_action(call.message.chat.id, action= "upload_document")
        bot.send_document(call.message.chat.id, "BQACAgQAAxkBAAII7WgD3VQw65pQ6vKp-ENcfcVEo7SlAALCFgACYZERUZW3GkWFUXoAATYE")


#-------------------------------------------------------------------
bot.polling() 

# bot.infinity_polling()

# inline_markup.add(InlineKeyboardButton(text= org_name[6], callback_data="return_menu"))

# remove_markup = ReplyKeyboardRemove()
# mess = bot.send_message(message.chat.id, """...""", reply_markup = remove_markup)
# sleep(0.5)
# bot.delete_message(message.chat.id, mess.message_id)