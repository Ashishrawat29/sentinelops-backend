from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.equipment import Equipment
from app.schemas.equipment_schema import (
    EquipmentCreate
)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# CREATE EQUIPMENT
@router.post("/")
def create_equipment(
    equipment: EquipmentCreate,
    db: Session = Depends(get_db)
):
    new_equipment = Equipment(
        equipment_name=equipment.equipment_name,
        category=equipment.category,
        status=equipment.status,
        health_score=equipment.health_score,
        deployment_location=equipment.deployment_location,
        last_maintenance=equipment.last_maintenance
    )

    db.add(new_equipment)
    db.commit()
    db.refresh(new_equipment)

    return {
        "message": "Equipment added successfully"
    }

# GET ALL EQUIPMENT
@router.get("/")
def get_all_equipment(
    db: Session = Depends(get_db)
):
    equipment = db.query(Equipment).all()

    return equipment

# GET SINGLE EQUIPMENT
@router.get("/{equipment_id}")
def get_equipment(
    equipment_id: int,
    db: Session = Depends(get_db)
):
    equipment = db.query(Equipment).filter(
        Equipment.id == equipment_id
    ).first()

    if not equipment:
        raise HTTPException(
            status_code=404,
            detail="Equipment not found"
        )

    return equipment

# UPDATE EQUIPMENT
@router.put("/{equipment_id}")
def update_equipment(
    equipment_id: int,
    updated_equipment: EquipmentCreate,
    db: Session = Depends(get_db)
):
    equipment = db.query(Equipment).filter(
        Equipment.id == equipment_id
    ).first()

    if not equipment:
        raise HTTPException(
            status_code=404,
            detail="Equipment not found"
        )

    equipment.equipment_name = updated_equipment.equipment_name
    equipment.category = updated_equipment.category
    equipment.status = updated_equipment.status
    equipment.health_score = updated_equipment.health_score
    equipment.deployment_location = updated_equipment.deployment_location
    equipment.last_maintenance = updated_equipment.last_maintenance

    db.commit()

    return {
        "message": "Equipment updated successfully"
    }

# DELETE EQUIPMENT
@router.delete("/{equipment_id}")
def delete_equipment(
    equipment_id: int,
    db: Session = Depends(get_db)
):
    equipment = db.query(Equipment).filter(
        Equipment.id == equipment_id
    ).first()

    if not equipment:
        raise HTTPException(
            status_code=404,
            detail="Equipment not found"
        )

    db.delete(equipment)
    db.commit()

    return {
        "message": "Equipment deleted successfully"
    }