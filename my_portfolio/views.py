from django.shortcuts import render


def aboutt(request):
    return render(request, 'aboutt.html')


def experience(request):
    return render(request, 'experience.html')


def education(request):
    return render(request, 'education.html')


def skills(request):
    return render(request, 'skills.html')


def interests(request):
    return render(request, 'interests.html')


def family(request):
    return render(request, 'family.html')
