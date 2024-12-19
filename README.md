## Web Programming Term Project

## Movie Insight (영화 평점 예측 시스템)

## 개요
이 프로젝트는 머신러닝 알고리즘을 활용하여 영화의 평점 예측하고 상세 정보를 제공하는 웹 기반 애플리케이션입니다. TMDB와 OMDB API를 통해 영화 데이터를 수집하고, 다중 회귀 분석을 사용하여 예측을 수행합니다. 또한 HTML, CSS, JavaScript로 구성된 사용자 친화적인 인터페이스를 제공합니다.

## 주요 기능
- TMDB API를 통한 영화 데이터 수집.
- 학습된 머신러닝 모델을 사용한 수익 예측.
- 영화 검색 및 상세 정보를 표시하는 사용자 친화적 웹 인터페이스.

## 사전 요구사항
다음이 시스템에 설치되어 있어야 합니다:
- Python 3.10 이상
- Node.js 20.x 이상
- MongoDB
- pip (Python 패키지 관리자)

## 설치 및 설정

### 1. 저장소 클론
```bash
git clone https://github.com/Deepbluewarn/webprogramming_term_project.git
cd webprogramming_term_project
```

### 2. 백엔드 설정

#### a. 환경 변수 설정
두 개의 `.env` 파일이 필요합니다.

1. 프로젝트 루트
```env
TMDB_API_BASE_URL=https://api.themoviedb.org/3
TMDB_API_KEY=YOUR_KEY
OMDB_API_KEY=YOUR_KEY
```

2. predict_model 디렉토리
```env
MONGODB_CONNECTION_STRING=YOUR_CONNECTION_STRING
```

#### b. 가상 환경 생성
```bash
cd predict_model
python -m venv venv
source venv/bin/activate   # Linux/MacOS
venv\Scripts\activate    # Windows
```

#### c. Python 의존성 설치
```bash
pip install -r requirements.txt
```

### 4. 머신러닝 모델 학습
서버를 실행하기 전에 머신러닝 모델을 학습시키고 저장해야 합니다:
```bash
python model/index.py
```
이 명령어는 지정된 디렉토리에 학습된 모델 파일(`model.pkl`)을 생성합니다.
`predict_model/analysis_plots`에서 분석 결과를 확인할 수 있습니다.

#### 5. Node.js 의존성 설치
```bash
npm install
```

### 3. 애플리케이션 실행

#### b. 프론트엔드 서버 시작
```bash
node app.js
```
애플리케이션은 `http://localhost:4343`에서 접근 가능합니다.

## 사용 방법
1. 웹 브라우저를 열고 `http://localhost:4343`에 접속합니다.
2. 검색창에서 제목으로 영화를 검색하고 포스터를 클릭하여 상세 페이지로 이동합니다.
3. 영화 상세 페이지에서 영화 상세 정보와 예측된 수익을 확인합니다.

## 향후 개선 사항
- 추가 데이터 소스 지원(Rotten Tomatoes, Google Trends 등).
- 고급 머신러닝 기법을 활용한 예측 모델 개선.
- 사용자 경험을 향상시키기 위한 UI 개선.

## 라이선스
이 프로젝트는 MIT 라이선스를 따릅니다.
