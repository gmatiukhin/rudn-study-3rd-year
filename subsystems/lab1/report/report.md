---
## Front matter
title: "Отчет по лабораторной работе 1"
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
Целью данной работы является приобретение практических навыков установки Rocky Linux на виртуальную машину с помощью инструмента Vagrant.

# Выполнение

## Развёртывание лабораторного стенда на ОС Linux
## Внесение изменений в настройки внутреннего окружения виртуальной машины

# Контрольные вопросы
1. Для чего предназначен Vagrant?
    - Vagrant позволяет автоматизировать процесс установки на виртуальную машину дистрибутива операционной системы и настройки необходимого в программного обеспечения.
1. Что такое box-файл? В чём назначение Vagrantfile?
    - Box-файл -- сохранённый образ виртуальной машины с развёрнутой в ней операционной системой; по сути, box-файл используется как основа для клонирования виртуальных машин с теми или иными настройками.
    - Vagrantfile -- конфигурационный файл, в котором указаны настройки запуска виртуальной машины.
1. Приведите описание и примеры вызова основных команд Vagrant.

    |Команда|Описание|
    --------|---------
    autocomplete|управляет установкой автозаполнения на хосте
    box|управляет ящиками: установка, снятие и т.д.
    cloud|управляет всем, что связано с Vagrant Cloud
    destroy|останавливает и удаляет все следы бродячей машины
    global-status|выводит статус Vagrant Environments для этого пользователя
    halt|останавливает машину Vagrant
    help|показывает справку по подкоманде
    init|инициализирует новую среду Vagrant, создавая Vagrantfile
    login|
    package|упаковывает работающую среду Vagrant в коробку
    plugin|управляет плагинами: устанавливает, удаляет, обновляет и т. д.
    port|отображает информацию о сопоставлениях гостевых портов
    powershell|подключается к машине через удаленное управление PowerShell
    provision|обеспечивает машину Vagrant
    push|развертывает код в этой среде в настроенном месте назначения
    rdp|подключается к машине через RDP
    reload|перезапускает машину Vagrant, загружает новую конфигурацию Vagrantfile
    resume|возобновить работу приостановленной машины Vagrant
    serve|запустить Vagrant сервер
    snapshot|управляет снимками: сохранением, восстановлением и т. д.
    ssh|подключается к машине через SSH
    ssh-config|выводит действительную конфигурацию OpenSSH для подключения к машине
    status|выводит статус машины Vagrant
    suspend|останавливает машину
    up|запускает и подготавливает среду Vagrant
    upload|загрузить в машину через коммуникатор
    validate|проверяет Vagrantfile
    version|печатает текущую и последнюю версию Vagrant
    winrm|выполняет команды на машине через WinRM
    winrm-config|выводит конфигурацию WinRM для подключения к машине

1. Дайте построчные пояснения содержания файлов vagrant-rocky.pkr.hcl, ks.cfg, Vagrantfile, Makefile
    - см. видео выполнения работы


# Вывод
Я установил Rocky Linux на виртуальную машыну, используя Vagrant.
