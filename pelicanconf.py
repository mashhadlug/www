#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
# import required filters
import sys
sys.path.append('./jinja-filters')
import mlug_summary

AUTHOR = 'admin'
SITENAME = 'گروه کاربران لینوکس مشهد'
SITEURL = ''
SITETITLE = 'گروه کاربران لینوکس مشهد'
SITESUBTITLE = 'آزادی، انتخاب، امنیت'

PATH = 'content'

TIMEZONE = 'Asia/Tehran'

DEFAULT_LANG = 'fa'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Disable
AUTHOR_SAVE_AS = False
CATEGORY_SAVE_AS = "{slug}/index.html"
TAG_SAVE_AS = False
CATEGORIES_SAVE_AS = False
TAGS_SAVE_AS = False

# Quotes
QUOTES = ({'text': """گروه کاربران لینوکس یا لاگ یک سازمان خصوصی، اغلب غیرانتفاعی
یا بدون هدف انتفاع است که برای اهداف پشتیبانی و یا آموزش
کاربران لینوکس بخصوص کاربران تازه‌کار لینوکس تشکیل می‌شود.
این عبارت اغلب به گروهی محلی گفته می‌شود که به صورت فیزیکی
دور هم جمع می‌شوند هر چند گاهی به گروه کاربرانی که در محدوده
جغرافیایی وسیع پراکنده شده‌اند و به صورت برخط با هم تعامل
دارند نیز گفته می‌شود.""" , 'author': 'ویکی پدیای فارسی', 'avatar': '/theme/images/icons/wikipedia.png'},
          {'text': """مشهدلاگ اجتماع آزادی از دوست‌داران گنو/لینوکس است که بیشتر در
شهر مشهد زندگی می‌کنند. ما به گرمی به کسانی که تمایل دارند
به اجتماع ما بپیوند، خوش‌آمد می‌گوییم. ما معمولاً یک هفته در
میان هر سه‌شنبه دیدار داریم و دربارهٔ گنو/لینوکس و فن‌آوری‌های
روز دنیای لینوکس صحبت می‌کنیم. فضای مشهدلاگ دوستانه است و شرکت
در آن برای همه آزاد و رایگان می‌باشد.""", 'author': 'گروه کاربران لینوکس مشهد', 'avatar': '/theme/images/icons/mashhadlug.gif'})

DEFAULT_PAGINATION = 10
#PAGINATION_PATTERNS = (
#    (1, '{base_name}/', '{base_name}/index.html'),
#    (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
#)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = 'template'

# Github Custom Domain
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

# Custom jinja filters
JINJA_FILTERS = {'mlug_summary':mlug_summary.filter_summary}
