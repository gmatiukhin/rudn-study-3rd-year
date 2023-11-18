---
lang: ru-RU
title: Лабораторная работа 3
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

# Вывод
Я приобрел практические навыки по установке и конфигурированию DHCP-сервера.
