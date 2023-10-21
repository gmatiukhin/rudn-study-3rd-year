---
## Front matter
title: "Домашняя работа № 2"
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
# 1

## 6. Имена служащих, имеющих, по крайней мере, одного иждивенца.
```sql
SELECT *
FROM СЛ JOIN ИЖД ON ИЖД.Код = СЛ.Код -- после JOIN остаются только строки для сотрудников которые имеют иждивенцев 
GROUP BY СЛ.Код -- выделить только одну строку на сотрудника
```

## 7. Имена служащих, работающих в отделе с названием «Информатика» над проектом с названием «Прогресс»
```sql
SELECT *
FROM СЛ -- для каждого сотрудника
    JOIN ОТ ON ОТ.No = СЛ.No -- находим его отдел
    JOIN Р_Н ON СЛ.Код = Р_Н.Код -- над какими проектами сотрудник работает
    JOIN ПР ON ПР.Np = Р_Н.Np -- и как эти проекты называются
WHERE
    ОТ.Назв = "Информатика"
    AND ПР.Назв = "Прогресс"
```

## 8. Имена служащих и имена его иждивенцев.
```sql
SELECT СЛ.Имя, GROUP_CONCAT(ИЖД.Имя) FROM СЛ JOIN ИЖД ON ИЖД.Код = СЛ.Код GROUP BY СЛ.Код ORDER BY COUNT(ИЖД.Имя) DESC
```

## 9. Названия проектов, за которые отвечает отдел, руководимый Ивановым
```sql
SELECT *
FROM ПР
    JOIN ОТ ON ПР.Noo = ОТ.No -- для проекта, отвечающий отдел
    JOIN СЛ ON СЛ.Код = ОТ.КодР -- для отдела, его начальник
WHERE
    СЛ.Фамилия = "Иванов"
```

## 10 Названия отделов, отвечающих за проекты с названием «Принцип ...»
```sql
SELECT *
FROM ОТ
    JOIN ПР ON ПР.Noo = ОТ.No -- отделы и их проекты
WHERE
    ПР.Назв LIKE "Принцип%"
```

## 11 Имена курируемых, работающих в том же отделе что и куратор.
```sql
WITH trainer AS (SELECT * FROM СЛ), -- берем две копии таблицы сотрудников
    trainee AS (SELECT * FROM СЛ) -- с двумя разными названиями
SELECT *
FROM trainee
    JOIN trainer ON trainer.Код = trainee.КодК -- один является куратором другого
WHERE trainer.No = trainee.No -- и их отдел совпадает

```

## 12 Названия проектов, выполняемых в месте, в котором размещается отдел, отвечающий за проект.
```sql
SELECT *
FROM ПР
    JOIN ОТ ON ОТ.No = ПР.Noo --  для проекта, отвечающий за него отдел
    JOIN О_М ON ОТ.No = О_М.No -- место отдела
WHERE
    О_М.Место = ПР.Место -- место проекта совпадает с местом отдела
```

## 13 Номера проектов, над которыми работает Иванов, но отдел, в котором он работает, не отвечает за проект
```sql
SELECT *
FROM ПР
    JOIN Р_Н ON Р_Н.Np = ПР.Np -- для проекта, кто работает над ним
    JOIN СЛ ON СЛ.Код = Р_Н.Код -- его имя и отдел
WHERE
    СЛ.No != ПР.Noo -- работает в отделе, который не отвечает за проект
    AND СЛ.Фамилия = "Иванов"
```

# 2
## 3 Выдать номера проектов, над которыми работают {только / все / только и все} сотрудники отдела, отвечающего за проект. 
```sql
-- Выдать номера проектов, над которыми работают {только} сотрудники отдела, отвечающего за проект.
WITH only_employees_of_dep AS (
    SELECT ПР.Np FROM ПР -- ищем такие проекты,
    WHERE NOT EXISTS ( -- что не бывает...
        SELECT * FROM Р_Н JOIN СЛ ON СЛ.Код = Р_Н.Код -- таких сотрудников...
        WHERE
            Р_Н.Np = ПР.Np -- которые работают над этим проектом,
            AND СЛ.No != ПР.Noo -- но они работают не в отделе этого проекта
        )
    ),
-- Выдать номера проектов, над которыми работают {все} сотрудники отдела, отвечающего за проект.
all_employees_of_dep AS (
    SELECT Np FROM ПР -- для каждого проекта,
    NATURAL JOIN (
        SELECT Р_Н.Np, СЛ.No, count(1) project_population  -- посчитаем количество людей,
        FROM Р_Н -- которые работают над этим проектом,
        NATURAL JOIN СЛ
        GROUP BY Np, No -- и распределим их по отделам, из которых они.
    )
    NATURAL JOIN (SELECT СЛ.No AS Noo, count(1) total_population FROM СЛ GROUP BY No) -- затем посчитаем количество людей в отделе, который ответственный за проект.
    WHERE No = Noo -- рассмотрим только тех людей, которые работают в ответственном отделе: если тех, кто работает над проектом, столько же, сколько всего людей в отделе, значит над проектом работает весь отдел
    AND project_population = total_population
    )

-- Выдать номера проектов, над которыми работают {только и все} сотрудники отдела, отвечающего за проект.
SELECT Np FROM only_employees_of_dep -- проекты, над которыми работают только свои
INTERSECT                           -- и среди них
SELECT Np FROM all_employees_of_dep -- проекты, над которыми работает весь отдел

```


# 3
## 5 Названия отделов, численность которых больше 10 человек, а средняя зарплата меньше 500 рублей.
```sql
WITH big_population AS (
    SELECT No, COUNT(1) AS population -- считаем население каждого отдела
    FROM СЛ
    GROUP BY No -- и фильтруем только те, где оно высокое
    HAVING population>10
    ),
low_salary AS (
    SELECT No, AVG(Зарплата) AS depsalary -- для каждого отдела ищем среднюю зарплату
    FROM СЛ
    GROUP BY No -- и фильтруем только те, где она низкая
    HAVING depsalary < 500
    )

SELECT No FROM (
    SELECT No FROM big_population
    INTERSECT
    SELECT No FROM low_salary
    )
```

## 6. Номера проектов, для которых из всех работающих над ними более половины сотрудники отвечающего отдела. 

```sql
WITH project_population AS (
    SELECT Np, count(1) AS total_population -- для каждого проекта ищем его общее население
    FROM Р_Н
    GROUP BY Р_Н.Np 
    ),
project_selfdep_population AS (
    SELECT ПР.Np, count(1) AS selfdep_population -- для каждого проекта ищем его население,
        FROM Р_Н
        JOIN СЛ ON СЛ.Код = Р_Н.Код -- но только для тех служащих,
        JOIN ПР ON ПР.Np = Р_Н.Np -- что, если посмотреть на проект над которым они работают,
    WHERE СЛ.No = ПР.Noo -- то за этот проект отвечает тот отдел, где работает этот служащий
    GROUP BY ПР.Np
    )

SELECT Np, (selfdep_population/total_population) proportion -- для каждого проекта посчитать отношение
FROM project_population -- между полным населением
NATURAL JOIN project_selfdep_population -- и населением из собственного отдела
WHERE proportion > 0.5 -- и выдавать только те, где эта пропорция больше 50%
```

## 7 Названия отделов, в которых более трех служащих имеют двух иждивенцев, родившихся в 2012 году. 
```sql
--save employees_with_matching_deps --no-execute
WITH employees_with_matching_deps AS (
    SELECT СЛ.Код, СЛ.No, count(ИЖД.Имя) AS dep_count -- считаем число иждивенцев
    FROM СЛ                                           -- для каждого служащего --
    LEFT OUTER JOIN ИЖД ON ИЖД.Код = СЛ.Код           -- даже для тех, у кого иждивенцев нет
    WHERE ИЖД.Дрожд LIKE "%2012%"                        -- и проверяем, что их дата рождения правильная 
    GROUP BY СЛ.Код  -- выводим только тех, у кого ровно два иждивенца с правильной датой рождения
    HAVING dep_count=2 --with employees_with_matching_deps --save deps_with_matching_employees
    SELECT No, count(1) AS emp_count FROM employees_with_matching_deps -- считаем, сколько сотрудников с правильными иждивенцами
    GROUP BY No -- есть в каждом отделе, а затем берем только те отделы, где таких сотрудников больше 3.
    HAVING emp_count>3
    )

SELECT *
FROM ОТ -- выписываем названия отделов,
NATURAL JOIN deps_with_matching_employees -- которые мы перечислили
```

## 8 Номера проектов, в работе над которыми наибольшее время затрачивает сотрудник отвечающего отдела.
```sql
SELECT ПР.Np, СЛ.Код,  --  ищем проекты, где сотрудник работал максимальное время
max(Время)
FROM Р_Н
    JOIN ПР ON ПР.Np = Р_Н.Np -- подключая данные о проекте
    JOIN СЛ ON Р_Н.Код = СЛ.Код -- и о сотруднике
GROUP BY ПР.Np -- ищем максимум для каждого проекта
HAVING СЛ.No = ПР.Noo -- и оставляем только те максимумы, где самое большое время от своего отдела
```

## 9 Номера проектов, в работе над которыми наибольшее время затрачива[ю]т сотрудник[и] отвечающего отдела. 
```sql
WITH project_deps_time_contribution AS (
    SELECT ПР.Np, ОТ.No, coalesce(sum(t1.Время), 0) AS dep_time -- собираем таблицу, где написано,
    FROM ПР -- для каждого проекта
        CROSS JOIN ОТ -- и каждого отдела
        LEFT OUTER JOIN ( -- (даже если никто из отдела не работал над этим проектом)
            SELECT Р_Н.*, СЛ.No FROM Р_Н -- выбираем сотрудников,
            JOIN СЛ ON СЛ.Код = Р_Н.Код 
        ) t1 ON ПР.Np = t1.Np AND t1.No = ОТ.No -- которые работали над этим проектом и из этого отдела
    GROUP BY ПР.Np,  -- суммируем время для каждого проекта и отдела, между всеми сотрудниками
    ОТ.No
    )

SELECT * FROM (
    SELECT pdtc.Np, No, max(pdtc.dep_time) AS max_time -- ищем тот отдел, который провел больше всего времени 
    FROM project_deps_time_contribution AS pdtc
    GROUP BY Np -- над одним проектом
)
NATURAL JOIN ПР -- затем проверяем, что за проект
WHERE ПР.Noo = No -- отвечает тот отдел, что провел макс. время
```

# 4
## 2 Номера проектов, имя руководителя отвечающего отдела и количество служащих, работающих над проектом при условии, что руководитель работает над не менее чем 2-мя другими проектами.
```sql
WITH project_population AS (
    SELECT Р_Н.Np, count(1) AS population -- ищем население проекта
    FROM Р_Н -- для каждого проекта
    GROUP BY Np
    ),
big_boss AS (
    SELECT Р_Н.Код, count(1) boss_proj_count -- ищем количество проектов,
    FROM Р_Н -- над которыми работает один сотрудник
    GROUP BY Р_Н.Код -- и оставляем только таких сотрудников, которые работают над больше чем 3.
    HAVING boss_proj_count > 3
    )

SELECT DISTINCT *
FROM ПР --для каждого проекта,
NATURAL JOIN project_population -- подключаем его население,
NATURAL JOIN big_boss -- оставляем только те, где начальник работает над 3 проектами
JOIN ОТ ON ПР.Noo = ОТ.No -- затем ищем отдел проекта
JOIN СЛ ON СЛ.Код = ОТ.КодР -- и начальника этого проекта;
WHERE EXISTS ( -- также должен
    SELECT * FROM Р_Н 
    WHERE Р_Н.Код = СЛ.Код -- начальник работать
        AND Р_Н.Np = ПР.Np -- над рассматриваемым проектом
)
```
