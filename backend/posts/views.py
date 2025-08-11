from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
        "title": "Home",
        "content": "This is the home page",
    }
    return render(request, "home.html", context)

# https://www.domain-name.com        =>  landing page
# https://www.domain-name.com/path   =>  spacial page

# PATH EX:  videos/cartoons/1
#           subjects/languages/english/a1-c2/spaking/1

# SCENARIO WITH USER
# 1. The user enters url to the browser and visits the site
# 2. The request comes to django and URLS.PY recieves it
# 3. URLS.PY checks the path and correctly identifies the view function
# 4. URLS.py passes the request to the fn and VIEWS.PY's fn creates 
#                                           a logical-response
# 5. The response is sent back to the user's browser