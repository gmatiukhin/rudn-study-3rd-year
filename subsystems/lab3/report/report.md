---
## Front matter
title: "Отчет по лабораторной работе 3"
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
---

# Цели работы
Приобретение практических навыков по установке и конфигурированию DHCP-сервера.

# Выполнение
## Установка
```bash
dnf -y install dhcp-server
```

## Базовая конфигурация

```bash
$ cat /etc/dhcp/dhcpcd.conf
option domain-name "gmatiukhin.net";
option domain-name-servers ns.gmatiukhin.net;

default-lease-time 600;
max-lease-time 7200;
log-facility local7;

subnet 192.168.1.0 netmask 255.255.255.0 {
    range 192.168.1.30 192.168.1.199;
    option routers 192.168.1.1;
    option broadcast-address 192.168.1.255;
}
```

## Обновление DNS

```bash
$ cat >> /var/named/master/fz/gmatiukhin.net
dhcp A 192.168.1.1
$ cat >> /var/named/master/rz/192.168.1
1 PRT dhcp.gmatiukhin.net
```

## Настройка firewall

```bash
$ firewall-cmd --add-service=dhcp
$ firewall-cmd --add-service=dhcp --permanent
```

## Настройка обновления DNS-зоны

```bash
$ sed -i 's/none/127.0.0.1/g' /etc/named/gmatiukhin.net
```

```bash
$ cat >> /etc/dhcp/dhcpcd.conf
# Use this to enble / disable dynamic dns updates globally.
ddns-updates on;
ddns-update-style interim;
ddns-domainname "gmatiukhin.net.";
ddns-rev-domainname "in-addr.arpa.";
zone gmatiukhin.net. {
    primary 127.0.0.1;
}
zone 1.168.192.in-addr.arpa. {
    primary 127.0.0.1;
}
```

# Контрольные вопросы
1. В каких файлах хранятся настройки сетевых подключений?
    - /etc/dhcp/dhcpcd.conf
2. За что отвечает протокол DHCP?
    - Динамисескию раздачу IP адресов.
3. Поясните принцип работы протокола DHCP. Какими сообщениями обмениваются клиент и сервер, используя протокол DHCP?
    - Изначально клиент находится в состоянии инициализации (INIT) и не имеет своего IP-адреса. Поэтому он отправляет широковещательное (broadcast) сообщение DHCPDISCOVER на все устройства в локальной сети.
    - DHCP-сервер отвечает на поиск предложением, он сообщает IP, который может подойти клиенту. IP выделяются из области (SCOPE) доступных адресов, которая задается администратором.
    - Клиент получает DHCPOFFER, а затем отправляет на сервер сообщение DHCPREQUEST. Этим сообщением он принимает предлагаемый адрес и уведомляет DHCP-сервер об этом.
    - Сервер получает от клиента DHCPREQUEST и окончательно подтверждает передачу IP-адреса клиенту сообщением DHCPACK.
4. В каких файлах обычно находятся настройки DHCP-сервера? За что отвечает каждый из файлов?
    - /etc/dhcp/dhcpcd.conf --- конфигурация сервера
5. Что такое DDNS? Для чего применяется DDNS?
    - Динамический DNS — технология, позволяющая информации на DNS-сервере обновляться в реальном времени и по желанию в автоматическом режиме. Она применяется для назначения постоянного доменного имени устройству (компьютеру, сетевому накопителю) с динамическим IP-адресом.
6. Какую информацию можно получить, используя утилиту ifconfig? Приведите примеры с использованием различных опций.
    - состояние интерфесов
    - примеры
        - `ifconfig eth0` --- только eth0
        - `ifconfig -s` --- все интерфесы коротко
        - `ifconfig -a` --- все интерфесы даже выключенные 
        - `ifconfig eth0 up` --- включить интерфейс eth0
7. Какую информацию можно получить, используя утилиту ping? Приведите примеры с использованием различных опций.
    - Утилита ping предназначена для проверки соединений в сетях на основе TCP/IP. Мы можем проыерить есть ли соединение с кем-либо
    - примеры
        - `pint <ip>`
        - `pint -c 5 <ip>` --- остаовиться после пяти ответов
        - `pint -I <eth> <ip>` --- посылать запросы с интерфейса eth0

# Вывод
Я приобрел практические навыкт по установке и конфигурированию DHCP-сервера.
