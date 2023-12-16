---
## Front matter
title: "Отчет по лабораторной работе 11"
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

# Контрольные вопросы

1. Вы хотите запретить удалённый доступ по SSH на сервер пользователю root и разрешить доступ пользователю alice. Как это сделать?
    ```
    $ cat >> /etc/ssh/sshd_config
    PermitRootLogin no
    AllowUsers alice
    $ systemctl restart sshd
    ```
2. Как настроить удалённый доступ по SSH через несколько портов? Для чего это может потребоваться?
    ```bash
    $ cat >> /etc/ssh/sshd_config
    Port 22
    Port 2022
    $ systemctl restart sshd
    ```
    Это даёт гарантию возможности открыть сеансы SSH, даже если была сделана ошибка в конфигурации. Еще это помогает при обфускации порта ssh, хотя 'security by obscurity' и не особо надежная защита.
3. Какие параметры используются для создания туннеля SSH, когда команда ssh устанавливает фоновое соединение и не ожидает какой-либо конкретной команды?
    `ssh -fLN`
4. Как настроить локальную переадресацию с локального порта 5555 на порт 80 сервера server2.example.com?
    `ssh -fLN 5555:server2.example.com:80`
5. Как настроить SELinux, чтобы позволить SSH связываться с портом 2022?
    ```
    $ semanage port -a -t ssh_port_t -p tcp 2022
    ```
6. Как настроить межсетевой экран на сервере, чтобы разрешить входящие подключения по SSH через порт 2022?
    ```
    $ firewall-cmd --add-port=2022/tcp
    ```

# Вывод
Я приобрел практические навыки по настройке удалённого доступа к серверу с помощью SSH.
