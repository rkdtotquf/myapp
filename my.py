import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

# CSV 파일 경로
file_path = '202312_202312_주민등록인구및세대현황_월간.csv'

# 데이터 로드
data = pd.read_csv(file_path, encoding='cp949')

# 스트림릿 페이지 제목
st.title('남녀 비율 그래프')

# 사용자 입력: 시, 군, 구 선택
regions = data['행정구역'].unique()
selected_region = st.selectbox('시, 군, 구를 선택하세요:', regions)

# 선택한 지역의 데이터 필터링
region_data = data[data['행정구역'] == selected_region]

# 남자와 여자 인구수
male_population = int(region_data['2023년12월_남자 인구수'].str.replace(',', '').values[0])
female_population = int(region_data['2023년12월_여자 인구수'].str.replace(',', '').values[0])

# 남녀 비율 계산
total_population = male_population + female_population
male_ratio = (male_population / total_population) * 100
female_ratio = (female_population / total_population) * 100

# 그래프 그리기
fig, ax = plt.subplots()
ax.bar(['남자 비율', '여자 비율'], [male_ratio, female_ratio], color=['blue', 'red'])
ax.set_ylabel('비율 (%)')
ax.set_ylim(0, 100)
ax.set_title(f'{selected_region}의 남녀 비율')

# 그래프 출력
st.pyplot(fig)
