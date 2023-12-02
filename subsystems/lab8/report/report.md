---
## Front matter
title: "Отчет по лабораторной работе 8"
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
Приобретение практических навыков по установке и конфигурированию SMTP-сервера.

# Выполнение

## Установка

```bash
$ dnf -y install postfix s-nail
$ firewall-cmd --add-service=smtp
$ firewall-cmd --add-service=smtp --permanent
$ systemctl enable --now postfix
```

## Базовая конфигурация

```bash
$ postconf -e 'myorigin = $mydomain'
$ postconf -e 'inet_protocols = ipv4'
$ postconf -e 'inet_interfaces = all'
$ postconf -e 'mynetworks = 127.0.0.0/8, 192.168.0.0/16'
$ postfix check
$ systemctl restart postfix
```

## Проверка отправки писма

```bash
echo . | mail -s test gmatiukhin@server.gmatiukhin.net
```

## Конфигурация для домена

```bash
$ echo "mail A 192.168.1.1" >> /var/named/master/fz/gmatiukhin.net
$ sed -i '/$ORIGIN/i MX 10 mail.gmatiukhin.net.' /var/named/master/fz/gmatiukhin.net
$ echo "1 PTR mail.gmatiukhin.net." >> /var/named/master/rz/192.168.1
$ sed -i '/$ORIGIN/i MX 10 mail.gmatiukhin.net.' /var/named/master/rz/192.168.1
$ postconf -e 'mydestination = $myhostname, localhost.$mydomain, localhost, $mydomain'
$ postfix check
$ systemctl restart postfix
$ systemctl restart named
```

## Проверка отправки письма

```bash
echo . | mail -s test gmatiukhin@gmatiukhin.net
```

# Контрольные вопросы
1. В каком каталоге и в каком файле следует смотреть конфигурацию Postfix?
    - /etc/postfix/main.cf
2. Каким образом можно проверить корректность синтаксиса в конфигурационном файле Postfix?
    - `postfix check`
3. В каких параметрах конфигурации Postfix требуется внести изменения в значениях для настройки возможности отправки писем не на локальный хост, а на доменные адреса?
    - `postconf -e 'mydestination = $myhostname, localhost.$mydomain, localhost, $mydomain'`
4. Приведите примеры работы с утилитой mail по отправке письма, просмотру имеющихся писем, удалению письма.
    - `echo <body> | mail -s <subject> <user>@<domain-name>` -- отправить письмо
    - `mail -N` -- просмотреть входящие
5. Приведите примеры работы с утилитой postqueue. Как посмотреть очередь сообщений? Как определить число сообщений в очереди? Как отправить все сообщения, находящиеся в очереди? Как удалить письмо из очереди?
    - `postqueue -p` -- просмореть очередь
    - `postqueue -f` -- отправить все

# Вывод
Я приобрел практические навыки по установке и конфигурированию SMTP-сервера.
