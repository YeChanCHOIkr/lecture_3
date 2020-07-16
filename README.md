### python 라이브러리 설치 명령어

```powershell
pip install virtualenv
```



#### virtualenv 명령어를 이용해서 가상환경을 만드는 방법

##### virtualenv  [원하고자하는 프로젝트명]

```powershell
virtualenv lecture_3 && cd lecture_3
```



![1](https://user-images.githubusercontent.com/25717861/87618639-4e6aef80-c755-11ea-9047-d5a5e72ca2e8.png)



#### 가상환경 활성화 

가상환경 할성화 명령어 activate.bat

Scripts 폴더내에 존재

```shell
cd Scripts && activate
```



#### 가상환경 비활성화

가상환경 비할성화 명령어 deactivate.bat

Scripts 폴더내에 존재

```shell
cd Scripts && deactivate
```





#### 설치한 라이브러리 관리는 requirements.txt에서 관리된다.

##### freeze 명령어를 이용해서 생성

생성방법

```shell
pip freeze > requirements.txt
```



#### requirements.txt 를 활용해서 라브러리 설치

```powershell
pip install -r requirements.txt
```



