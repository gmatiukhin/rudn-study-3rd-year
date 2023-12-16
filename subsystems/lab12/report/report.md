---
## Front matter
title: "Отчет по лабораторной работе 12"
subtitle: ""
author: "Матюхин Григорий, НПИбд-01-21, 1032211403"

## Generic otions
lang: ru-RU
toc-title: "Содержание"


## Pdf output format
toc: true # Table of contents
toc-depth: 2
lof: true # List of figures
lot: true # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4
documentclass: scrreprt
## I18n polyglossia
polyglossia-lang:
  name: russian
  options:
	- spelling=modern
	- babelshorthands=true
polyglossia-otherlangs:
  name: english
## I18n babel
babel-lang: russian
babel-otherlangs: english
## Fonts
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase,Scale=0.9
## Biblatex
biblatex: true
biblio-style: "gost-numeric"
biblatexoptions:
  - parentracker=true
  - backend=biber
  - hyperref=auto
  - language=auto
  - autolang=other*
  - citestyle=gost-numeric
## Pandoc-crossref LaTeX customization
figureTitle: "Рис."
tableTitle: "Таблица"
listingTitle: "Листинг"
lofTitle: "Список иллюстраций"
lotTitle: "Список таблиц"
lolTitle: "Листинги"
## Misc options
indent: true
header-includes:
 - \usepackage{indentfirst}
 - \usepackage{float} # keep figures where there are in the text
 - \floatplacement{figure}{H} # keep figures where there are in the text
 - \usepackage{fvextra}
 - \DefineVerbatimEnvironment{Highlighting}{Verbatim}{breaklines,commandchars=\\\{\}}
---

# Цели работы
Получение навыков по управлению системным временем и настройке синхронизации времени.

# Выполнение

## Утилиты времени

### timedatectl

```bash
$ timedatectl
               Local time: Sat 2023-12-16 15:24:44 MSK
           Universal time: Sat 2023-12-16 12:24:44 UTC
                 RTC time: Sat 2023-12-16 12:24:44
                Time zone: Europe/Moscow (MSK, +0300)
System clock synchronized: yes
              NTP service: active
          RTC in local TZ: no
```

### date

```bash
$ date
Sat Dec 16 03:25:49 PM MSK 2023
$ date +"%H:%M:%S"
15:26:17
```

### hwclock

```bash
$ hwclock
2023-12-16 15:27:03.952197+03:00
$ hwclock -v
hwclock from util-linux 2.39.3
System Time: 1702729638.420808
Trying to open: /dev/rtc0
Using the rtc interface to the clock.
Assuming hardware clock is kept in UTC time.
Waiting for clock tick...
...got clock tick
Time read from Hardware Clock: 2023/12/16 12:27:19
Hw clock time : 2023/12/16 12:27:19 = 1702729639 seconds since 1969
Time since last adjustment is 1702729639 seconds
Calculated Hardware Clock drift is 0.000000 seconds
2023-12-16 15:27:18.467388+03:00
```

## NTP сервер

### Установка

```bash
$ dnf -y install chrony
```

```bash
$ chronyc sources
MS Name/IP address         Stratum Poll Reach LastRx Last sample               
===============================================================================
^- ntp.truenetwork.ru            2   6    37    47   -560us[-2219us] +/-   79ms
^- atomail.ru                    2   6    37    48   -102us[-1761us] +/-   30ms
^- time.cloudflare.com           3   6    37    47   -298us[-1957us] +/-   12ms
^* ntp.ix.ru                     1   6    37    46    -98us[-1757us] +/- 2335us
```

### Настройка

```bash
$ cat >> /etc/chrony.conf
allow 192.168.0.0/16
$ systemctl restart chronyd
$ firewall-cmd --add-service=ntp --permanent
$ firewall-cmd --reload
```

```bash
$ cat >> /etc/chrony.conf
server server.gmatiukhin.net
$ systemctl restart chronyd
```

### Проверка

```bash
$ chronyc sources
MS Name/IP address         Stratum Poll Reach LastRx Last sample               
===============================================================================
^- 213.33.141.134                3   6   377     6    -18us[  +12us] +/-   50ms
^- 195.218.227.230               3   6   377     4   -396us[ -396us] +/-   76ms
^* ntp1.doorhan.ru               2   6   377     6    +23us[  +54us] +/- 3850us
^- dynamicip-176-215-178-23>     2   6   377    72  +2710us[+2814us] +/-   54ms
^- server.gmatiukhin.net         2   6   377     7   +915us[ +945us] +/-   18ms
```

# Контрольные вопросы
1. Почему важна точная синхронизация времени для служб баз данных?
    - Необходимо знать порядок операций.
2. Почему служба проверки подлинности Kerberos сильно зависит от правильной синхронизации времени?
    - Kerberos использует метку времени как часть протокола.
3. Какая служба используется по умолчанию для синхронизации времени на RHEL 7?
    - `chronyd`
4. Какова страта по умолчанию для локальных часов?
    - 10
5. Какой порт брандмауэра должен быть открыт, если вы настраиваете свой сервер как одноранговый узел NTP?
    - 123
6. Какую строку вам нужно включить в конфигурационный файл chrony, если вы хотите быть сервером времени, даже если внешние серверы NTP недоступны?
    - `local stratum 10`
7. Какую страту имеет хост, если нет текущей синхронизации времени NTP?
    - 10
8. Какую команду вы бы использовали на сервере с chrony, чтобы узнать, с какими серверами он синхронизируется?
    - `chronyc sources`
9. Как вы можете получить подробную статистику текущих настроек времени для процесса chrony вашего сервера?
    - `chronyc ntpdata`

# Вывод
Я приобрел навыки по управлению системным временем и настройке синхронизации времени.
