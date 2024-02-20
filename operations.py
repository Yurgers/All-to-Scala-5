import asyncio
from enum import Enum
from typing import Optional
from dataclasses import dataclass
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor

timeout_seconds = timedelta(seconds=15).total_seconds()


class Response(Enum):
    Success = 1
    RetryAfter = 2
    Failure = 3


class ApplicationStatusResponse(Enum):
    Success = 1
    Failure = 2


@dataclass
class ApplicationResponse:
    application_id: str
    status: ApplicationStatusResponse
    description: str
    last_request_time: datetime
    retriesCount: Optional[int]


async def get_application_status1(identifier: str) -> Response:
    # Метод, возвращающий статус заявки
    pass


async def get_application_status2(identifier: str) -> Response:
    # Метод, возвращающий статус заявки
    pass


async def get_application(identifier: str, application) -> tuple[Response, int]:
    count = 0
    isTrue = True
    while isTrue:
        count += 1
        res = await application(identifier)
        if res.RetryAfter:
            await asyncio.sleep(1)
        else:
            isTrue = False

    return res, count


async def perform_operation(identifier: str) -> ApplicationResponse:
    with ThreadPoolExecutor() as executor:
        res1, c1 = executor.submit(get_application, identifier, get_application_status1)
        res2, c2 = executor.submit(get_application, identifier, get_application_status2)

    status = ApplicationStatusResponse.Failure
    if res1 == res2 == Response.Success:
        status = ApplicationStatusResponse.Success

    app_resp = ApplicationResponse(
        application_id=identifier,
        status=status,
        description=f"Servise1 Status: {res1.name}, Servise2 Status: {res2.name}",
        last_request_time=datetime.now(),
        retriesCount: c1 + c2,
    )
    return app_resp
