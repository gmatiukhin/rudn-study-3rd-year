---
lang: ru-RU
title: Лабораторная работа 5
author: |
  Матюхин Григорий, НПИбд-01-21, 1032211403
institute: |
	\inst{1}RUDN University, Moscow, Russian Federation
date: 2023

toc: false
slide_level: 2
theme: metropolis
header-includes: 
 - \metroset{progressbar=frametitle,sectionpage=progressbar,numbering=fraction}
 - \usepackage{fvextra}
 - \DefineVerbatimEnvironment{Highlighting}{Verbatim}{breaklines,commandchars=\\\{\}}
 - '\makeatletter'
 - '\beamer@ignorenonframefalse'
 - '\makeatother'
aspectratio: 43
section-titles: true
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

### Конфигурация веб-сервера 1/2

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
```

### Конфигурация веб-сервера 2/2


```bash
$ cat >> /etc/httpd/conf.f/www.gmatiukhin.net
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

# Вывод
Я приобрел практические навыки по расширенному конфигурированию HTTP-сервера Apache в части безопасности и возможности использования PHP.
