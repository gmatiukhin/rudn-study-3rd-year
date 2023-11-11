---
## Front matter
title: "Отчет по лабораторной работе 2"
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
---

# Цели работы
Приобретение практических навыков по установке и конфигурированию DNS-сервера,
усвоение принципов работы системы доменных имён.

# Выполнение

## Установить на виртуальной машине server DNS-сервер bind и bind-utils

### Установка
```bash
dnf install -y bind bind-utils
systemctl enable --now named
```

### Делаем сервер по умолчанию для хоста и внутренней сети
```bash
nmcli connection edit eth0
remove ipv4.dns
set ipv4.ignore-auto-dns yes
set ipv4.dns 127.0.0.1
save
quit
systemctl restart NetworkManager
firewall-cmd --add-service=dns
firewall-cmd --add-service=dns --permanent
```

### Настраиваем направление DNS запросов

В /etc/named.conf, меняем строку
```
listen-on port 53 { 127.0.0.1; };
```
на
```
listen-on port 53 { 127.0.0.1; any; };
```
и строку
```
allow-query { localhost; };
```
на
```
allow-query { localhost; 192.168.0.0/16; };
```

## Сконфигурировать на виртуальной машине server кэширующий DNS-сервер

В /etc/named.conf, добавляем
```
forwarders { <список DNS-серверов машины хоста> };
forward first;
dnssec-enable no;
dnssec-validation no;
```

## Сконфигурировать на виртуальной машине server первичный DNS-сервер


### Конфигурируем зоны

```bash
cat > /etc/named/gmatiukhin.net
zone "gmatiukhin.net" IN {
    type master;
    file "master/fz/user.net";
    allow-update { none; };
};
zone "1.1.168.192.in-addr.arpa" IN {
    type master;
    file "master/rz/192.168.1";
    allow-update { none; };
};
cat >> /etc/named.conf
include "/etc/named/gmatiukhin.net"
```

```bash
cat > /var/named/master/fz/gmatiukhin.net
$TTL 1D
@   IN SOA  @ server.gmatiukhin.net. (
                    2023111100  ; serial
                    1D  ; refresh
                    1H  ; retry
                    1W  ; expire
                    3H )    ; minimum
    NS  @
    A   192.168.1.1
$ORIGIN gmatiukhin.net.
server  A   192.168.1.1
ns  A   192.168.1.1
```

```bash
cat > /var/named/master/rz/192.168.1
$TTL 1D
@   IN SOA  @ server.gmatiukhin.net. (
                    2023111100  ; serial
                    1D  ; refresh
                    1H  ; retry
                    1W  ; expire
                    3H )    ; minimum
    NS  @
    A   192.168.1.1
    PTR server.gmatiukhin.net.
$ORIGIN 1.1.168.192.in-addr.arpa
1   PTR server.user.net
1   PTR ns.user.net
```

### Устанавливаем права доступа
```bash
chown -R named:named /etc/named
chown -R named:named /var/named
restorecon -vR /etc
restorecon -vR /var/named
setsebool named_write_master_zones 1
setsebool -P named_write_master_zones 1
```

### Перезапускаем DNS сервер

```bash
systemctl restart named
```

# Контрольные вопросы
1. Что такое DNS?
    - Система доменных имён (Domain Name System, DNS) — распределённая система (распре делённая база данных), ставящая в соответствие доменному имени хоста (компьютера или другого сетевого устройства) IP-адрес, и наоборот.
2. Каково назначение кэширующего DNS-сервера?
    - он получает рекурсивные запросы от клиентов и выполняет их с помощью нерекурсивных запросов к авторитативным серверам
3. Чем отличается прямая DNS-зона от обратной?
4. В каких каталогах и файлах располагаются настройки DNS-сервера? Кратко охарактеризуйте, за что они отвечают.
5. Что указывается в файле resolv.conf?
    - настроики для процедуры определения имен
6. Какие типы записи описания ресурсов есть в DNS и для чего они используются?
    - SOA-запись -- указывает на авторитативность для зоны;
    - NS-запись -- перечисляет DNS-серверы зоны;
    - А -- задаёт отображение имени узла в IP-адрес;
    - PTR -- задаёт отображение IP-адреса в имя узла;
    - CNAME -- задаёт каноническое имя (для псевдонимов);
    - MX -- задаёт имена почтовым серверам
7. Для чего используется домен in-addr.arpa?
    - для обратного просмотра DNS
8. Для чего нужен демон named?
    - это демон DNS сервера `bind9`
9. В чём заключаются основные функции slave-сервера и master-сервера?
    master-сервер хранит информацию локально, slave-сервер получает ее удаленно либо от master, дибо от другого slave
10. Какие параметры отвечают за время обновления зоны?
    - ttl
11. Как обеспечить защиту зоны от скачивания и просмотра?
12. Какая запись RR применяется при создании почтовых серверов?
    - MX
13. Как протестировать работу сервера доменных имён?
    - при помощи утилиты host
14. Как запустить, перезапустить или остановить какую-либо службу в системе?
    - `systemctl [restart|stop] <service-name>`
15. Как посмотреть отладочную информацию при запуске какого-либо сервиса или службы?
    - `systemctl status <service-name>`
16. Где храниться отладочная информация по работе системы и служб? Как её посмотреть?
    - `journalctl -x -f -u <service-name>`
17. Как посмотреть, какие файлы использует в своей работе тот или иной процесс? Приведите несколько примеров.
    - `lsof -p <PID>`
    - `strace -f -t -e trace=file -p <PID>`
18. Приведите несколько примеров по изменению сетевого соединения при помощи командного интерфейса nmcli.
19. Что такое SELinux?
    - реализация системы принудительного контроля доступа, которая может работать параллельно с классической избирательной системой контроля доступа. 
20. Что такое контекст (метка) SELinux?
    - это совокупность всех атрибутов, которые связаны с объектами и субъектами.
21. Как восстановить контекст SELinux после внесения изменений в конфигурационные файлы?
    - `restorecon <filename>`
22. Как создать разрешающие правила политики SELinux из файлов журналов, содержащих сообщения о запрете операций?
23. Что такое булевый переключатель в SELinux?
    - это значение, которое меняет поведение SELinux.
24. Как посмотреть список переключателей SELinux и их состояние?
    - `getsebool -a`
25. Как изменить значение переключателя SELinux
    - `setsebool <bool-name> [on|off]`
    - `togglesebool <bool-name>`


# Вывод
