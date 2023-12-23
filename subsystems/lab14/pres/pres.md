---
lang: ru-RU
title: Лабораторная работа 14
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

# Вывод
Я приобрел навыки настройки доступа групп пользователей к общим ресурсам по протоколу SMB.
