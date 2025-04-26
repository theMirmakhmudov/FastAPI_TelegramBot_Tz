import random
import time

otp_store = {}

def generate_otp(user_id: int) -> str:
    otp = f"{random.randint(100000, 999999)}"
    expiry = time.time() + 60
    otp_store[user_id] = (otp, expiry)
    return otp

def check_verification_code(user_id: int, code: str) -> bool:
    data = otp_store.get(user_id)
    if not data:
        return False
    stored_code, expires_at = data
    if time.time() > expires_at:
        del otp_store[user_id]
        return False
    return stored_code == code