# !/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :WZXY.py
# @Time      :2022/9/11 1:24
# @Author    :JefferyH
import datetime
import random

import requests
import time
import json


#    我在校园自动打卡2.0


class WAXY:
    '''
    我在校园自动打卡小程序类
    提供方法：登录（login），打卡（Post）,获取batch_id(getSchoolinfo)
    '''

    def __init__(self,username,password,location):
        '''

        :param username: 打卡账号（我在校园手机号）
        :param password: 打卡密码
        :param location: 打卡地址
        '''
        self.username=username
        self.password=password
        self.infoUrl='https://gw.wozaixiaoyuan.com/basicinfo/mobile/my/index'
        self.loginUrl=f'https://gw.wozaixiaoyuan.com/basicinfo/mobile/login/username?username={self.username}&password={self.password}'
        self.getInfoUrl='https://gw.wozaixiaoyuan.com/health/mobile/health/getBatch'
        self.shcoolId=''
        self.location=location
        self.betchUrl='https://gw.wozaixiaoyuan.com/health/mobile/health/getBatch'
        self.headers={
    "Host": "gw.wozaixiaoyuan.com",
    "accept": "application/json, text/plain, */*",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; LIO-AL00 Build/HUAWEILIO-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4237 MMWEBSDK/20220709 Mobile Safari/537.36 MMWEBID/5197 MicroMessenger/8.0.25.2200(0x28001953) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 miniProgram/wxce6d08f781975d91",
    "content-type": "application/json;charset\u003dUTF-8",
    "x-requested-with": "com.tencent.mm",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "accept-encoding": "gzip, deflate",
    "accept-language": "zh-CN,zh;q\u003d0.9,ja-JP;q\u003d0.8,ja;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5",
}
    def rondomTemp(self):
        return round(random.uniform(35, 37),1)

    def login(self):
        '''
        登录
        :return:
        '''
        re=requests.get(self.loginUrl,headers=self.headers)
        # print(re.json())
        if re.json()['code']==101 or re.json()['code']==1:
            return {"mesg":-1,"data":re.json()['message']}

        self.headers = {
            "Host": "gw.wozaixiaoyuan.com",
            "accept": "application/json, text/plain, */*",
            'jwsession':re.cookies['JWSESSION'],
            "user-agent": "Mozilla/5.0 (Linux; Android 10; LIO-AL00 Build/HUAWEILIO-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4237 MMWEBSDK/20220709 Mobile Safari/537.36 MMWEBID/5197 MicroMessenger/8.0.25.2200(0x28001953) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 miniProgram/wxce6d08f781975d91",
            "content-type": "application/json;charset\u003dUTF-8",
            "x-requested-with": "com.tencent.mm",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            'referer': 'https://gw.wozaixiaoyuan.com/h5/mobile/health/index/health/detail?id=46200001',
            "accept-encoding": "gzip, deflate",
            "accept-language": "zh-CN,zh;q\u003d0.9,ja-JP;q\u003d0.8,ja;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5",
        }
        self.headers["cookie"] = 'JWSESSION=' + re.cookies['JWSESSION']
        return {"mesg":0,"data":"登陆成功"}
    def getSchoolinfo(self):
        '''
        获取batch_id
        :return:
        '''
        re=requests.get(self.getInfoUrl,headers=self.headers)
        if re.json()['code']==103:
            return "密码错误"
        self.shcoolId=re.json()['data']['list'][0]['id']
        # print(self.shcoolId)
    def getAdd(self):
        '''
        地址的逆向解析
        :return: _loc post 需要的data
        '''
        getCodeUrl=f'https://apis.map.qq.com/ws/geocoder/v1/?address={self.location}&key=WOQBZ-SK3CU-DXNVE-43DFO-6YXN3-NHF2C'
        res=requests.get(getCodeUrl)
        self.loc = res.json()['result']['location']
        url = f'https://apis.map.qq.com/ws/geocoder/v1/?location={self.loc["lat"]},{self.loc["lng"]}&key=WOQBZ-SK3CU-DXNVE-43DFO-6YXN3-NHF2C'
        ress = requests.get(url)
        self.nation_code=ress.json()['result']['ad_info']['nation_code']
        self.adcode=ress.json()['result']['ad_info']['adcode']
        self.city_code=ress.json()['result']['ad_info']['city_code']
        self.town=ress.json()['result']['address_reference']['town']['id']
        self.district=ress.json()['result']['ad_info']['district']
        self.province=ress.json()['result']['ad_info']['province']
        self.street=ress.json()['result']['address_reference']['street']['title']
        _loc=f"{ress.json()['result']['address_component']['nation']}/{ress.json()['result']['address_component']['province']}" \
             f"/{ress.json()['result']['address_component']['city']}/{ress.json()['result']['address_component']['district']}/" \
             f"{ress.json()['result']['address_reference']['town']['title']}/{ress.json()['result']['address_component']['street']}/{self.nation_code}/{self.adcode}/{self.city_code}/{self.town}"
        return _loc
    def check(self):
        '''
        获取用户基本信息
        :return: 返回用户基本信息
        '''
        try:
            re = requests.get(url=self.infoUrl, headers=self.headers)
            self.headers['referer']='https://gw.wozaixiaoyuan.com/h5/mobile/health/index/health/detail?id='+self.shcoolId
            return {"mesg": 0, 'data': {"name": re.json()['data']['name'],
                                    'class': re.json()['data']['classes'],
                                    "college": re.json()['data']['college']}}
        except Exception as e:
            self.getSchoolinfo()
            self.Post()
            return self.check()

    def Post(self):
        '''
        打卡
        这里的参数t1,t2,t3就是你们学校所设置的问题，有n个就写tn
        :return: 打卡结果
        '''

        self.postUrl = f'https://gw.wozaixiaoyuan.com/health/mobile/health/save?batch={self.shcoolId}'
        data={"location":self.getAdd(),"t1":"健康","t2":"低风险","t3":self.rondomTemp(),"t4":self.rondomTemp(),"t5":self.rondomTemp(),"type":0,"locationType":0}
        self.headers['referer']='https://gw.wozaixiaoyuan.com/h5/mobile/health/index/health/detail?id='+self.shcoolId
        re=requests.post(url=self.postUrl,headers=self.headers,json=data)
        if re.json()['code']==0:
            return {"mesg":0,"data":"打卡成功"}
        else:
            return {"mesg": -1, "data": "打卡失败"}


if __name__ == '__main__':
    username="泽塔",
    password='殴斯',
    location='M78星云'
    api = WAXY(username, password, location=location)
    api.login() #首先登录
    api.getSchoolinfo() #获取batchID
    res = api.Post() #打卡


