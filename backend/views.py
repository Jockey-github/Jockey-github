from django.shortcuts import render

# Create your views here.
from backend.models import Mock
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.core import serializers
import json


def index(request):
    """网站的主页"""
    return render(request, 'index.html')

@require_http_methods(["GET"])
def add_mock(request):
    response = {}
    try:
        mock = Mock(mock_name = request.GET.get('mock_name'))
        mock.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

@require_http_methods(["GET"])
def show_mock(request):
    response = {}
    try:
        mock = Mock.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", mock))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)