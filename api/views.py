from django.http.response import HttpResponse
from.models import Book
from rest_framework.response import Response
from .serializers import BookSerializer
from rest_framework.generics import GenericAPIView
from django.db.models import Q
import random

class BookDetails(GenericAPIView):
    serializer_class = BookSerializer
    def get(self, request, slug):
        queryset = Book.objects.get(slug=slug)
        serializer = BookSerializer(queryset)
        return Response(serializer.data)

class BookView(GenericAPIView):
    serializer_class = BookSerializer
    def get(self, request):
        """
        All the books 👇🏼⬇️
        -
        """
        queryset = Book.objects.all()
        serializer_class = BookSerializer(queryset, many=True)
        return Response(serializer_class.data)

    def post(self, request):
        """
        Add a book you want to sell
        -
        """
        data = request.data
        obj = Book.objects.create(user=request.user, name=data["name"], price=data["price"], text=data["text"], slug= str(random.randint(1, 99999))[:16], image=data["image"])
        serializer_class = BookSerializer(obj, many=True)
        return HttpResponse("Done")

class BookDelete(GenericAPIView):
    def post(self, request, slug):
        obj = Book.objects.get(Q(slug=slug))
        obj.delete()
        return HttpResponse("Done")

class BookEdit(GenericAPIView):
    serializer_class = BookSerializer
    def patch(self, request, slug):
        data = request.data
        obj = Book.objects.get(Q(slug=slug))
        x = BookSerializer(obj, data=request.data)
        if x.is_valid():
            x.save()
        return HttpResponse("Done")