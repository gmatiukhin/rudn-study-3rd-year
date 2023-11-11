---
## Front matter
title: "Отчет по лабораторной работе 8"
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
Изучение принципов маршрутизации в IPv4- и IPv6-сетях и принципов настройки сетевого оборудования

# Задача
1. Настройка динамической маршрутизации в сетях IPv4 и IPv62. Импортировать в GNS3 образ маршрутизатора FRR;
2. Построение туннеля IPv6–IPv4
3. Задание для самостоятельного выполнения

# Выполнение

## Настройка динамической маршрутизации в сетях IPv4 и IPv62. Импортировать в GNS3 образ маршрутизатора FRR;

Топология сети
[Topology](../images/1_topology.png)

Таблица адресов сетей:
Устройства|Сеть IPv4|Сеть IPv6
----------|---------|----------
PC1 – gw-01|10.0.10.0/24|2001:10::/64
PC2 – gw-03|10.0.11.0/24|2001:11::/64
gw-01 – gw-02|10.0.1.0/24|2001:1::/64
gw-02 – gw-03|10.0.2.0/24|2001:2::/64
gw-03 – gw-04|10.0.3.0/24|2001:3::/64
gw-04 – gw-01|10.0.4.0/24|2001:4::/64

Таблица адресации

Устройство|Интерфейс|Адрес IP/префикс|Шлюз по умолчанию|Следующее устройство
----------|---------|----------------|-----------------|----------
gw-01|eth0|10.0.10.1/24|n/a|PC1
gw-01|eth0|2001:10::1/64|n/a|PC1
gw-01|eth1|10.0.1.1/24|n/a|gw-02
gw-01|eth1|2001:1::1/64|n/a|gw-02
gw-01|eth2|10.0.4.2/24|n/a|gw-04
gw-01|eth2|2001:4::2/64|n/a|gw-04
gw-02|eth0|10.0.1.2/24|n/a|gw-01
gw-02|eth0|2001:1::2/64|n/a|gw-01
gw-02|eth1|10.0.2.1/24|n/a|gw-03
gw-02|eth1|2001:2::1/64|n/a|gw-03
gw-03|eth0|10.0.11.1/24|n/a|PC2
gw-03|eth0|2001:11::1/64|n/a|PC2
gw-03|eth1|10.0.2.2/24|n/a|gw-02
gw-03|eth1|2001:2::2/64|n/a|gw-02
gw-03|eth2|10.0.3.1/24|n/a|gw-04
gw-03|eth2|2001:3::1/64|n/a|gw-04
gw-04|eth0|10.0.3.2/24|n/a|gw-03
gw-04|eth0|2001:3::2/64|n/a|gw-03
gw-04|eth1|10.0.4.1/24|n/a|gw-01
gw-04|eth1|2001:4::1/64|n/a|gw-01
PC1|NIC|10.0.10.10/24|10.0.10.1|gw-01
PC1|NIC|2001:10::a/64|n/a|gw-01
PC2|NIC|10.0.11.10/24|10.0.11.1|gw-03
PC2|NIC|2001:11::a/64|n/a|gw-03

Насторим роутеры в согласии с данными таблицами:

Пример `msk-gmatiukhin-gw-01`:
[router example](../images/1_router_config_example.png)

Проверка `rip`а:
[rip](../images/1_rip.png)

Проверка `ospf`а:
[rip](../images/1_ospf.png)

## Построение туннеля IPv6–IPv4

Топология сети
[Topology](../images/2_topology.png)

Пример настоики интерфейсов и протоколов на одном из роутеров:
[Iface example](../images/2_iface_example.png)
[Protocol example](../images/2_protocol_example.png)

## Задание для самостоятельного выполнения

# Вывод
Я изучил принципы маршрутизации в IPv4- и IPv6-сетях и принципы настройки сетевого оборудования
