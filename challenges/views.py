from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

#dict of responses for each different month
monthly_challenges ={
    "january": "Eat no meat",
    "february": "Workout everyday",
    "march": "Workout everyday",
    "april": "Eat no meat",
    "may": "Workout everyday",
    "june": "Workout everyday",
    "july": "Eat no meat",
    "august": "Workout everyday",
    "september": "run everydat",
    "october": "Workout everyday",
    "november": "Eat no meat",
    "december": "Workout everyday"
   
}

# Create your views here.

#Redirect
def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("not a valid month")