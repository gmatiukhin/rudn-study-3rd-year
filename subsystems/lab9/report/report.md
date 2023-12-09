---
## Front matter
title: "Отчет по лабораторной работе 9"
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

# Контрольные вопросы
1. За что отвечает протокол SMTP?
    - SMTP - это сетевой протокол, предназначенный для передачи электронной почты в сетях TCP/IP.
2. За что отвечает протокол IMAP?
    - IMAP - протокол прикладного уровня для доступа к электронной почте.
3. За что отвечает протокол POP3?
    - POP3 - стандартный интернет-протокол прикладного уровня, используемый клиентами электронной почты для получения почты с удалённого сервера по TCP-соединению.
4. В чём назначение Dovecot?
    - это IMAP и POP3 сервер
5. В каких файлах обычно находятся настройки работы Dovecot? За что отвечает каждый из файлов?
    - /etc/dovecot/dovecot.conf - основные паременты конфигурации
    - /etc/dovecot/conf.d/10-auth.conf - настройка аутентификации
    - /etc/dovecot/conf.d/10-mail.conf - настройка почты
6. В чём назначение Postfix?
    - это SMTP сервер
7. Какие методы аутентификации пользователей можно использовать в Dovecot и в чём их отличие?
8. Приведите пример заголовка письма с пояснениями его полей.
    ```
    Date: Thu, 23 Nov 2023 10:55:48 -0800 (дата)
    From: GitHub <noreply@github.com> (отправитель)
    To: Grigorii Matiukhin <contact@gmatiukhin.site> (получатель)
    Message-ID: <655fa034c8514_73d80439734@lowworker-7cd95c995d-j4dlc.mail> (ID письма)
    Subject: [GitHub] A third-party OAuth application has been added to your account (тема)
    Mime-Version: 1.0 (версия Mime)
    Content-Type: text/plain; (тип подержимого письма)
    ```
9. Приведите примеры использования команд для работы с почтовыми протоколами через терминал (например через telnet).
    ```
    HELO <hostname>
    AUTH PLAIN <auth-string>
    MAIL TO: <email@address>
    RCPT TO: <email@address>
    DATA
    <some-text>
    .
    ```
10. Приведите примеры с пояснениями по работе с doveadm.

# Вывод
Я приобрел практические навыки по установке и простейшему конфигурированию POP3/IMAP-сервера.
