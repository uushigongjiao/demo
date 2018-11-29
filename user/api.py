from django.shortcuts import render


from user.logic import send_verify_code
# Create your views here.

def get_verify_code(request):

    phonenum = request.GET.get('phonenum')
    send_verify_code(phonenum)

    pass

def login(request):
    pass


def get_profile(request):
    pass


def modify_profile(request):
    pass



def upload_avatar(request):
    pass