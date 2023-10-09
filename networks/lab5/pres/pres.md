---
lang: ru-RU
title: Лабораторная работа 5
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
Построение простейших моделей сети на базе коммутатора и маршрутизаторов FRR и VyOS в GNS3, анализ трафика посредством Wireshark.

# Задача
1. Моделирование простейшей сети на базе коммутатора в GNS32.
1. Анализ трафика в GNS3 посредством Wireshark
1. Моделирование простейшей сети на базе маршрутизатора FRR в GNS3 
1. Моделирование простейшей сети на базе маршрутизатора VyOS в GNS3

# Моделирование простейшей сети на базе коммутатора в GNS32.

## Сеть
![Network](../images/1_network.png)

## Конфигурация VPCS
![PC1](../images/1_pc1.png)
![PC2](../images/1_pc2.png)

## Проверка соединения
![Ping](../images/1_ping.png)

# Анализ трафика в GNS3 посредством Wireshark
![Analysis](../images/2_analysis.png)

# Моделирование простейшей сети на базе маршрутизатора FRR в GNS3 

## Сеть
![Network](../images/3_network.png)

## Анализ трафика
![Analysis](../images/3_analysis.png)

# Моделирование простейшей сети на базе маршрутизатора VyOS в GNS3

## Сеть
![Network](../images/4_network.png)

## Анализ трафика
![Analysis](../images/4_analysis.png)

# Вывод
Я построенил простейшиу моделеи сети на базе коммутатора и маршрутизаторов FRR и VyOS в GNS3, проанализировал трафик посредством Wireshark.
