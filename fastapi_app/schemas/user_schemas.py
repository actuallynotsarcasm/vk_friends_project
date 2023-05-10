from pydantic import BaseModel

class user_create(BaseModel):

    name: str

class user_get_by_name(BaseModel):

    name: str

class user(BaseModel):

    id: int
    name: str

class request_send(BaseModel):

    recipient_name: str

class request_accept(BaseModel):

    id: int
    accepted: bool

class request(BaseModel):

    id: int
    sender_name: str
    recipient_name: str

class status_check(BaseModel):

    sender_name: str
    target_name: str