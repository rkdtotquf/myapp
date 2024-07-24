import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

# CSV 파일 경로
file_path = '202312_202312_주민등록인구및세대현황_월간.csv'

# 데이터 로드
data = pd.read_csv(file_path, encoding='cp949')

# 스트림릿 페이지 제목
st.title('남자와 여자 비율 그래프')

# 사용자 입력: 시 선택
regions = data['행정구역'].unique()
selected_region = st.selectbox('시를 선택하세요:', regions)

# 선택한 시의 데이터 필터링
region_data = data[data['행정구역'] == selected_region]

# 남자와 여자 인구수 가져오기
male_population = int(region_data['2023년12월_남자 인구수'].str.replace(',', '').values[0])
female_population = int(region_data['2023년12월_여자 인구수'].str.replace(',', '').values[0])

# 그래프 그리기
fig, ax = plt.subplots()
ax.bar(['남자', '여자'], [male_population, female_population], color=['blue', 'pink'])
ax.set_ylabel('인구수')
ax.set_title(f'{selected_region}의 남자와 여자 비율')

# 그래프 출력
st.pyplot(fig)

streamlit run streamlit_app.py
