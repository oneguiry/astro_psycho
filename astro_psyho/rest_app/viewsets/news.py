from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import viewsets, permissions

from core.controllers.news_controller import NewsController
from core.models import News
from permissions.models import AccountManager
from rest_app.serializers.core import NewsSerializer, NewsCreateSerializer, NewsDetailSerializer


class NewsViewSet(viewsets.ViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer()
    permission_classes = [permissions.AllowAny, ]
    http_method_names = ['get', 'post','patch', 'delete']

    def list(self, request):
        queryset = News.objects.all()
        serializer = NewsSerializer(queryset, many=True)
        return Response(serializer.data, status=200)

    # TODO: тут изменить в соответствии с пермишинами
    @swagger_auto_schema(
        request_body=NewsCreateSerializer(many=False),
        responses={200: "Successfully created"},
        permission_classes=[permissions.IsAdminUser]
    )
    def create(self, request, *args, **kwargs):
        title = request.data['title']
        body = request.data['body']
        user = AccountManager.objects.get(user=request.user)
        news = News.objects.create(title=title, body=body, author=user)
        serializer = NewsCreateSerializer(news, many=False)
        return Response(serializer.data, status=201)

    @swagger_auto_schema(
        operation_description="Редактирование параметров маршрута обследования",
        request_body=NewsDetailSerializer(many=False),
        responses={
            201: NewsSerializer(),
        }
    )
    def partial_update(self, request, pk=None, *args, **kwargs):
        news_controller = NewsController(pk)
        author = request.user

        title = request.data['title']
        body = request.data['body']
        pub_date = request.data['pub_date']
        news_controller.edit_news(title, body, author, pub_date)
        news = news_controller.get_news()
        serializer = NewsSerializer(news, many=False)
        return Response(serializer.data, status=201)
