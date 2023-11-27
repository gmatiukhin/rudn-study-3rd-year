---
## Front matter
title: "Отчет по лабораторной работе 6"
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
Приобретение практических навыков по установке и конфигурированию системы управления базами данных на примере программного обеспечения MariaDB.

# Выполнение

## Установка

```bash
$ dnf -y install mariadb mariadb-server
$ systemctl enable --now mariadb
$ mysql_secure_installation
```

## Конфигурация UTF-8


```bash
$ cat > /etc/my.cnf.d/utf8.cnf
[client]
default-character-set = utf8
[mysqld]
character-set-server = utf8
$ systemctl restart mariadb
```

## Создание простой таблицы

```bash
$ mysql -u root -p
```

```sql
CREATE DATABASE addressbook CHARACTER SET utf8 COLLATE utf8_general_ci;
USE addressbook;
CREATE TABLE city(name VARCHAR(40), city VARCHAR(40));
INSERT INTO city(name,city) VALUES ('Иванов','Москва');
INSERT INTO city(name,city) VALUES ('Петров', 'Сочи'), ('Сидоров', 'Дубна');
CREATE USER gmatiukhin@'%' IDENTIFIED BY 'password';
GRANT SELECT,INSERT,UPDATE,DELETE ON addressbook.* TO gmatiukhin@'%';
FLUSH PRIVILEGES;
quit
```

## Резервное копирование

```bash
$ mkdir -p /var/backup
$ mysqldump -u root -p addressbook > /var/backup/addressbook.sql
$ mysql -u root -p addressbook < /var/backup/addressbook.sql
```

# Контрольные вопросы
1. Какая команда отвечает за настройки безопасности в MariaDB?
    - `mysql_secure_installation`
2. Как настроить MariaDB для доступа через сеть?
    1. Установить `mariadb` и `mariadb-server`.
    2. Запустить сервис `mariadb`.
3. Какая команда позволяет получить обзор доступных баз данных после входа в среду оболочки MariaDB?
    - `status`
4. Какая команда позволяет узнать, какие таблицы доступны в базе данных?
    - `SHOW DATABASES;`
5. Какая команда позволяет узнать, какие поля доступны в таблице?
    - `DESCRIBE <table>;`
6. Какая команда позволяет узнать, какие записи доступны в таблице?
    - `SELECT * FROM <table>;`
7. Как удалить запись из таблицы?
    - `DELETE FROM <table> WHERE <condition>;`
8. Где расположены файлы конфигурации MariaDB? Что можно настроить с их помощью?
    - /etc/my.cnf.d
9. Где располагаются файлы с базами данных MariaDB?
    - /var/lib/mysql
10. Как сделать резервную копию базы данных и затем её восстановить?
    - `mysqldump -u root -p <table> > /path/to/backup.sql`
    - `mysql -u root -p <table> < /path/to/backup.sql`

# Вывод
Я приобрел практические навыки по установке и конфигурированию системы управления базами данных на примере программного обеспечения MariaDB.
