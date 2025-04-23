from pydantic import BaseModel
class PinRequest(BaseModel):
    pin: str
    mac: str
class PinResponse(BaseModel):
    pin: str
    status: str = 'ok'
