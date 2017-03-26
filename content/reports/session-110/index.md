save_as: reports/session-110/index.html
url: reports/session-110
title: جلسه ۱۱۰م گروه کاربران لینوکس مشهد
layout: page
author: Echo
date: 2012-07-23 16:21:00
meta: date by Echo on Mon, 07/23/2012 - 16:21
category: reports

جلسه ۱۱۰م گروه کاربران لینوکس در ساعت ۱۷ روز شنبه ۳۱ تیر ماه ۱۳۹۱، در محل شرکت
معیار گستر توس با حضور تعدادی از اعضای آن برگزار شد.
موضوعاتی که در این جلسه به آن‌ها پرداخته شد عبارتند از:

<!--more-->



## بررسی اخبار دنیای متن باز *آرش موسوی*
## نکته‌ی خط فرمان نحوه‌ی تغییر ابزارهای پیش‌فرض سیستم *بیژن ابراهیمی*

```
۱. مقدمه:
در سیستم‌های لینوکسی شما قادر به نصب نسخه‌های متفاوتی از یک ابزار و یا ابزار متفاوتی با کارائی یکسانی را دارید. به عنوان مثال ویرایش‌های متفاتی از ویرایگشر متن vim (مثلا vim.basic یا vim.tiny) در آن واحد می‌تواند بر روی یک سیستم نصب شود (و یا حتی ورژن‌های متفاوتی مانند پایتون ۲ و ۳). حال سوال اینجاست با اجرای دستور vim و یا python کدام یک از ابزار فوق اجرا می‌شوند. در سیستم‌های مبتنی بر دبین این مشکل با معرفی alternatives برطرف شده است. زمانی که دستور vim اجرا میشود، پروسه زیر طی می‌شود:

vim ---RUN--> /usr/bin/vim ----SYM-LINK----> /etc/alternatives/vim ----SYM-LINK----> /usr/bin/vim.tiny

در این پروسه ابتدافایل vim که خود سافت (سیمبالیک) لینکی به فایلی در آلترنتیو‌هاست اجرا میشود که خود این آلترنتیو، سافت لینکی به باینری نسخه پیش‌فرضی که سیستم می‌شناسد (در این مورد vim.tiny). 

۲. معرفی ابزار update-alternatives:
این ابزار برای ایجاد، حذف، نگهداری و نمایش این سمبالیک ها استفاده می‌شود.

	۲.۱ نمایش آلترنتیو‌ها
	برا نمایش آلترنتیو ها دو روش وجود دارد
		۲.۱.۱ مشاهده سیمبالیک لینک‌های آلترنتیو مورد نظر
		$ ls -la /etc/alternatives/vim
		۲.۲.۲ آرگومان display
		$ update-alternatives --display vim

	۲.۲ پیکره‌بندی آلترنتیو‌ها به صورت تعاملی
	# update-alternatives --config xxx
	که در اینجا xxx نام لینک آلترنتیوی است که مایل به ویرایش آن هستید.مثال:
	# update-alternatives --config vim
	# update-alternatives --config x-www-browser
	پس از اجرای این دستور، لیستی از ابزار معادل آورده شده و از کاربر برای انتخاب
	یکی از آنها، سوال پرسیده میشود.

	۲.۳ اضافه کردن گزینه‌ها(ابزار)ی بیشتر به لیست آلترنتیو‌ها
	# sudo update-alternatives --install /usr/bin/x-www-browser x-www-browser /home/echo/binary/firefox/firefox 41
	در مثال فوق به آلترنتیو x-www-browse (مرورگر پیش‌فرض محیط گرافیکی)، فایرفاکس با
	الویت ۴۰ اضافه می‌شود. ابزار با الویت بالاتر، اولین انتخاب سیستم خواهند بود. 
	بنابراین اگر مرورگر دیگری در این لیست با الویت پائین‌تری وجود داشته باشد (برای 
	مثال کرومیوم با الویت ۳۰)، فایرفاکس جایگزین آن خواهد شد
	
	# update-alternatives --install /usr/bin/vi vi /usr/bin/vim 900 --slave /usr/share/man/vi.1.gz vi.1.gz /usr/share/man/
	در مثال دیگر فوق، نشان داده شده که می‌توان برای الترنتیو جدید، مسیر فایل راهنما
	(اسلیو لینک) مجزائی مشخص کرد که با هر بار فراخوانی دستور man vi فراخوانده شود.

	۲.۴ حذف آلترنتیو
	# update-alternatives --remove vi /usr/bin/vim

	۲.۵ برای مشاهده دیگر پارامتر‌های این دستور به راهنمای دستور مراجعه کنید
	$ man update-alternatives
```
## معرفی مدیرفایل mc *مرتضی فخرائی*

```
# MidnightCommander
 
Mostly from manpage.
 
## Switches
 
-b, --nocolor
Force black and white display.
 
-c, --color
Force color mode, please check the section Colors for more information.
 
-e [file], --edit[=file]
Start the internal editor. If the file is specified, open it on startup. See also mcedit (1).
 
-v file, --view=file
Start the internal viewer to view the specified file. See also mcview (1).
 
-s, --slow
Turn on the slow terminal mode, in this mode the program will not draw expensive line drawing characters and will toggle verbose mode off.
 
-d, --nomouse
Disable mouse support.
 
---
 
## Keys
 
C is Ctrl. M is Alt.
 
C-x c
run the Chmod command on a file or on the tagged files.
 
C-x o
run the Chown command on the current file or on the tagged files.
 
C-x s
run the symbolic link command.
 
C-x i
set the other panel display mode to information.
 
C-x q
set the other panel display mode to quick view.
 
Tab, C-i
change the current panel.
 
Insert, C-t
to tag files
 
M-t
toggle the current display listing to show the next display listing mode. With this it is possible to quickly switch from long listing to regular listing and the user defined listing mode.
 
C-\\ (control-backslash)
show the directory hotlist and change to the selected directory.
+ (plus)
\\ (backslash)
use the "\" key to unselect a group of files. This is the opposite of the Plus key.
 
M-o
make the current directory of the current panel also the current directory of the other panel. Put the other panel to the listing mode if needed. If the current panel is panelized, the other panel doesn't become panelized.
 
M-y
moves to the previous directory in the history
 
M-u
moves to the next directory in the history
 
M-Enter
copy the currently selected file name to the command line.
 
M-Tab
does the filename, command, variable, username and hostname completion for you.
 
M-h
displays the history for the current input line.
 
M-p, M-n
use these keys to browse through the command history. M-p takes you to the last entry, M-n takes you to the next one.
 
C-a
puts the cursor at the beginning of line.
 
C-e
puts the cursor at the end of the line.
 
C-b, move-left
move the cursor one position left.
 
C-f, move-right
move the cursor one position right.
 
M-f
moves one word forward.
 
M-b
moves one word backward.
 
M-C-h, M-Backspace
delete one word backward.
 
Quick cd (M-c)
Use the quick cd command if you have full command line and want to cd somewhere.
 
C-x j
Background jobs.
 
F9 => configuration, learn keys
 
If you press Enter over a file that is not executable, the Midnight Commander checks the extension of the selected file against the extensions in the Extensions File. If a match is found then the code associated with that extension is executed. A very simple macro expansion takes place before executing the command. (debian => /etc/mc/mc.ext)
 
Previous directory. You can jump to the directory you were previously by using the special directory name '-' like this: cd -
 
Macro Substitution
When accessing a user menu, or executing an extension dependent command, or running a command from the command line input, a simple macro substitution takes place.
%d
The current directory name.
%F
The current file in the unselected panel.
%s and %S
The selected files: The tagged files if there are any. Otherwise the current file.
 
Completion
Attempt to perform completion on the text before current position. MC attempts completion treating the text as variable (if the text begins with $), username (if the text begins with ~), hostname (if the text begins with @) or command (if you are on the command line in the position where you might type a command
 
VFS:
FTP File System
/#ftp:[!][user[:pass]@]machine[:port][remote-dir]
 
extfs
to list CD-Audio tracks on your CD-ROM drive, type
cd #audio
 
Colors
<keyword>=<foregroundcolor>,<backgroundcolor>:<keyword>= ...
[Colors]
mine:
base_color=lightgray,default:normal=lightgray,default:selected=black,cyan:marked=yellow,default:markselect=white,cyan:errors=white,red:menu=lightgray,default:reverse=black,lightgray:dnormal=white,default:dfocus=black,cyan:dhotnormal=brightcyan,default:dhotfocus=brightcyan,cyan:viewunderline=brightred,default:menuhot=yellow,default:menusel=white,black:menuhotsel=yellow,black:helpnormal=black,lightgray:helpitalic=red,lightgray:helpbold=blue,lightgray:helplink=black,cyan:helpslink=yellow,default:gauge=white,black:input=black,cyan:directory=white,default:executable=brightcyan,default:link=brightcyan,default:stalelink=brightred,default:device=brightmagenta,default:core=red,default:special=black,default:editnormal=lightgray,default:editbold=yellow,default:editmarked=black,cyan:errdhotnormal=yellow,red:errdhotfocus=yellow,lightgray
 
Special Settings
old_esc_mode
By default the Midnight Commander treats the ESC key as a key prefix (old_esc_mode=0). If this option is set (old_esc_mode=1), the ESC key will act as a prefix key for one second, and if no extra keys have arrived, then the ESC key is interpreted as a cancel key (ESC ESC).
 
http://www.trembath.co.za/mctutorial.html
 
 
[[ !author acathur acathur@lavabit.com ]]
```

## معرفی برنامه xcompmgr *بیژن ابراهیمی*
([صفحه راهنما](http://man.cx/Xcompmgr))  

## بحث آزاد

* پروژه‌ی ویکی‌پدیای فارسی، هفته یازدهم شامل موضوعات مدیر پنجره [فلاکس‌باکس](http://fa.wikipedia.org/wiki/%D9%81%D9%84%D8%A7%DA%A9%D8%B3%E2%80%8C%D8%A8%D8%A7%DA%A9%D8%B3)، نرم‌افزار [وایرشارک](http://fa.wikipedia.org/wiki/%D9%88%D8%A7%DB%8C%D8%B1%D8%B4%D8%A7%D8%B1%DA%A9) و مستندات [صفحه راهنما](http://fa.wikipedia.org/wiki/%D8%B5%D9%81%D8%AD%D9%87_%D8%B1%D8%A7%D9%87%D9%86%D9%85%D8%A7) بود که به دلیل غیبت آقای رمضانیان، بررسی نشد.

این جلسه در ساعت ۱۹ خاتمه یافت.
