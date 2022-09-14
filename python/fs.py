import time
import requests
import json
#第一步读取八行包内容
# 以下为固定内容
# POST /wisdomprovider/router? HTTP/1.1
# Content-Length: 373
# Host: wisdom.tskjxy.com.cn
# Connection: Keep-Alive
# Accept-Encoding: gzip
# content-type: application/x-www-form-urlencoded;charset=utf8
class Openua:
    config = "123"

    def __init__(self, fielname):
        file = open(fielname, 'r', encoding="UTF-8")
        self.config = file.readline().strip("\n")
        print("成功加载请求体")
        i=True
        while i:
            go = int(self.config[-10:]) - int(time.time())  # 获取开始时间,获取当前时间，得到距离开始时间

            #print("\r距离活动开始报名还有" + str(go) + "秒",end="")
            if(go<2):
                print("\t开始抢活动")
                i=False
            time.sleep(0.5)


# print(Openua("config.txt").config)
# 在这里定义访问
class gogogo:
    def __init__(self,data):
        url="http://wisdom.tskjxy.com.cn/wisdomprovider/router?"
        headers = {"POST /wisdomprovider/router? HTTP/1.1":"","Content-Length":"373","Host":"wisdom.tskjxy.com.cn","Connection":"Keep-Alive","Accept-Encoding":"gzip","content-type":"application/x-www-form-urlencoded;charset=utf8"}
        # 无限循环抢活动开始
        # 无限循环抢活动开始
        i = True
        t=0
        while i:
            t=t+1
            re = requests.post(url,headers=headers, data=data)
            re=json.loads(re.text)
            print("\r"+str(t)+"次",end="")
            # {"msg": "很抱歉，与您报名“五汶决策锻造计划第三期“普法进校园””活动有时间冲突", "code": "-1", "detailCode": "145"}
            # temp=re.text=="{\"code\":\"-1\",\"detailCode\":\"999999\"}"
            # if(re["code"]=='-1' and len(re["msg"])>5):
            #     print("抢课失败："+re["msg"])
            #     i=False
            # elif(re["code"]=='-1'):
            #     print("\r抢课未成功-第"+str(t)+"次",end="")
            # elif(re["code"]!='-1'):
            #     print(str(t)+"次抢课成功")
            #     i=False
            time.sleep(0.01)
            if (re["code"] != '-1'):
             print(str(t)+"次抢课成功")
             i=False

print(gogogo(Openua("config.txt").config))

# print(gogogo("anonymousId=53e9c2e2-36cf-466a-9be0-b06e13e28914&method=wisdom.extra.activity.signUpPersonalInit&roleId=51e34772-7993-435c-9079-fd291365cda8&format=json&sign=4973381D3014B12F31EC68C9676A897583A58DA5&tenantCode=tskjxy&userId=53e9c2e2-36cf-466a-9be0-b06e13e28914&deviceId=218d5804335dede9&v=2.0&appKey=00000001&taskId=a580513c-93f1-4a7e-99b1-816280907441&timestamp=1663113600"))