from datetime import date
from django.shortcuts import get_object_or_404
from ninja.security import django_auth
from ninja import NinjaAPI
from .models import Event
from . import schemas

api = NinjaAPI(urls_namespace="events", auth=django_auth)


@api.get("/get-all-events", response=schemas.ApiResponse[list[schemas.EventSchema]])
def get_all_events(request):
    events = Event.objects.filter(user=request.user).all()
    return {
        "success": True,
        "data": [schemas.EventSchema.from_orm(event) for event in events],
    }


@api.get("/get-event", response=schemas.ApiResponse[schemas.EventSchema])
def get_event(request, date: date):
    event = Event.objects.filter(date=date, user=request.user).first()
    if not event:
        return {"success": False, "data": None}
    return {"success": True, "data": schemas.EventSchema.from_orm(event)}


@api.post("/create-event", response={201: schemas.ApiResponse[schemas.EventSchema]})
def create_event(request, payload: schemas.CreateEventSchema):
    event = Event.objects.create(
        user=request.user,
        emotional_state=payload.emotional_state,
        event_data=payload.event_data,
        date=payload.date,
    )
    return 201, {"success": True, "data": schemas.EventSchema.from_orm(event)}


@api.put("/update-event", response=schemas.ApiResponse[schemas.EventSchema])
def update_event(request, date: date, payload: schemas.UpdateEventSchema):
    event = get_object_or_404(Event, date=date, user=request.user)

    if payload.emotional_state is not None:
        event.emotional_state = payload.emotional_state
    if payload.event_data is not None:
        event.event_data = payload.event_data

    event.save()
    return {"success": True, "data": event}


@api.delete("/delete-event", response=schemas.ApiResponse[dict])
def delete_event(request, date: date):
    event = get_object_or_404(Event, date=date, user=request.user)
    event.delete()
    return {"success": True, "data": {}}
