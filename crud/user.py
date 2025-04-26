from models.user import User

async def create_user(user_id: int, username: str, phone_number: str) -> User:
    user = await User.create(user_id=user_id, username=username, phone_number=phone_number)
    return user

async def get_user_by_id(user_id: int) -> User | None:
    return await User.get_or_none(id=user_id)

async def get_all_users() -> list[User]:
    return await User.all()

async def update_user(user_id: int, **kwargs) -> User | None:
    user = await User.get_or_none(id=user_id)
    if user:
        for key, value in kwargs.items():
            setattr(user, key, value)
        await user.save()
    return user

async def delete_user(user_id: int) -> bool:
    user = await User.get_or_none(id=user_id)
    if user:
        await user.delete()
        return True
    return False