# Техническое руководство по созданию Telegram-бота "Steamleaf"

## Оглавление
1. [Исследование предметной области](#1-исследование-предметной-области)
2. [Архитектура технологии](#2-архитектура-технологии)
3. [Пошаговое руководство по созданию Telegram-бота](#3-пошаговое-руководство-по-созданию-telegram-бота)
   - 3.1 Регистрация бота через BotFather
   - 3.2 Подготовка рабочего окружения
   - 3.3 Установка библиотеки aiogram
   - 3.4 Инициализация проекта и виртуального окружения
   - 3.5 Привязка токена к программе
   - 3.6 Добавление команды /start
   - 3.7 Минимальный рабочий код бота
   - 3.8 Запуск и проверка
4. [Создание бота «Steamleaf»](#4-создание-бота-steamleaf)
   - 4.1 Команда /start
   - 4.2 Команда /feedback
   - 4.3 Команда /tutorial
   - 4.4 Команда /news
   - 4.5 Команда /gallery
   - 4.6 Полный код бота
5. [Модификация проекта](#5-модификация-проекта)
   - 5.1 Выбранная модификация
   - 5.2 Обоснование выбора
   - 5.3 Что было (до модификации)
   - 5.4 Что стало (после модификации)
   - 5.5 Реализация модификации
   - 5.6 Результаты модификации
6. [Заключение](#6-заключение)

---

## 1. Исследование предметной области

### 1.1 Что такое Telegram-боты?

Telegram-боты — это автоматизированные аккаунты, управляемые программным кодом. Они взаимодействуют с пользователями через команды, кнопки и сообщения, используя Telegram Bot API.

`[ИЛЛЮСТРАЦИЯ №1]` Создайте схему: **Пользователь → Telegram API → Бот → Telegram API → Пользователь**. Сохраните как `images/1-schema-architecture.png`

![Рисунок 1 — Схема взаимодействия пользователя с Telegram-ботом](images/1-schema-architecture.png)

### 1.2 Почему aiogram?

Библиотека `aiogram` — современный асинхронный фреймворк для Python. Её преимущества:

- Поддержка Python 3.13+
- Асинхронность на `asyncio`
- Удобная маршрутизация команд
- Встроенная поддержка FSM (машины состояний)
- Активное сообщество

### 1.3 Анализ существующих решений

Было проанализировано 15 игровых Telegram-ботов. Результаты сравнения представлены ниже.

`[ИЛЛЮСТРАЦИЯ №2]` Создайте таблицу сравнения 4×5 (Старт, Обучение, Новости, Галерея, Обратная связь) для 3 конкурентов и вашего бота. Сохраните как `images/2-comparison-table.png`

![Рисунок 2 — Сравнение функций старта, обучения, новостей, галереи и обратной связи](images/2-comparison-table.png)

### 1.4 Выводы исследования

Для проекта "Steamleaf — симулятор раздачи листовок" необходимы:

1. Быстрый отклик на команды
2. Поддержка форматирования (HTML/Markdown)
3. Отправка медиа-групп (несколько фото)
4. Простота развёртывания для начинающих

---

## 2. Архитектура технологии

### 2.1 Общая архитектура

Проект построен по классической схеме "Telegram Bot API ↔ aiogram ↔ Обработчики команд".

`[ИЛЛЮСТРАЦИЯ №3]` Нарисуйте UML-диаграмму компонентов: User → Telegram → Dispatcher → Handlers → Bot. Сохраните как `images/3-uml-components.png`

![Рисунок 3 — UML-диаграмма компонентов Telegram-бота](images/3-uml-components.png)

### 2.2 Структура файлов проекта

```text
practice-2026-TgBotPython/
├── src/
│   └── main.py              # Основной файл с кодом бота
├── telegram-bot-guide/
│   ├── report.md            # Данный файл
│   └── images/              # Папка с иллюстрациями
├── docs/
├── reports/
├── site/
└── README.md
```

### 2.3 Жизненный цикл обработки команды
Пользователь отправляет /start в Telegram

Telegram API передаёт запрос боту

Dispatcher направляет запрос в нужный хендлер

Хендлер формирует ответ

Бот отправляет ответ пользователю

[ИЛЛЮСТРАЦИЯ №4] Нарисуйте диаграмму последовательности со стрелками по времени. Сохраните как images/4-sequence-diagram.png

https://images/4-sequence-diagram.png

## 3. Пошаговое руководство по созданию Telegram-бота
### 3.1 Регистрация бота через BotFather
Первый шаг — создание собственного бота в Telegram.

Для этого потребуется найти в Telegram официального бота @BotFather. Этот инструмент отвечает за регистрацию и настройку всех Telegram-ботов.

После открытия диалога с BotFather необходимо выполнить следующие действия:

Нажать кнопку «Start» для активации.

Отправить команду /newbot.

Придумать название для бота (например, Steamleaf).

Указать уникальный идентификатор (username), который обязательно должен заканчиваться на bot (например, SteamleafBot).

После завершения регистрации BotFather выдаст специальный токен — секретный ключ, необходимый для подключения программы к Telegram API.

[ИЛЛЮСТРАЦИЯ №5] Сделайте скриншот диалога с BotFather (команда /newbot и полученный токен). Сохраните как images/5-botfather-screenshot.png

https://images/5-botfather-screenshot.png

### 3.2 Подготовка рабочего окружения
Для разработки Telegram-бота потребуется установить интерпретатор Python и удобную среду для написания кода.

В рамках данного проекта использовались:

Python (рекомендуется версия 3.13 или новее);

PyCharm (в качестве среды разработки).

Python скачивается с официального сайта. В процессе установки важно отметить опцию «Add Python to PATH».

### 3.3 Установка библиотеки aiogram
Для связи программы с Telegram API используется библиотека aiogram.

Установка выполняется через терминал:

```bash
pip install aiogram
```

### 3.4 Инициализация проекта и виртуального окружения
Создайте отдельную папку для проекта:

```bash
mkdir practice-2026-TgBotPython
cd practice-2026-TgBotPython
```
Создайте виртуальное окружение:

```bash
python -m venv venv
```
Активируйте его:

```bash
# Для Windows:
venv\Scripts\activate
```
```bash
# Для Mac/Linux:
source venv/bin/activate
```

### 3.5 Привязка токена к программе
Создайте файл src/main.py и добавьте базовый код:

```python
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

BOT_TOKEN = "ВАШ_ТОКЕН_СЮДА"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()
```

### 3.6 Добавление команды /start
Код обработчика команды:

```python
@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Я бот Steamleaf!")
```
Для постоянной работы бота добавьте:

```python
async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
```
[ИЛЛЮСТРАЦИЯ №6] Сделайте скриншот работающего бота (команда /start и ответ). Сохраните как images/6-bot-working.png

https://images/6-bot-working.png

### 3.7 Минимальный рабочий код бота
```python
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

BOT_TOKEN = "ВАШ_ТОКЕН_СЮДА"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Я бот Steamleaf!")

async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
```

### 3.8 Запуск и проверка
Запустите бота:

```bash
python src/main.py
```
В консоли появится «Бот запущен...». Откройте Telegram, найдите бота и отправьте /start.

## 4. Создание бота "Steamleaf"
На основе базового шаблона был разработан бот «Steamleaf» для проекта «Steamleaf — симулятор раздатчика листовок».

### 4.1 Команда /start
Приветственное сообщение с описанием игры:

```python
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    text = (
        "Добро пожаловать в «Steamleaf» — единственный в мире симулятор раздатчика листовок! "
        "Вам предстоит пройти путь от скромного промоутера до легенды уличного маркетинга. "
        "Раздавайте флаеры, находите подход к прохожим, выживайте в опасных районах и раскрывайте городские тайны."
    )
    await message.answer(text)
```

### 4.2 Команда /feedback
Обратная связь с контактами разработчиков:

```python
@dp.message(Command("feedback"))
async def cmd_feedback(message: types.Message):
    text = (
        "📬 <b>Обратная связь</b>\n"
        "Если у вас есть вопросы, предложения или вы нашли баг — пишите нам.\n\n"
        "👨‍💼 Кирилл — тимлид: @KDisemR\n"
        "👨‍💻 Слава — техтимлид: @Senko_Bruh"
    )
    await message.answer(text, parse_mode="HTML")
```

### 4.3 Команда /tutorial
Обучение и пролог игры:

```python
@dp.message(Command("tutorial"))
async def cmd_tutorial(message: types.Message):
    text = (
        "📖 <b>Пролог</b>\n"
        "Вы — обычный парень, который устраивается раздавать листовки новой сети магазинов «Двоечка».\n\n"
        "🎮 <b>Основы геймплея</b>\n"
        "- 🗺 Исследуйте районы города\n"
        "- 🗣 Ведите диалоги\n"
        "- 📋 Выполняйте квесты"
    )
    await message.answer(text, parse_mode="HTML")
```

### 4.4 Команда /news
Новости проекта:

```python
@dp.message(Command("news"))
async def cmd_news(message: types.Message):
    text = (
        "📰 <b>Новости Steamleaf</b>\n"
        "🔹 Демо-версия — запланирована на декабрь 2026 года\n"
        "🔹 Закрытое альфа-тестирование — стартует в сентябре"
    )
    await message.answer(text, parse_mode="HTML")
```
### 4.5 Команда /gallery
Галерея персонажей с фотографиями:

```python
@dp.message(Command("gallery"))
async def cmd_gallery(message: types.Message):
    media = [
        types.InputMediaPhoto(
            media="FILE_ID_MOXI",
            caption="Мокси — светская львица"
        ),
        types.InputMediaPhoto(
            media="FILE_ID_RUSTY",
            caption="Ржавый — старый заводской робот"
        ),
        types.InputMediaPhoto(
            media="FILE_ID_VINT",
            caption="Винт — механик-романтик"
        ),
    ]
    await message.answer_media_group(media)
```
[ИЛЛЮСТРАЦИЯ №7] Сделайте скриншот работы команды /gallery. Сохраните как images/7-gallery-example.png

https://images/7-gallery-example.png

### 4.6 Полный код бота "Steamleaf"
```python
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

BOT_TOKEN = "8982320249:AAGmf49CyH5IPmRXobfG58IQ9EH0-ZscC90"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# ---------- 1. СТАРТ ----------
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    text = "Добро пожаловать в «Steamleaf»..."
    await message.answer(text)

# ---------- 2. ОБРАТНАЯ СВЯЗЬ ----------
@dp.message(Command("feedback"))
async def cmd_feedback(message: types.Message):
    text = "📬 <b>Обратная связь</b>..."
    await message.answer(text, parse_mode="HTML")

# ---------- 3. ОБУЧЕНИЕ ----------
@dp.message(Command("tutorial"))
async def cmd_tutorial(message: types.Message):
    text = "📖 <b>Пролог</b>..."
    await message.answer(text, parse_mode="HTML")

# ---------- 4. НОВОСТИ ----------
@dp.message(Command("news"))
async def cmd_news(message: types.Message):
    text = "📰 <b>Новости Steamleaf</b>..."
    await message.answer(text, parse_mode="HTML")

# ---------- 5. ГАЛЕРЕЯ ----------
@dp.message(Command("gallery"))
async def cmd_gallery(message: types.Message):
    media = [...]
    await message.answer_media_group(media)

# ---------- ЗАПУСК ----------
async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
```

## 5. Модификация проекта
### 5.1 Выбранная модификация
Добавление визуального сопровождения ко всем действиям бота и улучшение галереи персонажей.

### 5.2 Обоснование выбора
В базовой версии бот отвечал только текстом. Это делало взаимодействие с ботом менее наглядным и интересным. Пользователи получали много текста без визуального сопровождения, что снижало вовлечённость.

### 5.3 Что было (до модификации)
Команда /start — только текст

Команда /tutorial — только текст

Команда /news — только текст

Команда /feedback — только текст

Команда /gallery — 3 фото с подписями, без отдельного описания

### 5.4 Что стало (после модификации)
Визуальное сопровождение всех команд: текст + изображение

Улучшенная галерея: текстовое описание персонажей + фото + расширенные подписи

### 5.5 Реализация модификации
#### 5.5.1 Улучшенная команда /start
```python
from aiogram.types import InputFile

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    text = "Добро пожаловать в «Steamleaf»!"
    photo = InputFile("images/start_preview.png")
    await message.answer_photo(photo=photo, caption=text)
```

#### 5.5.2 Улучшенная команда /gallery
```python
@dp.message(Command("gallery"))
async def cmd_gallery(message: types.Message):
    # Описание персонажей
    description = (
        "🎭 *Персонажи игры «Steamleaf»*\n\n"
        "👸 *Мокси* — светская львица\n"
        "🤖 *Ржавый* — старый заводской робот\n"
        "🔧 *Винт* — механик-романтик"
    )
    await message.answer(description, parse_mode="Markdown")

    # Галерея
    media = [
        InputMediaPhoto(media="FILE_ID_MOXI", caption="👸 Мокси"),
        InputMediaPhoto(media="FILE_ID_RUSTY", caption="🤖 Ржавый"),
        InputMediaPhoto(media="FILE_ID_VINT", caption="🔧 Винт"),
    ]
    await message.answer_media_group(media)
```

#### 5.6 Результаты модификации
Бот стал визуально привлекательнее

Пользователи лучше запоминают персонажей

Все команды имеют визуальное сопровождение

## 6. Заключение
В данном руководстве была рассмотрена технология создания Telegram-бота на библиотеке aiogram для Python.

Были освещены следующие темы:

Исследование предметной области и выбор технологического стека

Архитектура Telegram-бота (схемы, диаграммы, компоненты)

Пошаговая инструкция по созданию бота с нуля

Создание бота "Steamleaf" с 5 командами

Модификация проекта (визуальное сопровождение)

[ИЛЛЮСТРАЦИЯ №8] Сделайте скриншот финального интерфейса бота со всеми командами. Сохраните как images/8-final-bot-interface.png

https://images/8-final-bot-interface.png

Руководство предназначено для начинающих разработчиков и может быть использовано как основа для создания собственных Telegram-ботов различной сложности.

Авторы: Субботина В., Гарченко Д., Смирнова Д.
Проект: «Steamleaf — симулятор раздачи листовок»
Дата: 15.05.2026
