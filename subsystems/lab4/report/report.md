---
## Front matter
title: "Отчет по лабораторной работе 4"
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
---

# Цели работы
Приобретение практических навыков по установке и базовому конфигурированию HTTP-сервера Apache.

# Выполнение

## Установка

```bash
$ dnf -y groupinstall "Basic Web Server"
```

```bash
$ firewal-cmd --add-service=http
$ firewal-cmd --add-service=http --permanent
```

```bash
$ systemctl enable --now httpd
```

## Конфигурация DNS

```bash
$ cat >> /var/named/master/fz/gmatiukhin.net
www A 192.168.1.1
$ cat >> /var/named/master/rz/192.168.1
1 PRT www.gmatiukhin.net
```

## Настройка виртуального хостинга

```bash
cat > /etc/httpd/conf.d/server.gmatiukhin.net
<VirtualHost *:80>
    ServerAdmin webmaster@gmatiukhin.net
    DocumentRoot /var/www/html/server.gmatiukhin.net
    ServerName server.gmatiukhin.net
    ErrorLog logs/server.gmatiukhin.net-error_log
    CustomLog logs/server.gmatiukhin.net-access_log common
</VirtualHost>
```

```bash
cat > /etc/httpd/conf.d/www.gmatiukhin.net
<VirtualHost *:80>
    ServerAdmin webmaster@gmatiukhin.net
    DocumentRoot /var/www/html/www.gmatiukhin.net
    ServerName www.gmatiukhin.net
    ErrorLog logs/www.gmatiukhin.net-error_log
    CustomLog logs/www.gmatiukhin.net-access_log common
</VirtualHost>
```

```bash
cat > /var/www/html/server.gmatiukhin.net/index.html
Welcome to the server.gmatiukhin.net server.
cat > /var/www/html/www.gmatiukhin.net/index.html
Welcome to the www.gmatiukhin.net server.
```

### Проверка работы

```bash
curl server.gmatiukhin.net
Welcome to the server.gmatiukhin.net server.
curl www.gmatiukhin.net
Welcome to the www.gmatiukhin.net server.
```

# Контрольные вопросы
1. Через какой порт по умолчанию работает Apache?
    - 80
2. Под каким пользователем запускается Apache и к какой группе относится этот пользователь?
    - apache:apache
3. Где располагаются лог-файлы веб-сервера? Что можно по ним отслеживать?
    - /var/log/httpd/error\_log --- лог ошибок
    - /var/log/httpd/access\_log --- лог запросов
4. Где по умолчанию содержится контент веб-серверов?
    - /var/www/html
5. Каким образом реализуется виртуальный хостинг? Что он даёт?
    - Виртуальный хостинг — вид хостинга, при котором множество веб-сайтов расположено на одном веб-сервере. Мы создаем различные файлы конфигурации для различных виртуальных хостов.

# Вывод
Я приобрел практические навыки по установке и базовому конфигурированию HTTP-сервера Apache.
