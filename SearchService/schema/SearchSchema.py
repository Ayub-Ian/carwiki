# models.py
from pydantic import BaseModel, Field, constr
from typing import Optional

class SearchParams(BaseModel):
    searchTerm: Optional[str] = Field(default=None, alias='searchTerm')
    orderBy: Optional[str] = Field(default='auctionEnd')
    filterBy: Optional[str] = Field(default=None)
    seller: Optional[str] = Field(default=None)
    winner: Optional[str] = Field(default=None)
    pageNumber: int = Field(default=1, ge=1)
    pageSize: int = Field(default=10, ge=1)
