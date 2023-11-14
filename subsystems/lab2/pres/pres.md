---
lang: ru-RU
title: Лабораторная работа 2
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
Приобретение практических навыков по установке и конфигурированию DNS-сервера, усвоение принципов работы системы доменных имён.

# Выполнение

## Установить на виртуальной машине server DNS-сервер bind и bind-utils

### Установка
```bash
$ dnf install -y bind bind-utils
$ systemctl enable --now named
```

### Делаем сервер по умолчанию для хоста и внутренней сети
```bash
$ nmcli connection edit eth0
remove ipv4.dns
set ipv4.ignore-auto-dns yes
set ipv4.dns 127.0.0.1
save
quit
$ systemctl restart NetworkManager
$ firewall-cmd --add-service=dns
$ firewall-cmd --add-service=dns --permanent
```

### Настраиваем направление DNS запросов

В /etc/named.conf, меняем строку
```
listen-on port 53 { 127.0.0.1; };
```
на
```
listen-on port 53 { 127.0.0.1; any; };
```
и строку
```
allow-query { localhost; };
```
на
```
allow-query { localhost; 192.168.0.0/16; };
```

## Сконфигурировать на виртуальной машине server кэширующий DNS-сервер

В /etc/named.conf, добавляем
```
forwarders { <список DNS-серверов машины хоста> };
forward first;
dnssec-enable no;
dnssec-validation no;
```

## Сконфигурировать на виртуальной машине server первичный DNS-сервер


### Конфигурируем зоны

```bash
$ cat> /etc/named/gmatiukhin.net
zone "gmatiukhin.net" IN {
    type master;
    file "master/fz/user.net";
    allow-update { none; };
};
zone "1.1.168.192.in-addr.arpa" IN {
    type master;
    file "master/rz/192.168.1";
    allow-update { none; };
};
$ cat >> /tc/named.conf
include "/etc/named/gmatiukhin.net"
```

### Конфигурируем прямую зону

```bash
$ cat > /var/named/master/fz/gmatiukhin.net
$TTL 1D
@   IN SOA  @ server.gmatiukhin.net. (
                    2023111100  ; serial
                    1D  ; refresh
                    1H  ; retry
                    1W  ; expire
                    3H )    ; minimum
    NS  @
    A   192.168.1.1
$ORIGIN gmatiukhin.net.
server  A   192.168.1.1
ns  A   192.168.1.1
```

### Конфигурируем обратную зону

```bash
$ cat > /var/named/master/rz/192.168.1
$TTL 1D
@   IN SOA  @ server.gmatiukhin.net. (
                    2023111100  ; serial
                    1D  ; refresh
                    1H  ; retry
                    1W  ; expire
                    3H )    ; minimum
    NS  @
    A   192.168.1.1
    PTR server.gmatiukhin.net.
$ORIGIN 1.1.168.192.in-addr.arpa
1   PTR server.user.net
1   PTR ns.user.net
```

### Устанавливаем права доступа и перезапускаем DNS сервер
```bash
$ chown -R named:named /etc/named
$ chown -R named:named /var/named
$ restorecon -vR /etc
$ restorecon -vR /var/named
$ setsebool named_write_master_zones 1
$ setsebool -P named_write_master_zones 1

$ systemctl restart named
```

## Проверка
```bash
$ host -l gmatiukhin.net
gmatiukhin.net name server gmatiukhin.net.
gmatiukhin.net has address 192.168.1.1
ns.gmatiukhin.net has address 192.168.1.1
server.gmatiukhin.net has address 192.168.1.1
$ host -t PTR 192.168.1.1
1.1.168.192.in-addr.arpa domain name pointer server.gmatiukhin.net.
```

# Вывод
Я приобрел практические навыки по установке и конфигурированию DNS-сервера, усвоенил принципы работы системы доменных имён.
