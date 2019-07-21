import datetime
from datetime import timedelta
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from home.models import Match
from home.jackpot import possible_combinations
from django.http import HttpResponse


def topnavselector():
    date = datetime.date.today() # to get current date yy-mm-dd
    return date

def all_games(request):
    today, request_from, match_date = updater(request)
    games = Match.objects.all()
    return render(request, 'mysite/index.html',
                  {"games": games, "request_tom": request_from, "match_date": match_date})
def updater(request):
    if request.path == "/" or request.path == "/goalgoal/" or request.path == "/goalgoal/today/" or request.path == "/featured/" or request.path == "/featured/today/" or request.path == "/over/" or request.path == "/over/today/":
        today = topnavselector()
        request_from = 'today'
    elif request.path == "/tomorrow/" or request.path == "/goalgoal/tomorrow/" or request.path == "/featured/tomorrow/" or request.path == "/over/tomorrow/":
        today = topnavselector() + timedelta(days=1)
        request_from = 'tomorrow'
    elif request.path == "/yesterday/" or request.path == "/goalgoal/yesterday/" or request.path == "/featured/yesterday/" or request.path == "/over/yesterday/":
        today = topnavselector() + timedelta(days=-1)
        request_from = 'yesterday'
    match_date = today.strftime("%d-%m").replace('-', '/')  # date when the match is played in / formart
    return [today, request_from, match_date]

# 
# def goal_Goal(request):
#     today, request_from, match_date =updater(request)
#     games = TipGG.objects.filter(match_date=today).order_by('time', 'teams')
#     return render(request, 'mysite/goalgoal.html', {
#         "games": games, "request_tom": request_from, "match_date": match_date
#         })
#
# def featured(request):
#     today, request_from, match_date = updater(request)
#     games = Featured.objects.filter(match_date=today).order_by('time', 'teams')
#     return render(request, 'mysite/featured.html', {
#         "games": games, "request_tom": request_from, "match_date": match_date
#         })
#
#
# def jackpot(request):
#     games = possible_combinations(['Kenya - Germany', 'Spain - Italia', 'Brazil - Spain'])
#     # print (len(games))
#     return render(request, 'mysite/jackpot.html', {
#         "games": games
#         })
#
# def over(request):
#     today, request_from, match_date = updater(request)
#     over15 = Over15.objects.filter(match_date=today).order_by('time', 'teams')
#     over25 = Over25.objects.filter(match_date=today).order_by('time', 'teams')
#     over35 = Over35.objects.filter(match_date=today).order_by('time', 'teams')
#     return render(request, 'mysite/over.html', {'over15': over15, 'over25': over25,'over35': over35, 'request_tom': request_from, 'match_date': match_date})


# def game_detail(request, pk):
#     games_detail = get_object_or_404(AllGames, pk=pk)
#     return render(request, 'mysite/game_details.html', {'game': games_detail})
# no risk no reward


def comingsoon(request):
    return render(request, 'mysite/comingsoon.html')


def login(request):
    return render(request, 'mysite/login.html')


def error_404(request):
    data = {}
    return render(request, 'mysite/error_404.html', {'data': data})


def error_500(request):
    data = {}
    return render(request, 'mysite/error_505.html', {'data': data})
