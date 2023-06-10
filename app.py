import streamlit as st
import datetime
import time
import pandas as pd
import numpy as np
import math
from model import ourModel
from utils_ import preprocessing


model = ourModel()





def hourly_it(start, finish, cur_date):
    finish = (datetime.datetime.combine(cur_date, finish))
    start = (datetime.datetime.combine(cur_date, start))

    while finish >= start:
        if (start == finish and finish.minute == 0) : return False

        yield start
        start = start + datetime.timedelta(hours=1)
        


risk_info = [
    {"idx": 1,
     "header":"안전한 작업이 예상됩니다.",
     "description":"현재 우리 현장은 사고 위험이 낮지만, 건설사고에 대한 경각심을 높여주시기 바랍니다. 사고 예방을 위해 모든 작업자들은 안전을 최우선으로 생각하고 신중한 조치를 취해야 합니다. 작업 전에는 위험 분석을 실시하고 적절한 보호장비를 착용하여 안전성을 확보하며, 작업 중에도 주의를 늦추지 말고 안전 규정을 엄격히 준수해야 합니다. 작은 실수나 태만함이 큰 사고로 이어질 수 있습니다. 모두가 협력하여 사고 예방에 기여하고, 안전한 작업 환경을 유지하는 데 힘쓰도록 합시다. 안전은 우리의 가치이며, 모든 작업자들이 건강하고 안전하게 일할 수 있는 환경을 만들기 위해 노력해야 합니다."},
    {"idx": 2,
     "header":"비교적 안전한 작업이 예상됩니다.",
     "description":"저희 현장은 비교적으로 사고 위험이 낮을 수 있지만, 여전히 건설사고에 대한 경각심을 갖고 유의해주시길 바랍니다. 작업자분들은 안전을 저희 모두의 가장 큰 가치로 여기고, 작업을 수행할 때에도 안전에 최우선으로 신경써야 합니다. 작업 전에는 가능한 위험 요소를 식별하고 예방 조치를 철저히 취하며, 작업 중에는 항상 주의를 기울여야 합니다. 작은 실수도 큰 사고로 이어질 수 있습니다. 모두가 안전한 작업 환경을 만들기 위해 협력하고, 사고 예방에 기여하는 것이 중요합니다. 안전에 대한 경각심을 잃지 말고, 함께 안전을 유지하며 건설사고를 예방해 나가도록 합시다."},
    {"idx": 3,
     "header":"사고 발생확률이 낮습니다.",
     "description":"저희 현장에서는 사고 위험이 조금 낮을지도 모릅니다. 그러나 건설사고에 대한 경각심을 갖고 유의해주시길 바랍니다. 작업자분들께서는 안전을 저희 모두의 우선 순위로 여기고, 작업을 수행할 때에도 안전 규정을 철저히 준수해야 합니다. 작업 전에는 위험 요소를 식별하고 예방 조치를 취하며, 작업 중에는 항상 주의를 기울여야 합니다. 사소한 실수도 큰 사고로 이어질 수 있습니다. 모두가 안전한 작업 환경을 만들기 위해 협력하고, 사고 예방에 기여하는 것이 중요합니다. 건설사고에 대한 경각심을 잊지 말고, 함께 안전을 유지해 나가도록 합시다"},
    {"idx": 4,
     "header":"사고 발생확률이 조금 있습니다.",
     "description":"저희 현장에서는 사고 위험이 조금 있을 수 있으므로 건설사고에 대한 경각심을 갖고 유의해주시기 바랍니다. 모든 작업자분들께서는 안전을 최우선으로 여기고, 작업을 수행할 때에는 안전 절차와 규정을 엄격히 준수해야 합니다. 작업 전에는 가능한 위험을 식별하고 적절한 예방 조치를 취하며, 작업 중에도 항상 주의를 기울여야 합니다. 작은 부주의나 경솔한 행동이 큰 사고로 이어질 수 있습니다. 모두가 안전한 작업 환경을 만들기 위해 협력하고, 사고 예방에 적극적으로 참여하는 것이 중요합니다. 안전에 대한 경각심을 잊지 말고, 함께 안전을 유지하며 건설사고를 예방해 나가도록 합시다."},
    {"idx": 5,
     "header":"사고 발생확률이 있습니다.",
     "description":"저희 현장에서는 사고 위험이 존재하기 때문에 건설사고에 대한 경각심을 갖고 유의해주시길 바랍니다. 모든 작업자분들께서는 안전을 최우선으로 생각하고, 작업을 수행할 때에는 안전 규정을 철저히 준수해야 합니다. 위험한 작업에 참여할 경우에는 특히나 신중함을 기하고, 항상 안전장비를 올바르게 착용하여 작업해야 합니다. 작은 부주의나 경솔한 행동이 큰 사고로 이어질 수 있습니다. 모두가 안전한 작업 환경을 만들기 위해 협력하고, 사고 예방에 적극적으로 기여하는 것이 중요합니다. 안전에 대한 경각심을 가지고, 함께 안전을 유지하며 건설사고를 예방해 나가도록 합시다."},
    {"idx": 6,
     "header":"사고 발생확률이 높습니다.",
     "description":"저희 현장에서는 사고 위험이 상당히 높을 수 있으므로 건설사고에 대한 경각심을 가지고 유의해주시길 바랍니다. 모든 작업자분들께서는 안전을 최우선으로 여기고, 작업을 수행할 때에는 안전 규정을 철저히 준수해야 합니다. 특히 위험이 판단되는 경우에는 즉시 작업을 중단하고 상황을 평가해야 합니다. 작업을 중단하여 위험을 해소하고 안전을 확인하는 것이 우선이며, 이는 모두의 생명과 건강을 보호하는데 중요한 역할을 합니다. 모든 작업자들이 위험을 인식하고 위기 상황에서 적절한 조치를 취함으로써 사고를 예방할 수 있습니다. 함께 안전을 유지하며 건설사고를 최소화하는 데 힘쓰도록 합시다. 작업 중에 위험이 발견되면 결코 주저하지 말고 작업을 중단합시다."},
]



def on_click_fn(col=None):
    print(f'\t현재 session_state : {st.session_state.to_dict()}')

    # 1. 전처리 및 스케일러 적용
    input_list= preprocessing(st.session_state.to_dict())
    print(input_list)
    cur_time_start, cur_time_end = st.session_state.cur_time
    print(f'\t전처리 결과 : {input_list, cur_time_start, cur_time_end}')

    # 시간별 리스트 구현
    dates = []
    for hour in hourly_it(cur_time_start, cur_time_end, st.session_state.cur_date):
        dates.append(hour.strftime("%H"))

    # # 2. 모델 predict
    # res = []
    # risk = model.predict(input_list)
    res = []
    for hour in dates: # hour <class 'str'>
        input_list[-3] = int(hour)
        res.append(model.predict(input_list))
    print(res)

    risk = int(np.floor(np.mean(res)))
    print(risk)

    res = list(map(lambda x : x + 1, res))
    

    # 3. 결과
    if col is not None:
        with col:
            st.title('')
            st.header(f'👷‍♂️ 위험도 지수 {risk_info[risk]["idx"]}')
            st.subheader(f'{risk_info[risk]["header"]}')
            st.write(f'{risk_info[risk]["description"]}')

            # a, b = st.session_state.cur_time
            # dates = [(datetime.datetime.combine(datetime.date.today(), a) + datetime.timedelta(minutes=i*60)).strftime("%H:%M") for i in range(math.ceil(GetdateTimeDifferenceInHours(a, b)))]

            # chart_data = pd.DataFrame(
            #     res,
            #     # np.random.randn(len(dates), 1),
            #     columns=['시간에 따른 위험도 지수'], index=dates)
            
            # st.bar_chart(chart_data) #, use_container_width=False


    else:
        with st.empty():
            # for seconds in range(10):
            #     st.write(f"⏳ {seconds} seconds have passed")
            #     time.sleep(1)
            # st.write("✔️ 10 second over!")
            st.write('클릭했습니다!')




def main():
    # col1, col2 = st.columns(2)

    st.sidebar.title('🔖 일정 및 날씨')

    st.sidebar.date_input(
        "작업 날짜는 어떻게 되나요?",
        datetime.datetime.date(datetime.datetime.now()), key='cur_date')

    st.sidebar.slider(
        "작업시간을 선택해주세요",
        value=(datetime.time(10, 00), datetime.time(16, 00)), step = datetime.timedelta(minutes=30), key='cur_time')

    # st.sidebar.select_slider(
    #     '날씨를 선택해주세요',
    #     options=['☀️ 맑음', '☁️ 흐림', '🌫️ 안개', '💨 강풍', '🌧️ 강우', '🌨️ 강설'], key='weather')

    st.sidebar.slider(
        '최저기온과 최고기온을 기록해주세요.',
        -20.0, 40.0, (15.0, 23.0), step = 0.1, format = '%.1f°C', key = 'temperature')

    st.sidebar.slider('습도를 선택해주세요', 0.0, 100.0, 25.0, step = 0.1, format = '%.1f%%', key = 'wet')

    # st.sidebar.slider('평균기온', 0.0, 130.0, 25.0, step = 0.1, format = '%.1f°C', key = 'average_temperature')



    st.sidebar.title('🔖 공사 종류')

    st.sidebar.checkbox('공공 공사입니다', key = 'is_public')

    st.sidebar.checkbox('안전방호조치가 되어있습니다', key = 'secure_check')

    st.sidebar.checkbox('개인보호조치여부가 되어있습니다', key = 'personal_check')

    st.sidebar.checkbox('설계안정성검토가 되어있습니다', key ='design_stability_review')

    st.sidebar.radio(
        "시설물 대분류를 선택해주세요",
        ('건축', '토목', '산업환경설비', '조경'), horizontal=True, key= 'facility')

    st.sidebar.selectbox(
        '공사비를 선택해주세요',
        ('1,000만원 미만', '1,000만 ~ 2,000만원 미만',
        '2,000만 ~ 4,000만원 미만', '4,000만 ~ 1억원 미만',
        '1억 ~ 2억원 미만', '2억 ~ 3억원 미만', '3억 ~ 5억원 미만',
        '5억 ~ 10억원 미만', '10억 ~ 20억원 미만', '20억 ~ 50억원 미만',
        '50억 ~ 100억원 미만', '100억 ~ 150억원 미만', '150억 ~ 200억원 미만',
        '200억 ~ 300억원 미만', '300억 ~ 500억원 미만', '500억 ~ 1,000억원 미만', '1,000억원 이상'), key='construction_costs')

    st.sidebar.selectbox(
        '작업자수를 선택해주세요.',
        ('19인 이하',
        '20~49인',
        '50~99인',
        '100~299인',
        '300~499인',
        '500인 이상'), key='num_of_workers')

    st.sidebar.select_slider(
        '낙찰율을 선택해주세요',
        options=[
            '60% 미만', '60~64%', '65~69%', '70~74%', '75~79%', '80~84%', '85~89%', '90% 이상'
        ], key='successful_bid_rate')

    st.sidebar.select_slider(
        '공정율을 선택해주세요',
        options=[
            '10% 미만',
            '10~19%',
            '20~29%',
            '30~39%',
            '40~49%',
            '50~59%',
            '60~69%',
            '70~79%',
            '80~89%',
            '90% 이상'
        ], key='process_rate')
    

    



    # with col1:
        # st.title('👷 건설공사 현장 위험도 예측 서비스')
        # st.write('(TEAM. 대탈출)') # header
        # st.subheader('왼쪽 사이드바를 열어 현장 수치를 입력해주세요. 😀')
        # st.write('작업시간에 따라 바뀌는 위험도를 알려드려요!')

    st.markdown("""
        <style>
        @font-face {
            font-family: 'TTTtangsbudaejjigaeB';
            src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2212@1.0/TTTtangsbudaejjigaeB.woff2') format('woff2');
            font-weight: 700;
            font-style: normal;
        }
        @font-face {
            font-family: 'GmarketSansMedium';
            src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_2001@1.1/GmarketSansMedium.woff') format('woff');
            font-weight: normal;
            font-style: normal;
        }
        @font-face {
            font-family: 'S-CoreDream-3Light';
            src: url('https://cdn.jsdelivr.net/gh/projectnoonnu/noonfonts_six@1.2/S-CoreDream-3Light.woff') format('woff');
            font-weight: normal;
            font-style: normal;
        }
        .title {
            font-family: 'TTTtangsbudaejjigaeB', sans-serif; 
            font-size: 2.0em;
            text-align: justify;
        }
        .subheader {
            font-family: 'GmarketSansMedium', sans-serif; 
            font-size: 1.5em;
            text-align: justify;
        }
        .team {
            font-family: 'S-CoreDream-3Light', sans-serif; 
            color: gray;
            font-size: 0.5em;
            vertical-align : top;
            text-align: justify;
        }
        .war {
            font-family: 'S-CoreDream-3Light', sans-serif; 
            color: gray;
            font-size: 0.8em;
            text-align: justify;
        }
        body, p {
            font-family: 'S-CoreDream-3Light', sans-serif; 
            text-align: justify;
        }
        .ainfo > a {
            font-family: 'S-CoreDream-3Light', sans-serif; 
            color: gray;
            font-size: 0.8em;
            text-align: justify;
        }
        </style>
        """, unsafe_allow_html=True)
    
    st.markdown('<div class="title">👷 건설공사 현장 위험도 예측 서비스 👷 <span class="team"> (TEAM. 대탈출)</span> </div>\
                <br><br>\
                <p class="subheader"> ⬅ 왼쪽 사이드바를 열어 현장 수치를 입력해주세요.</p>\
                <br>\
                <p>항목을 모두 선택 후, 결과 확인하기를 누르면 작업현장에 대한 위험도를 알려드려요! ✨</p>\
                <p>항상 안전한 작업하세요 🙂</p>\
                <p class="war">본 서비스는 일반적인 안전 지침과 조언을 제공할 수 있지만, 작업현장의 구체적인 위험도를 파악하는 데는 제한이 있습니다. 그러나 저희는 항상 안전에 대한 주의를 강조하고, 작업현장에서 사고에 대한 경각심을 가지고 유의하라는 메시지를 전달해드릴 수 있습니다. 작업자들에게는 항상 안전을 최우선으로 생각하고, 안전 규정을 준수하며, 위험을 인식하고 대비책을 마련하는 습관을 갖도록 권장해드립니다.</p>\
                <iframe width="560" height="315" src="https://www.youtube-nocookie.com/embed/zeInTSwPccs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>\
                <div class="ainfo"><a href="https://www.kalis.or.kr/index.do#mainContainer">🔗 국토안전관리원 홈페이지 바로가기</a></div>\
                <div class="ainfo"><a href="https://www.facebook.com/KALIS2020/?locale=ko_KR">🔗 국토안전관리원 페이스북 바로가기</a></div>'
                
                , unsafe_allow_html=True)
    
    st.divider()
    container = st.container()
    container.empty()
    
    if st.sidebar.button('👉 결과 확인하기', on_click=on_click_fn, args=[container], disabled=disabled_time_slider(st.session_state)): # 
        print('✔')
    else:
        print('-')



def GetdateTimeDifferenceInHours(a, b):
    # Create datetime objects for each time (a and b)
    dateTimeA = datetime.datetime.combine(datetime.date.today(), a)
    dateTimeB = datetime.datetime.combine(datetime.date.today(), b)

    # Get the difference between datetimes (as timedelta)
    dateTimeDifference = dateTimeB - dateTimeA
    #print(dateTimeDifference)

    # Divide difference in seconds by number of seconds in hour (3600)  
    return dateTimeDifference.total_seconds() / 3600

def disabled_time_slider(session_state):
    a, b = session_state.cur_time

    dateTimeDifferenceInHours = GetdateTimeDifferenceInHours(a, b)
    res = (dateTimeDifferenceInHours <= 0)

    if res:
        with st.empty():
            st.sidebar.warning('작업시간은 최소 30분 간격이어야 합니다.', icon="ℹ️")
    return res





if __name__ == '__main__' :
    main()