from typing import List

import requests
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse, StreamingResponse

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
async def delete_user(user_id: str) -> dict:
    response = requests.delete(
        f"{settings.gestao_host}/api/users/{user_id}",
        timeout=600,
    )
    return JSONResponse(
        status_code=response.status_code,
        content=response.json(),
    )


@router.patch("/users/{user_id}/disable")
async def disable_user(user_id: str) -> dict:
    response = requests.patch(
        f"{settings.gestao_host}/api/users/{user_id}/disable",
        timeout=600,
    )
    return JSONResponse(
        status_code=response.status_code,
        content=response.json(),
    )


@router.patch("/users/{user_id}/enable")
async def enable_user(user_id: str) -> dict:
    response = requests.patch(
        f"{settings.gestao_host}/api/users/{user_id}/enable",
        timeout=600,
    )
    return JSONResponse(
        status_code=response.status_code,
        content=response.json(),
    )


@router.post("/login/user")
async def login_user(request: Request) -> dict:
    response = requests.post(
        f"{settings.gestao_host}/api/login/user",
        json=await request.json(),
        timeout=600,
    )
    return JSONResponse(
        status_code=response.status_code,
        content=response.json(),
    )


@router.post("/login/recover_password")
async def recover_password(request: Request) -> dict:
    response = requests.post(
        f"{settings.gestao_host}/api/login/recover_password",
        json=await request.json(),
        timeout=600,
    )
    return JSONResponse(
        status_code=response.status_code,
        content=response.json(),
    )


@router.get("/documents/affiliation/{user_id}")
async def get_affiliation_doc(user_id: str) -> StreamingResponse:
    response = requests.get(
        f"{settings.gestao_host}/api/documents/affiliation/{user_id}",
        timeout=600,
        stream=True,
    )
    return StreamingResponse(
        response.iter_content(chunk_size=1024),
        media_type=response.headers["Content-Type"],
    )


@router.get("/documents/report-users")
async def get_report_users() -> StreamingResponse:
    response = requests.get(
        f"{settings.gestao_host}/api/documents/report-users",
        timeout=600,
        stream=True,
    )
    return StreamingResponse(
        response.iter_content(chunk_size=1024),
        media_type=response.headers["Content-Type"],
    )
