---
## Front matter
title: "Отчет по лабораторной работе 5"
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
Приобретение практических навыков по расширенному конфигурированию HTTP-сервера Apache в части безопасности и возможности использования PHP.

# Выполнение

## HTTPS в Apache

### Создание ключа и сертификата

```bash
$ mkdir -p /etc/pki/tls/private
$ ln -s /etc/pki/tls/private /etc/ssl/private
$ openssl req -x508 -nodes -newkey rsa:2048 -keyout www.gmatiukhin.net.key -out www.gmatiukhin.net.crt
$ mv www.gmatiukhin.net.key /etc/pki/tls/private
$ mv www.gmatiukhin.net.crt /etc/pki/tls/certs
```

### Конфигурация веб-сервера

```bash
$ cat > /etc/httpd/conf.f/www.gmatiukhin.net
<VirtualHost *:80>
    ServerAdmin webmaster@user.net
    DocumentRoot /var/www/html/www.user.net
    ServerName www.user.net
    ServerAlias www.user.net
    ErrorLog logs/www.user.net-error_log
    CustomLog logs/www.user.net-access_log common
    RewriteEngine on
    RewriteRule ^(.*)$ https://%{HTTP_HOST}$1 [R=301,L]
</VirtualHost>

<IfModule mod_ssl.c>
    <VirtualHost *:443>
        SSLEngine on
        ServerAdmin webmaster@user.net
        DocumentRoot /var/www/html/www.user.net
        ServerName www.user.net
        ServerAlias www.user.net
        ErrorLog logs/www.user.net-error_log
        CustomLog logs/www.user.net-access_log common
        SSLCertificateFile /etc/ssl/certs/www.user.net.crt
        SSLCertificateKeyFile /etc/ssl/private/www.user.net.key
    </VirtualHost>
</IfModule>
```


```bash
$ firewall-cmd --add-service=https --permanent
$ firewall-cmd --reload
$ systemctl restart httpd
```

### Проверка

```bash
$ curl www.gmatiukhin.net
!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>301 Moved Permanently</title>
</head><body>
<h1>Moved Permanently</h1>
<p>The document has moved <a href="https://www.gmatiukhin.net/">here</a>.</p>
</body></html>
$ curl https://www.gmatiukhin.net --insecure
Welcome to the www.gmatiukhin.net server.
```

## Работа с PHP

### Установка

```bash
$ dnf instal -y php
```

### Создание простого файла с информацией

```bash
$ cat > /var/www/html/www.gmatiukhin.net/index.php
<?php
phpinfo();
?>
$ rm /var/www/html/www.gmatiukhin.net/index.html
```

### Перезапуск сервера

```bash
$ chown -R apache:apache /var/www
$ restorecon -vR /etc/
$ restorecon -vR /var/www
$ systemctl restart httpd
```

# Контрольные вопросы
1. В чём отличие HTTP от HTTPS?
    - HTTPS использует шифрование
2. Каким образом обеспечивается безопасность контента веб-сервера при работе через HTTPS?
    - Улучшение безопасности при использовании HTTPS вместо HTTP достигается за счёт использования криптографических протоколов при организации HTTP-соединения и передачи по нему данных. Для шифрования может применяться протокол SSL (Secure Sockets Layer) или протокол TLC (Transport Layer Security). Оба протокола используют асимметричное шифрование для аутентификации, симметричное шифрование для конфиденциальности и коды аутентичности сообщений для сохранения целостности сообщений
3. Что такое сертификационный центр? Приведите пример
    - Сертификационный центр представляет собой компонент глобальной службы каталогов, отвечающий за управление криптографическими ключами пользователей. Его открытый ключ широко известен общественности и не вызывает сомнений в подлинности.

# Вывод
Я приобрел практические навыки по расширенному конфигурированию HTTP-сервера Apache в части безопасности и возможности использования PHP.
