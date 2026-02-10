"""
example02 - 

Author: kaiby
Date: 2024/1/3 14:55
"""
import json

data = '''
{
  "code": 200,
  "msg": "success",
  "result": {
    "curpage": 1,
    "allnum": 3690,
    "list": [
      {
        "id": "92e5f080884dce68cbf751378a779e90",
        "ctime": "2021-02-04 19:22",
        "title": "河北三河国家农业科技园区建设农业联合体科技示范基地授牌仪式",
        "description": "河北三河国家农业科技园区举行建设三河市香丰肥业农业联合体科技示范基地授牌仪式2月4日上午，河北三河国家农业科技园区建设三河市香丰肥业农业联合体科技示范基地授...",
        "source": "农业新闻",
        "picUrl": "http://n.sinaimg.cn/sinakd202124s/161/w550h411/20210204/fce0-kirmait9302150.jpg",
        "url": "http://k.sina.com.cn/article_7452972885_1bc3b575500100uc40.html"
      },
      {
        "id": "f732f5db5bc872794e693e2f038b35e4",
        "ctime": "2021-02-04 00:00",
        "title": "投资者提问：2021年2月3日各大媒体报道了益海嘉里金龙鱼农业订单模式让...",
        "description": "投资者提问：2021年2月3日各大媒体报道了益海嘉里金龙鱼农业订单模式让农户腰包鼓了日子富了。农民交粮给金龙鱼，粮款24小时到账，比卖给粮食中介还增收了很...",
        "source": "农业新闻",
        "picUrl": "http://n.sinaimg.cn/sinakd202124s/162/w550h412/20210204/6706-kirmait9301473.jpg",
        "url": "http://finance.sina.com.cn/stock/relnews/dongmiqa/2021-02-04/doc-ikftpnny4511586.shtml"
      },
      {
        "id": "62ac899e8fcf654a74479b4239b4651f",
        "ctime": "2021-02-04 00:00",
        "title": "近日，国务院正式批复设立陕西杨凌综合保税区，全国唯一农业特色的综合保税区正...",
        "description": "近日，国务院正式批复设立陕西杨凌综合保税区，全国唯一农业特色的综合保税区正式落户杨凌。",
        "source": "农业新闻",
        "picUrl": "http://n.sinaimg.cn/sinakd20210204ac/182/w640h342/20210204/991d-kirmait9407892.jpg",
        "url": "http://finance.sina.com.cn/7x24/2021-02-04/doc-ikftpnny4511923.shtml"
      }
    ]
  }
}


'''

news_dict = json.loads(data)

for item in news_dict.get('result').get('list'):
    print(item.get('title'))
    print(item.get('url'))
