from django.urls import path
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from graphene_file_upload.django import FileUploadGraphQLView

urlpatterns = [
    path('graphql', csrf_exempt(FileUploadGraphQLView.as_view(graphiql=True)), name='api.graphql')
    # path('graphql', csrf_exempt(GraphQLView.as_view(graphiql=True)), name='api.graphql')
]
