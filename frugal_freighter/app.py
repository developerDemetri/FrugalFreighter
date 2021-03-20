from typing import Any, Dict


def handler(event: Dict[str, Any], _: Any) -> str:
    """
    Lambda entrypoint
    """
    print(event)
    return "TODO"
