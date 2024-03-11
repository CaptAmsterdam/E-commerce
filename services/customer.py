from fastapi import HTTPException
from schema.customer import customers, CustomerCreate, Customer



class CustormerService:


    @staticmethod
    def validate_username(payload: CustomerCreate):
        username: str = payload.username
        for customer in customers:
            if customer.username == payload.username:
                raise HTTPException(status_code=400, detail="Customer username already exist")
            return payload