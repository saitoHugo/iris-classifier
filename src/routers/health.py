from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health():
    """Check the API health status."""
    return {"message": "API health: OK!"}