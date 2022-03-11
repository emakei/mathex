from django.http import JsonResponse

def index(request):

    data = []
    
    a = int(request.GET.get('a', 0))
    b = int(request.GET.get('b', 0))
    c = int(request.GET.get('c', 0))

    d = b**2 - 4*a*c

    if d == 0:
        x = -b / (2*a)
        data.append(x)
    elif d > 0:
        x1 = (-b + d**0.5) / (2*a)
        x2 = (-b - d**0.5) / (2*a)
        data.append(x1)
        data.append(x2)

    return JsonResponse(data, safe=False)