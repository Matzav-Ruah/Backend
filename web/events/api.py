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
