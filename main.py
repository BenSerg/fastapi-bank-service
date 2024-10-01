from fastapi import FastAPI
from routers.calculate import router as calculate_router

app = FastAPI()

app.include_router(calculate_router)
