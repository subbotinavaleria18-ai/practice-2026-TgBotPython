import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

BOT_TOKEN = "8982320249:AAGmf49CyH5IPmRXobfG58IQ9EH0-ZscC90"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# ---------- 1. СТАРТ ----------
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer_photo(
        photo="AgACAgIAAxkBAAN0aghnqNBJR2J4WUeNP07JMAY7uTAAApEgaxuv70hIKG35ND-uLNwBAAMCAAN3AAM7BA",
        caption=(
            "Добро пожаловать в «Steamleaf» — единственный в мире симулятор раздатчика листовок! "
            "Вам предстоит пройти путь от скромного промоутера до легенды уличного маркетинга. "
            "Раздавайте флаеры, находите подход к прохожим, выживайте в опасных районах и раскрывайте городские тайны. "
            "Помните: каждая листовка меняет чью-то жизнь, а может, и вашу. "
            "Следите за новостями, изучайте персонажей и проходите обучение прямо здесь. Готовы принять вызов «Двоечки»?"
        )
    )

# ---------- 2. ОБРАТНАЯ СВЯЗЬ ----------
@dp.message(Command("feedback"))
async def cmd_feedback(message: types.Message):
    text = (
        "📬 <b>Обратная связь</b>\n"
        "Если у вас есть вопросы, предложения или вы нашли баг — пишите нашим тимлидам.\n\n"
        "👨‍💼 <b>Кирилл</b> — тимлид проекта\n"
        "Связь: @KDisemR\n"
        "По сюжету, геймдизайну и идеям.\n\n"
        "👨‍💻 <b>Слава</b> — техтимлид\n"
        "Связь: @Senko_Bruh\n"
        "По багам, технической части и работе бота."
    )
    await message.answer(text, parse_mode="HTML")

    media = [
        types.InputMediaPhoto(
            media="AgACAgIAAxkBAAN4aghrO_GLHLt60rocotzt0qJeofgAAqUgaxuv70hIIlUn2KgV3x0BAAMCAAN5AAM7BA",
            caption="👨‍💼 Кирилл"
        ),
        types.InputMediaPhoto(
            media="AgACAgIAAxkBAAN6aghrPm7rS2xTTryVQBRWJIaxDLQAAqYgaxuv70hIBR2aRbNhxGABAAMCAAN5AAM7BA",
            caption="👨‍💻 Слава"
        ),
    ]
    await message.answer_media_group(media)

# ---------- 3. ОБУЧЕНИЕ ----------
@dp.message(Command("tutorial"))
async def cmd_tutorial(message: types.Message):
    text = (
        "📖 <b>Пролог</b>\n"
        "Вы — обычный парень, который устраивается раздавать листовки новой сети магазинов «Двоечка». "
        "План прост: отработать смену, получить деньги и забыть. Но город полон странных личностей: "
        "светских львиц, нервных менеджеров, уличных философов и просто безумцев. "
        "Каждая листовка превращается в маленькое приключение, а каждый диалог может открыть неожиданный путь.\n\n"
        "🎮 <b>Основы геймплея</b>\n"
        "- 🗺 Исследуйте районы города: каждый со своими NPC и опасностями.\n"
        "- 🗣 Ведите диалоги: убеждайте, шутите, льстите или дерзите — ваш стиль влияет на реакцию.\n"
        "- 📋 Выполняйте квесты: от простой передачи листовки до многоходовых заданий с переодеваниями.\n"
        "- ⏱ Следите за временем и ресурсами: смена не бесконечна, а приличный костюм стоит денег."
    )
    await message.answer(text, parse_mode="HTML")

    await message.answer_photo(
        photo="AgACAgIAAxkBAAN2aghq7ZS1ON34sbh5ai1ZBAg3OmsAAqMgaxuv70hIj7-fVdtWYPYBAAMCAAN4AAM7BA",
        caption="<b>Steamleaf — мир улиц и листовок</b>",
        parse_mode="HTML"
    )
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

# ---------- 5. ГАЛЕРЕЯ ПЕРСОНАЖЕЙ ----------
@dp.message(Command("gallery"))
async def cmd_gallery(message: types.Message):
    await message.answer(
        "🖼 <b>Персонажи Steamleaf</b>\n"
        "<i>Нажми на персонажа, чтобы узнать о нем подробнее</i> 👇",
        parse_mode="HTML"
    )

    media = [
        types.InputMediaPhoto(
            media="AgACAgIAAxkBAAMcagTbaO8Xhbd1G5IsLRU391RFt14AAk0Xaxv68ilIC0Ck31RW5mgBAAMCAAN5AAM7BA",
            caption="Мокси — светская львица, любит вечеринки и выгодные знакомства."
        ),
        types.InputMediaPhoto(
            media="AgACAgIAAxkBAAMeagTbbNqHYO48gPzEEANaUxP0EjIAAk4Xaxv68ilI92a1D8DeYuQBAAMCAAN5AAM7BA",
            caption="Ржавый — старый заводской робот, местный талисман и философ."
        ),
        types.InputMediaPhoto(
            media="AgACAgIAAxkBAAMgagTbd05JHCzDVhuC7pCMRxOTH7kAAk8Xaxv68ilIn_ppl3HHBHABAAMCAAN5AAM7BA",
            caption="Винт — механик-романтик, меняет масло и шутит про судьбу."
        ),
    ]
    await message.answer_media_group(media)

async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
