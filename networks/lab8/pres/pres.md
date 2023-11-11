---
lang: ru-RU
title: Лабораторная работа 8 
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
 - \makeatletter
 - \beamer@ignorenonframefalse
 - \makeatother
 - \usepackage{fvextra}
 - \DefineVerbatimEnvironment{Highlighting}{Verbatim}{breaklines,commandchars=\\\{\}}
aspectratio: 43
section-titles: true
---

# Цели работы
Изучение принципов маршрутизации в IPv4- и IPv6-сетях и принципов настройки сетевого оборудования

# Задача
1. Настройка динамической маршрутизации в сетях IPv4 и IPv6
2. Построение туннеля IPv6–IPv4
3. Задание для самостоятельного выполнения

# Выполнение

# Настройка динамической маршрутизации в сетях IPv4 и IPv6

Топология сети
![Topology](../images/1_topology.png)

## Таблица адресов сетей:
Устройства|Сеть IPv4|Сеть IPv6
----------|---------|----------
PC1 – gw-01|10.0.10.0/24|2001:10::/64
PC2 – gw-03|10.0.11.0/24|2001:11::/64
gw-01 – gw-02|10.0.1.0/24|2001:1::/64
gw-02 – gw-03|10.0.2.0/24|2001:2::/64
gw-03 – gw-04|10.0.3.0/24|2001:3::/64
gw-04 – gw-01|10.0.4.0/24|2001:4::/64

## Пример настройки роутера:
![router example](../images/1_router_config_example.png)

## Проверка `rip`:
![rip](../images/1_rip.png)

## Проверка `ospf`:
![ospf](../images/1_ospf.png)

# Построение туннеля IPv6–IPv4

## Топология сети
![Topology](../images/2_topology.png)

## Пример настоики интерфейсов и протоколов на одном из роутеров:

![Iface example](../images/2_iface_example.png)

## Пример настоики интерфейсов и протоколов на одном из роутеров:
![Protocol example](../images/2_protocol_example.png)

## Результат
![Trace](../images/2_trace.png)

# Вывод
Я изучил принципы маршрутизации в IPv4- и IPv6-сетях и принципы настройки сетевого оборудования

