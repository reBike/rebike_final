# **๐ณย What is ReBike?**

---

> ์ํ ์ฐ๋ ๊ธฐ ์ข๋ฅ AI ๋ถ์ ๋ฐ ๋ถ๋ฆฌ์๊ฑฐ ์ํํ๋ฅผ ์ํ ํ๋ซํผ
> 

## ๐ชตย **System Architecture**

<img src="https://user-images.githubusercontent.com/41159837/183132843-212abe8a-5000-4acd-9a17-a8deab497ac2.png" width="100%" height="100%"/>

## ๐ตย **Tech Stack**
|Dev-Ops|<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=Docker&logoColor=black"> <img src="https://img.shields.io/badge/Amazon EC2-FF9900?style=for-the-badge&logo=Amazon%20EC2&logoColor=white"> <img src="https://img.shields.io/badge/S3%20Bucket-569A31?style=for-the-badge&logo=Amazon%20S3&logoColor=white"> <img src="https://img.shields.io/badge/Amazon RDS-527FFF?style=for-the-badge&logo=Amazon#20RDS&logoColor=black"> <img src="https://img.shields.io/badge/NGINX-009639?style=for-the-badge&logo=NGINX&logoColor=black"> |
|----------|:-------------:|
|__Frontend__| <img src="https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=React&logoColor=black"> <img src="https://img.shields.io/badge/Redux-764ABC?style=for-the-badge&logo=Redux&logoColor=black"> <img src="https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=TypeScript&logoColor=black"> <img src="https://img.shields.io/badge/MUI-007FFF?style=for-the-badge&logo=MUI&logoColor=black"> <img src="https://img.shields.io/badge/styled%20components-DB7093?style=for-the-badge&logo=styled%20components&logoColor=black"> |
|__Backend__| <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white"> <img src="https://img.shields.io/badge/Gunicorn-499848?style=for-the-badge&logo=Gunicorn&logoColor=black"> <img src="https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=Swagger&logoColor=black"> <img src="https://img.shields.io/badge/RabbitMQ-FF6600?style=for-the-badge&logo=RabbitMQ&logoColor=black"> <img src="https://img.shields.io/badge/Elasticsearch-005571?style=for-the-badge&logo=Elasticsearch&logoColor=black"> <img src="https://img.shields.io/badge/Kibana-005571?style=for-the-badge&logo=Kibana&logoColor=black"> <img src="https://img.shields.io/badge/Celery-37814A?style=for-the-badge&logo=Celery&logoColor=black"> <img src="https://img.shields.io/badge/Redis-DC382D?style=for-the-badge&logo=Redis&logoColor=black"> |
|__DB__| <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=MySQL&logoColor=black"> |
|__AI__| <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=PyTorch&logoColor=black"> <img src="https://img.shields.io/badge/YOLOv5-00FFFF?style=for-the-badge&logo=YOLO&logoColor=black"> <img src="https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=Google%20Colab&logoColor=black"> |
|__Monitoring__| <img src="https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge&logo=Prometheus&logoColor=black"> <img src="https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=Grafana&logoColor=black"> <img src="https://img.shields.io/badge/cAdvisor-2496ED?style=for-the-badge&logo=cAdvisor&logoColor=white"> |
|__Others__| <img src="https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=Postman&logoColor=black"> <img src="https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=Slack&logoColor=black"> <img src="https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=Notion&logoColor=white"> <img src="https://img.shields.io/badge/GitKraken-179287?style=for-the-badge&logo=GitKraken&logoColor=black"> <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=black"> |


## ๐ธย **Core Screens**

<img src="https://user-images.githubusercontent.com/41159837/183132826-5238c9e3-b067-4cfc-a2b3-bed4c43f6dbd.png" width="50%" height="50%"/>

### **Redux**

```
acitions
โฟ DecodeActions.tsx
	dispatch๊ฐ ์ด๋ค type์ ๋ฐ๋ผ ํจ์๋ฅผ ์คํํด์ค์ง ์ ํ๋ค. state๊ฐ์ ์ด๋ป๊ฒ ๋ณ๊ฒฝํ ์ง ์ ํด์ฃผ๋ ํ์ผ
	์ธ์๋ก token๊ฐ์ ๋ฐ์์ ๊ทธ๊ฑธ ๋์ฝ๋ฉ ํด์ค๋ค . 
	๊ทธ๋ฆฌ๊ณ  payload์ [success, action[success, payload]] ๋ฅผ ์ค์ 

โฟ ImgIDReducer.tsx
    dispatch๋ก ์คํํ  ์ก์ ๊ฐ 1๊ฐ (SAVE_ID) ์ด๊ฑธ๋ก id ๊ฐ์ ๋๊ฒจ์ค๋ค.

reducer
โฟ DecodeReducer.tsx
	state ์ด๊ธฐ๊ฐ ์ค์  ๋ฐ dispatch๋ฅผ ํฌํจํ๊ณ  ์๋ ๊ณณ action ์ด ๋ค์ด์์ action.payload๋ก 
	id, alias ๋ฅผ ๊ฐ์ ธ์ state๊ฐ์ dispatch์์ ๋์ด์จ ๋ฐ์ดํฐ๋ฅผ ํ์ฉํด ๋ณ๊ฒฝํด์ค๋ค .(์ ์ญ๊ด๋ฆฌ ์์)
	ex.	const userIdtoRedux = ReduxModule().decodeInfo?.id;
	

โฟ ImgIDReducer.tsx
    SAVE_ID ํ์์ผ๋ก dispatch ๊ฐ ์คํ๋์ผ๋ฉด ๊ฑฐ๊ธฐ์ ์ ์ฅ๋ payload๋ฅผ ๊ฐ์ ธ์ ๊ทธ ๊ฐ์ ๋ฆฌํดํด์ค๋ค.
    dispatch(save_ID(res.data.image_id)); ์คํํ itemID ๋ฆฌํด
	  ex. const itemID = useSelector((state: RootReducerType) => state.ImgIDReducer);

โฟ index.tsx
    root ๋ฆฌ๋์ ๊ด๋ฆฌ ๋ง๋ค์ด ๋์ DecodeReducer, ImgIDReducer๋ฅผ ์ด๊ดํ๋ค. app.tsx์์ ๋ถ๋ฌ์ ์ฌ์ฉ
```

> ReduxModule
ํ ํฐ์ด ์์ ๋๋ง dispatch๋ฅผ ํตํด id๋ฅผ ๊ฐ์ ธ์ค๋ ค๊ณ  ๋ฐ๋ก ๋ชจ๋๋ก ๋บด๋์
ํ ํฐ์ decoderedux๋ฅผ ํตํด ๋์ฝ๋ฉ์ํจ ํ id๋ฅผ ๋ฆฌํดํ๋ค.
> 

- ์ ๋ฆฌ
    1. redux๋ฅผ ํตํด token decode ํ uuid ์ ์ญ๊ด๋ฆฌ 
    2. ์ปดํฌ๋ํธ ์ฌํ์ฉ์ ์ํด uploadํ ์ด๋ฏธ์ง ๋ฐ ๋ด๊ฐ ๋ฒ๋ฆฐ ์ฐ๋ ๊ธฐ ์์ธํ์ด์ง๋ฅผ ์ํ trash_id ์ ์ญ๊ด๋ฆฌ 
    

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

- MyTrashcan โ ์ฌ๋ ธ๋ ์ฌ์ง๋ค์ ๋ชจ๋ ํ์ธ๊ฐ๋ฅ <br>
autosave - On : ์ฌ๋ฆฐ ์ฌ์ง์ ์๋ ์ ์ฅ / Off : ์ ์ฅ๋์ง ์์ <br>
    <img src="https://user-images.githubusercontent.com/41159837/183141351-b185a97e-97fd-46d7-afb6-94543aa1b802.gif" width="50%" height="50%"/>
    
- Graph โ ์ฌ๋ฆฐ ์ฌ์ง์ ์ข๋ฅ์ ์ ํ์ ๊ฐ๋ฅ    
Default : ์ง๊ธ๊น์ง ์ฌ๋ ธ๋ ์ด ์ฌ์ง ์ข๋ฅ, ๊ฐ์    
์์ ๋ ์ง, ๋ ๋ ์ง๋ฅผ ์ง์ ํ์ฌ ์ํ๋ ๋ ์ง์ ์ฌ๋ฆฐ ์ฐ๋ ๊ธฐ ์ข๋ฅ ํ์ธ    
    <img src="https://user-images.githubusercontent.com/41159837/183141349-7dd721c0-40c3-4751-b0c9-cca96a6cdc62.gif" width="50%" height="50%"/>
    
- Challenge โ ์ฌ์ง์ ์ฌ๋ ธ์ ๋ ํ์ฑํ/Change Info โ ๋น๋ฐ๋ฒํธ, ๋๋ค์ ๋ณ๊ฒฝ/Log Out

    <img src="https://user-images.githubusercontent.com/41159837/183141312-e0b49008-be07-4da6-9114-e3afb336b73a.gif" width="50%" height="50%"/>

## ๐ฟย ERD

<img src="https://user-images.githubusercontent.com/41159837/183132832-e911786b-a2b5-4647-baea-c66199e8ac85.png" width="70%" height="70%"/>

### **users api**

- ***api/users/***
    - `GET` : ํ์๊ฐ์ ์ ์์ด๋, ๋๋ค์ ์ค๋ณต ์ฒดํฌ ๊ฒฐ๊ณผ
    - `POST` : ํ์ ๊ฐ์ ์ ๋ณด ์ ์ฅ
    - `PATCH` : ํ์ ์ ๋ณด ์์ 
- ***api/users/auth***
    - `POST` : access token, refresh token ๊ฐฑ์ 
- ***api/users/autosave***
    - `GET` : ์๋ก๋ ์ฌ์ง ์๋์ ์ฅ ์ฌ๋ถ
    - `PATCH` : ์๋ก๋ ์ฌ์ง ์๋์ ์ฅ ์ฌ๋ถ ๋ณ๊ฒฝ

### **trash api**

- ***api/challenges***
    - `GET` : ๋ชจ๋  ๋์ ๊ณผ์  ์ ๋ณด
- ***api/statistics/ranking***
    - `GET` : ์ธ๊ธฐ์์ผ๋ก ์ ๋ ฌ๋ ์ผ์ฃผ์ผ๊ฐ์ ์ฌํ์ฉ ๋ฐ์ดํฐ
- ***api/users/{user_id}/results/tasks***
    - `POST` : ์ฌ์ฉ์๊ฐ ์๋ก๋ํ ์ฌ์ง ๋ถ์ ๋น๋๊ธฐ ์ฒ๋ฆฌ
- ***api/users/{user_id}/results/tasks/{task_id}***
    - `GET` : task_id๋ก ๋ถ์ ์๋ฃ ์ฌ๋ถ ํ์ธ, ํ๋ก ํธ์์ polling
- ***api/users/{user_id}/challenges***
    - `GET` : ์ฌ์ฉ์๊ฐ ๋ฌ์ฑํ ๋์ ๊ณผ์  ์ ๋ณด
- ***api/users/{user_id}/pages/{page_number}***
    - `GET` : ์ฌ์ฉ์๊ฐ ์๋ก๋ํ ์ฌํ์ฉ ์ด๋ฏธ์ง ๋ฐ์ดํฐ, ํ์ด์ง๋ค์ด์ ์ด์ฉ
- ***api/trash/users/{user_id}/statistics***
    - `GET` : ์ฌ์ฉ์๊ฐ ์๋ก๋ํ ๋ชจ๋  ์ฌํ์ฉ ๋ฐ์ดํฐ์ ํต๊ณ
- ***api/trash/users/{user_id}/statistics/period/{from_date}/{to_date}***
    - `GET` : ์ฌ์ฉ์๊ฐ ์ค์ ํ ๋ ์ ๋ฐ๋ฅธ ์ฌํ์ฉ ๋ฐ์ดํฐ ํต๊ณ

### S**earch api**

- ***api/search/***
    - `POST` : value ๊ฐ์ ๋ง๋ ๊ฒ์ ๊ฒฐ๊ณผ ๋ฐํ

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

- ์ผ๋ผ์คํฑ ์์น์ ๊ฐ ๋ฐ์ดํฐ๋ค์ ์๊ฐํํ๋ฉฐ, ํด๋น ๋ฐ์ดํฐ๋ค์ ๊ด๋ฆฌํ๋๋ฐ ๋์์ ์ฃผ๋ ํ๋ก๊ทธ๋จ
- ์ถํ. ๋ฐ์ดํฐ ๊ด๋ฆฌ ๋ฐ, ๋ฐ์ดํฐ ์๊ฐํ๋ฅผ ํตํ ๋ณด๋ค ์ข์ ๊ฐ๋ฐํ๊ฒฝ์ ๊ตฌํํ๊ธฐ ์ํด ์ฌ์ฉ,

<img src="https://user-images.githubusercontent.com/41159837/183142233-4e4129a6-9ece-4ac5-8f26-b016799938fd.png" width="50%" height="50%"/>

## ๐ชดย **AI**

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
    - set JWTโs default_settings
        
        <img src="https://user-images.githubusercontent.com/41159837/183143775-f17eea8b-c3d6-48cc-9ba1-c050fc3072fe.png" width="50%" height="50%"/>
        
- JWT on frontEND
    - restore tokens by using redux
    - if we need some user data, we donโt need to make connection with backend
    by opening JWT payload, we can get user data
    
- JWT on backEND
    - after we identify user by check login data, give authorization by using JWT
    - by using refresh_token, we enhanced our security level

## ๐ป Monitoring

<img src="https://user-images.githubusercontent.com/41159837/183143868-35b43d78-a69b-4e3e-a1ba-365234ab67b2.png" width="50%" height="50%"/>

## Prometheus

- exporter๊ฐ ๋งคํธ๋ฆญ์ ์์งํ๊ณ  HTTP ํต์ ์ ํตํด metric data๋ฅผ ๊ฐ์ ธ๊ฐ ์ ์๊ฒ /metrics ๋ผ๋ HTTP ์๋ํฌ์ธํธ๋ฅผ ์ ๊ณตํ๋ค. ๊ทธ๋ฌ๋ฉด Prometheus server๊ฐ ์ด exporter์ ์๋ํฌ์ธํธ์ HTTP GET ์์ฒญ์ ์ด์ฉํ์ฌ metric data๋ฅผ pull ํ๋ค.
- ํด๋น ๋ธ๋์ metric data

<img src="https://user-images.githubusercontent.com/41159837/183143866-e2bb4650-3098-4f79-8e45-c3eb89ef032b.png" width="50%" height="50%"/>

## Grafana

- Prometheus์ ์๊ฐํ ๋๊ตฌ๊ฐ ๋ถ์กฑํ์ฌ ์ด๋ฅผ ์ง์  ์ฌ์ฉํ์ง๋ ์๊ณ  ๋๊ฒ Grafana๋ผ๋ Data Visualization tool์ ์ด์ฉํ์ฌ ์๊ฐํํ๊ณ  ์๋ค.

<img src="https://user-images.githubusercontent.com/41159837/183143860-5af55454-9527-4844-822a-99984c363178.png" width="50%" height="50%"/>

CPU load / RAM usage / Memory swap

## Cadvisor

- ์์ฑ๋ ๋์ปค ์ปจํ์ด๋๋ฑ์ ๋ํ ๋ฐ์ดํฐ๋ฅผ ์์งํด์ค๋ค.

<img src="https://user-images.githubusercontent.com/41159837/183143853-66b83ff7-1a9a-4d99-a8cf-4a6930214cdc.png" width="50%" height="50%"/>

## **How to Start**



## **Project Tree**



# โข๏ธโฑ **Members of Team-E**
|์ด๋ฆ|๊ฐ๋ฐ๋ถ์ผ|์๊ฐํ์ด์ง|
|---|---|---|
|๐ฆฅ๊น์ฉ๋ฏผ|Back-end,DevOps|https://github.com/Ryokuman
|๐๊น์ ๋ฆผ|Back-end,DevOps,AI|https://github.com/Ellie010707
|๐๋ฐ์ฑ๋น|Back-end,DevOps|https://github.com/SeongbinPark
|๐ง๐ปโโ๏ธ์ด์ฑํ|Front-end|https://github.com/chloe1129
|๐น์ด์ ์ฐ|Front-end|https://github.com/RayLee-Kor
|๐ผ์งํธ๋ณ|Front-end|https://github.com/bicco2

