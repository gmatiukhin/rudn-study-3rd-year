---
lang: ru-RU
title: Лабораторная работа 4
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

### server.gmatiukhin.net

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

### www.gmatiukhin.net

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

### Контент

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

# Вывод
Я приобрел практические навыки по установке и базовому конфигурированию HTTP-сервера Apache.
