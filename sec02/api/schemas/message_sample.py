from datetime import datetime
from pydantic import BaseModel, Field


class MessageBase(BaseModel):
    name: str | None = Field(None,
                             examples=["System"],
                             description="Message from")
    message: str | None = Field(None,
                                examples=["Default Message"],
                                description="Message body")
    priority: int = Field(0, examples=[5],
                          description="Message priority. "
                          "Higher value means high priority.")


class Message(MessageBase):
    time: datetime | None = Field(None, description="Message post time")
