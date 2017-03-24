save_as: reports/session-111/index.html
url: reports/session-111
title: گزارش جلسه ۱۱۱م گروه کاربران لینوکس مشهد
layout: page
author: Echo
date: 2012-07-29 09:43:00
meta: date by Echo on Sun, 07/29/2012 - 09:43
category: reports

جلسه ۱۱۱م گروه کاربران لینوکس در ساعت ۱۷ روز شنبه ۷ مرداد ماه ۱۳۹۱، در محل
شرکت معیار گستر توس با حضور تعدادی از اعضای آن برگزار شد.


<!--more-->


موضوعاتی که در این جلسه به آن‌ها پرداخته شد عبارتند از:

## بررسی اخبار دنیای متن باز *آرش موسوی*
## آشنایی با نحوه کانفیگ و کامپایل کرنل لینوکس *کوروش مهری*

```
A. Download Kernel Source file
	$ apt-get source linux-image-<kernel_version>
	$ wget http://www.kernel.org/pub/linux/kernel/...linux-<kernel_version>.tar.bz2
B. Extract the source file in /usr/src
	$ tar xjf linux-2.6.8.1.tar.bz2
C. Config new kernel
	$ make oldconfig #OR
	$ make menucofig
D. Compile Kernel & Modules
	$ make
	$ make modules
E. Install new Compiled Modules & Kernel
	# make modules_install
	# make install
D. Update Grub
	# update-grub
```

## معرفی ابزار dirsplit *بیژن ابراهیمی*
معرفی ابزار dirsplit برای تقسیم محتوای یک دایرکتوری به دایرکتوری‌هایی با
اندازه مشخص  ([صفحه راهنما](http://man.cx/dirsplit))  

## نکته خط‌فرمان *حامد رمضانیان*
معرفی ابزار compgen در پوسته bash

## بررسی فعالیت هفته‌ی یازدهم پروژه‌ی ویکی‌پدیای فارسی *حامد رمضانیان*
بررسی فعالیت هفته‌ی یازدهم پروژه‌ی ویکی‌پدیای فارسی شامل موضوعات مدیر پنجره
[فلاکس‌باکس](http://fa.wikipedia.org/wiki/%D9%81%D9%84%D8%A7%DA%A9%D8%B3%E2%80
%8C%D8%A8%D8%A7%DA%A9%D8%B3)، نرم‌افزار [وایرشارک](http://fa.wikipedia.org/wik
i/%D9%88%D8%A7%DB%8C%D8%B1%D8%B4%D8%A7%D8%B1%DA%A9) و مستندات [صفحه راهنما](ht
tp://fa.wikipedia.org/wiki/%D8%B5%D9%81%D8%AD%D9%87_%D8%B1%D8%A7%D9%87%D9%86%D
9%85%D8%A7)
## بحث آزاد



این جلسه در ساعت ۱۹ به کار خود پایان داد.
