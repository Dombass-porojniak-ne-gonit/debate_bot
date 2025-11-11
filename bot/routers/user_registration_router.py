from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InaccessibleMessage, Message

from bot.services.user_service import UserService
from bot.utils.fsm_states import RegistrationStates
from bot.utils.keyboards import build_welcome_keyboard, remove_keyboard

router = Router(name="user_registration_router")


@router.message(CommandStart(), F.chat.type == "private")
async def cmd_start_private(
    message: Message, state: FSMContext, user_service: UserService
) -> None:
    """Handle /start in private chat"""
    telegram_user = message.from_user
    if not telegram_user:
        await message.answer("Помилка: Не вдалося ідентифікувати користувача")
        return

    await state.clear()

    user = await user_service.user_repo.get_by_telegram_id(telegram_user.id)

    if user:
        await message.answer(
            f"З поверненням, {user.first_name or 'User'}! 👋\n\n"
            f"Використовуйте /help щоб побачити доступні команди.",
            reply_markup=remove_keyboard(),
        )
    else:
        await message.answer(
            "Привіт! Щоб почати, будь ласка, зареєструй свій профіль у боті.",
            reply_markup=build_welcome_keyboard(),
        )


@router.callback_query(
    F.data == "private.user.start_registration", F.chat.type == "private"
)
async def start_registration(callback: CallbackQuery, state: FSMContext) -> None:
    if callback.message is None or isinstance(callback.message, InaccessibleMessage):
        callback.answer("Помилка пыд час обробки повідомлення")
        return
    await callback.message.edit_text("Чудово! Давайте налаштуємо ваш профіль.")

    # Send separate message asking for first name
    await callback.message.answer(
        "📝 Будь ласка, введіть ваше ім'я:", reply_markup=remove_keyboard()
    )

    await state.set_state(RegistrationStates.waiting_for_first_name)
    await callback.answer()


@router.callback_query(F.data == "show_help")
async def show_help_callback(callback: CallbackQuery) -> None:
    """Handle help button from welcome screen."""
    try:
        if not callback.message or isinstance(callback.message, InaccessibleMessage):
            callback.answer("Помилка пыд час обробки повідомлення")
            return
        await callback.message.edit_text(
            "Доступні команди:\n\n/start - Реєстрація\n/help - Показати це повідомлення",
            reply_markup=build_welcome_keyboard(),
        )
    except Exception:
        # Message is already showing help, just answer callback
        pass
    await callback.answer()
