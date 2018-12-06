import random

import requests
from django.core.cache import cache

from worker import call_by_worker
from worker import celery_app

def gen_verify_code(length=6):
    return random.randrange(10 **(length-1),10 **length)



@call_by_worker
def send_verify_code(phonenum):
    vcode = gen_verify_code()
    key = 'VerifyCode-%s' % phonenum
    cache.set(key,vcode,120)
    sms_cfg = config.HY_SMS_PARAMS.copy()
    sms_cfg['content'] = sms_cfg['content'] % vcode
    sms_cfg['mobile'] = phonenum
    response = requests.post(config.HY_SMS_URL,data=sms_cfg)
    return  response


def check_vcode(phonenum,vcode):
    key = 'VerifyCode-%s' % phonenum
    saved_vcode = cache.get(key)
    return saved_vcode ==  vcode