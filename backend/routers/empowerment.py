from fastapi import APIRouter

router = APIRouter()

@router.get("/tutorials")
def get_tutorials():
    # Placeholder
    return [{"id": 1, "title": "AI for Marketing"}]
