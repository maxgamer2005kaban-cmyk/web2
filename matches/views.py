from django.shortcuts import render

# Create your views here.
def matches_detail(request, match_id):
    return render(request, 'matches/match_detail.html')

def matches_main_page(requests):
    return render(requests, 'matches/matches_main_page.html')