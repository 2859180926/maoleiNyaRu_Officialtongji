import requests as req
from time import strftime, localtime

def fans(mid, name=-1):
    mid = str(mid)
    name = str(name)
    if name == -1:
        name = mid
    url = "https://api.bilibili.com/x/relation/stat?vmid=" + mid + "&jsonp=jsonp"
    resp = req.get(url)# 通过url爬取到我们想要的json数据
    info = eval(resp.text)
    with open(name + '粉丝数统计.txt', 'a') as f:
        f.write(strftime("%Y", localtime()) + "年" + strftime("%m", localtime()) + "月" + strftime("%d",
                                                                                                 localtime()) + "日" + strftime("%H:%M:%S", localtime())+name + "粉丝数：" + str(
            info['data']['follower']) + '\n')# 获取data中的follower就是粉丝数啦
    print(strftime("%Y", localtime()) + "年" + strftime("%m", localtime()) + "月" + strftime("%d",
                                                                                           localtime()) + "日" + strftime("%H:%M:%S", localtime()) +name + "粉丝数：" + str(
        info['data']['follower']) + '\n')

if __name__ == "__main__":
    fans(697091119, '猫雷NyaRu_Official')
