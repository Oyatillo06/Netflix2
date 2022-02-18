from django.contrib.postgres.search import TrigramSimilarity
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Movie,Actor,Comment
from .serializers import ActorSerializer, MovieSerializer,CommentSerializer


class Home(APIView):
    def get(self,request):
        xabar={"message":"Hello world"}
        return JsonResponse(xabar)
# class ActorAPIView(APIView):

    # def get(self,request):
    #     actors=Actor.objects.all()
    #     ser=ActorSerializer(actors,many=True)
    #     return Response(ser.data)
    # def post(self,request):
    #     aktyor=request.data
    #     ser=ActorSerializer(data=aktyor)
    #     if ser.is_valid():
    #         ser.save()
    #     return Response(ser.data)
    # def delete(self,request,pk):
    #     aktyor=Actor.objects.get(id=pk)
    #     aktyor.delete()
    #     return JsonResponse({"xabar":"Ohirildi"})
    # def put(self,request,pk):
    #     aktyor=Actor.objects.get(id=pk)
    #     ser=ActorSerializer(aktyor,data=request.data)
    #     if ser.is_valid():
    #         ser.save()
    #         return Response(ser.data)
    #     return JsonResponse({"xabar":"Ozkartirildi"})
# class MovieAPIView(APIView):
#     def get(self,request):
#         movie=Movie.objects.all()
#         ser=MovieSerializer(movie,many=True)
#         return Response(ser.data)
#     def post(self,request):
#         movie=request.data
#         ser=MovieSerializer(data=movie)
#         if ser.is_valid():
#             ser.save()
#         return Response(ser.data)
#     def delete(self,request,pk):
#         movie=Movie.objects.get(id=pk)
#         movie.delete()
#         return JsonResponse({"xabar":"Ohirildi"})
#     def put(self,request,pk):
#         movie=Movie.objects.get(id=pk)
#         ser=MovieSerializer(movie,data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data)
#         return JsonResponse({"xabar":"Ozkartirildi"})
class ActorViewSet(ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

    def get_queryset(self):
        actors = Actor.objects.all()
        soz = self.request.query_params.get("search")
        if soz is not None:
            actors = Actor.objects.annotate(
                similarity=TrigramSimilarity("ism", soz)
            ).filter(similarity__gte=0.7).order_by("-similarity")
        return actors

    @action(detail=True,methods=['GET'])
    def movies(self,request,*args,**kwargs):
        actor=self.get_object()
        movie=Movie.objects.filter(actor=actor)
        ser=MovieSerializer(movie,many=True)
        return Response(ser.data)

    @action(detail=True, methods=['POST'])
    def movi(self, request, *args, **kwargs):
        actor = self.get_object()
        ser = MovieSerializer(data=request.data, many=True)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)



class MovieViewSet(ModelViewSet):
    queryset=Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [SearchFilter, ]
    search_fields = ["nom", ]
    @action(detail=True,methods=["GET"])
    def actors(self,request,*args,**kwargs):
        movie=self.get_object()
        actor=Actor.objects.filter(movie=movie)
        ser=ActorSerializer(actor,many=True)
        return Response(ser.data)
    @action(detail=True,methods=['POST'])
    def ators(self,request,*args,**kwargs):
        movie=self.get_object()
        ser=ActorSerializer(data=request.data,many=True)
        if ser.is_valid():
            ser.save()
        return Response(ser.data)
class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    @action(detail=True,methods=['GET'])
    def movies(self,request,*args,**kwargs):
        coment=self.get_object()
        movie = Movie.objects.filter(coment=coment)
        ser = MovieSerializer(movie, many=True)
        return Response(ser.data)





