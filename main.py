from fastapi import Fastapi

import random


app = Fastapi()


@app.get('/')
async def root():
    return {'example': 'This is an example', 'data': 0}