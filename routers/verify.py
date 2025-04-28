from fastapi import APIRouter, Query, HTTPException, Body
from starlette import status
from core.verify import check_verification_code
from models.user import User

router = APIRouter(prefix="/verify", tags=["LMS-Register-API"])


@router.post("/check-code", status_code=status.HTTP_200_OK)
async def check_code(verification_code: int = Query(default=...)):
    user = await User.get_or_none(verification_code=verification_code)

    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    is_valid = check_verification_code(user.user_id, user.verification_code)
    if not is_valid:
        raise HTTPException(status_code=400, detail="Invalid or expired verification code")

    user = await User.get_or_none(user_id=user.user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")

    user.is_verified = True
    user.expires_date = None
    user.verification_code = None
    await user.save()

    return {"status": True, "message": "User verified successfully", "user_id": user.user_id}
