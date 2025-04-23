import os
from fastapi import FastAPI, Depends, HTTPException, Request
from pin_schema import PinRequest, PinResponse
from auth_store import store
API_KEY=os.getenv('VIKTOR_API_KEY','change')
app=FastAPI()

def guard(r:Request):
    if r.headers.get('x-api-key')!=API_KEY: raise HTTPException(401)
@app.post('/submit',response_model=PinResponse,dependencies=[Depends(guard)])
async def submit(p:PinRequest):
    return store.validate_pin(p.pin,p.mac)
@app.post('/generate/{rank}',response_model=PinResponse,dependencies=[Depends(guard)])
async def gen(rank:str):
    return store.issue_new(rank)
