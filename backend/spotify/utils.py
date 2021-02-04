from typing import Dict

from .exceptions import CodeNotProvided


def retrieve_code(params: Dict[str, str]) -> str:
    code = params.get("code")
    if code is None:
        raise CodeNotProvided
    return code
