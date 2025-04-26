from fastapi import APIRouter, Query, HTTPException, Body
from starlette import status

from core.verify import generate_otp, check_verification_code
from models.user import User

router = APIRouter(prefix="/verify", tags=["LMS-Register-API"])


@router.get("/generate_code", status_code=status.HTTP_200_OK)
async def send_verification_code(user_id: int = Query(default=...)):
    otp = generate_otp(user_id)
    return {
        "user_id": user_id,
        "otp": otp,
        "message": "Verification code generated",
        "expires_in": "60 seconds"
    }

@router.post("/check-code", status_code=status.HTTP_200_OK)
async def check_code(user_id: int = Query(default=...), code: str = Query(default=...)):
    is_valid = check_verification_code(user_id, code)
    if not is_valid:
        raise HTTPException(status_code=400, detail="Invalid or expired verification code")

    user = await User.get_or_none(user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if user.is_verified == True:
        raise HTTPException(status_code=400, detail="User has already verified")
    user.is_verified = True
    await user.save()
    return {"message": "User verified successfully", "user_id": user_id}
