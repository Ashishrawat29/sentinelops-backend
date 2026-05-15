from fastapi import APIRouter

from app.schemas.user_schema import (
    UserCreate,
    UserLogin,
)

router = APIRouter()


@router.post("/register")
def register(
    user: UserCreate,
):

    return {

        "message":
            "User registered successfully",

        "user":
            user.email,
    }


@router.post("/login")
def login(
    user: UserLogin,
):

    return {

        "access_token":
            "demo_token",

        "token_type":
            "bearer",

        "role":
            "Admin",
    }