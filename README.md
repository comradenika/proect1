# Hangman Game / Игра "Виселица"

Многопользовательская игра "Виселица" с графической визуализацией на Python.

## Как открыть проект в Visual Studio Code

### Способ 1: Через командную строку
```bash
code /путь/к/proect1
```

### Способ 2: Через меню VS Code
1. Откройте Visual Studio Code
2. Выберите `File` → `Open Folder` (или `Ctrl+K Ctrl+O`)
3. Выберите папку проекта `proect1`

### Способ 3: Из терминала в папке проекта
```bash
cd proect1
code .
```

## Требования / Requirements

- Python 3.x
- Модуль `turtle` (входит в стандартную библиотеку Python)
- Visual Studio Code (рекомендуется)

## Рекомендуемые расширения VS Code

При первом открытии проекта VS Code предложит установить рекомендуемые расширения:
- **Python** (ms-python.python) - Поддержка Python
- **Pylance** (ms-python.vscode-pylance) - Быстрая языковая поддержка

## Как запустить игру

### Через VS Code:
1. Откройте файл `proectpy1/proect.py`
2. Нажмите `F5` или выберите `Run` → `Start Debugging`
3. Или нажмите `Ctrl+F5` для запуска без отладки

### Через терминал:
```bash
cd proectpy1
python3 proect.py
```

## Структура проекта

```
proect1/
├── .vscode/              # Конфигурация VS Code
│   ├── launch.json       # Настройки запуска/отладки
│   ├── settings.json     # Настройки рабочей области
│   └── extensions.json   # Рекомендуемые расширения
├── proectpy1/
│   ├── proect.py         # Главный файл игры
│   ├── words.txt         # Словарь слов для игры
│   └── game_history.txt  # История игр
└── README.md             # Этот файл
```

## Возможности игры

- Многопользовательский режим (до 3 игроков одновременно)
- Визуализация с помощью Turtle Graphics
- Система подсчета очков
- История игр
- Поддержка грузинского и английского языков

## Отладка в VS Code

Проект настроен для отладки в VS Code:
- Точки остановки (breakpoints) работают
- Интегрированный терминал для ввода данных
- Пошаговое выполнение кода

## Troubleshooting

**Проблема**: Turtle окно не открывается
**Решение**: Убедитесь, что у вас установлен Python с поддержкой Tkinter

**Проблема**: VS Code не находит Python
**Решение**: Выберите интерпретатор Python через Command Palette (`Ctrl+Shift+P` → "Python: Select Interpreter")

---

## How to Open Project in Visual Studio Code

### Method 1: Via Command Line
```bash
code /path/to/proect1
```

### Method 2: Via VS Code Menu
1. Open Visual Studio Code
2. Select `File` → `Open Folder` (or `Ctrl+K Ctrl+O`)
3. Select the `proect1` project folder

### Method 3: From Terminal in Project Folder
```bash
cd proect1
code .
```

## Running the Game

### Via VS Code:
1. Open `proectpy1/proect.py`
2. Press `F5` or select `Run` → `Start Debugging`
3. Or press `Ctrl+F5` to run without debugging

### Via Terminal:
```bash
cd proectpy1
python3 proect.py
```

## Game Features

- Multi-player mode (up to 3 players simultaneously)
- Turtle Graphics visualization
- Score tracking system
- Game history
- Georgian and English language support

Enjoy the game! / Приятной игры!
