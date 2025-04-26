from fastapi import APIRouter, status, HTTPException, Query

from models.user import User
from schemas.user import UserOut, CreateUserFrom

router = APIRouter(
    prefix="/user",
    tags=["LMS-Register-API"]
)

@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=UserOut)
async def register_user(user: CreateUserFrom):
    new_user = await User.create(**user.dict())
    return new_user

@router.get("/current-user", status_code=status.HTTP_200_OK, response_model=UserOut)
async def get_current_user(user_id: int = Query()):
    user = await User.get_or_none(user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
