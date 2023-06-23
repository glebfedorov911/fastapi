from fastapi import APIRouter, Depends

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from .models import Role
from .schemas import RoleCreate

router = APIRouter(
    prefix='/role',
    tags=['Role'],
)

@router.post('/newrole')
async def add_role(role: RoleCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Role).values(**role.dict())
    await session.execute(stmt)
    await session.commit()
    return {'status':'success'}

@router.get('/roles')
async def get_role(session: AsyncSession = Depends(get_async_session)):
    query = select(Role)
    result = await session.execute(query)

    return {'data': result.all()}