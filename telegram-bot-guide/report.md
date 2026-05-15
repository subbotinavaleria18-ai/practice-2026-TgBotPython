# Техническое руководство по созданию Telegram-бота "Steamleaf"

## Оглавление
1. [Исследование предметной области](#1-исследование-предметной-области)
2. [Архитектура технологии](#2-архитектура-технологии)
3. [Пошаговое руководство для начинающих](#3-пошаговое-руководство-для-начинающих)
4. [Примеры кода](#4-примеры-кода)
5. [Модификация проекта](#5-модификация-проекта)
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

Для проекта "Steamleaf" необходимы:

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
steamleaf-bot/
├── src/
│   └── main.py              # Основной файл с кодом бота
├── telegram-bot-guide/
│   ├── report.md            # Данный файл
│   └── images/              # Папка с иллюстрациями
└── README.md'
```
### 2.3 Жизненный цикл обработки команды
Пользователь отправляет /start в Telegram

Telegram API передаёт запрос боту

Dispatcher направляет запрос в нужный хендлер

Хендлер формирует ответ

Бот отправляет ответ пользователю

[ИЛЛЮСТРАЦИЯ №4] Нарисуйте диаграмму последовательности со стрелками по времени. Сохраните как images/4-sequence-diagram.png

https://images/4-sequence-diagram.png

## 3. Пошаговое руководство для начинающих

### Шаг 1: Установка Python

Скачайте Python 3.13+ с [официального сайта](https://python.org). При установке обязательно отметьте "Add Python to PATH".

### Шаг 2: Создание бота в Telegram

1. Найдите в Telegram **@BotFather**
2. Отправьте команду `/newbot`
3. Придумайте имя бота (например, `SteamleafBot`)
4. Получите **токен** — секретную строку вида `123456:ABC-DEF`

`[ИЛЛЮСТРАЦИЯ №5]` Сделайте скриншот диалога с BotFather (команда /newbot и полученный токен). Сохраните как `images/5-botfather-screenshot.png`

![Рисунок 5 — Получение токена бота у BotFather](images/5-botfather-screenshot.png)

### Шаг 3: Настройка окружения

Создайте папку проекта и откройте её в терминале:

```bash
mkdir steamleaf-bot
cd steamleaf-bot
```

Создайте виртуальное окружение:

```python -m venv venv
```
Активируйте его:
```bash
# Windows:
venv\Scripts\activate
```
```bash
# Mac/Linux:
source venv/bin/activate
```
### Шаг 4: Установка зависимостей
Установите aiogram:

```bash
pip install aiogram
```

### Шаг 5: Написание кода

Создайте файл src/main.py:

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
### Шаг 6: Запуск бота
```python
src/main.py
```
Вы увидите «Бот запущен....» Откройте Telegram и напишите /start вашему боту.

[ИЛЛЮСТРАЦИЯ №6] Сделайте скриншот чата с ботом: команда /start и ответ бота. Сохраните как images/6-bot-working.png

https://images/6-bot-working.png

##4. Примеры кода
### 4.1 Команда с HTML-форматированием (обратная связь)
```python
@dp.message(Command("feedback"))
async def cmd_feedback(message: types.Message):
    text = (
        "📬 <b>Обратная связь</b>\n"
        "Если у вас есть вопросы, пишите нам.\n\n"
        "👨‍💼 Кирилл: @KDisemR\n"
        "👨‍💻 Слава: @Senko_Bruh"
    )
    await message.answer(text, parse_mode="HTML")
```
###4.2 Отправка нескольких фото (галерея)
```python
from aiogram.types import InputMediaPhoto

@dp.message(Command("gallery"))
async def cmd_gallery(message: types.Message):
    media = [
        InputMediaPhoto(media="FILE_ID_1", caption="Мокси — светская львица"),
        InputMediaPhoto(media="FILE_ID_2", caption="Ржавый — старый робот"),
        InputMediaPhoto(media="FILE_ID_3", caption="Винт — механик-романтик"),
    ]
    await message.answer_media_group(media)
[ИЛЛЮСТРАЦИЯ №7] Сделайте скриншот работы команды /gallery (3 фото с подписями). Сохраните как images/7-gallery-example.png

https://images/7-gallery-example.png
```
### 4.3 Получение file_id для фото
```python
@dp.message()
async def get_file_id(message: types.Message):
    if message.photo:
        file_id = message.photo[-1].file_id
        await message.answer(f"File ID: `{file_id}`", parse_mode="Markdown")
```

markdown
## 5. Модификация проекта (творческий пункт)

### 5.1 Выбранная модификация

**Добавление визуального сопровождения ко всем действиям бота и улучшение галереи персонажей.**

### 5.2 Обоснование выбора

В базовой версии бот отвечал только текстом. Это делало взаимодействие с ботом менее наглядным и интересным. Пользователи получали много текста без визуального сопровождения, что снижало вовлечённость.

Также в команде `/gallery` описание персонажей было только внутри подписей к фото. При быстром просмотре пользователь мог пропустить важную информацию о персонажах.

### 5.3 Что было (до модификации)

- Команда `/start` — только текст
- Команда `/tutorial` — только текст
- Команда `/news` — только текст
- Команда `/feedback` — только текст
- Команда `/gallery` — 3 фото с подписями, но без отдельного описания персонажей

### 5.4 Что стало (после модификации)

1. **Визуальное сопровождение всех команд:**
   - `/start` — приветственное изображение + текст
   - `/tutorial` — изображение с тематикой обучения + текст
   - `/news` — изображение-анонс + текст новостей
   - `/feedback` — изображение с контактами + текст

2. **Улучшенная галерея персонажей:**
   - Добавлено текстовое описание всех персонажей перед галереей
   - Каждое фото сопровождается расширенной подписью
   - Добавлена интерактивная клавиатура для выбора персонажа

### 5.5 Реализация

#### 5.5.1 Улучшенная команда /start

```python
from aiogram.types import InputFile

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    text = (
        "Добро пожаловать в «Steamleaf» — единственный в мире симулятор раздатчика листовок! "
        "Вам предстоит пройти путь от скромного промоутера до легенды уличного маркетинга."
    )
    # Отправка изображения с текстом
    photo = InputFile("images/start_preview.png")  # или file_id
    await message.answer_photo(photo=photo, caption=text)
5.5.2 Улучшенная команда /gallery (с описанием персонажей)
python
from aiogram.types import InputMediaPhoto

@dp.message(Command("gallery"))
async def cmd_gallery(message: types.Message):
    # Сначала отправляем общее описание персонажей
    description = (
        "🎭 *Персонажи игры «Steamleaf»*\n\n"
        "В мире Steamleaf вас встречают колоритные персонажи, "
        "каждый со своей историей и характером:\n\n"
        "👸 *Мокси* — светская львица, любит вечеринки и выгодные знакомства. "
        "Может помочь попасть в высшее общество, но потребует взамен услугу.\n\n"
        "🤖 *Ржавый* — старый заводской робот, местный талисман и философ. "
        "Любит давать мудрые (и не очень) советы. Знает всё о городе.\n\n"
        "🔧 *Винт* — механик-романтик, меняет масло и шутит про судьбу. "
        "Может улучшить вашу экипировку за небольшую плату."
    )
    await message.answer(description, parse_mode="Markdown")

    # Затем отправляем галерею с фото
    media = [
        InputMediaPhoto(
            media="FILE_ID_MOXI",
            caption="👸 *Мокси*\nСветская львица. Любит вечеринки и выгодные знакомства."
        ),
        InputMediaPhoto(
            media="FILE_ID_RUSTY",
            caption="🤖 *Ржавый*\nСтарый заводской робот. Местный талисман и философ."
        ),
        InputMediaPhoto(
            media="FILE_ID_VINT",
            caption="🔧 *Винт*\nМеханик-романтик. Меняет масло и шутит про судьбу."
        ),
    ]
    await message.answer_media_group(media)
```
5.5.3 Пример для команды /tutorial
python
@dp.message(Command("tutorial"))
async def cmd_tutorial(message: types.Message):
    text = (
        "📖 *Пролог*\n\n"
        "Вы — обычный парень, который устраивается раздавать листовки..."
    )
    photo = InputFile("images/tutorial_preview.png")  # или file_id
    await message.answer_photo(photo=photo, caption=text, parse_mode="Markdown")
5.5.4 Команда /feedback с изображением
python
@dp.message(Command("feedback"))
async def cmd_feedback(message: types.Message):
    text = (
        "📬 *Обратная связь*\n\n"
        "Если у вас есть вопросы, предложения или вы нашли баг — пишите нам.\n\n"
        "👨‍💼 Кирилл — тимлид: @KDisemR\n"
        "👨‍💻 Слава — техтимлид: @Senko_Bruh"
    )
    photo = InputFile("images/feedback.png")  # или file_id
    await message.answer_photo(photo=photo, caption=text, parse_mode="Markdown")
5.6 Результаты модификации
✅ Бот стал визуально привлекательнее

✅ Пользователи лучше запоминают персонажей (текст + фото)

✅ Информация о персонажах не теряется при быстром просмотре

✅ Все команды теперь имеют визуальное сопровождение

✅ Повышение вовлечённости пользователей

5.7 Создание изображений для бота
Для реализации модификации необходимо создать следующие изображения:

Изображение	Описание	Куда сохранить
start_preview.png	Приветственная картинка для команды /start	src/images/
tutorial_preview.png	Иллюстрация к обучению /tutorial	src/images/
news_preview.png	Изображение к новостям /news	src/images/
feedback.png	Изображение с контактами для /feedback	src/images/
moxi.png	Портрет персонажа Мокси	src/images/
rusty.png	Портрет персонажа Ржавый	src/images/
vint.png	Портрет персонажа Винт	src/images/
