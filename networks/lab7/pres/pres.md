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
 - '\makeatletter'
 - '\beamer@ignorenonframefalse'
 - '\makeatother'
aspectratio: 43
section-titles: true
---

# Цель
Получение навыков настройки службы DHCP на сетевом оборудовании для распределения адресов IPv4 и IPv6.

# Задача
- Настройка DHCP в случае IPv4
- Настройка DHCP в случае IPv6
    - без отслеживания состояния
    - с отслеживанием состояния

# Выполнение

## Топология сети
![Topology](../images/network.png)

## Настройка DHCP в случае IPv4

```
dhcp-server {
    shared-network-name gmatiukhin {
        domain-name gmatiukhin.net
        name-server 10.0.0.1
        subnet 10.0.0.0/24 {
            range hosts {
                start 10.0.0.2
                stop 10.0.0.253
            }
        }
    }
}
```
## PC
![PC](../images/dhcpv4-pc.png)

## Статистика
![Stats](../images/dhcpv4-stat.png)

## Настройка DHCP в случае IPv6 без отслеживания состояния

```
dhcpv6-server {
    shared-network-name gmatiukhin-stateless {
        common-options {
            domain-search gmatiukhin.net
            name-server 2000::1
        }
        subnet 2000::0/64 {
        }
    }
}
```

## Router advert
```
router-advert {
    interface eth1 {
        other-config-flag
        prefix 2000::/64 {
        }
    }
}
```

## IP, DNS
![IP](../images/dhcpv6-pc2-ip.png)
![DNS](../images/dhcpv6-pc2-dns.png)

## Настройка DHCP в случае IPv6 с отслеживанием состояния

```
dhcpv6-server {
    shared-network-name gmatiukhin-stateful {
        subnet 2001::0/64 {
            address-range {
                start 2001::100 {
                    stop 2001::199
                }
            }
            domain-search gmatiukhin.net
            name-server 2001::1
        }
    }
}
```

## Router advert
```
router-advert {
    interface eth2 {
        managed-flag
    }
}
```

## IP, DNS
![IP](../images/dhcpv6-pc3-ip.png)
![DNS](../images/dhcpv6-pc3-dns.png)

# Вывод
Я получил навыки настройки службы DHCP на сетевом оборудовании для распределения адресов IPv4 и IPv6.
