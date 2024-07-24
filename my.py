import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import koreanize-matplotlib

# CSV 파일 경로
file_path = '202406_202406_연령별인구현황_월간.csv'

# 데이터 로드
data = pd.read_csv(file_path, encoding='cp949')

# 스트림릿 페이지 제목
st.title('초등학생 비율 그래프')

# 사용자 입력: 지역 선택
regions = data['행정구역'].unique()
selected_region = st.selectbox('지역을 선택하세요:', regions)

# 선택한 지역의 데이터 필터링
region_data = data[data['행정구역'] == selected_region]

# 초등학생 연령대의 인구수 계산 (6세부터 12세)
elementary_school_population = region_data[['2024년06월_계_6세', '2024년06월_계_7세', '2024년06월_계_8세',
                                             '2024년06월_계_9세', '2024년06월_계_10세', '2024년06월_계_11세',
                                             '2024년06월_계_12세']].sum(axis=1).values[0]

# 총인구수
total_population = int(region_data['2024년06월_계_총인구수'].str.replace(',', '').values[0])

# 초등학생 비율 계산
elementary_school_ratio = (elementary_school_population / total_population) * 100

# 그래프 그리기
fig, ax = plt.subplots()
ax.bar(['초등학생 비율'], [elementary_school_ratio])
ax.set_ylabel('비율 (%)')
ax.set_ylim(0, 100)
ax.set_title(f'{selected_region}의 초등학생 비율')

# 그래프 출력
st.pyplot(fig)
