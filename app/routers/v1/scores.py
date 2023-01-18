"""
Create endpoint to calculate score
"""
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.app_settings import AppSettings, get_settings
from app.schemas.schema_input import InputRequest
from app.models.model_score import Scores
from app.services.service_consult import consult_service
from app.sql_app.session_db import get_session
from app.sql_app.crud import create_score

router_score = APIRouter()



@router_score.post("/score")
async def score(
    resquest: InputRequest, 
    settings: AppSettings = Depends(get_settings),
    db: AsyncSession = Depends(get_session)
) -> JSONResponse:
    """Calculate score
    """
    status_code: int = 200
    response_dict: dict
    response_service = await consult_service(settings=settings)
    if response_service is None:
        response_dict = {"Failed": None}
        status_code = 404
    else:
        response_dict = response_service.json()
    score = Scores(
        input_requests=resquest.dict(),
        output_response=response_dict,
        score=10
    )
    await create_score(db, score)
    response = JSONResponse(
        content=response_dict,
        status_code=status_code
    )
    return response
