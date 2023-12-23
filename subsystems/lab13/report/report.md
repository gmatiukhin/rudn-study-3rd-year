---
## Front matter
title: "Отчет по лабораторной работе 13"
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
Приобретение навыков настройки сервера NFS для удалённого доступа к ресурсам.

# Выполнение

## Настройка сервера NFSv4

```bash
$ dnf -y install nfs-utils
```

### Создание основной директории для экспорта

```bash
$ mkdir -r /srv/nfs
$ cat >> /etc/exports
/srv/nfs *(ro)
$ semanage fcontext -a -t nfs_t "/srv/nfs(/.*)?"
$ restorecon -vR /srv/nfs
```

### Активация NFS

```bash
$ systemctl enable --now nfs-server
$ firewall-cmd --add-service=nfs --add-service=mountd --add-service=rpc-bind --permanent
$ firewall-cmd --reload
```

## Монтирование NFS на клиенте

```bash
$ mkdir -p /mnt/nfs
$ cat >> /etc/fstab
server.gmatiukhin.net:/srv/nfs /mnt/nfs nfs _netdev 0 0
$ mount -a
```

## Подключение каталогов к дереву NFS

```bash
$ mkdir -p /srv/nfs/www
$ cat >> /etc/exports
/srv/nfs/www 192.168.0.0/16(rw)
$ cat >> /etc/fstab
/var/www /srv/nfs/www none bind 0 0
$ exportfs -r
$ mount -a
```

## Подключение каталогов для работы пользователей

```bash
# as user
$ mkdir -p -m 700 ~/common
$ touch ~/common/gmatiukhin@server.txt
$ mkdir -p /srv/nfs/home/gmatiukhin
$ cat >> /etc/exports
/srv/nfs/home/gmatiukhin 192.168.0.0/16(rw)
$ cat >> /etc/fstab
/home/gmatiukhin/common /srv/nfs/home/gmatiukhin none bind 0 0
$ exportfs -r
$ mount -a
```

# Контрольные вопросы
1. Как называется файл конфигурации, содержащий общие ресурсы NFS?
    - `/etc/exports`
2. Какие порты должны быть открыты в брандмауэре, чтобы обеспечить полный доступ к серверу NFS?
    - `111/tcp`
    - `2049/tcp`
    - `4045/tcp`
3. Какую опцию следует использовать в /etc/fstab, чтобы убедиться, что общие ресурсы NFS могут быть установлены автоматически при перезагрузке
    - `_netdev`

# Вывод
Я приобрел навыки настройки сервера NFS для удалённого доступа к ресурсам.
