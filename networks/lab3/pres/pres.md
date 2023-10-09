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
 - '\makeatletter'
 - '\beamer@ignorenonframefalse'
 - '\makeatother'
aspectratio: 43
section-titles: true
---


# Цели работы
Изучение посредством Wireshark кадров Ethernet, анализ PDU протоколов транспортного и прикладного уровней стека TCP/IP.

# Задача

## MAC-адресация

Найдем MAC-адрес одного из сетевых соединений.

```bash
$ ifconfig enp28s0 | rg "ether"
        ether f4:39:09:42:63:ab  txqueuelen 1000  (Ethernet)
```
Рассмотрим его структуру:

- f4:39:09 -- Organisationally Unique Identifier
    - f4
        - .... ..0. -- universally managed
        - .... ...0 -- unicast address

- 42:63:ab -- Network Interface Controller

## Анализ кадров канального уровня в Wireshark

### ICMP

![Echo](../images/icmp_echo.png)

### Рассмотрим пакеты ICMP Echo

![Ping](../images/ping.png)
![Pong](../images/pong.png)

### ARP

![ARP](../images/arp.png)

## Анализ протоколов транспортного уровня в Wireshark

### HTTP запрос к http://info.cern.ch/

![HTTP](../images/http.png)

### Запрос

![GET](../images/http_get.png)

### Ответ

![OK](../images/http_ok.png)

### DNS запрос о info.cern.ch

![DNS](../images/dns.png)

### Запрос

![Query](../images/dns_query.png)

### Ответ

![Response](../images/dns_resp.png)

## Анализ handshake протокола TCP в Wireshark

### Модель работы протокола:

![Model](../images/handshake_desc.png)

### Протокол в действии:

![Reality](../images/handshake.png)

# Вывод
Я изучил посредством Wireshark кадров Ethernet, проанализировал PDU протоколы транспортного и прикладного уровней стека TCP/IP.
