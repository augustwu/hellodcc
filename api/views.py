# Create your views here.
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from urllib.parse import urlsplit, parse_qs

class HelloWorldView(APIView):


    def get(self,request):
        url = request.build_absolute_uri()
        query = urlsplit(url).query
        params = parse_qs(query)
        resp = {k: v[0] for k, v in params.items()}

        return Response(resp)
