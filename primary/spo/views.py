import os
import time
from django.http import JsonResponse

def index(request):
    service_name = os.environ.get("SERVICE_NAME", "unknown")
    if service_name == "primary":
        time.sleep(2)  # имитируем задержку
    return JsonResponse({"service": service_name})