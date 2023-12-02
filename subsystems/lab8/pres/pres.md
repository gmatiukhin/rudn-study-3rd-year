---
lang: ru-RU
title: Лабораторная работа 8
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

# Вывод
Я приобрел практические навыки по установке и конфигурированию SMTP-сервера.
