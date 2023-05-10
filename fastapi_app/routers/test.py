from fastapi import APIRouter

router = APIRouter()

@router.get('/test')
async def test():
    return {'val1': 'val2', 'val3': {'val4': 23, 56: 'val5'}}

@router.get('/account')
async def account_info(id: int):
    return {'id': id, 'name': ''}

@router.get('/account/friends')
async def account_info(id: int):
    return {}

@router.get('/account/requests')
async def account_info(id: int):
    return {}