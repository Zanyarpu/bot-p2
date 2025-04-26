import telebot
from telebot.types import KeyboardButton, ReplyKeyboardMarkup
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


# Buttons Text:
menu_back_BTN_TEXT = "منـــوی اصـــلی  ↪️"
return_back_BTN_TEXT = "مرحلـــه قبلـــی  ➡️"
Return_BTN_LIST = [return_back_BTN_TEXT, menu_back_BTN_TEXT]


#///////////////////////////////////////////////////////////////////////////
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
    for return_btn in Return_BTN_LIST:
        markup.add(KeyboardButton(return_btn))
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
    ]

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for field in Field_list:
        markup.add(KeyboardButton(field))

    markup.add(KeyboardButton(menu_back_BTN_TEXT))

    return markup, Field_list


#-------------------------------------------------------------------
def send_search_type_BTN(section_index):

    type_class_list = [
        'جستجـــوی هـمـــــــــه کلاس ها 🔠',
        'جستجوی کلاس ها بر اساس ترم 🔢',

    ]
    type_docs_list = [
        'جستجـــوی هـمـــــــــه جزوه ها 🔠',
        'جستجوی جزوه ها بر اساس ترم 🔢',
    ]

    type_list = []
    markup = ReplyKeyboardMarkup(resize_keyboard=True)

    if section_index == 0:
        for type_search in type_class_list:
            markup.add(KeyboardButton(type_search))
            type_list = type_class_list

    elif section_index == 1:
        for type_search in type_docs_list:
            markup.add(KeyboardButton(type_search))
            type_list = type_docs_list
    
    markup.add(KeyboardButton(return_back_BTN_TEXT))
    markup.add(KeyboardButton(menu_back_BTN_TEXT))

    return markup, type_list


#-------------------------------------------------------------------
def send_Semester_BTN():

    semester_list = [
        'تــرم  1⃣', 'تــرم  2⃣',
        'تــرم  3⃣', 'تــرم  4⃣',
        'تــرم  5⃣','تــرم  6⃣',
        'تــرم  7⃣', 'تــرم  8⃣',
    ]

    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for sl in range(0, 7, 2):
        markup.add(KeyboardButton(semester_list[sl+1]), 
                   KeyboardButton(semester_list[sl]))

    markup.add(KeyboardButton(return_back_BTN_TEXT))
    markup.add(KeyboardButton(menu_back_BTN_TEXT))

    return markup, semester_list

#-------------------------------------------------------------------
def send_webs_BTN():

    web_name = [
        'سایت دانشکده 🌐',
        'سایت کتابخانه 📚' ,
        'سامانه سمــاد 🍔',
        'سمــــــــاد اپ ✅',
        'سامانه نــــــاد 📝',
        'صنـدوق رفــاه دانشجویـان 📥',
        'سایت انجمن علمی کامپیوتر 🖥'
    ]
    
    web_url = [
        "https://miyanehtech.tabrizu.ac.ir/fa",
        "https://0000.ss",
        "https://samad-mi.tabrizu.ac.ir/index/index.rose",
        "https://samad.app",
        "http://46.209.208.110:7010/Student/Pages/acmstd/loginPage.jsp",
        "https://refah.swf.ir/Account/Login/?ReturnUrl=%2F",
        "https://0000.ss"
    ]

    inline_markup = InlineKeyboardMarkup()
    for sw in range(7):
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
    for support_id in support_list:
        markup.add(KeyboardButton(support_id))
    markup.add(KeyboardButton(menu_back_BTN_TEXT))

    return markup, support_list
    

def get_support_id_BTN(request, support_list):

    supports_name = [
        'ارتباط با ادمین',
        'ارتباط با توسعه دهنده'
    ]
    supports_id = [
        'https://t.me/Alireza_ktbi',
        'https://t.me/ZNR_KD'
    ]
    
    inline_markup = InlineKeyboardMarkup(row_width=2)

    if request == support_list[0]:
        inline_markup.add(InlineKeyboardButton(text= supports_name[0], url= supports_id[0]))
        inline_markup.add(InlineKeyboardButton(text= supports_name[1], url= supports_id[1]))

    elif request == support_list[1]:
        inline_markup.add(InlineKeyboardButton(text= supports_name[1], url= supports_id[1]))

    return inline_markup


#///////////////////////////////////////////////////////////////////////////
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


#///////////////////////////////////////////////////////////////////////////