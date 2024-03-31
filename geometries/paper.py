from pydantic import BaseModel, ConfigDict, Field

class Paper(BaseModel):
    model_config = ConfigDict(frozen=True)

    name: str
    width: int = Field(gt=0)
    height: int = Field(gt=0)

    def __str__(self) -> str:
        return f"Paper({self.name}, {self.width}×{self.height})"
    
    @property
    def landscape(self):
        return Paper(name=self.name, width=self.height, height=self.width)


A4 = Paper(name="A4", width=210, height=297)
A3 = Paper(name="A3", width=297, height=420)
