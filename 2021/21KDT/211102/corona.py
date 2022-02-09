######### 해당 code는 실제로 AWS내에서 실행한다 #########


import requests
import xmltodict
import time
import pandas as pd
import re
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')
import pymysql
from sqlalchemy import create_engine

db_connection_str = 'mysql+pymysql://ogu:1234@52.78.90.155/corona19'       # AWS내 mysql 서버 계정 및 서버 IP, DB명
db_connection = create_engine(db_connection_str)
conn = db_connection.connect()


url_decide_base = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson"
url_decide_serviceKey = "S8%2Ftx%2BhEP7bZDZI%2By0P1ZKvPuHpx%2BVUKpt6ay8faxnxR%2FTRO9M5UAy8%2BafhJBNVzQG%2Fgwoym2S4Xbe1dUXivUw%3D%3D"

url_district_base = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson"
url_district_serviceKey = url_decide_serviceKey

url_seoul_vaccine = 'http://openapi.seoul.go.kr:8088/706e775a4577686136356f44596267/xml/tvCorona19VaccinestatNew/1/999/'

url_vaccine = 'https://api.odcloud.kr/api/15077756/v1/vaccine-stat?page=1&perPage=3000&serviceKey=S8%2Ftx%2BhEP7bZDZI%2By0P1ZKvPuHpx%2BVUKpt6ay8faxnxR%2FTRO9M5UAy8%2BafhJBNVzQG%2Fgwoym2S4Xbe1dUXivUw%3D%3D'

url_pages = "1000" #페이지당열갯수
url_start_date = "20200303" #시작날짜
url_end_date = datetime.today().strftime("%Y%m%d%H%M%S")[:8] #끝날짜
while True:
        realtime = datetime.today().strftime("%Y%m%d%H%M%S")[8:]  # 9시 30~35분 사이에 데이터 불러오기 실행
    if realtime >= '093000' and realtime < '953005':
    print('start')
    try:
        print('Getting In Data Of CORONA19 Decide')
        url = url_decide_base + "?serviceKey=" + url_decide_serviceKey + "&pageNo=1&numOfRows=" + url_pages + "&startCreateDt="+ url_start_date + "&endCreateDt=" + url_end_date

        req = requests.get(url).content

        xmlObject = xmltodict.parse(req)
        dict_data = xmlObject['response']['body']['items']['item']

        dfDecide = pd.DataFrame(dict_data)

        dfDecide.drop(['createDt', 'seq', 'stateTime', 'updateDt', 'resutlNegCnt'], axis=1, inplace=True)
        dfDecide.sort_values(['stateDt'], ascending=False, inplace=True)
        dfDecide['stateDt'] = pd.to_datetime(dfDecide['stateDt']) - pd.DateOffset(days=1)
        dfDecide = dfDecide.astype({"accExamCnt":"int64", "accExamCompCnt":"int64", "careCnt":"int64", "clearCnt":"int64", "deathCnt":"int64", "decideCnt":"int64", "examCnt":"int64", "accDefRate":"float64"}).copy()

        dfDecide['newDecideCnt'] = 0

        for i in range(len(dfDecide)-1):
            dfDecide['newDecideCnt'][i] = int(dfDecide.iloc[i]['decideCnt']) - int(dfDecide.iloc[i+1]['decideCnt'])
            
        dfDecide = dfDecide[['stateDt', 'newDecideCnt', 'examCnt', 'decideCnt', 'deathCnt', 'clearCnt', 'careCnt', 'accDefRate', 'accExamCnt', 'accExamCompCnt']].copy()
        dfDecide.rename(columns={'stateDt':'날짜', 'newDecideCnt':'당일 확진자 수', 'examCnt':'검사 진행 수', 'decideCnt':'누적 확진자 수', 'deathCnt':'누적 사망자 수', 'clearCnt':'누적 격리 해제 수', 
                                 'careCnt':'치료 중 환자 수', 'accDefRate':'누적 확진률', 'accExamCnt':'누적 검사 수', 'accExamCompCnt':'누적 검사 완료 수'}, inplace=True)

        dfDecide.to_sql(name='Decide', con=db_connection, if_exists='replace',index=False)
    except:
        print('DECIDE ERROR')
      
    ##############################################################################################################################
    try:
        print('Getting In Data Of CORONA19 District')

        url_district= url_district_base + "?serviceKey=" + url_district_serviceKey + "&pageNo=1&numOfRows=" + url_pages + "&startCreateDt="+ url_start_date + "&endCreateDt=" + url_end_date

        req = requests.get(url_district).content

        xmlObject = xmltodict.parse(req)
        dict_data = xmlObject['response']['body']['items']['item']

        dfDistrict = pd.DataFrame(dict_data)
        dfDistrict = dfDistrict[(dfDistrict['gubun'] != '합계') & (dfDistrict['gubun'] != '검역')].reset_index(drop=True).copy()

        tempDf = pd.DataFrame(columns=['stateDt', 'Seoul', 'Busan', 'Daegu', 'Incheon', 'Gwangju', 'Daejeon', 'Ulsan', 'Sejong', 'Gyeonggi-do', 'Gangwon-do', 'Chungcheongbuk-do', 'Chungcheongnam-do' ,'Jeollabuk-do' ,'Jeollanam-do' ,'Gyeongsangbuk-do' ,'Gyeongsangnam-do' ,'Jeju'])

        for i in range(0, len(dfDistrict), 17):
            tempDistrict = dfDistrict.iloc[i:i+17]
            temp = tempDistrict[['incDec', 'stdDay']].transpose()
            yearData = int(temp[i]['stdDay'].split(' ')[0][:-1])
            monthData = int(temp[i]['stdDay'].split(' ')[1][:-1])
            dayData = int(temp[i]['stdDay'].split(' ')[2][:-1])
            
            temp.columns = dfDistrict['gubunEn'][:17]
            temp['stateDt'] = pd.to_datetime(datetime(yearData, monthData, dayData).strftime("%Y-%m-%d")) - pd.DateOffset(days=1)
            temp.head(1)
            temp = temp.head(1)[['stateDt', 'Seoul', 'Busan', 'Daegu', 'Incheon', 'Gwangju', 'Daejeon', 'Ulsan', 'Sejong', 'Gyeonggi-do', 'Gangwon-do', 'Chungcheongbuk-do', 'Chungcheongnam-do' ,'Jeollabuk-do' ,'Jeollanam-do' ,'Gyeongsangbuk-do' ,'Gyeongsangnam-do' ,'Jeju']].copy()
            
            tempDf = tempDf.append(temp)
            
        tempDf.reset_index(drop=True, inplace=True)
        tempDf = tempDf.astype('int64')
        tempDf = tempDf.astype({"stateDt":"datetime64[ns]"})

        tempDf.rename(columns={'stateDt':'날짜', 'Seoul':'서울', 'Busan':'부산', 'Daegu':'대구', 'Incheon':'인천', 'Gwangju':'광주', 'Daejeon':'대전', 'Ulsan':'울산', 'Sejong':'세종',
                                   'Gyeonggi-do':'경기', 'Gangwon-do':'강원', 'Chungcheongbuk-do':'충북', 'Chungcheongnam-do':'충남', 'Jeollabuk-do':'전북',
                                   'Jeollanam-do':'전남', 'Gyeongsangbuk-do':'경북', 'Gyeongsangnam-do':'경남', 'Jeju':'제주'}, inplace=True)

        tempDf.to_sql(name='District', con=db_connection, if_exists='replace',index=False)  
        
    except:
        print('DISTRICT ERROR')
    ################################################################################################################################
    try:
        print('Getting In Data Of CORONA19 DistrictRaw')

        dfDistrict.drop(['stdDay', 'updateDt', 'seq', 'qurRate', 'gubunCn'], axis=1, inplace=True)

        dfDistrict = dfDistrict.astype({"createDt":"datetime64[ns]"}).copy()

        dfDistrict['createDt'] = dfDistrict['createDt'] - pd.DateOffset(days=1)
        dfDistrict['stateDt'] = dfDistrict['createDt'].dt.date         # YYYY-MM-DD(문자)
        dfDistrict.drop(['createDt'], axis=1, inplace=True)

        dfDistrict = dfDistrict.astype({"stateDt":"datetime64[ns]", "defCnt":"int64", "deathCnt":"int64", "incDec":"int64"}).copy()
        dfDistrict = dfDistrict[['stateDt', 'gubun', 'gubunEn', 'defCnt', 'deathCnt', 'incDec', 'isolClearCnt', 'isolIngCnt', 'localOccCnt', 'overFlowCnt']].copy()

        dfDistrict['isolClearCnt'] = dfDistrict['isolClearCnt'].fillna(0).astype("int64")
        dfDistrict['isolIngCnt'] = dfDistrict['isolIngCnt'].fillna(0).astype("int64")
        dfDistrict['localOccCnt'] = dfDistrict['localOccCnt'].fillna(0).astype("int64")
        dfDistrict['overFlowCnt'] = dfDistrict['overFlowCnt'].fillna(0).astype("int64")

        dfDistrict = dfDistrict.astype({"isolClearCnt":"int64", "isolIngCnt":"int64", "localOccCnt":"int64", "overFlowCnt":"int64"}).copy()

        dfDistrict.rename(columns={'stateDt':'날짜', 'gubun':'지역명', 'gubunEn':'지역명(En)', 'defCnt':'확진자 수', 'deathCnt':'사망자 수', 'incDec':'전일 대비 증감 수',
                                   'isolClearCnt':'격리 해제 수', 'isolIngCnt':'격리 중 환자 수', 'localOccCnt':'지역 발생 수', 'overFlowCnt':'해외 유입 수'}, inplace=True)

        dfDistrict.to_sql(name='DistrictRaw', con=db_connection, if_exists='replace',index=False)  

    except:
        print('DISTRICTRAW ERROR')
    ################################################################################################################################
    try:
        print('Getting In Data Of CORONA19 VaccineSeoul')

        req = requests.get(url_seoul_vaccine).content

        xmlObject = xmltodict.parse(req)
        dict_data = xmlObject['tvCorona19VaccinestatNew']['row']

        dfSeoulVac = pd.DataFrame(dict_data)

        dfSeoulVac = dfSeoulVac.astype({"S_VC_DT":"datetime64[ns]"}).copy()

        dfSeoulVac = dfSeoulVac.astype({"FIR_SUB":"int64", "FIR_INC":"int64", "FIR_INC_RATE":"float64", "FIR_INC1":"int64", "SCD_INC":"int64", "SCD_INC_RATE":"float64", "SCD_INC1":"int64"}).copy()
        dfSeoulVac.rename(columns={'S_VC_DT':'날짜', "FIR_SUB":"접종대상자", "FIR_INC":"누적 1차 접종자 수", "FIR_INC_RATE":"1차 접종률", 
                                   "FIR_INC1":"당일 1차 접종자 수", "SCD_INC":"누적 2차 접종자 수", "SCD_INC_RATE":"2차 접종률", "SCD_INC1":"당일 2차 접종자 수"}, inplace=True)
                                   
        dfSeoulVac.to_sql(name='VaccineSeoul', con=db_connection, if_exists='replace',index=False)  
    except:
        print('VACCINESEOUL ERROR')
    ###############################################################################################################################
    try:
        print('Getting In Data Of CORONA19 VaccineKorea')

        req = requests.get(url_vaccine).content

        df_vaccine = pd.read_json(req)

        df_full_vaccine = pd.DataFrame(columns=['accumulatedFirstCnt', 'accumulatedSecondCnt', 'baseDate', 'firstCnt', 'secondCnt', 'sido', 'totalFirstCnt', 'totalSecondCnt'])

        for i in range(len(df_vaccine)):
            temp = pd.Series(df_vaccine['data'][i])
            if temp['sido'] == '전국':
                continue
            df_full_vaccine = df_full_vaccine.append(temp, ignore_index=True)
            
        df_full_vaccine.loc[df_full_vaccine.sido == '전라남도', 'sido'] = '전남'
        df_full_vaccine.loc[df_full_vaccine.sido == '전라북도', 'sido'] = '전북'
        df_full_vaccine.loc[df_full_vaccine.sido == '경상남도', 'sido'] = '경남'
        df_full_vaccine.loc[df_full_vaccine.sido == '경상북도', 'sido'] = '경북'
        df_full_vaccine.loc[df_full_vaccine.sido == '충청남도', 'sido'] = '충남'
        df_full_vaccine.loc[df_full_vaccine.sido == '충청북도', 'sido'] = '충북'

        df_full_vaccine.drop(['accumulatedFirstCnt', 'accumulatedSecondCnt'], axis=1, inplace=True)
        df_full_vaccine['sido'] = df_full_vaccine['sido'].str[:2]
        df_full_vaccine.sort_values('baseDate', ascending=False, inplace=True)
        df_full_vaccine.reset_index(drop=True, inplace=True)

        df_full_vaccine = df_full_vaccine.astype({"baseDate":"datetime64[ns]", "firstCnt":"int64", "secondCnt":"int64", "totalFirstCnt":"int64", "totalSecondCnt":"int64"}).copy()
        df_full_vaccine['baseDate'] = df_full_vaccine['baseDate'] - pd.DateOffset(days=1)
        df_full_vaccine = df_full_vaccine[['baseDate', 'sido', 'firstCnt', 'secondCnt', 'totalFirstCnt', 'totalSecondCnt']].copy()
        df_full_vaccine.rename(columns={'baseDate':'날짜', 'firstCnt':'1차 접종 수', 'secondCnt':'2차 접종 수', 'sido':'지역명', 'totalFirstCnt':'누적 1차 접종 수', 'totalSecondCnt':'누적 2차 접종 수'}, inplace=True)

        df_full_vaccine.to_sql(name='VaccineKorea', con=db_connection, if_exists='replace',index=False)
    except:
        print('VACCINEKOREA ERROR')

print('$$$$$$$ END $$$$$$$')

















