---
lang: ru-RU
title: Лабораторная работа 11
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
Приобретение практических навыков по настройке удалённого доступа к серверу с помощью SSH.

# Выполнение

## Запрет доступа для root

```bash
$ cat >> /etc/ssh/sshd_config
PermitRootLogin no
$ systemctl restart sshd
```

```bash
$ ssh root@server.gmatiukhin.net
```

## Ограничение списка пользователей

```bash
$ cat >> /etc/ssh/sshd_config
AllowUsers gmatiukhin 
$ systemctl restart sshd
```

```bash
$ ssh vagrant@server.gmatiukhin.net
$ ssh gmatiukhin@server.gmatiukhin.net
```

## Настройка дополнительных портов

```bash
$ cat >> /etc/ssh/sshd_config
Port 22
Port 2022
$ systemctl restart sshd
$ semanage port -a -t ssh_port_t -p tcp 2022
$ firewall-cmd --add-port=2022/tcp
```

```bash
$ ssh gmatiukhin@server.gmatiukhin.net -p2022
```

## Удаленный доступ по ключу

```bash
$ cat >> /etc/ssh/sshd_config
PubkeyAuthentication yes
$ systemctl restart sshd
```

```bash
$ ssh-keygen
$ ssh-copy-id gmatiukhin@gmatiukhin.gmatiukhin.net
$ ssh gmatiukhin@server.gmatiukhin.net
```

## Перенаправление трафика

```bash
$ ssh -fNL 8080:localhost:80 gmatiukhin@server.gmatiukhin.net
$ curl localhost:8080
```

## Запуск консольных приложений

```bash
$ ssh gmatiukhin@server.gmatiukhin.net MAIL=~/Maildir mail
```

## Запуск графических приложений

```bash
$ cat >> /etc/ssh/sshd_config
X11Forwarding yes
$ systemctl restart sshd
```

```bash
$ ssh -YC gmatiukhin@server.gmatiukhin.net firefox
```

# Вывод
Я приобрел практические навыки по настройке удалённого доступа к серверу с помощью SSH.
