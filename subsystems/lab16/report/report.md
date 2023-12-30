---
## Front matter
title: "Отчет по лабораторной работе 16"
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

# Контрольные вопросы
1. Поясните принцип работы Fail2ban.
    - Данное программное средство отслеживает сетевую активность на портах узла путём сканирования текстовых лог-файлов. При выявлении программой неадекватной активности какого-то узла его IP-адрес помещается в чёрный список, а все пакеты с этого адреса блокируются. Блокировка настраивается путём внесения изменений в правила межсетевого экрана.
2. Настройки какого файла более приоритетны: jail.conf или jail.local?
    - `jail.local`
3. Как настроить оповещение администратора при срабатывании Fail2ban?
    ```bash
    [DEFAULT]
    destemail = yourname@example.com
    sender = yourname@examplecom
    sendername = Fail2ban
    mta = sendmail
    action = %(action_mwl)s
    ```
4. Поясните построчно настройки по умолчанию в конфигурационном файле /etc/fail2ban/jail.conf, относящиеся к веб-службе.
5. Поясните построчно настройки по умолчанию в конфигурационном файле /etc/fail2ban/jail.conf, относящиеся к почтовой службе.
6. Какие действия может выполнять Fail2ban при обнаружении атакующего IP-адреса? Где можно посмотреть описание действий для последующего использования в настройках Fail2ban?
7. Как получить список действующих правил Fail2ban?
8. Как получить статистику заблокированных Fail2ban адресов?
9. Как разблокировать IP-адрес?

# Вывод
Я приобрел навыки работы с программным средством Fail2ban для обеспечения базовой защиты от атак типа «brute force».
