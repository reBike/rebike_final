# **🌳 What is ReBike?**

---

> 생활 쓰레기 종류 AI 분석 및 분리수거 생활화를 위한 플랫폼
> 

## 🪵 **System Architecture**

<img src="https://user-images.githubusercontent.com/41159837/183132843-212abe8a-5000-4acd-9a17-a8deab497ac2.png" width="100%" height="100%"/>

## 🌵 **Tech Stack**
|Dev-Ops|<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=Docker&logoColor=black"> <img src="https://img.shields.io/badge/Amazon EC2-FF9900?style=for-the-badge&logo=Amazon%20EC2&logoColor=white"> <img src="https://img.shields.io/badge/S3%20Bucket-569A31?style=for-the-badge&logo=Amazon%20S3&logoColor=white"> <img src="https://img.shields.io/badge/Amazon RDS-527FFF?style=for-the-badge&logo=Amazon#20RDS&logoColor=black"> <img src="https://img.shields.io/badge/NGINX-009639?style=for-the-badge&logo=NGINX&logoColor=black"> |
|-------|--------|
|__Frontend__| <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=React&logoColor=black"> <img src="https://img.shields.io/badge/Redux-764ABC?style=for-the-badge&logo=Redux&logoColor=black"> <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=TypeScript&logoColor=black"> <img src="https://img.shields.io/badge/MUI-007FFF?style=for-the-badge&logo=MUI&logoColor=black"> <img src="https://img.shields.io/badge/styled%20components-DB7093?style=for-the-badge&logo=styled%20components&logoColor=black"> |
|__Backend__| <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white"> <img src="https://img.shields.io/badge/Gunicorn-499848?style=for-the-badge&logo=Gunicorn&logoColor=black"> <img src="https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=Swagger&logoColor=black"> <img src="https://img.shields.io/badge/RabbitMQ-FF6600?style=for-the-badge&logo=RabbitMQ&logoColor=black"> <img src="https://img.shields.io/badge/Elasticsearch-005571?style=for-the-badge&logo=Elasticsearch&logoColor=black"> <img src="https://img.shields.io/badge/Kibana-005571?style=for-the-badge&logo=Kibana&logoColor=black"> <img src="https://img.shields.io/badge/Celery-37814A?style=for-the-badge&logo=Celery&logoColor=black"> <img src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=Redis&logoColor=black"> |
|__DB__| <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=MySQL&logoColor=black"> |
|__AI__| <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=PyTorch&logoColor=black"> <img src="https://img.shields.io/badge/YOLOv5-00FFFF?style=for-the-badge&logo=YOLO&logoColor=black"> <img src="https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=Google%20Colab&logoColor=black"> |
|__Monitoring__| <img src="https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=Prometheus&logoColor=black"> <img src="https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=Grafana&logoColor=black"> <img src="https://img.shields.io/badge/cAdvisor-2496ED?style=for-the-badge&logo=cAdvisor&logoColor=white"> |
|__Others__| <img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=black"> <img src="https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=Slack&logoColor=black"> <img src="https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=Notion&logoColor=white"> <img src="https://img.shields.io/badge/GitKraken-179287?style=for-the-badge&logo=GitKraken&logoColor=black"> <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=black"> |


## 🌸 **Core Screens**

<img src="https://user-images.githubusercontent.com/41159837/183132826-5238c9e3-b067-4cfc-a2b3-bed4c43f6dbd.png" width="50%" height="50%"/>

### **Redux**

```
acitions
⎿ DecodeActions.tsx
	dispatch가 어떤 type에 따라 함수를 실행해줄지 정한다. state값을 어떻게 변경할지 정해주는 파일
	인자로 token값을 받아서 그걸 디코딩 해준다 . 
	그리고 payload에 [success, action[success, payload]] 를 설정

⎿ ImgIDReducer.tsx
    dispatch로 실행할 액션 값 1개 (SAVE_ID) 이걸로 id 값을 넘겨준다.

reducer
⎿ DecodeReducer.tsx
	state 초기값 설정 및 dispatch를 포함하고 있는 곳 action 이 들어와서 action.payload로 
	id, alias 를 가져와 state값을 dispatch에서 넘어온 데이터를 활용해 변경해준다 .(전역관리 시작)
	ex.	const userIdtoRedux = ReduxModule().decodeInfo?.id;
	

⎿ ImgIDReducer.tsx
    SAVE_ID 타입으로 dispatch 가 실행됐으면 거기서 저장된 payload를 가져와 그 값을 리턴해준다.
    dispatch(save_ID(res.data.image_id)); 실행후 itemID 리턴
	  ex. const itemID = useSelector((state: RootReducerType) => state.ImgIDReducer);

⎿ index.tsx
    root 리듀서 관리 만들어 놓은 DecodeReducer, ImgIDReducer를 총괄한다. app.tsx에서 불러와 사용
```

> ReduxModule
토큰이 있을 때만 dispatch를 통해 id를 가져오려고 따로 모듈로 뺴놓음
토큰을 decoderedux를 통해 디코딩시킨 후 id를 리턴한다.
> 

- 정리
    1. redux를 통해 token decode 후 uuid 전역관리 
    2. 컴포넌트 재활용을 위해 upload한 이미지 및 내가 버린 쓰레기 상세페이지를 위한 trash_id 전역관리 
    

### Mainpage

- Search
    
    <img src="https://user-images.githubusercontent.com/41159837/183141339-a913037d-2bad-4d61-89e8-139116a8f34d.gif" width="50%" height="50%"/>

- UploadImage (polling)
    
    <img src="https://user-images.githubusercontent.com/41159837/183141344-7c23a598-5be9-40b8-a18e-7b0efc533216.gif" width="50%" height="50%"/>
    
- PopularTrash
    
    <img src="https://user-images.githubusercontent.com/41159837/183141301-d4fbe806-6044-4c7b-8a9a-1d31ecd3e416.gif" width="50%" height="50%"/>
    

### Sign up/ Sign in

- Sign Up
    
    <img src="https://user-images.githubusercontent.com/41159837/183135163-ba83f739-d076-45fb-bd74-9cc560f6af85.gif" width="50%" height="50%"/>
    
- Sign In
    
    <img src="https://user-images.githubusercontent.com/41159837/183135150-b8a752ed-df17-4ce0-a4b4-ac115a8c143f.gif" width="50%" height="50%"/>

### MyPage

- MyTrashcan → 올렸던 사진들을 모두 확인가능
autosave - On : 올린 사진을 자동 저장 / Off : 저장되지 않음
    <img src="https://user-images.githubusercontent.com/41159837/183141351-b185a97e-97fd-46d7-afb6-94543aa1b802.gif" width="50%" height="50%"/>
    
- Graph → 올린 사진의 종류와 수 파악 가능    
Default : 지금까지 올렸던 총 사진 종류, 개수    
시작 날짜, 끝 날짜를 지정하여 원하는 날짜에 올린 쓰레기 종류 확인    
    <img src="https://user-images.githubusercontent.com/41159837/183141349-7dd721c0-40c3-4751-b0c9-cca96a6cdc62.gif" width="50%" height="50%"/>
    
- Challenge → 사진을 올렸을 때 활성화/Change Info → 비밀번호, 닉네임 변경/Log Out

    <img src="https://user-images.githubusercontent.com/41159837/183141312-e0b49008-be07-4da6-9114-e3afb336b73a.gif" width="50%" height="50%"/>

## 🌿 ERD

<img src="https://user-images.githubusercontent.com/41159837/183132832-e911786b-a2b5-4647-baea-c66199e8ac85.png" width="70%" height="70%"/>

### **users api**

- ***api/users/***
    - `GET` : 회원가입 시 아이디, 닉네임 중복 체크 결과
    - `POST` : 회원 가입 정보 저장
    - `PATCH` : 회원 정보 수정
- ***api/users/auth***
    - `POST` : access token, refresh token 갱신
- ***api/users/autosave***
    - `GET` : 업로드 사진 자동저장 여부
    - `PATCH` : 업로드 사진 자동저장 여부 변경

### **trash api**

- ***api/challenges***
    - `GET` : 모든 도전과제 정보
- ***api/statistics/ranking***
    - `GET` : 인기순으로 정렬된 일주일간의 재활용 데이터
- ***api/users/{user_id}/results/tasks***
    - `POST` : 사용자가 업로드한 사진 분석 비동기 처리
- ***api/users/{user_id}/results/tasks/{task_id}***
    - `GET` : task_id로 분석 완료 여부 확인, 프론트에서 polling
- ***api/users/{user_id}/challenges***
    - `GET` : 사용자가 달성한 도전과제 정보
- ***api/users/{user_id}/pages/{page_number}***
    - `GET` : 사용자가 업로드한 재활용 이미지 데이터, 페이지네이션 이용
- ***api/trash/users/{user_id}/statistics***
    - `GET` : 사용자가 업로드한 모든 재활용 데이터의 통계
- ***api/trash/users/{user_id}/statistics/period/{from_date}/{to_date}***
    - `GET` : 사용자가 설정한 날에 따른 재활용 데이터 통계

### S**earch api**

- ***api/search/***
    - `POST` : value 값에 맞는 검색 결과 반환

### Elastic_search

<img src="https://user-images.githubusercontent.com/41159837/183142243-d5d8a26c-e3b7-4e06-83be-96b45f6d535b.png" width="100%" height="100%"/>

- used_library
    - `elasticsearch`
    - `django_elasticsearch_dsl`
- setup_es.py
    - elastic_search default data setter
        1. make connection with `django_elasticsearch_dsl`
            
            <img src="https://user-images.githubusercontent.com/41159837/183142917-54026b58-761b-42a9-9063-b68f0042b2f8.png" width="50%" height="50%"/>
            
        2. make default data by using `search_cofig.json` 
            
            <img src="https://user-images.githubusercontent.com/41159837/183142923-932df86b-f5d8-413c-bc2e-6debd3871d0f.png" width="50%" height="50%"/>
            
            <img src="https://user-images.githubusercontent.com/41159837/183142925-04062de1-2392-46f7-833b-57d7e80177bc.png" width="50%" height="50%"/>
            
        3. bulk default data on elastic_search
            
            <img src="https://user-images.githubusercontent.com/41159837/183142927-8c397975-1d18-471e-abd5-6e52f6567bf7.png" width="50%" height="50%"/>
            
- elastic_search on Search api
    - get  search_value from query_param
        
        <img src="https://user-images.githubusercontent.com/41159837/183143129-e310f3db-c82d-43fa-852b-38f8487959b2.png"width="50%" height="50%"/>
        
    - make connection with elastic_search by using `django_elasticsearch_dsl`
        
        <img src="https://user-images.githubusercontent.com/41159837/183143135-e499a402-28a3-4b29-a4ab-ae87c2bf8f66.png" width="50%" height="50%"/>
        
    - get data which contained key that has correlation with search_value
    - example
        1. send request
            
            <img src="https://user-images.githubusercontent.com/41159837/183143143-d43d270f-3b6b-4735-96fc-22ac08e445cb.png" width="50%" height="50%"/>
            
        2. output
            
            <img src="https://user-images.githubusercontent.com/41159837/183143147-cb648a62-4f0c-4fa2-85a5-98eecea52d0a.png" width="50%" height="50%"/>
            
- why_elastic_search?
    - elastic_search has bunch of useful functions with searching data
    - elastic_search is much lighter than other DB
        
        <img src="https://user-images.githubusercontent.com/41159837/183143137-83cd72f4-b992-4c5b-bf20-7272b765b5a4.png" width="50%" height="50%"/>
        

### KIBANA

- 일라스틱 서치의 각 데이터들을 시각화하며, 해당 데이터들을 관리하는데 도움을 주는 프로그램입니다.
- 추후. 데이터 관리 및, 데이터 시각화를 통한 보다 좋은 개발환경을 구현하기 위해 사용,

<img src="https://user-images.githubusercontent.com/41159837/183142233-4e4129a6-9ece-4ac5-8f26-b016799938fd.png" width="50%" height="50%"/>

## 🪴 **AI**

<img src="https://user-images.githubusercontent.com/41159837/183143436-45b192d7-9393-421e-9c29-197373b8db84.png" width="70%" height="70%"/>

<img src="https://user-images.githubusercontent.com/41159837/183143428-f90abae0-4f7c-44ef-9028-c47a1bd693cc.jpg" width="30%" height="30%"/><img src="https://user-images.githubusercontent.com/41159837/183143432-a5be1cd3-08b8-4a53-97f3-90d344444d0c.jpg" width="30%" height="30%"/>

<img src="https://user-images.githubusercontent.com/41159837/183143423-fa6d79a9-ade8-4a86-8f8a-f75a27a24622.png" width="50%" height="50%"/>

<img src="https://user-images.githubusercontent.com/41159837/183143419-334ccefb-c836-4f6a-93f4-24dc2b4af605.png" width="50%" height="50%"/>

- Result  
    <img src="https://user-images.githubusercontent.com/41159837/183143416-e56783c1-72db-4ced-860f-2119246c98dd.jpeg" width="30%" height="30%"/>
    <img src="https://user-images.githubusercontent.com/41159837/183143412-6278b796-e52a-411e-b91a-665fbc98bb02.jpg" width="30%" height="30%"/>
## JWT

- used_library
    - `djangorestframework-jwt`
- JWT_Settings.py
    - set JWT’s default_settings
        
        <img src="https://user-images.githubusercontent.com/41159837/183143775-f17eea8b-c3d6-48cc-9ba1-c050fc3072fe.png" width="50%" height="50%"/>
        
- JWT on frontEND
    - restore tokens by using redux
    - if we need some user data, we don’t need to make connection with backend
    by opening JWT payload, we can get user data
    
- JWT on backEND
    - after we identify user by check login data, give authorization by using JWT
    - by using refresh_token, we enhanced our security level

## 💻 Monitoring

<img src="https://user-images.githubusercontent.com/41159837/183143868-35b43d78-a69b-4e3e-a1ba-365234ab67b2.png" width="50%" height="50%"/>

## Prometheus

- exporter가 매트릭을 수집하고 HTTP 통신을 통해 metric data를 가져갈 수 있게 /metrics 라는 HTTP 엔드포인트를 제공한다. 그러면 Prometheus server가 이 exporter의 엔드포인트에 HTTP GET 요청을 이용하여 metric data를 pull 한다.
- 해당 노드의 metric data

<img src="https://user-images.githubusercontent.com/41159837/183143866-e2bb4650-3098-4f79-8e45-c3eb89ef032b.png" width="50%" height="50%"/>

## Grafana

- Prometheus의 시각화 도구가 부족하여 이를 직접 사용하지는 않고 대게 Grafana라는 Data Visualization tool을 이용하여 시각화하고 있다.

<img src="https://user-images.githubusercontent.com/41159837/183143860-5af55454-9527-4844-822a-99984c363178.png" width="50%" height="50%"/>

CPU load / RAM usage / Memory swap

## Cadvisor

- 생성된 도커 컨테이너등에 대한 데이터를 수집해준다.

<img src="https://user-images.githubusercontent.com/41159837/183143853-66b83ff7-1a9a-4d99-a8cf-4a6930214cdc.png" width="50%" height="50%"/>

## **How to Start**



## **Project Tree**



# ™️ⁱ **Members of Team-E**
|이름|개발분야|소개페이지|
|---|---|---|
|🦥김용민|Back-end|https://github.com/Ryokuman
|💛김유림|Back-end,AI|https://github.com/Ellie010707
|🥇박성빈|Back-end|https://github.com/SeongbinPark
|🧚🏻‍♀️이채현|Front-end|https://github.com/chloe1129
|🎹이정우|Front-end|https://github.com/RayLee-Kor
|👼진호병|Front-end|https://github.com/bicco2

