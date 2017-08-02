from django.conf.urls import url
from django.views import View
from django.http import JsonResponse, HttpResponse

import json
import datetime


class Controller(View):

    def get(self, request):
        if 'events' not in request.session:
            request.session["events"] = []
        return JsonResponse({"data": request.session["events"]})

    def post(self, request):
        content = request.body.decode('utf-8')
        try:
            new_event = json.loads(content)
        except Exception:
            return JsonResponse({"error": "invalid_json_format"}, status=400)

        if not isinstance(new_event, dict):
            return JsonResponse({"error": "invalid_event_object_fields"}, status=400)

        keys = new_event.keys()
        if 'title' not in keys or 'date' not in keys:
            return JsonResponse({"error": "invalid_event_object_fields"}, status=400)

        title = str(new_event['title'])
        date = str(new_event['date'])

        if title is "":
            return JsonResponse({"error": "invalid_title_empty"}, status=400)

        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            return JsonResponse({"error": "invalid_date_format"}, status=400)

        if 'events' not in request.session:
            request.session["events"] = []
        events = request.session["events"]
        events.append({"title": title, "date": date})
        request.session["events"] = events
        return HttpResponse(status=201)

    def delete(self, request):
        request.session["events"] = []
        return HttpResponse(status=204)


urlpatterns = [
    url(r'^$', Controller.as_view())
]
