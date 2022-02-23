from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import viewsets
from app.serializer import SmsSerializer
import random,redis

# 连接redis数据库
r = redis.Redis(host="192.168.0.133",port=6379,password=123,db=0)

class PhoneSms(viewsets.ViewSet):
    def phone(self,request):
        try:
            phones = request.data
            key = phones["phone"]
            if r.get(key + "_flag"):
                return Response({"msg":"获取验证码频繁"},status=204)
            else:
                smss = random.randint(1000,9999)
                r.set(key + "_flag",1,ex = 60)
                r.set(key,smss,ex = 60)
                datas = [{"phone":key,"sms":smss}]
                ser = SmsSerializer(datas,many=True)
        except Exception as e:
            print(e)
            return Response({"msg":"Not Found"},status=404)
        else:
            return Response(ser.data)
    def smsphone(self,request):
        try:
            phones = request.data
            key = phones["phone"]
            sms = r.get(key).decode()
            if sms == None:
                return Response({"msg":"验证码失效！"},status=204)
            elif sms == phones["sms"]:
                return Response({"msg":"ok"})
        except Exception as e:
            print(e)
            return Response({"msg": "Not Found"}, status=404)
        else:
            return Response({"msg": "Not Found"}, status=404)