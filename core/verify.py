from datetime import datetime, timedelta
import random
otp_store = {}
expires_date = datetime.utcnow() + timedelta(minutes=1)

def generate_otp(user_id: int, expires_date: datetime = expires_date) -> str:
    otp = f"{random.randint(100000, 999999)}"
    otp_store[user_id] = (otp, expires_date)
    return otp

def check_verification_code(user_id: int, code: str, expires_date: datetime = expires_date) -> bool:
    data = otp_store.get(user_id)
    if not data:
        return False
    stored_code, expires_at = data
    if expires_date > expires_at:
        del otp_store[user_id]
        return False
    return stored_code == code