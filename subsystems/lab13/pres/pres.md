---
lang: ru-RU
title: Лабораторная работа 13
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
Приобретение навыков настройки сервера NFS для удалённого доступа к ресурсам.

# Выполнение

# Настройка сервера NFSv4

```bash
$ dnf -y install nfs-utils
```

## Создание основной директории для экспорта

```bash
$ mkdir -r /srv/nfs
$ cat >> /etc/exports
/srv/nfs *(ro)
$ semanage fcontext -a -t nfs_t "/srv/nfs(/.*)?"
$ restorecon -vR /srv/nfs
```

## Активация NFS

```bash
$ systemctl enable --now nfs-server
$ firewall-cmd --add-service=nfs --add-service=mountd --add-service=rpc-bind --permanent
$ firewall-cmd --reload
```

# Монтирование NFS на клиенте

```bash
$ mkdir -p /mnt/nfs
$ cat >> /etc/fstab
server.gmatiukhin.net:/srv/nfs /mnt/nfs nfs _netdev 0 0
$ mount -a
```

# Подключение каталогов к дереву NFS

```bash
$ mkdir -p /srv/nfs/www
$ cat >> /etc/exports
/srv/nfs/www 192.168.0.0/16(rw)
$ cat >> /etc/fstab
/var/www /srv/nfs/www none bind 0 0
$ exportfs -r
$ mount -a
```

# Подключение каталогов для работы пользователей

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

# Вывод
Я приобрел навыки настройки сервера NFS для удалённого доступа к ресурсам.
