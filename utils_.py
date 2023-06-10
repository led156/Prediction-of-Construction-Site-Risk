import streamlit as st

to_value_by_dict = {
    'construction_costs': {'1,000만원 미만' : 500, # TODO: 전처리보고 value 설정
                            '1,000만 ~ 2,000만원 미만' : 1500,
                            '2,000만 ~ 4,000만원 미만': 3000, 
                            '4,000만 ~ 1억원 미만':7000,
                            '1억 ~ 2억원 미만':15000, 
                            '2억 ~ 3억원 미만':25000,
                            '3억 ~ 5억원 미만':40000,
                            '5억 ~ 10억원 미만':75000,
                            '10억 ~ 20억원 미만':150000,
                            '20억 ~ 50억원 미만': 300000,
                            '50억 ~ 100억원 미만':750000,
                            '100억 ~ 150억원 미만':1250000,
                            '150억 ~ 200억원 미만':1750000,
                            '200억 ~ 300억원 미만':2500000,
                            '300억 ~ 500억원 미만':  4000000,
                            '500억 ~ 1,000억원 미만':7500000,
                            '1,000억원 이상':10000000}, 

    'facility': {'건축' : 3, 
                 '토목' : 2, 
                 '산업환경설비' : 1, 
                 '조경' : 0}, 

    'num_of_workers': {'19인 이하' : 10,
                        '20~49인' : 30,
                        '50~99인' : 75,
                        '100~299인' : 150,
                        '300~499인' : 400,
                        '500인 이상' : 700}, 
    
    'process_rate': {'10% 미만' : 0,
                    '10~19%' : 1,
                    '20~29%' : 2,
                    '30~39%' : 3,
                    '40~49%' : 4,
                    '50~59%' : 5,
                    '60~69%' : 6,
                    '70~79%' : 7,
                    '80~89%' : 8,
                    '90% 이상' : 9}, 
    
    'successful_bid_rate': {'60% 미만' : 0, 
                            '60~64%' : 1, 
                            '65~69%' : 2, 
                            '70~74%' : 3, 
                            '75~79%' : 4, 
                            '80~84%' : 5, 
                            '85~89%' : 6, 
                            '90% 이상' : 7}, 

    'weather': {'☀️ 맑음' : 0, 
                '☁️ 흐림' : 1, 
                '🌫️ 안개' : 2, 
                '💨 강풍' : 3, 
                '🌧️ 강우' : 4, 
                '🌨️ 강설' : 5},

    'design_stability_review': {True : 0, False : 1}, 
    'secure_check': {True : 0, False : 1}, 
    'personal_check': {True : 0, False : 1}, 
    'is_public': {True : 0, False : 1}, 
    

    }


    # 'wet': 25.0, 
    # 'average_temperature': 25.0, 
    # 'temperature': (15.0, 23.0), 

    # 'cur_time': (datetime.time(10, 0), datetime.time(16, 0)), 
    # 'cur_date': datetime.date(2023, 6, 3), 
# 	공공민간구분	습도	안전방호조치여부	개인보호조치여부	공사비	낙찰율	공정율	작업자수	설계안정성검토	사고요일	사고시간	일교차	위험도 지수	시설물 대분류
def preprocessing(state_dict):
    input_format = {
        'is_public':  0, 
        'wet': 0,
        
        'secure_check':  0, 
        'personal_check':  0, 
        'construction_costs': 0, 
        'successful_bid_rate': 0, 
        'process_rate':  0, 
        'num_of_workers':  0, 
 
        # 'weather':  0, 
        'design_stability_review':  0, 
        'cur_days': 0, 
        'cur_time': 0,
        
        'average_temperature':  0, 
        'facility': 0, 
        
        # 'wet':  0,  
        

        # 'highest temperature': 0,
        # 'minimum temperature': 0, 

        # 'cur_time_start': 0, 
        # 'cur_time_end': 0,
        
        
        }
    
    used_key = ['construction_costs', 'is_public', 'facility', 'design_stability_review', 'num_of_workers', 'personal_check', 'secure_check', 'successful_bid_rate', 'process_rate']
    # used_key = ['is_public', 'facility', 'cur_date', 'design_stability_review', 'num_of_workers', 'construction_costs', 'personal_check', 'secure_check']
    

    for key in used_key: #to_value_by_dict.keys()
        input_format[key] = to_value_by_dict[key][state_dict[key]]

    input_format['wet'] = state_dict['wet']
    
    min_temp, max_temp = state_dict['temperature']
    input_format['average_temperature'] = max_temp-min_temp


    ##input_format['cur_time_start'], input_format['cur_time_end'] = state_dict['cur_time']

    input_format['cur_days'] = state_dict['cur_date'].weekday()
    
    
    
    return (list(input_format.values()))