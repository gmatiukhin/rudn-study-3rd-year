---
lang: ru-RU
title: Лабораторная работа 4
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
Установка и настройка GNS3 и сопутствующего программного обеспечения.

# Задача
1. Установить GNS3-all-in-one, GNS3 VM, проверить корректность запуска;
2. Импортировать в GNS3 образ маршрутизатора FRR;
3. Импортировать в GNS3 образ маршрутизатора VyOS.

## Установка GNS3 на Arch Linux

```bash
pacman -Syu yay
```
```bash
yay -S qemu docker vpcs dynamips libvirt ubridge inetutils
```
```bash
yay -S gns3-server gns3-gui
```
```bash
sudo usermod -aG ubridge,libvirt,kvm $USER
```

## Установка GNS3 VM для QEMU/KVM

```bash
wget https://github.com/GNS3/gns3-gui/releases/download/ v<VERSION>/GNS3.VM.KVM.<VERSION>.zip
unzip GNS3.VM.KVM.<VERSION>.zip -d gns
cd gns
./start-gns3mv.sh
```

## GNS3 VM
![GNS3 VM](../images/gns-vm.png)

## GNS3 Setup Wizard 1/2
![GNS3 Setup Wizard](../images/gns-setup-wizard.png)

## GNS3 Setup Wizard 2/2
![GNS3 Setup Wizard](../images/gns-remote-server.png)

## Импорт образа маршрутизатора 1/7
![FRR Router Installation](../images/frr-0.png)

## Импорт образа маршрутизатора 2/7
![FRR Router Installation](../images/frr-1.png)

## Импорт образа маршрутизатора 3/7
![FRR Router Installation](../images/frr-2.png)

## Импорт образа маршрутизатора 4/7
![FRR Router Installation](../images/frr-3.png)

## Импорт образа маршрутизатора 5/7
![FRR Router Installation](../images/frr-4.png)

## Импорт образа маршрутизатора 6/7
![FRR Router Installation](../images/frr-5.png)

## Импорт образа маршрутизатора 7/7
![FRR Router Installation](../images/frr-6.png)

## Конфигурация маршрутизатора
![FRR Router Configuration](../images/conf-0.png)
![FRR Router Configuration](../images/conf-1.png)

# Вывод
Я установил и настроил GNS3 и сопутствующее программное обеспечение.
