---
lang: ru-RU
title: Лабораторная работа 16
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
Получить навыки работы с программным средством Fail2ban для обеспечения базовой защиты от атак типа «brute force».

# Выполнение

## Установка

```bash
$ dnf -y install fail2ban
$ systemctl enable --now fail2ban
```

## Конфигурация
### Глобальные настройки

```bash
cat > /etc/fail2ban/jail.d/customization.local
[DEFAULT]
bantime = 3600
```

### Настройки SSH

```bash
cat >> /etc/fail2ban/jail.d/customization.local
[sshd]
enabled = true
port = ssh,2022
[sshd-ddos]
enabled = true
filter = sshd
[selinux-ssh]
enabled = true
```

### Настройки HTTP

```bash
cat >> /etc/fail2ban/jail.d/customization.local
[apache-auth]
enabled = true
[apache-badbots]
enabled = true
[apache-noscript]
enabled = true
[apache-overflows]
enabled = true
[apache-nohome]
enabled = true
[apache-botsearch]
enabled = true
[apache-fakegooglebot]
enabled = true
[apache-modsecurity]
enabled = true
[apache-shellshock]
enabled = true
```

### Настройки почты

```bash
cat >> /etc/fail2ban/jail.d/customization.local
[postfix]
enabled = true
[postfix-rbl]
enabled = true
[dovecot]
enabled = true
[postfix-sasl]
enabled = true
```

## Проверка работы
### Статус

```bash
$ fail2ban-client status
Status
|- Number of jail:	16
`- Jail list:	apache-auth, apache-badbots, apache-botsearch, apache-fakegooglebot, apache-modsecurity, apache-nohome, apache-noscript, apache-overflows, apache-shellshock, dovecot, postfix, postfix-rbl, postfix-sasl, selinux-ssh, sshd, sshd-ddos
```

### Статус одной службы

```bash
$ fail2ban-client status sshd
Status for the jail: sshd
|- Filter
|  |- Currently failed:	0
|  |- Total failed:	0
|  `- Journal matches:	_SYSTEMD_UNIT=sshd.service + _COMM=sshd
`- Actions
   |- Currently banned:	0
   |- Total banned:	0
   `- Banned IP list:
```

# Вывод
Я приобрел навыки работы с программным средством Fail2ban для обеспечения базовой защиты от атак типа «brute force».
