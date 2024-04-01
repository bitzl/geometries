from pydantic import BaseModel, ConfigDict, Field
from typing import Self
from math import floor

from geometries.cards import Card
from geometries.paper import Paper


class Fitting(BaseModel):
    model_config = ConfigDict(frozen=True)

    fractional_columns: float = Field(ge=0)
    fractional_rows: float = Field(ge=0)

    @classmethod
    def create(cls: Self, card: Card, paper: Paper, distance: float = 0) -> Self:
        columns = (distance + paper.width) / (card.width + distance)
        rows = (distance + paper.height) / (card.height + distance)
        return cls(
            fractional_columns=columns,
            fractional_rows=rows,
        )

    @property
    def columns(self) -> int:
        return floor(self.fractional_columns)

    @property
    def rows(self) -> int:
        return floor(self.fractional_rows)

    @property
    def cards_per_sheet(self) -> int:
        return self.columns * self.rows
