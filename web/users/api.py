from ninja import NinjaAPI
from ninja.security import django_auth
from django.contrib.auth import authenticate, login, logout
from django.middleware.csrf import get_token
from django.db import IntegrityError
from django.db.models import Q
from .models import User
from . import schemas
from datetime import timedelta, datetime
from events.models import Event


api = NinjaAPI(urls_namespace="users")


@api.get("/get-csrf-token")
def get_csrf_token(request):
    return {"success": True, "csrftoken": get_token(request)}


@api.post("/login")
def login_view(request, payload: schemas.SignInSchema):
    user = authenticate(request, username=payload.email, password=payload.password)
    if user is not None:
        login(request, user)
        return {"success": True, "data": schemas.UserSchema.from_orm(user)}
    return {"success": False, "message": "Invalid credentials"}


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


@api.post("/logout", auth=django_auth)
def logout_view(request):
    logout(request)
    return {"success": True}


@api.get("/user", auth=django_auth)
def user(request):
    return {"success": True, "data": schemas.UserSchema.from_orm(request.user)}


@api.get("/leaderboard", auth=django_auth)
def get_leaderboard(request):
    users = User.objects.all().order_by("-streak_count", "id")[:3]
    position = (
        User.objects.filter(
            Q(streak_count__gt=request.user.streak_count)
            | Q(streak_count=request.user.streak_count, id__lt=request.user.id)
        ).count()
        + 1
    )
    return {
        "success": True,
        "data": {
            "users": [schemas.UserProfileSchema.from_orm(user) for user in users],
            "activeUserPosition": position,
        },
    }


@api.get("/get-user-streak", response=schemas.ApiResponse[schemas.StreakSchema])
def get_user_streak(request):
    dates = (
        Event.objects.filter(user=request.user)
        .order_by("-date")
        .values_list("date", flat=True)
    )
    if not dates:
        return {"success": True, "data": {"streak_count": 0}}
    if dates[0] < datetime.today().date() - timedelta(days=1):
        return {"success": True, "data": {"streak_count": 0}}
    streak = 1
    prev = dates[0]
    for current in dates[1:]:
        if prev - current == timedelta(days=1):
            streak += 1
            prev = current
        elif prev == current:
            continue
        else:
            break
    return {"success": True, "data": {"streak_count": streak}}
