
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, request
import json
from faker import Faker
from difflib import SequenceMatcher

jobs = [
        "의회의원/고위공무원 및 공공단체임원",
        "기업고위임원",
        "정부행정 관리자",
        "경영지원 관리자",
        "기타 행정 및 경영지원 관리자",
        "연구 관리자",
        "교육 관리자",
        "법률/경찰/소방 및 교도 관리자",
        "보험 및 금융 관리자",
        "보건의료관련 관리자",
        "사회복지관련 관리자",
        "문화/예술/디자인 및 영상관련 관리자",
        "정보통신관련 관리자",
        "기타 전문서비스 관리자",
        "건설 및 광업 관련 관리자",
        "전기/가스 및 수도 관련 관리자",
        "제품 생산관련 관리자",
        "기타 건설/전기 및 생산 관련 관리자",
        "영업 및 판매 관련 관리자",
        "운송관련 관리자",
        "숙박/여행/오락 및 스포츠 관련 관리자",
        "음식서비스관련 관리자",
        "환경/청소 및 경비 관련 관리자",
        "기타 판매 및 고객 서비스 관리자",
        "생명과학 연구원",
        "자연과학 연구원",
        "인문과학 연구원",
        "사회과학 연구원",
        "생명과학 시험원",
        "농림어업관련 시험원",
        "자연과학 시험원",
        "컴퓨터 하드웨어 기술자 및 연구원",
        "통신공학 기술자 및 연구원",
        "컴퓨터시스템 설계 및 분석가",
        "시스템 소프트웨어 개발자",
        "응용 소프트웨어 개발자",
        "데이터베이스 개발자",
        "네트워크시스템 개발자",
        "컴퓨터 보안 전문가",
        "웹 및 멀티미디어 기획자",
        "웹 개발자",
        "정보 시스템 운영자",
        "통신 및 방송송출 장비 기사",
        "건축가 및 건축공학 기술자",
        "토목공학 기술자",
        "조경 기술자",
        "도시 및 교통설계 전문가",
        "측량 및 지리정보 전문가",
        "건설자재 시험원",
        "화학공학 기술자 및 연구원",
        "화학공학 시험원",
        "금속 / 재료공학 연구원 및 기술자",
        "금속 / 재료공학 시험원",
        "환경공학 기술자 및 연구원",
        "환경공학 시험원",
        "전기공학 기술자 및 연구원",
        "전자공학 기술자 및 연구원",
        "기계공학 기술자 및 연구원",
        "전기/전자 및 기계 공학 시험원",
        "산업안전 및 위험 관리원",
        "보건위생 및 환경 검사원",
        "비파괴 검사원",
        "항공기 조종사",
        "선장/항해사 및 도선사",
        "관제사",
        "식품공학 기술자 및 연구원",
        "섬유공학 기술자 및 연구원",
        "가스/에너지 기술자 및 연구원",
        "소방공학 기술자 및 연구원",
        "식품/섬유 공학 및 에너지 시험원",
        "캐드원",
        "기타 공학관련 기술자 및 시험원",
        "전문 의사",
        "일반 의사",
        "한의사",
        "치과 의사",
        "수의사",
        "약사 및 한약사",
        "간호사",
        "영양사",
        "임상병리사",
        "방사선사",
        "치과기공사",
        "치과위생사",
        "의지보조기기사",
        "물리 및 작업 치료사",
        "임상 심리사 및 기타 치료사",
        "응급구조사",
        "위생사",
        "안경사",
        "의무기록사",
        "간호조무사",
        "안마사",
        "사회복지사",
        "보육 교사",
        "직업상담사 및 취업 알선원",
        "상담 전문가 및 청소년 지도사",
        "시민 단체 활동가",
        "기타 사회복지관련 종사원",
        "성직자",
        "기타 종교관련 종사자",
        "대학 교수",
        "대학 시간강사",
        "중/고등학교 교사",
        "초등학교 교사",
        "특수교육 교사",
        "유치원 교사",
        "문리 및 어학 강사",
        "컴퓨터 강사",
        "기술 및 기능계 강사",
        "예능 강사",
        "학습지 및 방문 교사",
        "기타 문리/기술 및 예능 강사",
        "장학관/연구관 및 교육 관련 전문가",
        "대학 교육조교",
        "보조 교사 및 기타 교사",
        "판사 및 검사",
        "변호사",
        "법무사 및 집행관",
        "변리사",
        "정부 및 공공 행정 전문가",
        "인사 및 노사 관련 전문가",
        "회계사",
        "세무사",
        "관세사",
        "경영 및 진단 전문가",
        "투자 및 신용 분석가",
        "자산 운용가",
        "보험 및 금융 상품 개발자",
        "증권 및 외환 딜러",
        "손해사정인",
        "기타 금융 및 보험 관련 전문가",
        "상품기획 전문가",
        "여행상품 개발자",
        "광고 및 홍보 전문가",
        "조사 전문가",
        "행사기획자",
        "감정평가 전문가",
        "해외 영업원",
        "기술 영업원",
        "상품중개인 및 경매사",
        "부동산 컨설턴트 및 중개인",
        "기타 기술영업 및 중개 관련 종사자",
        "작가 및 관련 전문가",
        "번역가",
        "통역가",
        "기자 및 논설위원",
        "출판물 전문가",
        "큐레이터 및 문화재 보존원",
        "사서 및 기록물관리사",
        "감독 및 기술감독",
        "배우 및 모델",
        "아나운서 및 리포터",
        "촬영기사",
        "음향 및 녹음 기사",
        "영상/녹화 및 편집 기사",
        "조명기사 및 영사기사",
        "기타 연극/영화 및 영상 관련 종사자",
        "화가 및 조각가",
        "사진기자 및 사진가",
        "만화가 및 만화영화 작가",
        "국악 및 전통예능인",
        "지휘자/작곡가 및 연주가",
        "가수 및 성악가",
        "무용가 및 안무가",
        "제품 디자이너",
        "패션 디자이너",
        "실내장식 디자이너",
        "시각 디자이너",
        "웹 및 멀티미디어 디자이너",
        "경기감독 및 코치",
        "직업 운동선수",
        "경기심판 및 경기기록원",
        "스포츠 및 레크레이션 강사",
        "기타 스포츠 및 레크레이션 관련 전문가",
        "연예인 및 스포츠 매니저",
        "마술사 및 기타 문화/ 예술 관련 종사자",
        "조세행정 사무원",
        "관세행정 사무원",
        "병무행정 사무원",
        "국가/지방 및 공공행정 사무원",
        "기획 및 마케팅 사무원",
        "인사 및 교육/훈련 사무원",
        "자재관리 사무원",
        "생산 및 품질 관리 사무원",
        "무역 사무원",
        "운송 사무원",
        "총무 사무원",
        "회계 사무원",
        "경리 사무원",
        "비서",
        "전산 자료 입력원 및 사무 보조원",
        "출납창구 사무원",
        "보험 심사원 및 사무원",
        "금융관련 사무원",
        "신용 추심원",
        "법률관련 사무원",
        "감사 사무원",
        "통계관련 사무원",
        "여행 사무원",
        "안내 / 접수 사무원 및 전화교환원",
        "고객 상담 및 모니터 요원",
        "기타 사무원",
        "경찰관",
        "소방관",
        "소년보호관 및 교도관",
        "경호원",
        "청원 경찰",
        "무인 경비원",
        "기타 경호 및 보안 관련 종사원",
        "간병인",
        "기타 의료/복지 관련 서비스 종사원",
        "이용사",
        "미용사",
        "피부미용 및 체형관리사",
        "메이크업 아티스트 및 분장사",
        "애완동물 미용사",
        "기타 미용관련 서비스 종사원",
        "결혼 상담원 및 웨딩플래너",
        "혼례 종사원",
        "장례 상담원 및 장례 지도사",
        "기타 이미용/예식 및 의료보조 서비스 종사원",
        "항공기 객실승무원",
        "선박 및 열차 객실승무원",
        "여행 및 관광통역 안내원",
        "숙박시설 서비스원",
        "오락시설 서비스원",
        "기타 여가 및 스포츠 관련 종사원",
        "한식 주방장 및 조리사",
        "중식 주방장 및 조리사",
        "양식 주방장 및 조리사",
        "일식 주방장 및 조리사",
        "기타 주방장 및 조리사",
        "바텐더",
        "웨이터",
        "기타 음식서비스 종사원",
        "자동차 영업원",
        "제품 및 광고 영업원",
        "보험 설계사 및 간접투자증권 판매인",
        "상점 판매원",
        "매표원 및 복권 판매원",
        "매장계산원 및 요금정산원",
        "상품 대여원",
        "방문 판매원",
        "통신서비스판매원",
        "텔레마케터",
        "인터넷 판매원",
        "노점 및 이동 판매원",
        "홍보 도우미 및 판촉원",
        "곡식작물 재배원",
        "채소 및 특용작물 재배원",
        "과수작물 재배원",
        "원예작물 재배원",
        "조경원",
        "낙농업관련 종사원",
        "가축 사육 종사원",
        "기타 사육관련 종사원",
        "조림/영림 및 벌목원",
        "임산물채취 및 기타 임업 관련 종사원",
        "양식원",
        "어부 및 해녀",
        "제빵원 및 제과원",
        "떡제조원",
        "정육원 및 도축원",
        "식품 및 담배 등급원",
        "김치 및 밑반찬 제조 종사원",
        "기타 식품가공관련 종사원",
        "패턴사",
        "재단사",
        "재봉사",
        "제화원",
        "기타 섬유 및 가죽 관련 기능 종사원",
        "한복 제조원",
        "양장 및 양복 제조원",
        "모피 및 가죽의복 제조원",
        "의복/가죽 및 모피 수선원",
        "기타 의복 제조원",
        "목제품 제조관련 종사원",
        "가구 제조 및 수리원",
        "악기제조 및 조율사",
        "간판 제작 및 설치원",
        "금형원",
        "주조원",
        "단조원",
        "제관원",
        "판금원",
        "용접원",
        "자동차 정비원",
        "항공기 정비원",
        "선박 정비원",
        "철도 기관차 및 전동차 정비원",
        "기타 운송장비 정비원",
        "공업기계 설치 및 정비원",
        "승강기 설치 및 정비원",
        "물품 이동 장비 설치 및 정비원",
        "냉동/냉장 /공조기 설치 및 정비원",
        "보일러 설치 및 정비원",
        "건설 및 광업기계 설치 및 정비원",
        "농업용 및 기타 기계장비 설치 및 정비원",
        "가전제품 설치 및 수리원",
        "기타 전기/전자기기 설치 및 수리원",
        "산업전공",
        "내선전공",
        "외선전공",
        "강구조물 가공원 및 건립원",
        "경량 철골공",
        "철근공",
        "콘크리트공",
        "건축 석공",
        "건축 목공",
        "조적공 및 석재 부설원",
        "기타 건설관련 기능 종사원",
        "미장공",
        "방수공",
        "단열공",
        "바닥재 시공원",
        "도배공 및 유리 부착원",
        "건축 도장공",
        "섀시 조립 및 설치원",
        "기타 건축마감관련 기능 종사원",
        "광원/채석원 및 석재 절단원",
        "철로 설치 및 보수원",
        "기타 채굴 및 토목 관련 종사자",
        "영상 및 관련 장비 설치 및 수리원",
        "통신 및 관련 장비 설치 및 수리원",
        "통신/방송 및 인터넷 케이블 설치 및 수리원",
        "공예원",
        "귀금속 및 보석 세공원",
        "건설 배관공",
        "공업 배관공",
        "기타 배관공",
        "배관 세정원 및 방역원",
        "기타 기능관련 종사원",
        "제분 및 도정 관련 기계 조작원",
        "곡물가공제품 기계 조작원",
        "육류/어패류 및 낙농품 가공 기계조작원",
        "과실 및 채소 관련 기계조작원",
        "음료 제조관련 기계 조작원",
        "기타 식품가공관련 기계조작원",
        "섬유제조 기계조작원",
        "표백 및 염색 관련 조작원",
        "직조기 및 편직기 조작원",
        "신발제조기 조작원 및 조립원",
        "기타 직물 및 신발 관련 기계조작원 및 조립원",
        "세탁관련 기계조작원",
        "석유 및 천연가스제조 관련 제어장치 조작원",
        "화학물 가공장치 조작원",
        "기타 석유 및 화학물 가공장치 조작원",
        "화학제품 생산기 조작원",
        "타이어 및 고무제품 생산기 조작원",
        "플라스틱제품 생산기 조작원",
        "고무 및 플라스틱 제품 조립원",
        "주조기 조작원",
        "단조기 조작원",
        "용접기 조작원",
        "금속가공관련 제어장치 조작원",
        "금속가공 기계조작원",
        "제관기 조작원",
        "판금기 조작원",
        "도장기 조작원",
        "도금 및 금속분무기 조작원",
        "유리제조 및 가공기 조작원",
        "점토제품 생산기 조작원",
        "시멘트 및 광물제품 제조기 조작원",
        "광석 및 석제품 가공기 조작원",
        "기타 비금속제품관련 생산기 조작원",
        "금속공작기계 조작원",
        "냉/난방 관련 설비 조작원",
        "자동조립라인 및 산업용 로봇 조작원",
        "자동차 조립원",
        "자동차 부분품 조립원",
        "운송장비 조립원",
        "일반기계 조립원",
        "금속기계부품 조립원",
        "발전 및 배전장치 조작원",
        "전기 및 전자 설비 조작원",
        "전기 부품 및 제품제조 기계조작원",
        "전자 부품 및 제품 제조 기계조작원",
        "전기/전자 부품 및 제품 조립원",
        "철도 및 전동차 기관사",
        "화물열차 차장 및 관련 종사원",
        "택시 운전원",
        "버스 운전원",
        "화물차 및 특수차 운전원",
        "기타 자동차 운전원",
        "물품이동 장비 조작원",
        "건설 및 채굴 기계 운전원",
        "선박 갑판승무원 및 관련 종사원",
        "상/하수도 처리장치 조작원",
        "재활용 처리 및 소각로 조작원",
        "목재 가공관련 기계 조작원",
        "가구조립원",
        "펄프 및 종이 제조장치 조작원",
        "종이제품 생산기 조작원",
        "기타 목재 및 종이 관련 기계조작원",
        "인쇄기 조작원",
        "사진인화 및 현상기 조작원",
        "기타 제조관련 기계 조작원",
        "건설 및 광업 단순 종사원",
        "하역 및 적재 단순 종사원",
        "우편물 집배원",
        "택배원",
        "음식 배달원",
        "기타 배달원",
        "제조관련 단순 종사원",
        "청소원",
        "환경 미화원 및 재활용품 수거원",
        "경비원",
        "검표원",
        "가사 도우미",
        "육아 도우미",
        "패스트푸드원",
        "주방 보조원",
        "주유원",
        "기타 판매관련 단순 종사원",
        "농림어업관련 단순 종사원",
        "계기 검침원 및 가스점검원",
        "수금원",
        "주차 관리원 및 안내원",
        "구두 미화원",
        "세탁원 및 다림질원",
        "기타 서비스관련 단순 종사원",
        "영관급 이상",
        "위관급",
        "장기 부사관 및 준위",
    ]



app = Flask(__name__)

@app.route('/')
def hello_world():
    global jobs

    return render_template('index.html')

@app.post('/result/')
def result():
    global jobs

    keyword = request.form['keyword']
    job_dict = {}
    for job in jobs:
        job_dict[job] = SequenceMatcher(None , keyword,job).ratio()
    job_list = [i[0] for i in sorted(job_dict.items(), key=lambda x :x[1], reverse=True)[1:11]]

    result = json.dumps(job_list)
    return result

    return render_template('result.html')





