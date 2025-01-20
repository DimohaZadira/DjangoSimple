from ninja import Router, Form, Schema
from . import models
import uuid
router = Router()

@router.get("/add_v2")
def add(request, a: int, b: int):
    return {"result": a + b}


class UltraKek(Schema):
    name: str
    telegram_id: int
    
@router.post("/create_ultra_kek")
def create_ultra_kek(request, ultra_kek: UltraKek):
    print("got ultra kek", ultra_kek)
    et_user = models.EtTestUser(
        id = uuid.uuid4(),
        telegram_id = ultra_kek.telegram_id
    )  
    et_user.save() 
    return {"sosal?": "da"}