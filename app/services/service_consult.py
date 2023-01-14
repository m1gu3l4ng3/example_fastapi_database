import requests
from typing import Optional

from app.config.app_settings import AppSettings

URL_POST = "/json"

async def consult_service(settings: AppSettings) -> Optional[requests.Response]:
    """
    """
    try:
        response = requests.get(
            f"{settings.url_one}{URL_POST}"
        )
        response.raise_for_status()
    except requests.HTTPError:
        return
    return response