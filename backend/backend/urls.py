from django.conf.urls import url
from .rest_controller import RestController
from .grapql_controller import GraphqlController

urlpatterns = [
    url(r'^$', RestController.as_view()),
    url(r'^graphql', GraphqlController.as_view())
]
