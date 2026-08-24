from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.customer import Customer
from app.schemas.customer import (
    CustomerCreate,
    CustomerResponse
)

router = APIRouter(
    prefix="/customer",
    tags=["Customer"]
)


@router.post(
    "/",
    response_model=CustomerResponse,
    status_code=201
)
def create_customer(
    customer: CustomerCreate,
    db: Session = Depends(get_db)
):

    new_customer = Customer(
        name=Customer.name,
        category=Customer.category,
        address=Customer.address,
        opening_balance=Customer.opening_balance
    )

    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)

    return new_customer


@router.get(
    "/{customer_id}",
    response_model=CustomerResponse
)
def get_customer(
    customer_id: int,
    db: Session = Depends(get_db)
):

    customer = (
        db.query(Customer)
        .filter(Customer.id == customer_id)
        .first()
    )

    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    return customer


@router.put(
    "/{customer_id}",
    response_model=CustomerResponse
)
def customer_customer(
    customer_id: int,
    customer_data: CustomerCreate,
    db: Session = Depends(get_db)
):

    customer = (
        db.query(Customer)
        .filter(Shipment.id == customer_id)
        .first()
    )

    if customer is None:
        raise HTTPException(
            status_code=404,
            detail="Customer not found"
        )

    customer.name = customer_data.name
    customer.category = customer_data.category
    customer.address = customer_data.address
    customer.opening_balance = customer_data.opening_balance

    db.commit()
    db.refresh(customer)

    return customer

