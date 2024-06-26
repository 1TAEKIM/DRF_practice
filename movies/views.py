from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination

from .models import Movie, Actor, Review
from .serializers import MovieSerializer, ActorSerializer, ReviewSerializer


# 개별 페이지네이션 설정
class MoviepageNumberPagination(PageNumberPagination):
    page_size = 2


# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True) # 여러 데이터를 직렬화 할 때 many=True
#         # MovieSerializer에 파이썬 객체 형태의 데이인 movies를 넣어 주면 데이터가
#         # 딕셔너리 형태로 바뀜 -> 변환된 데이터에는 serializer.data 로 접근 할 수 있음
        
#         # Response 는 DRF에서 제공 -> 파이썬 딕셔너리로 변환된 데이터는 Response 에서 JSON 형태로 바뀜
#         return Response(serializer.data, status=200)
    
#     elif request.method == 'POST':
#         # POST 요청으로 전달된 데이터는 request.data로 접근
#         data = request.data
#         serializer = MovieSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 위의 코드를 클래스형 뷰로 변환
# class MovieList(APIView):
#     # 클래스에 함수를 추가하는 것이기 때문에 반드시 self를 첫 번째 파라미터로 받아야함
#     def get(self, request):
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
        
#     def post(self, request):
#         serializer = MovieSerializer(data=request.data)
        
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# 위의 코드를 제네릭 뷰로 변환
class MovieList(ListCreateAPIView):
    # queryset, serializer_class는 필수 옵션
    # queryset은 GET 요청을 처리할 때 돌려줄 객체들을 지정
    queryset = Movie.objects.all()
    # serializer_class는 조회와 생성 시 사용할 시리얼라이저 설정하는 옵션
    serializer_class = MovieSerializer
    # 페이지네이션 설정 추가 (이렇게 넣어 주면 기존의 전역 페이지네이션 설정 값은 무시)
    pagination_class = MoviepageNumberPagination


# GET (특정한 영화 데이터 조회), PATCH (특정한 영화 데이터 수정), DELETE (특정한 영화 데이터 삭제)
# @api_view(['GET', 'PATCH', 'DELETE'])
# def movie_detail(request, pk):
    
#     movie = get_object_or_404(Movie, pk=pk) # 함수의 첫 번째 파라미터로는 조회할 모델, 두 번째 파라미터로는 조회할 pk값
#     # 존재하지 않는 데이터를 요청하면 get_object_or_404() 함수는 이런 상황에 자동으로 404 에러 발생시킴
#     if request.method == 'GET':
#         serializer = MovieSerializer(movie) # 오직 1개의 데이터를 조회하기 때문에 many옵션 필요 없음
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     elif request.method == 'PATCH':
#         # 부분 데이터 수정이기 때문에 partial=True, 
#         # 모든 데이터를 수정하는 PUT 요청이면 partial 옵션 사용x
#         serializer = MovieSerializer(movie, data=request.data, partial=True)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         movie.delete()
#         # 데이터가 삭제되면 반환할 데이터가 없기 때문에 204 반환
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class MovieDetail(APIView):
#     def get_object(self, pk):
#         movie = get_object_or_404(Movie, pk=pk)
#         return movie

#     def get(self, request, pk):
#         movie = self.get_object(pk)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)

#     def patch(self, request, pk):
#         movie = self.get_object(pk)
#         serializer = MovieSerializer(movie, data=request.data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         movie = self.get_object(pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# 위의 코드를 제네릭 뷰 RetrieveUpdateDestroyAPIView 를 사용
class MovieDetail(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer



# 개별 페이지네이션 설정
class ActorpageNumberPagination(PageNumberPagination):
    page_size = 5



# @api_view(['GET', 'POST'])
# def actor_list(request):
#     if request.method == 'GET':
#         actors = Actor.objects.all()
#         serializer = ActorSerializer(actors, many=True)
#         return Response(serializer.data, status=200)

#     elif request.method == 'POST':
#         data = request.data
#         serializer = ActorSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class ActorList(APIView):
#     def get(self, request):
#         actors = Actor.objects.all()
#         serializer = ActorSerializer(actors, many=True)
#         return Response(serializer.data, status=200)
    
#     def post(self, request):
#         serializer = MovieSerializer(data = request.data)
        
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# 위의 코드를 제네릭 뷰로 변환
class ActorList(ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    pagination_class = ActorpageNumberPagination




# @api_view(['GET', 'PATCH', 'DELETE'])
# def actor_detail(request, pk):
#     actor = get_object_or_404(Actor, pk=pk)
    
#     if request.method == 'GET':
#         serializer = ActorSerializer(actor)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     elif request.method == 'PATCH':
#         serializer = ActorSerializer(actor, data=request.data, partial=True)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         actor.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class ActorDetail(APIView):
#     def get_object(self, pk):
#         actor = get_object_or_404(Actor, pk=pk)
#         return actor
    
#     def get(self, request, pk):
#         actor = self.get_object(pk)
#         serializer = ActorSerializer(actor)
#         return Response(serializer.data)
    
#     def patch(self, request, pk):
#         actor = self.get_object(pk)
#         serializer = ActorSerializer(actor, data=request.data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         actor = self.get_object(pk)
#         actor.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class ActorDetail(RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    


# @api_view(['GET', 'POST'])
# def review_list(request, pk):
#     movie = get_object_or_404(Movie, pk=pk)
    
#     if request.method == 'GET':
#         # movie=movie 를 전달하여 영화 ID 기준으로 작성된 리뷰 데이터를 가지고 올 수 있음
#         reviews = Review.objects.filter(movie=movie)
#         serializer = ReviewSerializer(reviews, many=True)
        
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     elif request.method == 'POST':
#         serializer = ReviewSerializer(data=request.data)
        
#         if serializer.is_valid():
#             # ReviewSerializer 에서 영화 데이터를 직접 입력 받지 않고 URL에서 pk 값을 기준으로
#             # 입력 받기 때문에 save()에 movie 를 전달한 것
#             serializer.save(movie=movie)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# 위의 코드를 제네릭 뷰로 수정
class ReviewList(ListCreateAPIView):
    serializer_class = ReviewSerializer

    # 이번에는 특정 영화를 먼저 가져오고, 영화로 리뷰를 필터해야 되기 때문에 get_queryset() 함수 사용
    def get_queryset(self):
        # URL로부터 받은 pk 값은 self.kwargs로 접근
        movie = get_object_or_404(Movie, pk=self.kwargs.get('pk'))
        return Review.objects.filter(movie=movie)

    def perform_create(self, serializer):
        movie = get_object_or_404(Movie, pk=self.kwargs.get('pk'))
        serializer.save(movie=movie)
