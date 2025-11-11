from collections.abc import Awaitable, Callable
from typing import Generic, TypeVar
from uuid import UUID

from tortoise import Model
from tortoise.queryset import QuerySet
from tortoise.transactions import in_transaction

T = TypeVar("T", bound=Model)
ModelData = dict[str, object]  # Represents arbitrary model field data


class BaseRepository(Generic[T]):
    model: type[T]

    def __init__(self, model: type[T]) -> None:
        self.model = model

    async def create(self, **kwargs: object) -> T | None:
        return await self.model.create(**kwargs)

    async def get_or_create(
        self, defaults: ModelData | None = None, **filters: object
    ) -> tuple[T, bool]:
        return await self.model.get_or_create(
            defaults=defaults or {}, using_db=None, **filters
        )

    async def bulk_create(self, objects: list[ModelData]) -> list[T]:
        instances = [self.model(**obj) for obj in objects]
        await self.model.bulk_create(instances)
        return instances

    async def get_by_id(self, id: UUID) -> T | None:
        return await self.model.get_or_none(id=id)

    async def get_all(
        self, limit: int = 100, offset: int = 0, order_by: list[str] | None = None
    ) -> list[T]:
        queryset = self.model.all().limit(limit).offset(offset)
        if order_by:
            queryset = queryset.order_by(*order_by)
        return await queryset

    async def filter(
        self,
        limit: int = 100,
        offset: int = 0,
        order_by: list[str] | None = None,
        **filters: object,
    ) -> list[T]:
        queryset = self.model.filter(**filters).limit(limit).offset(offset)
        if order_by:
            queryset = queryset.order_by(*order_by)
        return await queryset

    async def first(self, **filters: object) -> T | None:
        return await self.model.filter(**filters).first()

    async def exists(self, **filters: object) -> bool:
        return await self.model.filter(**filters).exists()

    async def update(self, instance: T, **data: object) -> T:
        for key, value in data.items():
            setattr(instance, key, value)
        await instance.save()
        return instance

    async def update_by_id(self, id: UUID, **data: object) -> T | None:
        instance = await self.get_by_id(id)
        if instance:
            return await self.update(instance, **data)
        return None

    async def bulk_update(self, instances: list[T], fields: list[str]) -> None:
        _ = await self.model.bulk_update(instances, fields=fields)

    async def delete(self, instance: T) -> None:
        await instance.delete()

    async def delete_by_id(self, id: UUID) -> bool:
        instance = await self.get_by_id(id)
        if instance:
            await instance.delete()
            return True
        return False

    async def bulk_delete(self, **filters: object) -> int:
        queryset = self.model.filter(**filters)
        count = await queryset.count()
        _ = await queryset.delete()
        return count

    async def count(self, **filters: object) -> int:
        return await self.model.filter(**filters).count()

    async def count_all(self) -> int:
        return await self.model.all().count()

    def get_queryset(self) -> QuerySet[T]:
        return self.model.all()

    async def execute_in_transaction(
        self, func: Callable[..., Awaitable[object]], *args: object, **kwargs: object
    ) -> object:
        async with in_transaction():
            return await func(*args, **kwargs)
