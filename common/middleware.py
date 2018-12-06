from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

from user.models import User
from lib.http import render_json
from common import error


class AuthMiddleware(MiddlewareMixin):
    WHITE_LIST = [
        'api/user/verify',
        'api/user/login',
    ]

    def process_request(self,request):
        for path in self.WHITE_LIST:
            if request.path.startswith(path):
                return

    def process_request(self,request):
        uid = request.session.get('uid')
        if uid:
            try:
                request.user = User.objects.get(id=uid)
                return
            except User.DoesNotExist:
                request.session.flush()
        return render_json(None,code=error.LOGIN_ERROR)

