---
lang: ru-RU
title: Лабораторная работа 15
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
Получение навыков по работе с журналами системных событий.

# Выполнение

## Настройка сервера сетевого журнала

```bash
$ cat > /etc/rsyslog.d/netlog-server.conf
$ModLoad imtcp
$InputTCPServerRun 514
$ systemctl restart rsyslog
```

```bash
$ firewall-cmd --add-port=514/tcp
$ firewall-cmd --add-port=514/tcp --permanent
```

## Настройка клиента сетевого журнала

```bash
$ cat > /etc/rsyslog.d/netlog-client.conf
*.* @@server.gmatiukhin.net:514
$ systemctl restart rsyslog
```

# Вывод
Я приобрел навыки по работе с журналами системных событий.
