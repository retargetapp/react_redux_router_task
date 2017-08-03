from django.views import View
from django.http import JsonResponse
import graphene


class Event(graphene.ObjectType):
    title = graphene.String(required=True)
    date = graphene.String(required=True)

class Query(graphene.ObjectType):
    events = graphene.List(Event,title=graphene.String(), date=graphene.String())

    def resolve_events(self, args, context, info):

        events = context["events"]
        if 'title' in args.keys():
            events = list(filter(lambda e: e["title"] == args["title"], events))

        if 'date' in args.keys():
            events = list(filter(lambda e: e["date"] == args["date"], events))

        events = list(map(
            lambda raw_data: Event(title=raw_data["title"], date=raw_data["date"]),
            events
        ))
        return list(events)


schema = graphene.Schema(query=Query)


class GraphqlController(View):

    def get(self, request):
        if 'query' not in request.GET.keys():
            return JsonResponse({"error": "query-parameter-not-defined"}, status=400)

        if 'events' not in request.session:
            request.session["events"] = []

        try:
            result = schema.execute(request.GET['query'], context_value=dict(request.session))
        except Exception:
            return JsonResponse({"error": "invalid-graphql-query"}, 400)

        return JsonResponse(result.data)
