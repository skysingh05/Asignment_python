from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import App
import json

@csrf_exempt
def add_app(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            app = App.objects.create(
                app_name=data.get("app_name"),
                version=data.get("version"),
                description=data.get("description")
            )
            return JsonResponse({"id": app.id, "message": "App created"}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    else:
        # Return a response for GET requests
        return JsonResponse({"error": "Method not allowed. Please use POST."}, status=405)



def get_app(request, id):
    try:
        app = App.objects.get(id=id)
        return JsonResponse({
            "app_name": app.app_name,
            "version": app.version,
            "description": app.description
        })
    except App.DoesNotExist:
        return JsonResponse({"error": "App not found"}, status=404)

@csrf_exempt
def delete_app(request, id):
    if request.method == "DELETE":
        try:
            app = App.objects.get(id=id)  # Query by app_name
            app.delete()
            return JsonResponse({"message": "App deleted"}, status=204)
        except App.DoesNotExist:
            return JsonResponse({"error": "App not found"}, status=404)
    else:
        return JsonResponse({"error": "Method not allowed"}, status=405)
