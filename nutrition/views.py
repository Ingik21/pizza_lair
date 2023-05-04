from django.shortcuts import render, get_object_or_404


def nutrition(request):
    return render(request, 'general/nutrition.html')
