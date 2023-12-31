from fastapi.routing import APIRouter

from gateway.web.api import echo, gestao, monitoring

api_router = APIRouter()
api_router.include_router(monitoring.router)
api_router.include_router(echo.router, prefix="/echo", tags=["echo"])
api_router.include_router(gestao.router, prefix="/gestao", tags=["gestao"])
