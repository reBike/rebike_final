# **🌳 What is ReBike?**

---

> 생활 쓰레기 종류 AI 분석 및 분리수거 생활화를 위한 플랫폼
> 

→ ai 이미지 인식 구동 움짤 첨부

## 🪵 **System Architecture**

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/15f8c624-684d-4661-b1cb-875dbe6f27d1/Untitled.png)

## 🌵 **Tech Stack**

## 🌸 **Core Screens**

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5da3e36d-bb84-40a3-a12f-9d70c347369a/Untitled.png)

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
    

### Mainpage (gif 넣기)

- UploadImage (polling)
    
    ![업로드이미지.gif](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5011ad02-896a-4901-9a71-b884efabc7a8/%E1%84%8B%E1%85%A5%E1%86%B8%E1%84%85%E1%85%A9%E1%84%83%E1%85%B3%E1%84%8B%E1%85%B5%E1%84%86%E1%85%B5%E1%84%8C%E1%85%B5.gif)
    
- PopularTrash
    
    ![인기쓰레기.gif](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6f43cfc2-efcf-4ae9-b7df-d60e1373de69/%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%80%E1%85%B5%E1%84%8A%E1%85%B3%E1%84%85%E1%85%A6%E1%84%80%E1%85%B5.gif)
    

### Signup/Login

- Register
    
    ![로그인.gif](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5ae7fe6c-5ecf-456d-a4c1-b587f81ccd34/%E1%84%85%E1%85%A9%E1%84%80%E1%85%B3%E1%84%8B%E1%85%B5%E1%86%AB.gif)
    

### MyPage

- MyTrashcan → 올렸던 사진들을 모두 확인가능
autosave - On : 올린 사진을 자동 저장 / Off : 저장되지 않음
- Graph → 올린 사진의 종류와 수 파악 가능
Default : 지금까지 올렸던 총 사진 종류, 개수
시작 날짜, 끝 날짜를 지정하여 원하는 날짜에 올린 쓰레기 종류 확인
- Challenge → 사진을 올렸을 때 활성화
유저들이 직접 시도하면서 찾는 재미
- Change Info → 비밀번호, 닉네임 변경

## 🌿 ERD

![스크린샷 2022-08-04 오후 2.06.49.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6f9ab2c3-1ffe-4208-bfee-c7d33ba37734/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-08-04_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_2.06.49.png)

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

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/345a6a7f-500e-4fae-aad5-b9c5904fe83c/Untitled.png)

- used_library
    - `elasticsearch`
    - `django_elasticsearch_dsl`
- setup_es.py
    - elastic_search default data setter
        1. make connection with `django_elasticsearch_dsl`
            
            ![스크린샷 2022-08-04 오후 3.26.59.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/711b5e50-f665-4f10-b94b-29fed8e42289/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-08-04_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_3.26.59.png)
            
        2. make default data by using `search_cofig.json` 
            
            ![스크린샷 2022-08-04 오후 3.27.30.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5e595271-368c-446b-b866-7ad1a345d2b7/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-08-04_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_3.27.30.png)
            
            ![스크린샷 2022-08-04 오후 3.28.19.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/101f0ac1-4438-4f95-988c-027114af4029/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-08-04_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_3.28.19.png)
            
        3. bulk default data on elastic_search
            
            ![스크린샷 2022-08-04 오후 3.28.40.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0b6ee636-3a3f-4328-8b26-cc5d1d961a22/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-08-04_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_3.28.40.png)
            
- elastic_search on Search api
    - get  search_value from query_param
        
        ![스크린샷 2022-08-04 오후 3.29.34.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/58b20484-862a-4158-9c73-13e11640af2a/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-08-04_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_3.29.34.png)
        
    - make connection with elastic_search by using `django_elasticsearch_dsl`
        
        ![스크린샷 2022-08-04 오후 3.30.35.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a08266b0-8ed0-4a69-b6c8-ae7cfbdfea8e/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-08-04_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_3.30.35.png)
        
    - get data which contained key that has correlation with search_value
    - example
        1. send request
            
            ![스크린샷 2022-08-04 오후 4.30.58.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c5b5b496-3fd8-4379-9f9b-9062a1b788cf/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-08-04_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_4.30.58.png)
            
        2. output
            
            ![스크린샷 2022-08-04 오후 4.31.28.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/22d5823c-7c81-4825-999c-5872cd7683c1/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-08-04_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_4.31.28.png)
            
- why_elastic_search?
    - elastic_search has bunch of useful functions with searching data
    - elastic_search is much lighter than other DB
        
        ![스크린샷 2022-08-04 오후 3.44.22.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/debdadeb-8cdd-486f-af0b-c9a45d4a3cd5/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-08-04_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_3.44.22.png)
        

### KIBANA

- 일라스틱 서치의 각 데이터들을 시각화하며, 해당 데이터들을 관리하는데 도움을 주는 프로그램입니다.
- 추후. 데이터 관리 및, 데이터 시각화를 통한 보다 좋은 개발환경을 구현하기 위해 사용,

![스크린샷 2022-08-04 오후 2.19.50.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6f7e567c-4025-453c-b138-26ee73d28524/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-08-04_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_2.19.50.png)

## 🪴 **AI**

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c8db2b0b-5f53-49da-a26c-7bc13b443ddb/Untitled.png)

![train_batch0.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c7df8204-e32f-4596-bc61-c490e1f5c522/train_batch0.jpg)

![train_batch2.jpg](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/22331509-982c-4ed4-97ff-7b1a423abceb/train_batch2.jpg)

![results.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1b7aeeb1-1ae7-4851-8d25-85924f042e75/results.png)

![P_curve.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bf03523e-a0b9-41ae-a252-900b49fe7129/P_curve.png)

## JWT

- used_library
    - `djangorestframework-jwt`
- JWT_Settings.py
    - set JWT’s default_settings
        
        ![스크린샷 2022-08-04 오후 3.51.12.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f740b00e-0f78-439b-bfba-de15bc7b47f1/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA_2022-08-04_%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE_3.51.12.png)
        
- JWT on frontEND
    - restore tokens by using redux
    - if we need some user data, we don’t need to make connection with backend
    by opening JWT payload, we can get user data
- JWT on backEND
    - after we identify user by check login data, give authorization by using JWT
    - by using refresh_token, we enhanced our security level

## 💻 Monitoring

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/dba112d2-d844-4e25-83f6-3c14127debb6/Untitled.png)

## Prometheus

- exporter가 매트릭을 수집하고 HTTP 통신을 통해 metric data를 가져갈 수 있게 /metrics 라는 HTTP 엔드포인트를 제공한다. 그러면 Prometheus server가 이 exporter의 엔드포인트에 HTTP GET 요청을 이용하여 metric data를 pull 한다.
- 해당 노드의 metric data

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/60d4b652-1c46-4f25-9575-44b3a48cf5c0/Untitled.png)

## Grafana

- Prometheus의 시각화 도구가 부족하여 이를 직접 사용하지는 않고 대게 Grafana라는 Data Visualization tool을 이용하여 시각화하고 있다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2e812724-95c4-4e18-b9b9-57802e8bcd5a/Untitled.png)

CPU load / RAM usage / Memory swap

## Cadvisor

- 생성된 도커 컨테이너등에 대한 데이터를 수집해준다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8c2a04aa-687d-4d67-9815-025e8229dc4b/Untitled.png)

## **How to Start**

백앤드 프론트 합치고…

## **Project Tree**

프로젝트 폴더 구조

# ™️ⁱ **Members of Team-E**
