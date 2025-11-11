"""
User registration FSM router.
"""

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.services.user_service import UserService
from bot.utils.fsm_states import RegistrationStates
from bot.utils.keyboards import build_phone_request_keyboard, remove_keyboard

router = Router(name="user_registration_fsm_router")


@router.message(RegistrationStates.waiting_for_first_name, F.text)
async def process_first_name(message: Message, state: FSMContext) -> None:
    if not message.text:
        message.answer("Помилка пыд час обробки повідомлення")
        return
    first_name = message.text.strip()

    if not first_name or len(first_name) > 30 or len(first_name) < 2:
        await message.answer(
            "❌ Некоректне ім'я. Будь ласка, введіть ваше ім'я:",
            reply_markup=remove_keyboard(),
        )
        return

    await state.update_data(first_name=first_name)

    # Acknowledge first name
    await message.answer(
        f"Приємно познайомитися, {first_name}! 👋", reply_markup=remove_keyboard()
    )

    # Ask for last name
    await message.answer("Тепер, будь ласка, введіть ваше прізвище:")

    await state.set_state(RegistrationStates.waiting_for_last_name)


@router.message(RegistrationStates.waiting_for_last_name, F.text)
async def process_last_name(message: Message, state: FSMContext) -> None:
    if not message.text:
        message.answer("Помилка пыд час обробки повідомлення")
        return
    last_name = message.text.strip()

    # Validate: not empty, not too long, not a button emoji/command
    if not last_name or len(last_name) > 255 or last_name.startswith(("⏭", "📱", "/")):
        await message.answer(
            "❌ Некоректне прізвище. Будь ласка, введіть ваше справжнє прізвище (1-255 символів, без емодзі):",
            reply_markup=remove_keyboard(),
        )
        return

    await state.update_data(last_name=last_name)

    # Acknowledge progress
    await message.answer("Майже готово! 📱")

    # Ask for phone number with keyboard
    await message.answer(
        "Ви можете поділитися номером телефону за допомогою кнопки нижче, "
        "ввести його вручну або пропустити цей крок:",
        reply_markup=build_phone_request_keyboard(),
    )

    await state.set_state(RegistrationStates.waiting_for_phone_number)


@router.message(RegistrationStates.waiting_for_phone_number, F.contact)
async def process_phone_contact(
    message: Message, state: FSMContext, user_service: UserService
) -> None:
    """Process phone number from contact share."""
    if not message.contact:
        message.answer("Помилка пыд час обробки повідомлення")
        return
    phone_number = message.contact.phone_number
    await finish_registration(message, state, phone_number, user_service)


@router.message(
    RegistrationStates.waiting_for_phone_number,
    F.text.in_(["⏭️ Skip", "⏭️ Пропустити", "⏭️ Пропустить"]) | F.text.startswith("⏭"),
)
async def process_phone_skip(
    message: Message, state: FSMContext, user_service: UserService
) -> None:
    """Skip phone number."""
    await finish_registration(message, state, None, user_service)


@router.message(RegistrationStates.waiting_for_phone_number, F.text)
async def process_phone_text(
    message: Message, state: FSMContext, user_service: UserService
) -> None:
    """Process phone number from text input."""
    if not message.text:
        message.answer("Помилка пыд час обробки повідомлення")
        return
    phone_number = message.text.strip()

    if len(phone_number) > 20:
        await message.answer(
            "Номер телефону занадто довгий. Будь ласка, спробуйте ще раз або пропустіть:"
        )
        return

    await finish_registration(message, state, phone_number, user_service)


async def finish_registration(
    message: Message,
    state: FSMContext,
    phone_number: str | None,
    user_service: UserService,
) -> None:
    """Complete registration and save user to database."""
    data = await state.get_data()
    telegram_user = message.from_user

    if not telegram_user:
        await message.answer("Помилка: Не вдалося ідентифікувати користувача")
        await state.clear()
        return

    # Get language from Telegram user settings
    user_language = telegram_user.language_code or "ua"
    if user_language == "uk":
        user_language = "ua"
    user_language = user_language[:10]  # Ensure max 10 chars for DB

    user = await user_service.register_user(
        telegram_id=telegram_user.id,
        first_name=data.get("first_name"),
        last_name=data.get("last_name"),
        username=telegram_user.username,
        phone_number=phone_number,
        language=user_language,
    )

    await state.clear()
    await message.answer(
        f"Реєстрація завершена!\n\n"
        f"Вітаємо, {user.first_name} {user.last_name}!\n\n"
        f"Використовуйте /help щоб побачити доступні команди.",
        reply_markup=remove_keyboard(),
    )
