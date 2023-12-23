---
## Front matter
title: "Отчет по лабораторной работе 14"
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
Приобретение навыков настройки доступа групп пользователей к общим ресурсам по протоколу SMB.

# Выполнение

## Настройка сервера Samba

```bash
$ dnf -y install samba samba-client cifs-utils
```

### Настойка групп и каталогов

```bash
$ groupad -g 1010 sambagroup
$ usermod -aG sambagroup gmatiukhin
$ mkdir -p /srv/sambashare
$ chgrp sambagroup /srv/sambashare
$ chmod g=rwx /srv/sambashare
$ semanage fcontext -a -t samba_share_t "/srv/sambashare(/.*)?"
$ restorecon -vR /srv/sambashare
$ setsebool samba_export_all_rw 1
$ setsebool samba_export_all_rw 1 -P
```

### Конфигурация

```
# /etc/samba/smb.conf
[global]
workgroup = gmatiukhin-net
...
[sambashare]
comment = My Samba Share
path = /srv/sambashare
write list = @sambagroup
```

### Запуск

```bash
$ systemctl enable --now smb
$ firewall-cmd --add-setvice=samba --permanent
$ firewall-cmd --reload
$ smbpasswd -L -a gmatiukhin
```

# Контрольные вопросы
1. Какова минимальная конфигурация для smb.conf для создания общего ресурса, который предоставляет доступ к каталогу /data?
```
# /etc/samba/smb.conf
[sambashare]
path = /data
write list = @sambagroup
```
2. Как настроить общий ресурс, который даёт доступ на запись всем пользователям, имеющим права на запись в файловой системе Linux?
3. Как ограничить доступ на запись к ресурсу только членам определённой группы?
```
chgrp <group> <path>
chmod g=rwx <path>
```
4. Какой переключатель SELinux нужно использовать, чтобы позволить пользователям получать доступ к домашним каталогам на сервере через SMB?
    - `samba_export_all_rw`
5. Как ограничить доступ к определённому ресурсу только узлам из сети 192.168.10.0/24?
6. Какую команду можно использовать, чтобы отобразить список всех пользователей Samba на сервере?
7. Что нужно сделать пользователю для доступа к ресурсу, который настроен как многопользовательский ресурс?
8. Как установить общий ресурс Samba в качестве многопользовательской учётной записи, где пользователь alice используется как минимальная учётная запись пользователя?
9. Как можно запретить пользователям просматривать учётные данные монтирования Samba в файле /etc/fstab?
10. Какая команда позволяет перечислить все экспортируемые ресурсы Samba, доступные на определённом сервере?

# Вывод
Я приобрел навыки настройки доступа групп пользователей к общим ресурсам по протоколу SMB.
