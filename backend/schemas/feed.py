from pydantic import BaseModel

class Feed(BaseModel):
    total_cards: int
    current_card: int
    history: list[int]
