"""
app schema for request body validation using pydantic
"""

from pydantic import BaseModel, Field

class ChatSchema(BaseModel):
    name: str=  Field(default='John Doe',min_length=10)

class PromptSchema(BaseModel):
    prompt:str 

class MessageSchema(BaseModel):
    senderName: str 
    content: str 
    chat_id: int 

# Response Schemas 
class CreateChatResponse(BaseModel):
    id: int
    name: str 

class PromptResponse(BaseModel):
    answer: str

class GetChatResponse(BaseModel):
    error: bool
    chats: list[CreateChatResponse]

class CreateMessageResponse(BaseModel):
    error: bool 
    description: str 

class GetMessagesResponse(BaseModel):
    error: bool
    messages: list[MessageSchema]

class DeleteChatResponse(CreateMessageResponse):
    pass 