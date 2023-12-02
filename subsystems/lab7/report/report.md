---
## Front matter
title: "Отчет по лабораторной работе 7"
subtitle: ""
author: "Матюхин Григорий, НПИбд-01-21, 10320202211403"

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

# Контрольные вопросы
1. Где хранятся пользовательские файлы firewalld?
    - `/etc/firewalld/services/`
2. Какую строку надо включить в пользовательский файл службы, чтобы указать порт TCP 2022?
    - `<port protocol="tcp" port="2022"/>`
3. Какая команда позволяет вам перечислить все службы, доступные в настоящее время на вашем сервере?
    - `firewall-cmd --get-services`
4. В чем разница между трансляцией сетевых адресов (NAT) и маскарадингом (masquerading)?
    - NAT -- механизм преобразования IP-адресов транзитных пакетов.
    - Маскарадинг -- тип трансляции сетевого адреса, при которой вместо адреса отправителя динамически подставляется адрес назначенного интерфейса.
5. Какая команда разрешает входящий трафик на порт 4404 и перенаправляет его в службу ssh по IP-адресу 10.0.0.10?
    - `firewall-cmd --add-forward-port=port=4404:toport=22:toaddr=10.0.0.10`
6. Какая команда используется для включения маcкарадинга IP-пакетов для всех пакетов, входящих в зону public?
    - `firewall-cmd --zone=public --add-masquerade`

# Вывод
Я приобрел практические навыки настройки межсетевого экрана в Linux в части переадресации портов и настройки Masquerading.
