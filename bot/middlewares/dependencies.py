from typing import Any

from aiogram import BaseMiddleware

from bot.factories.service_factory import ServiceFactory


class DependencyInjectionMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler,
        event,
        data,
    ) -> Any:
        data.update(ServiceFactory.create_all_services())
        return await handler(event, data)
