---
lang: ru-RU
title: Лабораторная работа 6
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

# Вывод
Я приобрел практические навыки по установке и конфигурированию системы управления базами данных на примере программного обеспечения MariaDB.
