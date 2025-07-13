from fastapi import APIRouter

router = APIRouter()

@router.get("/prompts")
def get_prompts():
    # Placeholder
    return [{"id": 1, "title": "Cyberpunk City"}]
