from django.shortcuts import render
from rest_framework import generics
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response


class ArticleListView(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # permission_classes = permissions(permissions.IsAuthenticated,)
    def perform_create(self, serializer):
        return serializer.save()
    def get_queryset(self):
        return self.queryset.filter()
    
class ArticleCreate(generics.CreateAPIView):
    serializer_class = ArticleSerializers
    queryset = Article.objects.all()
    def create(self, request, *args, **kwargs):      
        return super(ArticleCreate, self).create(request, *args, **kwargs)
    
class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field = 'id'
    
    def perform_update(self, serializer):
        return serializer.save()
    def get_queryset(self):
        return self.queryset.filter()
    

# @api_view(['GET'])    
# def articleList(request):
#     articles = Article.objects.all()
#     serializer = ArticleSerializer(articles, many = True)
#     return Response(serializer.data)
    
# class ArticleDetailView(generics.RetrieveAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# @api_view(['GET'])      
# def articleDetail(request,pk):
#     article = Article.objects.get(id=pk)
#     serializer = ArticleSerializer(article, many = False)
#     return Response(serializer.data)


    
    
# @api_view(['POST'])
# def articleCreate(request):    
#     serializer = ArticleSerializer(data = request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# @api_view(['POST'])
# def articleUpdate(request, pk):
#     article = Article.objects.get(id = pk)
#     serializer = ArticleSerializer(instance=article, data = request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

# @api_view(['DELETE'])
# def articleDelete(request,pk):
#     article = Article.ojects.get(id = pk)
#     article.delete()
#     return Response("Article delete!")
    
    

@api_view(['GET'])    
@permission_classes((permissions.AllowAny,))
def apiOverview(request):
    api_urls = {
        'List':'/list/',
        'Detail':'/article/<pk>/',
        'Create':'/article-create/',
        'Update':'/article-update/<pk>/',
        'Delete':'/article-delete/<pk>/',
    }
    return Response(api_urls)
    
