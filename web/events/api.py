from django.shortcuts import get_object_or_404
from ninja.security import django_auth
from ninja import NinjaAPI
from .models import Event
from . import schemas

api = NinjaAPI(urls_namespace="events", auth=django_auth)


@api.get("/get-all-events", response=list[schemas.EventSchema])
def get_all_events(request):
    events = Event.objects.filter(user=request.user).all()
    return [schemas.EventSchema.from_orm(event) for event in events]


@api.get("/get-event", response=schemas.EventSchema)
def get_event(request, event_id: int):
    return get_object_or_404(Event, id=event_id, user=request.user)


@api.post("/create-event", response={201: schemas.EventSchema})
def create_event(request, payload: schemas.CreateEventSchema):
    event = Event.objects.create(
        user=request.user,
        emotional_state=payload.emotional_state,
        data=payload.data,
    )
    return 201, event


@api.put("/update-event/{event_id}", response=schemas.EventSchema)
def update_event(request, event_id: int, payload: schemas.UpdateEventSchema):
    event = get_object_or_404(Event, id=event_id, user=request.user)

    if payload.emotional_state is not None:
        event.emotional_state = payload.emotional_state
    if payload.data is not None:
        event.data = payload.data

    event.save()
    return event


@api.delete("/delete-event/{event_id}", response={200: dict})
def delete_event(request, event_id: int):
    event = get_object_or_404(Event, id=event_id, user=request.user)
    event.delete()
    return 200, {"success": True}
