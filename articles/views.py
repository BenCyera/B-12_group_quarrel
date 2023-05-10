from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from articles.models import Categorys, Article
from articles.serializers import ArticleSerializer, ArticleCreateSerializer


# 카테고리별 메인페이지
class ArticleListView(APIView):
    def get(self, request, category_id):
        articles = Article.objects.filter(category_id=category_id)
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request, category_id):
        serializer = ArticleCreateSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, category_id=category_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 게시글 상세페이지
class ArticleDetailView(APIView):
    def get(self, article_id):
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    # 게시글 수정하기
    def put() :
        pass

    # 게시글 삭제하기
    def delete() :
        pass


# 댓글 조회, 등록, 수정, 삭제
class CommentView(APIView):
    def get(self, request, category_id, article_id, comment_id):
        pass
    
    def post(self, request, category_id, article_id, comment_id):
        pass
    
    def put(self, request, category_id, article_id, comment_id):
        pass
    
    def delete(self, request, category_id, article_id, comment_id):
        pass
    

# 좋아요 등록, 취소
class Like(APIView):
    def post(self, category_id, article_id):
        pass


# 북마크 게시글 조회, 등록, 취소
class BookMarkView(APIView):
    def get(self, category_id, article_id):
        pass
    
    def post(self, category_id, article_id):
        pass


# 내가 쓴 게시글 조회
class ArticleUserView(APIView):
    def get(self, user_id):
        pass