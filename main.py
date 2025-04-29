from fastapi import FastAPI
from core.db_conf import init_db
from routers.user import router as user_router
from routers.verify import router as verify_router

app = FastAPI(
    title="FastAPI-LMS-Task"
)

@app.on_event("startup")
async def startup():
    await init_db()
    print("DB Connected ✅")

app.include_router(user_router)
app.include_router(verify_router)