from .models import SayHello
from .serializers import SayHelloSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response


@csrf_exempt
def hello(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        hello = SayHello.objects.all()
        serializer = SayHelloSerializer(hello, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SayHelloSerializer(data=data)
        if serializer.is_valid():
            print("SSSS", serializer)

            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
