from typing import TYPE_CHECKING
from urllib.parse import urlencode

if TYPE_CHECKING:
    from weekly.config import Config


def get_callback_url(config: "Config", token: str) -> str:
    fe_url = config["FRONTEND_URL"]
    return "?".join([fe_url, urlencode({"token": token})])
