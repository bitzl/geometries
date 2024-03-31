from pydantic import BaseModel, ConfigDict, Field


class Card(BaseModel):
    model_config = ConfigDict(frozen=True)
    
    width: int = Field(gt=0)
    height: int = Field(gt=0)
    

    def __str__(self) -> str:
        return f"Card({self.width}×{self.height})"
    
    def __lt__(self, other: 'Card') -> bool:
        return self.width * self.height < other.width * other.height


spielkarte = Card(width=60, height=90)
patience_karte = Card(width=44, height=67)
