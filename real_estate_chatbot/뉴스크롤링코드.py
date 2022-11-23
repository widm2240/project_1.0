# -*- coding: utf-8 -*-
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

## 부동산

# 라이브러리 불러오기
import requests
from bs4 import BeautifulSoup

# 네이버 주요 뉴스 텍스트, 이미지, URL 가져오기
def naver_sites_all(url):
  global MainNewsText01
  global MainNewsText02
  global MainNewsUrl01
  global MainNewsUrl02
  global MainNewsImg01
  global MainNewsImg02 
  response = requests.request("GET", url)
  soup = BeautifulSoup(response.content,'html.parser')
  titles = soup.select("ul.headline_list dt a")[:4]
  titles2 = soup.select("dt.photo a")[:2] 
  news_thumbnail = soup.select('dt.photo img')[:2]
  places_title = []
  places_url= []
  link_thumbnail = []

  for one in titles:
    if one.string != None:
      places_title.append(one.string)
  for i in places_title[:1]:
    MainNewsText01 = i
  for i in places_title[1:2]:
    MainNewsText02 = i

  for i in titles2:
    places_url.append("https://land.naver.com"+i.attrs["href"])
  for i in places_url[:1]:
    MainNewsUrl01 = i
  for i in places_url[1:2]:
    MainNewsUrl02 = i

  for img in news_thumbnail:
    link_thumbnail.append(img.attrs['src'])
  for i in link_thumbnail[:1]:
    MainNewsImg01 = i
  for i in link_thumbnail[1:2]:
    MainNewsImg02 = i

# 주요 뉴스 스킬
@app.route('/api/sayMainNews', methods=['POST'])
def sayMainNews():
    body = request.get_json()
    print(body)
    print(body['userRequest']['utterance'])

    url = "https://land.naver.com/news/headline.naver"
    naver_sites_all(url)

    responseMain = {
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "listCard": {
          "header": {
            "title": "주요 뉴스"
          },
          "items": [
            {
              "title": f"{MainNewsText01}",
              "imageUrl": f"{MainNewsImg01}",
              "link": {
                "web": f"{MainNewsUrl01}"
              }
            },
            {
              "title": f"{MainNewsText02}",
              "imageUrl": f"{MainNewsImg02}",
              "link": {
                "web": f"{MainNewsUrl02}"
              }
            },
           ],
          "buttons": [
            {
              "label": "뒤로 가기",
              "action": "block",
              "blockId": "636b35e4af8d760349365f56"
            },
            {
              "label": "더보기",
              "action": "webLink",
              "webLinkUrl": url
            }         
          ]
        }
      }
    ]
  }
}

    return responseMain

# 핫이슈 텍스트, 이미지, URL 가져오기
def naver_hotissue_all(url):
  global HotIssueText01
  global HotIssueText02
  global HotIssueUrl01
  global HotIssueUrl02
  global HotIssueImg01
  global HotIssueImg02
  response = requests.request("GET", url)
  soup = BeautifulSoup(response.content,'html.parser')
  titles = soup.select("div.hot_list strong")[:4]
  titles2 = soup.select("dt.photo a")[:2]
  news_thumbnail = soup.select('dt.photo img')[:2]
  places_title = []
  places_url=[]
  link_thumbnail = []

  for one in titles:
    if one.string != None:
      places_title.append(one.string)
  for i in places_title[:1]:
    HotIssueText01 = i
  for i in places_title[1:2]:
    HotIssueText02 = i

  for i in titles2:
    places_url.append("https://land.naver.com"+i.attrs["href"])
  for i in places_url[:1]:
    HotIssueUrl01 = i
  for i in places_url[1:2]:
    HotIssueUrl02 = i

  for img in news_thumbnail:
    link_thumbnail.append(img.attrs['src'])
  for i in link_thumbnail[:1]:
    HotIssueImg01 = i
  for i in link_thumbnail[1:2]:
    HotIssueImg02 = i

# 핫이슈 스킬
@app.route('/api/sayHotIssue', methods=['POST'])
def sayHotIssue():
    body = request.get_json()
    print(body)
    print(body['userRequest']['utterance'])

    url = "https://land.naver.com/news/hotIssue.naver"
    naver_hotissue_all(url)

    responseHotIssue = {
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "listCard": {
          "header": {
            "title": "핫이슈"
          },
          "items": [
            {
              "title": f"{HotIssueText01}",
              "imageUrl": f"{HotIssueImg01}",
              "link": {
                "web": f"{HotIssueUrl01}"
              }
            },
            {
              "title": f"{HotIssueText02}",
              "imageUrl": f"{HotIssueImg02}",
              "link": {
                "web": f"{HotIssueUrl02}"
              }
            },
           ],
          "buttons": [
            {
              "label": "뒤로 가기",
              "action": "block",
              "blockId": "636b35e4af8d760349365f56"
            },
            {
              "label": "모바일로 보기",
              "action": "webLink",
              "webLinkUrl": "https://m2.land.naver.com/news/hotissue"
            }         
          ]
        }
      }
    ]
  }
}

    return responseHotIssue

## 지역별 뉴스

# 지역별 뉴스 텍스트, 이미지, URL 가져오기
def naver_region_all(url):
  global RegionImg01
  global RegionImg02
  global RegionText01
  global RegionText02
  global RegionUrl01
  global RegionUrl02

  response = requests.request("GET", url)
  soup = BeautifulSoup(response.content,'html.parser')
  news_thumbnail = soup.select('dt.photo img')[:2]
  titles = soup.select("div.section_headline dt a")[:4]
  titles2 = soup.select("dt.photo a")[:2]
  places_url=[]  
  places_title = []
  link_thumbnail = []

  for img in news_thumbnail:
      link_thumbnail.append(img.attrs['src'])
  for i in link_thumbnail[:1]:
    RegionImg01 = i
  for i in link_thumbnail[1:2]:
    RegionImg02 = i

  for one in titles:
    if one.string != None:
      places_title.append(one.string)
  for i in places_title[:1]:
    RegionText01 = i
  for i in places_title[1:2]:
    RegionText02 = i

  for i in titles2:
    places_url.append("https://land.naver.com"+i.attrs["href"])
  for i in places_url[:1]:
    RegionUrl01 = i
  for i in places_url[1:2]:
    RegionUrl02 = i

# 서울 스킬
@app.route('/api/saySeoul', methods=['POST'])
def saySeoul():
    body = request.get_json()
    print(body)
    print(body['userRequest']['utterance'])

    Seoul = "https://land.naver.com/news/region.naver?city_no=1100000000&dvsn_no="
    naver_region_all(Seoul)

    responseSeoul = {
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "listCard": {
          "header": {
            "title": "서울특별시 뉴스"
          },
          "items": [
            {
              "title": f"{RegionText01}",
              "imageUrl": f"{RegionImg01}",
              "link": {
                "web": f"{RegionUrl01}"
              }
            },
            {
              "title": f"{RegionText02}",
              "imageUrl": f"{RegionImg02}",
              "link": {
                "web": f"{RegionUrl02}"
              }
            },
           ],
          "buttons": [
            {
              "label": "뒤로 가기",
              "action": "block",
              "blockId": "636b36be0abf120ff67a4ddc"
            },
            {
              "label": "더보기",
              "action": "webLink",
              "webLinkUrl": Seoul
            }
          ]
        }
      }
    ]
  }
}

    return responseSeoul

# 경기 스킬
@app.route('/api/sayGyeonggi', methods=['POST'])
def sayGyeonggi():
    body = request.get_json()
    print(body)
    print(body['userRequest']['utterance'])

    Gyeonggi = "https://land.naver.com/news/region.naver?city_no=4100000000&dvsn_no="
    naver_region_all(Gyeonggi)

    responseGyeonggi = {
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "listCard": {
          "header": {
            "title": "경기도 뉴스"
          },
          "items": [
            {
              "title": f"{RegionText01}",
              "imageUrl": f"{RegionImg01}",
              "link": {
                "web": f"{RegionUrl01}"
              }
            },
            {
              "title": f"{RegionText02}",
              "imageUrl": f"{RegionImg02}",
              "link": {
                "web": f"{RegionUrl02}"
              }
            },
           ],
          "buttons": [
            {
              "label": "뒤로 가기",
              "action": "block",
              "blockId": "636b36be0abf120ff67a4ddc"
            },
            {
              "label": "더보기",
              "action": "webLink",
              "webLinkUrl": Gyeonggi
            }
          ]
        }
      }
    ]
  }
}

    return responseGyeonggi

# 인천 스킬
@app.route('/api/sayIncheon', methods=['POST'])
def sayIncheon():
    body = request.get_json()
    print(body)
    print(body['userRequest']['utterance'])

    Incheon = "https://land.naver.com/news/region.naver?city_no=2800000000&dvsn_no="
    naver_region_all(Incheon)

    responseIncheon = {
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "listCard": {
          "header": {
            "title": "인천 뉴스"
          },
          "items": [
            {
              "title": f"{RegionText01}",
              "imageUrl": f"{RegionImg01}",
              "link": {
                "web": f"{RegionUrl01}"    
              }
            },
            {
              "title": f"{RegionText02}",
              "imageUrl": f"{RegionImg02}",
              "link": {
                "web": f"{RegionUrl02}"
              }
            },
           ],
          "buttons": [
            {
              "label": "뒤로 가기",
              "action": "block",
              "blockId": "636b36be0abf120ff67a4ddc"
            },
            {
              "label": "더보기",
              "action": "webLink",
              "webLinkUrl": Incheon
            }
          ]
        }
      }
    ]
  }
}

    return responseIncheon

# 부산 스킬
@app.route('/api/sayBusan', methods=['POST'])
def sayBusan():
    body = request.get_json()
    print(body)
    print(body['userRequest']['utterance'])

    Busan = "https://land.naver.com/news/region.naver?city_no=2600000000&dvsn_no="
    naver_region_all(Busan)

    responseBusan = {
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "listCard": {
          "header": {
            "title": "부산 뉴스"
          },
          "items": [
            {
              "title": f"{RegionText01}",
              "imageUrl": f"{RegionImg01}",
              "link": {
                "web": f"{RegionUrl01}"
              }
            },
            {
              "title": f"{RegionText02}",
              "imageUrl": f"{RegionImg02}",
              "link": {
                "web": f"{RegionUrl02}"
              }
            },
           ],
          "buttons": [
            {
              "label": "뒤로 가기",
              "action": "block",
              "blockId": "636b36be0abf120ff67a4ddc"
            },
            {
              "label": "더보기",
              "action": "webLink",
              "webLinkUrl": Busan
            }
          ]
        }
      }
    ]
  }
}

    return responseBusan

# 대전 스킬
@app.route('/api/sayDaejeon', methods=['POST'])
def sayDaejeon():
    body = request.get_json()
    print(body)
    print(body['userRequest']['utterance'])

    Daejeon = "https://land.naver.com/news/region.naver?city_no=3000000000&dvsn_no="
    naver_region_all(Daejeon)

    responseDaejeon = {
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "listCard": {
          "header": {
            "title": "대전 뉴스"
          },
          "items": [
            {
              "title": f"{RegionText01}",
              "imageUrl": f"{RegionImg01}",
              "link": {
                "web": f"{RegionUrl01}"
              }
            },
            {
              "title": f"{RegionText02}",
              "imageUrl": f"{RegionImg02}",
              "link": {
                "web": f"{RegionUrl02}"
              }
            },
           ],
          "buttons": [
            {
              "label": "뒤로 가기",
              "action": "block",
              "blockId": "636b36be0abf120ff67a4ddc"
            },
            {
              "label": "더보기",
              "action": "webLink",
              "webLinkUrl": Daejeon
            }
          ]
        }
      }
    ]
  }
}

    return responseDaejeon

# 대구 스킬
@app.route('/api/sayDae_gu', methods=['POST'])
def sayDae_gu():
    body = request.get_json()
    print(body)
    print(body['userRequest']['utterance'])

    Dae_gu = "https://land.naver.com/news/region.naver?city_no=2700000000&dvsn_no="
    naver_region_all(Dae_gu)

    responseDae_gu = {
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "listCard": {
          "header": {
            "title": "대구 뉴스"
          },
          "items": [
            {
              "title": f"{RegionText01}",
              "imageUrl": f"{RegionImg01}",
              "link": {
                "web": f"{RegionUrl01}"
              }
            },
            {
              "title": f"{RegionText02}",
              "imageUrl": f"{RegionImg02}",
              "link": {
                "web": f"{RegionUrl02}"
              }
            },
           ],
          "buttons": [
            {
              "label": "뒤로 가기",
              "action": "block",
              "blockId": "636b36be0abf120ff67a4ddc"
            },
            {
              "label": "더보기",
              "action": "webLink",
              "webLinkUrl": Dae_gu
            }
          ]
        }
      }
    ]
  }
}

    return responseDae_gu

# 울산 스킬
@app.route('/api/sayUlsan', methods=['POST'])
def sayUlsan():
    body = request.get_json()
    print(body)
    print(body['userRequest']['utterance'])

    Ulsan = "https://land.naver.com/news/region.naver?city_no=3100000000&dvsn_no="
    naver_region_all(Ulsan)

    responseUlsan = {
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "listCard": {
          "header": {
            "title": "울산 뉴스"
          },
          "items": [
            {
              "title": f"{RegionText01}",
              "imageUrl": f"{RegionImg01}",
              "link": {
                "web": f"{RegionUrl01}"
              }
            },
            {
              "title": f"{RegionText02}",
              "imageUrl": f"{RegionImg02}",
              "link": {
                "web": f"{RegionUrl02}"
              }
            },
           ],
          "buttons": [
            {
              "label": "뒤로 가기",
              "action": "block",
              "blockId": "636b36be0abf120ff67a4ddc"
            },
            {
              "label": "더보기",
              "action": "webLink",
              "webLinkUrl": Ulsan
            }
          ]
        }
      }
    ]
  }
}

    return responseUlsan

# 세종 스킬
@app.route('/api/saySejong', methods=['POST'])
def saySejong():
    body = request.get_json()
    print(body)
    print(body['userRequest']['utterance'])

    Sejong = "https://land.naver.com/news/region.naver?city_no=3600000000&dvsn_no="
    naver_region_all(Sejong)

    responseSejong = {
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "listCard": {
          "header": {
            "title": "세종 뉴스"
          },
          "items": [
            {
              "title": f"{RegionText01}",
              "imageUrl": f"{RegionImg01}",
              "link": {
                "web": f"{RegionUrl01}"
              }
            },
            {
              "title": f"{RegionText02}",
              "imageUrl": f"{RegionImg02}",
              "link": {
                "web": f"{RegionUrl02}"
              }
            },
           ],
          "buttons": [
            {
              "label": "뒤로 가기",
              "action": "block",
              "blockId": "636b36be0abf120ff67a4ddc"
            },
            {
              "label": "더보기",
              "action": "webLink",
              "webLinkUrl": Sejong
            }
          ]
        }
      }
    ]
  }
}

    return responseSejong

# 광주 스킬
@app.route('/api/sayGwangju', methods=['POST'])
def sayGwangju():
    body = request.get_json()
    print(body)
    print(body['userRequest']['utterance'])

    Gwangju = "https://land.naver.com/news/region.naver?city_no=2900000000&dvsn_no="
    naver_region_all(Gwangju)

    responseGwangju = {
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "listCard": {
          "header": {
            "title": "광주 뉴스"
          },
          "items": [
            {
              "title": f"{RegionText01}",
              "imageUrl": f"{RegionImg01}",
              "link": {
                "web": f"{RegionUrl01}"
              }
            },
            {
              "title": f"{RegionText02}",
              "imageUrl": f"{RegionImg02}",
              "link": {
                "web": f"{RegionUrl02}"
              }
            },
           ],
          "buttons": [
            {
              "label": "뒤로 가기",
              "action": "block",
              "blockId": "636b36be0abf120ff67a4ddc"
            },
            {
              "label": "더보기",
              "action": "webLink",
              "webLinkUrl": Gwangju
            }
          ]
        }
      }
    ]
  }
}

    return responseGwangju

# 강원도 스킬
@app.route('/api/sayGangwon', methods=['POST'])
def sayGangwon():
    body = request.get_json()
    print(body)
    print(body['userRequest']['utterance'])

    Gangwon = "https://land.naver.com/news/region.naver?city_no=4200000000&dvsn_no="
    naver_region_all(Gangwon)

    responseGangwon = {
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "listCard": {
          "header": {
            "title": "강원도 뉴스"
          },
          "items": [
            {
              "title": f"{RegionText01}",
              "imageUrl": f"{RegionImg01}",
              "link": {
                "web": f"{RegionUrl01}"
              }
            },
            {
              "title": f"{RegionText02}",
              "imageUrl": f"{RegionImg02}",
              "link": {
                "web": f"{RegionUrl02}"
              }
            },
           ],
          "buttons": [
            {
              "label": "뒤로 가기",
              "action": "block",
              "blockId": "636b36be0abf120ff67a4ddc"
            },
            {
              "label": "더보기",
              "action": "webLink",
              "webLinkUrl": Gangwon
            }
          ]
        }
      }
    ]
  }
}

    return responseGangwon

# 충북 스킬
@app.route('/api/sayChungbuk', methods=['POST'])
def sayChungbuk():
    body = request.get_json()
    print(body)
    print(body['userRequest']['utterance'])

    Chungbuk = "https://land.naver.com/news/region.naver?city_no=4300000000&dvsn_no="
    naver_region_all(Chungbuk)

    responseChungbuk = {
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "listCard": {
          "header": {
            "title": "충청북도 뉴스"
          },
          "items": [
            {
              "title": f"{RegionText01}",
              "imageUrl": f"{RegionImg01}",
              "link": {
                "web": f"{RegionUrl01}"
              }
            },
            {
              "title": f"{RegionText02}",
              "imageUrl": f"{RegionImg02}",
              "link": {
                "web": f"{RegionUrl02}"
              }
            },
           ],
          "buttons": [
            {
              "label": "뒤로 가기",
              "action": "block",
              "blockId": "636b36be0abf120ff67a4ddc"
            },
            {
              "label": "더보기",
              "action": "webLink",
              "webLinkUrl": Chungbuk
            }
          ]
        }
      }
    ]
  }
}

    return responseChungbuk

# 충남 스킬
@app.route('/api/sayChungnam', methods=['POST'])
def sayChungnam():
    body = request.get_json()
    print(body)
    print(body['userRequest']['utterance'])

    Chungnam = "https://land.naver.com/news/region.naver?city_no=4400000000&dvsn_no="
    naver_region_all(Chungnam)

    responseChungnam = {
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "listCard": {
          "header": {
            "title": "충청남도 뉴스"
          },
          "items": [
            {
              "title": f"{RegionText01}",
              "imageUrl": f"{RegionImg01}",
              "link": {
                "web": f"{RegionUrl01}"
              }
            },
            {
              "title": f"{RegionText02}",
              "imageUrl": f"{RegionImg02}",
              "link": {
                "web": f"{RegionUrl02}"
              }
            },
           ],
          "buttons": [
            {
              "label": "뒤로 가기",
              "action": "block",
              "blockId": "636b36be0abf120ff67a4ddc"
            },
            {
              "label": "더보기",
              "action": "webLink",
              "webLinkUrl": Chungnam
            }
          ]
        }
      }
    ]
  }
}

    return responseChungnam

# 경북 스킬
@app.route('/api/sayGyeongbuk', methods=['POST'])
def sayGyeongbuk():
    body = request.get_json()
    print(body)
    print(body['userRequest']['utterance'])

    Gyeongbuk = "https://land.naver.com/news/region.naver?city_no=4700000000&dvsn_no="
    naver_region_all(Gyeongbuk)

    responseGyeongbuk = {
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "listCard": {
          "header": {
            "title": "경상북도 뉴스"
          },
          "items": [
            {
              "title": f"{RegionText01}",
              "imageUrl": f"{RegionImg01}",
              "link": {
                "web": f"{RegionUrl01}"
              }
            },
            {
              "title": f"{RegionText02}",
              "imageUrl": f"{RegionImg02}",
              "link": {
                "web": f"{RegionUrl02}"
              }
            },
           ],
          "buttons": [
            {
              "label": "뒤로 가기",
              "action": "block",
              "blockId": "636b36be0abf120ff67a4ddc"
            },
            {
              "label": "더보기",
              "action": "webLink",
              "webLinkUrl": Gyeongbuk
            }
          ]
        }
      }
    ]
  }
}

    return responseGyeongbuk

# 경남 스킬
@app.route('/api/sayGyeongnam', methods=['POST'])
def sayGyeongnam():
    body = request.get_json()
    print(body)
    print(body['userRequest']['utterance'])

    Gyeongnam = "https://land.naver.com/news/region.naver?city_no=4800000000&dvsn_no="
    naver_region_all(Gyeongnam)

    responseGyeongnam = {
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "listCard": {
          "header": {
            "title": "경상남도 뉴스"
          },
          "items": [
            {
              "title": f"{RegionText01}",
              "imageUrl": f"{RegionImg01}",
              "link": {
                "web": f"{RegionUrl01}"
              }
            },
            {
              "title": f"{RegionText02}",
              "imageUrl": f"{RegionImg02}",
              "link": {
                "web": f"{RegionUrl02}"
              }
            },
           ],
          "buttons": [
            {
              "label": "뒤로 가기",
              "action": "block",
              "blockId": "636b36be0abf120ff67a4ddc"
            },
            {
              "label": "더보기",
              "action": "webLink",
              "webLinkUrl": Gyeongnam
            }
          ]
        }
      }
    ]
  }
}

    return responseGyeongnam

# 전북 스킬
@app.route('/api/sayJeonbuk', methods=['POST'])
def sayJeonbuk():
    body = request.get_json()
    print(body)
    print(body['userRequest']['utterance'])

    Jeonbuk = "https://land.naver.com/news/region.naver?city_no=4500000000&dvsn_no="
    naver_region_all(Jeonbuk)

    responseJeonbuk = {
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "listCard": {
          "header": {
            "title": "전라북도 뉴스"
          },
          "items": [
            {
              "title": f"{RegionText01}",
              "imageUrl": f"{RegionImg01}",
              "link": {
                "web": f"{RegionUrl01}"
              }
            },
            {
              "title": f"{RegionText02}",
              "imageUrl": f"{RegionImg02}",
              "link": {
                "web": f"{RegionUrl02}"
              }
            },
           ],
          "buttons": [
            {
              "label": "뒤로 가기",
              "action": "block",
              "blockId": "636b36be0abf120ff67a4ddc"
            },
            {
              "label": "더보기",
              "action": "webLink",
              "webLinkUrl": Jeonbuk
            }
          ]
        }
      }
    ]
  }
}

    return responseJeonbuk

# 전남 스킬
@app.route('/api/sayJeonnam', methods=['POST'])
def sayJeonnam():
    body = request.get_json()
    print(body)
    print(body['userRequest']['utterance'])

    Jeonnam = "https://land.naver.com/news/region.naver?city_no=4600000000&dvsn_no="
    naver_region_all(Jeonnam)

    responseJeonnam = {
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "listCard": {
          "header": {
            "title": "전라남도 뉴스"
          },
          "items": [
            {
              "title": f"{RegionText01}",
              "imageUrl": f"{RegionImg01}",
              "link": {
                "web": f"{RegionUrl01}"
              }
            },
            {
              "title": f"{RegionText02}",
              "imageUrl": f"{RegionImg02}",
              "link": {
                "web": f"{RegionUrl02}"
              }
            },
           ],
          "buttons": [
            {
              "label": "뒤로 가기",
              "action": "block",
              "blockId": "636b36be0abf120ff67a4ddc"
            },
            {
              "label": "더보기",
              "action": "webLink",
              "webLinkUrl": Jeonnam
            }
          ]
        }
      }
    ]
  }
}

    return responseJeonnam

# 제주 스킬
@app.route('/api/sayJeju', methods=['POST'])
def sayJeju():
    body = request.get_json()
    print(body)
    print(body['userRequest']['utterance'])

    Jeju = "https://land.naver.com/news/region.naver?city_no=5000000000&dvsn_no="
    naver_region_all(Jeju)

    responseJeju = {
  "version": "2.0",
  "template": {
    "outputs": [
      {
        "listCard": {
          "header": {
            "title": "제주도 뉴스"
          },
          "items": [
            {
              "title": f"{RegionText01}",
              "imageUrl": f"{RegionImg01}",
              "link": {
                "web": f"{RegionUrl01}"
              }
            },
            {
              "title": f"{RegionText02}",
              "imageUrl": f"{RegionImg02}",
              "link": {
                "web": f"{RegionUrl02}"
              }
            },
           ],
          "buttons": [
            {
              "label": "뒤로 가기",
              "action": "block",
              "blockId": "636b36be0abf120ff67a4ddc"
            },
            {
              "label": "더보기",
              "action": "webLink",
              "webLinkUrl": Jeju
            }
          ]
        }
      }
    ]
  }
}

    return responseJeju