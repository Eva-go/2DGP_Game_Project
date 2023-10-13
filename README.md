# 2DGP_Game_Project
2016182041 조영환


# 게임 영상
![image](https://github.com/Eva-go/2DGP_Game_Project/blob/master/ReadMe/stage1.png?raw=true)
![video](https://github.com/Eva-go/2DGP_Game_Project/assets/55368765/8a77a7b6-e434-4f44-96a7-789a50f37d14)



# 게임 소개
slay the spire을 보고 데모게임을 제작하였습니다.
![image](https://user-images.githubusercontent.com/55368765/121574453-3d0f8d80-ca61-11eb-93a5-a66aff269943.png)

로그라이크 게임으로 적을 물리치면 다음 스테이지로 넘어갑니다. (총3스테이지)

## 개발 계획
![image](https://github.com/Eva-go/2DGP_Game_Project/blob/master/ReadMe/%EA%B0%9C%EB%B0%9C%20%EA%B3%84%ED%9A%8D.png?raw=true)

플레이어: HP,Cost로 구성한다.

카드: 카드 Cost비용, 카드 효과, 카드 개수를 구성한다.

몬스터: 몬스터의 수, 몬스터의 공격력, 몬스터 HP를 구성한다.

맵: 던전 형식의 맵,이벤트 맵 구현

오브젝트 제작: 캐릭터,몬스터 제작 및 카드강화,스테이지 구현

## 개발 범위
![image](https://github.com/Eva-go/2DGP_Game_Project/blob/master/ReadMe/%EA%B0%9C%EB%B0%9C%EB%B2%94%EC%9C%84.png?raw=true)

맵: 3스테이지로 구성한다.

카드 : 3장의 카드를 40장의 덱으로 구성한다.

캐릭터 : 1개의 캐릭터 제작

몬스터 : player와 조우시 행동, player가 턴을 끝내면 공격개시

사운드 : 공격,몬스터공격,player 피해 구현

게임기능 : 피격시 체력감소, cost 및 카드 사용후 클리어시 cost 및 카드 소지가 그대로 진행

# 게임플레이 스크린샷
![image](https://github.com/Eva-go/2DGP_Game_Project/assets/55368765/05c3f284-c950-4a24-bd96-f6713de1df70)
![image](https://github.com/Eva-go/2DGP_Game_Project/assets/55368765/8fa0f68c-6a57-4219-a405-612dffade387)
![image](https://github.com/Eva-go/2DGP_Game_Project/assets/55368765/5bb0b9e2-996e-4dab-b214-01fcf71ae6c7)
![image](https://github.com/Eva-go/2DGP_Game_Project/assets/55368765/2f526e9a-8aab-46b8-b7b8-6bdda8036fe4)
![image](https://github.com/Eva-go/2DGP_Game_Project/assets/55368765/9e44fc2c-b566-4230-9bc4-8fb70e0f3abb)
![image](https://github.com/Eva-go/2DGP_Game_Project/assets/55368765/2c1052be-2e3f-4201-a8d8-cbc784e06dcd)

## 사용된 기술
stack,deque 를 이용한 카드 뽑기 및 카드 저장
list 를 이용한 cost 갯수 저장
main handle를 이용한 player turn 및 enemy turn 구현

