from sqlmodel import SQLModel, Field
from datetime import datetime, timezone

def get_utc_now():
    return datetime.now(timezone.utc)

class Blog(SQLModel, table=True):
    id: int = Field(default=True, primary_key=True)
    title: str | None = Field(index=True)
    created_at: datetime = Field(default_factory=get_utc_now)

