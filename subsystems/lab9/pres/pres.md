---
lang: ru-RU
title: Лабораторная работа 10
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
Приобретение практических навыков по установке и простейшему конфигурированию POP3/IMAP-сервера.

# Выполнение

## Установка

```bash
$ dnf -y install dovecot telnet
```

## Настройка dovecot

```bash
$ cat >> /etc/dovecot/dovecot.conf
protocols = imap pop3
$ cat >> /etc/dovecot/conf.d/10-auth.conf
auth_mechanisms = plain
```

Необходимо удостовериться, что `/etc/dovecot/conf.d/auth-system.conf.ext`содержит сдедующие настроки авторизации:

```
passdb {
    driver = pam
}
userdb = {
    driver = passwd
}
```

## Создание директории для входящих писем

```bash
$ cat >> /etc/dovecot/conf.d/10-mail.conf
mail_locaton = maildir:~/Maildir
$ postconf -e 'home_mailbox = Maildir/'
```

## Настройка firewalld

```bash
$ firewall-cmd --add-service=pop3 --permanent
$ firewall-cmd --add-service=pop3s --permanent
$ firewall-cmd --add-service=imap --permanent
$ firewall-cmd --add-service=imaps --permanent
$ firewall-cmd --reload
```

## Запуск сервисов

```bash
$ restorecon -vR /etc
$ systemctl restart postfix
$ systemctl enable --now dovecot
```

# Вывод
Я приобрел практические навыки по установке и простейшему конфигурированию POP3/IMAP-сервера.
