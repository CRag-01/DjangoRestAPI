from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    return JsonResponse({"message":"Hi there, This is your Django API response!"})

