from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json
from gossip_api.services.main import res_overview


@api_view(["POST"])
def overview(request):
  if request.method == "POST":
    try:
      user = request.data
      print(user)
      url = user.get("url")
      web_source = user.get("source") or None     
      if url:
          res = res_overview(url, web_source)
          print(type(res))
          res_dict = json.loads(res)
          print(res_dict)
          return JsonResponse(res_dict, status=status.HTTP_200_OK)
      else:
           return JsonResponse({"error": "URL is required."}, status=status.HTTP_400_BAD_REQUEST)
    except json.JSONDecodeError:
      return JsonResponse({"error": "Invalid JSON format."}, status=status.HTTP_400_BAD_REQUEST)
