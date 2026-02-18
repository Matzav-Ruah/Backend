from ninja import NinjaAPI
from ninja.security import django_auth
from django.contrib.auth import authenticate, login, logout
from django.middleware.csrf import get_token
from django.db import IntegrityError
from .models import User
from . import schemas

api = NinjaAPI(urls_namespace="users")


@api.get("/get-csrf-token")
def get_csrf_token(request):
    return {"success": True, "csrftoken": get_token(request)}


@api.post("/login")
def login_view(request, payload: schemas.SignInSchema):
    user = authenticate(request, username=payload.email, password=payload.password)
    if user is not None:
        login(request, user)
        return {"success": True}
    return {"success": False, "message": "Invalid credentials"}


@api.post("/logout", auth=django_auth)
def logout_view(request):
    logout(request)
    return {"success": True}


@api.get("/user", auth=django_auth, response=schemas.UserSchema)
def user(request):
    return schemas.UserSchema.from_orm(request.user)


@api.post("/register")
def register(request, payload: schemas.SignInSchema):
    try:
        User.objects.create_user(
            username=payload.email, email=payload.email, password=payload.password
        )
        return {"success": True, "message": "User registered successfully"}
    except IntegrityError:
        return {
            "success": False,
            "message": "An account with this email already exists.",
        }
    except Exception:
        return {"success": False, "message": "Registration failed. Please try again."}
