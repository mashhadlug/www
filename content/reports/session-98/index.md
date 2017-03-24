save_as: reports/session-98/index.html
url: reports/session-98
title: گزارش جلسه ۹۸م
layout: page
author: Echo
date: 2012-04-29 09:31:00
meta: date by Echo on Sun, 04/29/2012 - 09:31
category: reports

جلسه ۹۸م گروه کاربران در ساعت ۱۷ روز شنبه ۹ اردیبهشت‌ماه ۱۳۹۱ با حضور تعدادی
از اعضای آن در شرکت معیار گستر توس برگزار شد موضوعاتی که در این جلسه به آن‌ها
پرداخته شد عبارتند از:  


<!--more-->



## اخبار دنیای متن باز *آرش موسوی*

## پخش فیلم (TED.com) *اختراعی که یک هنرمند دربند را رها کرد*

[Video](http://www.ted.com/talks/mick_ebeling_the_invention_that_unlocked_a_locked_in_artist.html)
[Subtitle](http://tedtalksubtitledownload.appspot.com/get_subtitle?tedtalkid=1115&lang=fa&timeIntro=15330))

## نکته خط فرمانی *بیژن ابراهیمی*

معرفی دستور stat: از دستور stat برای نمایش وضعیت فایل یا فایل سیستم استفاده میشود
```
SYNOPSIS
       stat [OPTION]... FILE...
```

در مثال‌های زیر نمونه‌ای از خروجی این دستور را مشاهده خواهید کرد:

خروجی دستور stat برای دریافت متاداده‌های یک فایل:
```
(echo ~ $) stat /etc/resolv.conf 
  File: `/etc/resolv.conf'
  Size: 38        	Blocks: 8          IO Block: 4096   regular file
Device: 821h/2081d	Inode: 279140      Links: 1
Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2012-04-29 08:54:56.310426822 +0430
Modify: 2012-04-29 08:54:54.425927010 +0430
Change: 2012-04-29 08:54:54.425927010 +0430
```

خروجی دستور stat برای دریافت متاداده‌های یک دایرکتوری:
```
stat /etc
  File: `/etc'
  Size: 4096      	Blocks: 8          IO Block: 4096   directory
Device: 821h/2081d	Inode: 258561      Links: 114
Access: (0755/drwxr-xr-x)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2012-04-29 09:12:07.693926966 +0430
Modify: 2012-04-29 08:51:47.021926766 +0430
Change: 2012-04-29 08:51:47.021926766 +0430
```

خروجی دستور stat برای دیافت متاداده‌های فایل سیستم (مونت شده):
```
stat /etc
  File: `/etc'
  Size: 4096      	Blocks: 8          IO Block: 4096   directory
Device: 821h/2081d	Inode: 258561      Links: 114
Access: (0755/drwxr-xr-x)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2012-04-29 09:12:07.693926966 +0430
Modify: 2012-04-29 08:51:47.021926766 +0430
Change: 2012-04-29 08:51:47.021926766 +0430
(echo ~ $) stat /
  File: `/'
  Size: 4096      	Blocks: 8          IO Block: 4096   directory
Device: 821h/2081d	Inode: 2           Links: 21
Access: (0755/drwxr-xr-x)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2012-04-28 10:22:04.426149617 +0430
Modify: 2012-04-09 19:41:04.943829929 +0430
Change: 2012-04-09 19:41:04.943829929 +0430
```

خروجی دستور stat قابل قالب‌بندی شدن میباشد. برای این منظور میتوان
از پارامتر c استفاده کرد:
```
stat -c "%a %u:%g %n" /etc/*.conf
644 0:0 /etc/adduser.conf
644 0:0 /etc/ca-certificates.conf
644 0:0 /etc/debconf.conf
644 0:0 /etc/deluser.conf
644 0:0 /etc/discover-modprobe.conf
644 0:0 /etc/ffserver.conf
640 0:108 /etc/fuse.conf
644 0:0 /etc/gai.conf
644 0:0 /etc/gssapi_mech.conf
644 0:0 /etc/hdparm.conf
```

در مثال بالا پارامتر های زیر:

```
%a		نمایش مجوز فایل به صورت اکتال
%u		نمایش شناسه کاربر مالک فایل
%g 		نمایش شناسه گروه مالک فایل
%n		نام فایل
```

برای اطلاع بیشتر از انواع فرمت‌بندی به راهنمای دستور مراجعه کنید:
```
$ man stat
```

تعریف یک alias برای نمایش فایل ها و پوشه به صورت مجوز اوکتالی آنها:

```
vim ~/.bashrc
	[append the following lines in your ~/.bashrc file, if you use BASH]
	alias las="stat -c '%a %u:%g %n' ./*"
```

حال میتوان با دستور معادل las خروجی زیر را پوشه فعلی در خط فرمان گرفت:

```
(echo wallpapers $) las
644 1000:1000 ./20475-nightmare.jpg
644 1000:1000 ./22463-SpiriT.jpg
644 1000:1000 ./22470-Boney-Penguin.jpg
644 1000:1000 ./22474-drNo.011_r_3.png
644 1000:1000 ./22477-g5.lim.jpg
644 1000:1000 ./22486-star.jpg
644 1000:1000 ./biggytux.jpg
644 1000:1000 ./BIG.jpg
```

## آشنایی با روشهای تبدیل دی‌وی‌دی به قالب‌های کم‌حجم به صورت حرفه‌ای *مرتضی فخرائی*


### DVD Ripping

Transcoding or converting DVDs to video files without losing much of its quality.  


### Tools

- transcode: http://transcoding.org/  
- DVDRip:  http://www2.exit1.org/dvdrip/  
- k9copy: http://k9copy.sourceforge.net/  
- h264enc: http://h264enc.sourceforge.net/  
- ...: https://duckduckgo.com/?q=dvd+ripping+linux  

### h264enc

A well written interactive shell script that uses mplayer's mencoder program and  
x264 codec to do the job. It can also create matroska files.   

After install/download run:  


	$ h264enc -sc  

to check if the dependencies you need are all there.
Put DVD in the drive and run:  

	$ h264enc -scan  

and see what you got in that DVD. You can also try:  

	$ mplayer -dvd-device $your_dvd_device_here dvd://$track_number  

to find the track that should be used.  

Now, DVD can be converted directly using h264enc or by first dumping it to a raw  
mpeg video file and converting that file with h264enc. In dumping method you first  
need to run:  

	$ mplayer dvd://$track_number -dumpstream -dumpfile $movie_name_dumpfile.vob  
h264enc needs at least two options to run. First the passmode and then the preset.  
For more information do RTFM! (https://duckduckgo.com/?q=!wiki+RTFM). For example:  

	$ h264enc -2p -p hq  

will excute the program in 2-pass mode with High Quality preset and helps with a  
step by step guide through the rest of the ripping and transcoding process.
And that's it. h264enc is interactive, very intutitive itself and has a good manpage!  

Good luck.

[[ !author acathur acathur@lavabit.com ]]


این جلسه در ساعت ۱۹ خاتمه یافت

