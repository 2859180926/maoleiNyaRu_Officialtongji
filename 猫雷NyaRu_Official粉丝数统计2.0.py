import requests as req

from time import strftime, localtime

import csv

from pyecharts.charts import Line
from pyecharts import options as opts

def fans(mid, name=-1):
    mid = str(mid)
    name = str(name)
    if name == -1:
        name = mid
    url = "https://api.bilibili.com/x/relation/stat?vmid=" + mid + "&jsonp=jsonp"
    resp = req.get(url)# 通过url爬取到我们想要的json数据
    info = eval(resp.text)
    print_content=strftime("%Y", localtime()) + "年" + strftime("%m", localtime()) + "月" + strftime("%d",
                                                                                           localtime()) + "日" + strftime("%H:%M:%S", localtime()) +"\n"+name + "粉丝数\n" +"本次查询："+str(
        info['data']['follower'])
    with open(name + '粉丝数统计.csv', 'a+', newline="") as f:
        f.seek(0)
        reader = [i for i in csv.reader(f)]
        datas =  [i[3] for i in reader]
        f.seek(2)
        csv_write=csv.writer(f,dialect='excel')
    
        csv_write.writerow(["猫雷粉丝", strftime("%m", localtime()) + "月" + strftime("%d", localtime()) + "日"
                             + strftime("%H:%M:%S", localtime()) ,strftime("%H:%M:%S", localtime()),
                  str(info['data']['follower']),str(int(info['data']['follower'])-int(datas[-1]))])
        # 获取data中的follower就是粉丝数啦
        #print(datas)
    print(print_content)
    print("上次查询："+str(datas[-1]))
    print("涨粉数："+str(int(info['data']['follower'])-int(datas[-1])))
          
def fans_chart(file):
    with open("猫雷NyaRu_Official粉丝数统计.csv","r") as f:
        reader = [i for i in csv.reader(f)]

        colums = [i[1] for i in reader]
        datas =  [i[3] for i in reader]
        line = (Line(init_opts=opts.InitOpts(width="2000px",height="600px"))
                .add_xaxis(colums)
                .add_yaxis("粉丝数", datas)
                .set_global_opts(xaxis_opts=opts.AxisOpts(
            name="X轴",
            axislabel_opts={"rotate":30}
             ),
            yaxis_opts=opts.AxisOpts(
                position="right",name="Y轴"),
            #datazoom_opts=opts.DataZoomOpts(),
            )
                )

        line.render("猫雷粉丝数可视化.html")
if __name__ == "__main__":
    fans(697091119, '猫雷NyaRu_Official')
    fans_chart("猫雷NyaRu_Official粉丝数统计.csv")
