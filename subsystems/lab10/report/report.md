---
## Front matter
title: "Отчет по лабораторной работе 10"
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
Приобретение практических навыков по конфигурированию SMTP-сервера в части настройки аутентификации.

# Выполнение

## LMTP

### Активация LMTP

```bash
$ sed -i 's/protocols = imap pop3/protocols = imap pop3 lmtp/g' /etc/dovecot/dovecot.conf
```

### Конфигурация сервиса для связи с Postfix

Содержимое /etc/dovecot/conf.d/10-master.conf должно включать:

```
service lmtp {
    unix_listener /var/spool/postfix/private/dovecot-lmtp {
        group = postfix
        user = postfix
        mode = 0600
    }
}
```

### Насройка Postfix

```bash
$ postconf -e 'mailbox_transport = lmtp:unix:private/dovecot-lmtp
```

### Конфигурация формата имени пользователя

```bash
$ sed -i 's/#auth_username_format = %Lu/auth_username_format = %Ln/g'
```

### Перезагрузка и пременение конфигураций

```bash
$ systemctl restart postfix
$ systemctl restart dovecot
```

## SMTP аутентификация

### Определение службы аутентификации

Содержимое /etc/dovecot/conf.d/10-master.conf должно включать:

```
service auth {
    unix_listener /var/spool/postfix/private/auth {
        group = postfix
        user = postfix
        mode = 0660
    }
    unix_listener auth-userdb {
        mode = 0600
        user = dovecot
    }
}
```

### Задаем тип конфигурации и путь к сокету, а так же настраиваем запрет на использование сервера как relay

```bash
$ postconf -e 'smtpd_sasl_type = dovecot'
$ postconf -e 'smtpd_sasl_path = private/auth
$ postconf -e 'smtpd_recipient_restrictions = reject_unknown_recipient_domain, permit_mynetworks, reject_non_fqdn_recipient, reject_unauth_destination, reject_unverified_recipient, permit
$ postconf -e 'mynetworks = 127.0.0.0/8'
```

## SMTP over TLS

### Используем сертификаты Dovecot

```bash
$ cp /etc/pki/dovecot/certs/dovecot.pem /etc/pki/tls/certs
$ cp /etc/pki/dovecot/private/dovecot.pem /etc/pki/tls/private
```

### Конфигурируем Postfix

```bash
$ postconf -e 'smtpd_tls_cert_file=/etc/pki/tls/certs/dovecot.pem'
$ postconf -e 'smtpd_tls_key_file=/etc/pki/tls/private/dovecot.pem'
$ postconf -e 'smtpd_tls_session_cache_database = btree:/var/lib/postfix/smtpd_scache'
$ postconf -e 'smtpd_tls_security_level = may'
$ postconf -e 'smtp_tls_security_level = may'
```

### Дальнейшая конфирурация SMTP-сервера

Содержимое /etc/postfix/master.cf должно включать:

```
submission inet n - n - - smtpd
    -o smtpd_tls_security_level=encrypt
    -o smtpd_sasl_auth_enable=yes
    -o smtpd_recipient_restrictions=reject_non_fqdn_recipient,reject_unknown_recipient_domain,permit_sasl_authenticated,reject
```

### Настройка firewalld

```bash
$ firewall-cmd --add-service=smtp-submission
$ firewall-cmd --add-service=smtp-submission --permanen
```

# Вывод
Я приобрел практические навыки по конфигурированию SMTP-сервера в части настройки аутентификации.
