from typing import List

import requests
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse

from gateway.settings import settings

router = APIRouter()


@router.get("/patrimony/")
async def get_patrimonys(
    limit: int = 10,
    offset: int = 0,
) -> List[dict]:
    response = requests.get(
        f"{settings.patrimonio_host}/api/patrimony",
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


@router.get("/patrimony/{patrimony_id}")
async def get_patrimony(patrimony_id: str) -> dict:
    response = requests.get(
        f"{settings.patrimonio_host}/api/patrimony/{patrimony_id}",
        timeout=600,
    )
    return JSONResponse(
        status_code=response.status_code,
        content=response.json(),
    )


@router.post("/patrimony/")
async def create_patrimony(request: Request) -> dict:
    response = requests.post(
        f"{settings.patrimonio_host}/api/patrimony",
        json=await request.json(),
        timeout=600,
    )
    return JSONResponse(
        status_code=response.status_code,
        content=response.json(),
    )


@router.put("/patrimony/{patrimony_id}")
async def update_patrimony(patrimony_id: str, request: Request) -> dict:
    response = requests.put(
        f"{settings.patrimonio_host}/api/patrimony/{patrimony_id}",
        json=await request.json(),
        timeout=600,
    )
    return JSONResponse(
        status_code=response.status_code,
        content=response.json(),
    )


@router.delete("/patrimony/{patrimony_id}")
async def delete_patrimony(patrimony_id: str) -> None:
    response = requests.delete(
        f"{settings.patrimonio_host}/api/patrimony/{patrimony_id}",
        timeout=600,
    )
    return JSONResponse(
        status_code=response.status_code,
        content=response.json(),
    )
