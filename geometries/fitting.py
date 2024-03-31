from pydantic import BaseModel, ConfigDict, Field
from typing import Self
from math import floor

from geometries.cards import Card
from geometries.paper import Paper


class Fitting(BaseModel):
    model_config = ConfigDict(frozen=True)

    columns: float = Field(ge=0)
    rows: float = Field(ge=0)
    cards_per_page: int = Field(ge=0)

    @classmethod
    def create(cls: Self, card: Card, paper: Paper, distance: float = 0) -> Self:
        columns = (distance + paper.width) / (card.width + distance)
        rows = (distance + paper.height) / (card.height + distance)
        cards_per_page = floor(columns) * floor(rows)
        return cls(
            columns=columns,
            rows=rows,
            cards_per_page=cards_per_page,
        )
