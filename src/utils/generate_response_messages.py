from fastapi import status

def generate_response_message(
    status_code: int = status.HTTP_404_NOT_FOUND,
    msg: str | None = None,
):
    """
    Generates a FastAPI response model documentation mapping for error responses.

    Args:
        status_code (int): HTTP status code (default: 404).
        msg (str | None): Custom error message.

    Returns:
        dict: Response documentation for FastAPI route decorators.
    """
    return {
        status_code: {
            "description": msg if msg else "Aucune information enregistrée",
            "content": {
                "application/json": {
                    "example": {"detail": {"message": msg if msg else "Aucune information enregistrée"}}
                }
            },
        }
    }
