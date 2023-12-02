---
lang: ru-RU
title: Лабораторная работа 7
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
Получить навыки настройки межсетевого экрана в Linux в части переадресации портов и настройки Masquerading.

# Выполнение

## Создание пльзовательской службы firewalld
```bash
$ cp /usr/lib/firewalld/services/ssh.xml /etc/firewalld/services/ssh-custom.xml
$ sed -i 's/SSH/SSH Custom/' /etc/firewalld/services/ssh-custom.xml
$ sed -i 's/22/2022/' /etc/firewalld/services/ssh-custom.xml
```

## Активация службы
```bash
$ firewall-cmd --list-services
cockpit dhcp dhcpv6-client dns http https ssh
$ firewall-cmd --reload
$ firewall-cmd --add-service=ssh-custom
$ firewall-cmd --list-services
cockpit dhcp dhcpv6-client dns http https ssh ssh-custom
$ firewall-cmd --add-forward-port=port=2022:proto=tcp:toport=22
```

## Маскарадинг
```bash
$ echo "net.ipv4.ip_forward = 1" > /etc/sysctl.d/90-forward.conf
$ sysctl -p /etc/sysctl.d/90-forward.conf
$ firewall-cmd --zone=public --add-masquerade --permanent
$ firewall-cmd --reload
```

# Вывод
Я приобрел практические навыки настройки межсетевого экрана в Linux в части переадресации портов и настройки Masquerading.
