save_as: reports/session-102/index.html
url: reports/session-102
title: گزارش جلسه‌ی ۱۰۲ام
layout: page
author: tuxitop
date: 2012-05-30 19:07:00
meta: date by tuxitop on Wed, 05/30/2012 - 19:07
category: reports

جلسه ۱۰۲م گروه کاربران در ساعت ۱۷ روز دوشنبه هشتم خرداد ماه ۱۳۹۱، در محل شرکت
معیار گستر توس با حضور تعدادی از اعضای آن برگزار شد.


<!--more-->


موضوعاتی که در این جلسه به آن‌ها پرداخته شد عبارتند از:  
## بررسی اخبار دنیای متن باز *آرش موسوی*

## آشنایی با دبین گنو هرد *مهدی عطائیان*
اطلاعات بیشتر در [ویکی‌پدیا](http://fa.wikipedia.org/wiki/%DA%AF%D9%86%D9%88_%D9%87%D8%B1%D8%AF)  

## معرفی ابزار Bitlbee *مرتضی فخرایی*

درگاهی برای ارسال پیام فوری در IRC

### BitlBee
In simple word: BitlBee enables you to use your IRC client with popular chat networks  like GMail or Yahoo.

Technically speaking, BitlBee is and IRC instant messaging gateway. It communicates with the end-user via the IRC protocol whilst interacting with popular chat networks such as AIM and ICQ (both via OSCAR), .NET Messeng" "er Service, Yahoo! and
Jabber.

### Install Or Not
BilBee is a and irc deamon. You can install it on your own system: 
`apt-get install bitlbee`

Or choose one of many ready to use public servers out there:
[[http://bitlbee.org/main.php/servers.html]]

### Using BitlBee
Just fire up your irc client and connect to a BilBee server. In case you installed it on your machine, check if it's running with:  
`lsof -i -n|grep -i bitlb`
and it should be listening on localhost and port 6667/ircd.  

When connected, type `help` on the root screen, where you can see bunch of welcome message from BitlBee server. From there it should be pretty straight forward.  

### Help
Consider reading [[http://princessleia.com/bitlbee.php]] and [[http://wiki.bitlbee.org/]] to get and idea what's it all about!  


[[!author acathur acathur@lavabit.com]]


## ترفند‌هایی در مونت کردن فایل پشتیبان تهیه شده از کل هارد‌دیسک *بیژن ابراهیمی*

```
موضوع:ترفند‌هایی در مونت کردن فایل پشتیبان تهیه شده از کل هارد‌دیسک
ارايه دهنده: بیژن ابراهیمی

سناریو:
فرض کنید فایل پشتیبانی را از کل هارد دیسک خود که شامل چندین پارتیشن می‌باشد، به صورت زیر بدست‌اورده اید:
# dd if=/dev/sda of=hdd.iso

به دلیل آنکه فایل پشتیبان فوق حاوی اطلاعات بیشتری همچون رکورد‌های مستر‌بوت و فلگ‌های مربوطه و حتی چندین پارتیشن جداگانه می‌باشد، شما نمیتوانید آن را به صورت دستی با دستور mount مشاهده کنید!

# mount -o loop hdd.iso /mnt
mount: you must specify the filesystem type

راه حل:
برای مشاهده اطلاعات موجود در پارتیشن مختلف فایل پشتیبان هارددیسک خود کافی است به دستور mount بگوئیم که از چندمین بایت شروع به عمل مونت کردن کند. برای به دست آوردن آدرس شروع پارتیشن میتوانید از برنامه parted استفاده کنید:

$ parted hdd.iso
(parted) [unit]--------------> برای تغییر واحد پیش‌فرض برنامه
uni? [compact]? [B]----------> واحد پیش‌فرض را به بایت تغییر میدهد
(parted) [p]-----------------> نمایش لیست پارتیشن‌ها
Model:  (file)
Disk /backup/hdd.iso: 969971712B
Sector size (logical/physical): 512B/512B
Partition Table: msdos
Number  Start       End         Size        Type      File system  Flags
 1      16384B      200015871B  199999488B  primary   ext2
 2      200015872B  969932799B  769916928B  extended               lba
 5      200032256B  969932799B  769900544B  logical   ext2


مشاهده می‌کنید که اولین پارتیشن هارد دیسک (primary) از بایت 16384 شروع شده است! حال برای مونت کردن پارتیشن مزبور کافی است از پارامتر offset استفاده کنیم:
# mount -o loop,ro,offset=16384 hdd.iso /mnt

همچنین میتوانیم برای جدا کردن پارتیشن داخل فایل پشتیبان، به عنوان مثال پارتیشن اول از دستور dd به صورت زیر استفاده کنیم:

$ dd if=hdd.iso skip=16384 bs=512 count=390624 of=hdd_primary_partition.iso
```


## بحث آزاد  
## بحث و تبادل‌نظر

بحث و تبادل‌نظر اعضای فعال در همایش برگزار شده پیرامون نکات ضعف و قدرت آن
