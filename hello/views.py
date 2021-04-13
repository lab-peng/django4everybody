from django.shortcuts import render
from django.shortcuts import HttpResponse


def sessionview(request):
    visits = request.session.get('visits', 0) + 1
    request.session['visits'] = visits
    if visits > 4:
        del request.session['visits']

    response = HttpResponse(f'view count={visits}')
    response.set_cookie('dj4e_cookie', '116ce366', max_age=1000)
    return response
