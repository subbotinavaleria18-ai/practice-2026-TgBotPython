import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

BOT_TOKEN = "8982320249:AAGmf49CyH5IPmRXobfG58IQ9EH0-ZscC90"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# ---------- 1. СТАРТ ----------
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    text = (
        "Добро пожаловать в «Steamleaf» — единственный в мире симулятор раздатчика листовок! "
        "Вам предстоит пройти путь от скромного промоутера до легенды уличного маркетинга. "
        "Раздавайте флаеры, находите подход к прохожим, выживайте в опасных районах и раскрывайте городские тайны. "
        "Помните: каждая листовка меняет чью-то жизнь, а может, и вашу. "
        "Следите за новостями, изучайте персонажей и проходите обучение прямо здесь. Примите вызов!"
    )
    await message.answer(text)

# ---------- 2. ОБРАТНАЯ СВЯЗЬ ----------
@dp.message(Command("feedback"))
async def cmd_feedback(message: types.Message):
    text = (
        "📬 <b>Обратная связь</b>\n"
        "Если у вас есть вопросы, предложения или вы нашли баг — пишите нам.\n\n"
        "👨‍💼 Кирилл — тимлид: @KDisemR\n"
        "👨‍💻 Слава — техтимлид: @Senko_Bruh\n\n"
        "Пожалуйста, описывайте проблему как можно подробнее. Спасибо!"
    )
    await message.answer(text, parse_mode="HTML")

# ---------- 3. ОБУЧЕНИЕ ----------
@dp.message(Command("tutorial"))
async def cmd_tutorial(message: types.Message):
    text = (
        "📖 <b>Пролог</b>\n"
        "Вы — обычный парень, который устраивается раздавать листовки новой сети магазинов «Двоечка». "
        "План прост: отработать смену, получить деньги и забыть. Но город полон странных личностей: "
        "светских львиц, нервных менеджеров, уличных философов и просто безумцев. "
        "Каждая листовка превращается в маленькое приключение, а каждый диалог может открыть "
        "неожиданный путь. Кем вы станете — вечным раздатчиком или тем, кто вырвется наверх?\n\n"
        "🎮 <b>Основы геймплея</b>\n"
        "- 🗺 Исследуйте районы города: каждый со своими NPC и опасностями.\n"
        "- 🗣 Ведите диалоги: убеждайте, шутите, льстите или дерзите — ваш стиль влияет на реакцию.\n"
        "- 📋 Выполняйте квесты: от простой передачи листовки до многоходовых заданий с переодеваниями.\n"
        "- ⏱ Следите за временем и ресурсами: смена не бесконечна, а приличный костюм стоит денег."
    )
    await message.answer(text, parse_mode="HTML")

# ---------- 4. НОВОСТИ ----------
@dp.message(Command("news"))
async def cmd_news(message: types.Message):
    text = (
        "📰 <b>Новости Steamleaf</b>\n"
        "🔹 Демо-версия — запланирована на декабрь 2026 года.\n"
        "🔹 Закрытое альфа-тестирование — стартует в сентябре, набор тестеров откроем в августе.\n"
        "🔹 Первый сюжетный квест с Мокси уже готов!\n\n"
        "Подписывайтесь на наш Telegram-канал: https://t.me/Steamleaf"
    )
    await message.answer(text, parse_mode="HTML", disable_web_page_preview=True)

# ---------- 5. ГАЛЕРЕЯ ----------
@dp.message(Command("gallery"))
async def cmd_gallery(message: types.Message):
    # Замени на свои file_id
    photo_moxy = "AgACAgIAAxkBAAMcagTbaO8Xhbd1G5IsLRU391RFt14AAk0Xaxv68ilIC0Ck31RW5mgBAAMCAAN5AAM7BA"
    photo_rusty = "AgACAgIAAxkBAAMeagTbbNqHYO48gPzEEANaUxP0EjIAAk4Xaxv68ilI92a1D8DeYuQBAAMCAAN5AAM7BA"
    photo_vint = "AgACAgIAAxkBAAMgagTbd05JHCzDVhuC7pCMRxOTH7kAAk8Xaxv68ilIn_ppl3HHBHABAAMCAAN5AAM7BA"

    media = [
        types.InputMediaPhoto(
            media=photo_moxy,
            caption="Мокси — светская львица, любит вечеринки и выгодные знакомства."
        ),
        types.InputMediaPhoto(
            media=photo_rusty,
            caption="Ржавый - старый заводской робот, местный талисман и философ."
        ),
        types.InputMediaPhoto(
            media=photo_vint,
            caption="Винт — механик-романтик, меняет масло и шутит про судьбу."
        ),
    ]
    await message.answer_media_group(media)

# ---------- ГЛАВНАЯ ФУНКЦИЯ ЗАПУСКА ----------
async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
