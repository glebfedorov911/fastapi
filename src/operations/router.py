import time

from fastapi import APIRouter, Depends, HTTPException
from fastapi_cache.decorator import cache
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from operations.models import Operation
from operations.schemas import OperationCreate

router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)


@router.get("/long_operation")
@cache(expire=30)
def get_long_op():
    time.sleep(2)
    return "Много много данных, которые вычислялись сто лет"


@router.get("")
async def get_specific_operations(operation_type: str, session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(Operation).where(Operation.c.type == operation_type)
        result = await session.execute(query)
        return {
            "status": "success",
            "data": result.all(),
            "details": None
        }
    except Exception:
        # Передать ошибку разработчикам
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "data": None,
            "details": None
        })


@router.post("")
async def add_specific_operations(new_operation: OperationCreate, session: AsyncSession = Depends(get_async_session)):
    """
    docstring
    """
    stmt = insert(Operation).values(**new_operation.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}
