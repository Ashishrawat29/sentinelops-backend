from fastapi import APIRouter

from app.schemas.equipment_schema import (
    EquipmentCreate,
)

router = APIRouter()


# CREATE EQUIPMENT

@router.post("/")
def create_equipment(
    equipment: EquipmentCreate,
):

    return {

        "message":
            "Equipment added successfully",

        "equipment":
            equipment.dict(),
    }


# GET ALL EQUIPMENT

@router.get("/")
def get_all_equipment():

    return {

        "message":
            "Equipment endpoint working",
    }


# GET SINGLE EQUIPMENT

@router.get("/{equipment_id}")
def get_equipment(
    equipment_id: int,
):

    return {

        "equipment_id":
            equipment_id,

        "message":
            "Equipment details endpoint working",
    }


# UPDATE EQUIPMENT

@router.put("/{equipment_id}")
def update_equipment(
    equipment_id: int,
    updated_equipment: EquipmentCreate,
):

    return {

        "message":
            "Equipment updated successfully",

        "equipment_id":
            equipment_id,
    }


# DELETE EQUIPMENT

@router.delete("/{equipment_id}")
def delete_equipment(
    equipment_id: int,
):

    return {

        "message":
            "Equipment deleted successfully",

        "equipment_id":
            equipment_id,
    }