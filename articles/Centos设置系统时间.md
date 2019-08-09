查看系统时间：
> date

设置系统时间：
> date -s "2018-11-22 16:10:00"

查看硬件时间：
> hwclock --show
or
> hwclock -r

设置硬件时间：
> hwclock --set --date '2018-11-22 16:10:00' 

设置系统时间和硬件时间同步：
> hwclock  --hctosys

保存时钟：
> hwclock -w

查看时间：
> timedatectl status
      Local time: 四 2018-11-22 08:19:03 UTC
  Universal time: 四 2018-11-22 08:19:03 UTC
        RTC time: 四 2018-11-22 16:18:52
       Time zone: UTC (UTC, +0000)
     NTP enabled: yes
NTP synchronized: yes
 RTC in local TZ: no
      DST active: n/a

设置时间
> timedatectl set-time '2018-11-22 16:10:00'

查看系统时区：
> date +%z 
+0000
or
> date -R
Thu, 22 Nov 2018 08:24:10 +0000
or
> timedatectl status

设置时区：
> tzselect




CentOS下永久修改系统时间的方法
https://www.landui.com/help/show-5308.html

centos设置时区，永久修改时间
https://jingyan.baidu.com/article/3ea51489d16ac752e61bba88.html