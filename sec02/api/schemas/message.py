from datetime import datetime
from pydantic import BaseModel, Field


class MessageBase(BaseModel):
    name: str | None = Field(None,
                             examples=["System"],
                             description="Message from")
    message: str | None = Field(None,
                                examples=["Default Message"],
                                description="Message body")


class Message(MessageBase):
    time: datetime | None = Field(None, description="Message post time")
