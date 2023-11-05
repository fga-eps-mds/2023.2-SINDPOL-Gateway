from typing import List

import requests
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from gateway.settings import settings

router = APIRouter()


@router.get("/users/")
async def get_users(
    limit: int = 10,
    offset: int = 0,
) -> List[dict]:
    response = requests.get(
        f"{settings.gestao_host}/api/users",
        params={
            "limit": limit,
            "offset": offset,
        },
        timeout=600,
    )
    return JSONResponse(
        status_code=response.status_code,
        content=response.json(),
    )


@router.get("/users/{user_id}")
async def get_user(user_id: str) -> dict:
    response = requests.get(
        f"{settings.gestao_host}/api/users/{user_id}",
        timeout=600,
    )
    return JSONResponse(
        status_code=response.status_code,
        content=response.json(),
    )


@router.post("/users/")
async def create_user(request: Request) -> dict:
    response = requests.post(
        f"{settings.gestao_host}/api/users",
        json=await request.json(),
        timeout=600,
    )
    return JSONResponse(
        status_code=response.status_code,
        content=response.json(),
    )


@router.put("/users/{user_id}")
async def update_user(user_id: str, request: Request) -> dict:
    response = requests.put(
        f"{settings.gestao_host}/api/users/{user_id}",
        json=await request.json(),
        timeout=600,
    )
    return JSONResponse(
        status_code=response.status_code,
        content=response.json(),
    )


@router.delete("/users/{user_id}")
async def delete_user(user_id: str) -> None:
    response = requests.delete(
        f"{settings.gestao_host}/api/users/{user_id}",
        timeout=600,
    )
    return JSONResponse(
        status_code=response.status_code,
        content=response.json(),
    )


@router.patch("/users/{user_id}/disable")
async def disable_user(user_id: str) -> None:
    response = requests.patch(
        f"{settings.gestao_host}/api/users/{user_id}/disable",
        timeout=600,
    )
    return JSONResponse(
        status_code=response.status_code,
        content=response.json(),
    )
