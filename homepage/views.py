from django.shortcuts import render

# Create your views here.
def landing_page(request):
    if str(request.user)!="AnonymousUser":
        #redirect to homepage
        print('user found ',request.user)
    context ={
        'title':'Login | Register'
    }
    return render(request,"homepages/landing_page.html",context)