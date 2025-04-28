from fastapi import APIRouter, status, HTTPException, Query

from core.verify import generate_otp, expires_date
from models.user import User
from schemas.user import UserOut, CreateUserFrom

router = APIRouter(
    prefix="/user",
    tags=["LMS-Register-API"]
)

@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=UserOut)
async def register_user(user: CreateUserFrom):
    existing_user = await User.get_or_none(user_id=user.user_id)
    if existing_user:
        raise HTTPException(status_code=409, detail="User already exists")

    new_user = await User.create(user_id=user.user_id, fullname=user.fullname, username=user.username, phone_number=user.phone_number, verification_code=generate_otp(user.user_id), expires_date=expires_date)
    return new_user

@router.get("/login", status_code=status.HTTP_200_OK)
async def login_user(user_id: int = Query(...)):
    user = await User.get_or_none(user_id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    user.verification_code = generate_otp(user_id)
    user.expires_date = expires_date
    await user.save()

    return user
