import requests
from os import name
import xml.etree.ElementTree as et
import pandas as pd
import bs4
from lxml import html
from urllib.parse import urlencode, quote_plus, unquote
from datetime import datetime 
# datetime.today().strftime("%Y%m%d%H%M%S")    # YYYYmmddHHMMSS 형태의 시간 출력

# datetime.today().strftime("%Y/%m/%d %H:%M:%S")  # YYYY/mm/dd HH:MM:SS 형태의 시간 출력
DEAL_YMD = datetime.today().strftime("%Y%m") #YYYYmm형태의 시간 출력
DEAL_YMD
print(DEAL_YMD)

#인증키 입력
Encoding = 'Nzg1xq0t8RAGwo5Andw2gnphQO1azrV%2FhPI4m9tGUgoF7oe2A2EQRY8saDhA0UuhV%2FxN%2BzYQ0adwtYP%2FeuW4mw%3D%3D'
Decoding = 'Nzg1xq0t8RAGwo5Andw2gnphQO1azrV/hPI4m9tGUgoF7oe2A2EQRY8saDhA0UuhV/xN+zYQ0adwtYP/euW4mw=='


# for i in LAWD:
def CreateDF(LAWD, DEAL_YMD):
  url = 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade'
  params ={'serviceKey' : Decoding, 'LAWD_CD' : LAWD, 'DEAL_YMD' : DEAL_YMD }
  response = requests.get(url, params=params)
  content = response.text

  #bs4 사용하여 item 태그 분리

  xml_obj = bs4.BeautifulSoup(content,'lxml-xml')
  rows = xml_obj.findAll('item')

  # 각 행의 컬럼, 이름, 값을 가지는 리스트 만들기
  row_list = [] # 행값
  name_list = [] # 열이름값
  value_list = [] #데이터값

  for i in range(0, len(rows)):
      columns = rows[i].find_all()
      #첫째 행 데이터 수집
      for j in range(0,len(columns)):
          if i ==0:
              # 컬럼 이름 값 저장
              name_list.append(columns[j].name)
          # 컬럼의 각 데이터 값 저장
          value_list.append(columns[j].text)
      # 각 행의 value값 전체 저장
      row_list.append(value_list)
      # 데이터 리스트 값 초기화
      value_list=[]


  #xml값 DataFrame으로 만들기
  apt_df = pd.DataFrame(row_list, columns=name_list)
  return apt_df


from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.sql import text 
def db_create():
    # 로컬
	# engine = create_engine("postgresql://postgres:1234@localhost:5432/chatbot", echo = False)
		
	# Heroku
    
    engine = create_engine("postgresql://qxqcovcxobgrzr:136d1a4ee21d7d53fefe41723c82cadb3a41edd4203ef9b4759b8ecb1daf68a7@ec2-107-23-76-12.compute-1.amazonaws.com:5432/d7477vdhmjaq31", echo = False)

    engine.connect()
    # engine.execute("""
    #     CREATE TABLE IF NOT EXISTS apt_final(
    #         거래금액 VARCHAR(30) NOT NULL,
    #         거래유형 VARCHAR(30) NOT NULL,
    #         건축년도 INT NOT NULL,
    #         년 INT NOT NULL,
    #         법정동 VARCHAR(50) NOT NULL,
    #         아파트 VARCHAR(50) NOT NULL,
    #         월 INT NOT NULL,
    #         일 INT NOT NULL,
    #         전용면적 FLOAT NOT NULL,
    #         중개사소재지 VARCHAR(50) NOT NULL,
    #         지번 VARCHAR(30) NOT NULL, 
    #         지역코드 INT NOT NULL,
    #         층 INT NOT NULL,
    #         해체사유발생일 VARCHAR(20),
    #         해체여부 VARCHAR(20)   
    #     );"""
    # )
    df = None
    print(df)
    LAWD = ['11110', '11200', '11215', '11230',
     '11260', '11290', '11305', '11320', '11350', '11380', '11410', '11440', '11470',
     '11500', '11530', '11545', '11560', '11590', '11620', '11650', '11680', '11710', '11740', '26110', '26140', '26170', '26200', '26230', '26260', 
     '26290', '26320', '26350', '26380', '26410', '26440', '26470', '26500', '26530', '26710', '27110', '27140', '27170', '27200', '27230', '27260',
     '27290', '27710', '28110', '28140', '28177', '28185', '28200', '28237', '28245', '28260', '28710', '28720', '29110', '29140', '29155', '29170', 
     '29200', '30110', '30140', '30170', '30200', '30230', '31110', '31140', '31170', '31200', '31710', '36110', '41111', '41113', '41115', '41117', 
     '41131', '41133', '41135', '41150', '41171', '41190', '41210', '41220', '41250', '41270', '41281', '41285', '41287', '41290', '41310', '41360', 
     '41370', '41390', '41410', '41430', '41450', '41461', '41463', '41465', '41480', '41500', '41550', '41570', '41590', '41610', '41630', '41650', 
     '41670', '41800', '41820', '41830', '42110', '42130', '42150', '42170', '42190', '42210', '42230', '42720', '42730', '42750', '42760', '42770',
     '42780', '42790', '42800', '42810', '42830', '43111', '43112', '43113', '43114', '43130', '43150', '43720', '44131', '44133', '44150', '44180', 
     '44200', '44210', '44230', '44800']
    for idx in LAWD:
     # newdf 코드
        newdf = CreateDF(idx, DEAL_YMD)
        df = pd.concat([df, newdf])
    print(newdf)
    print(df)
  # 맨 아래 / 마지막 행 남기고 전부 제거 :: last
    df = df.drop_duplicates(['건축년도', '년', '법정동', '아파트', '전용면적', '지번', '지역코드'], keep = 'last')
    #df.drop(['해체사유발생일'], axis=1, inplace=True)
    print(df)
    df.to_sql(name='apt_final', con=engine, schema = 'public', if_exists='replace', index=False)
    


if __name__ == "__main__":
    db_create()
