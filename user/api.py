

from django.shortcuts import render

from lib.http import render_json
from user.logic import send_verify_code,check_vcode
from user.models import User
from common import error
# Create your views here.

def get_verify_code(request):

    phonenum = request.GET.get('phonenum')
    send_verify_code(phonenum)

    return render_json(None,0)

def login(request):
    phonenum = request.POST.get('phonenum')
    vcode = request.POST.get('vcode')
    if check_vcode(phonenum,vcode):
        user,created = User.objects.get_or_create(phonenum=phonenum)


        request.session['uid'] = user.id
        return render_json(user.to_dict(),0)
    else:
        return render_json(None,error.VCODE_ERROR)



def get_profile(request):
    user = request.user
    return render_json(user.profile.to_dict(),0)


def modify_profile(request):
    pass



def upload_avatar(request):
    pass