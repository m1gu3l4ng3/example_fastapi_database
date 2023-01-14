"""
Create endpoint to calculate score
"""
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from app.config.app_settings import AppSettings, get_settings
from app.models.model_input import InputRequest
from app.services.service_consult import consult_service

router_score = APIRouter()



@router_score.post("/score")
async def score(
    resquest: InputRequest, 
    settings: AppSettings = Depends(get_settings)
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
    response = JSONResponse(
        content=response_dict,
        status_code=status_code
    )
    return response
