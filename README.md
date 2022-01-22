# 마케시안씨앤이 과제 테스트

본 문서는 마케시안씨앤이 과제 테스트를 위한 문서입니다.

과제 테스트는 4가지 주제로 구성되어 있으며 해결할 수 있는 과제만 수행하시면 됩니다.

4가지 주제는 아래와 같습니다.
```
1. 알고리즘
2. 웹 개발 (Backend)
3. 어플리케이션 개발
4. 인공지능
```

과제 테스트를 완료한 후 github에 업로드하여 주소를 jyahn@marketian.co.kr으로 보내주세요.

---

# 1. 알고리즘

## 문제
1부터 주어진 자연수 N까지 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

- 사용 언어: Python
- `problem_1.py` 파일에 있는 problem 함수를 완성해 주세요.

## 입력
첫 줄에 자연수 N이 주어진다. N은 100이하이다.

## 출력
1부터 주어진 수까지의 수 중 소수와 소수의 개수를 출력한다.

## 예제
```
50
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
소수의 개수 : 15

100
2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97
소수의 개수 : 25
```

---

# 2. 웹 개발 (Backend)
게시글을 조회하고, 등록하고, 삭제하고, 수정할 수 있는 기능을 만들어 보려고 합니다.

개발 요건을 잘 확인하고, 게시글 기능을 완성해 주세요.

## 개발 환경

- 개발 언어: Python 3.6+
- 서버 프레임워크: django 2.2
- 데이터베이스 및 라이브러리: sqlite3, djangorestframework
- IDE : Visual Studio Code

---

### URL 설정

- 게시글 관련 URL은 아래와 같이 작성하면 됩니다.
  - 게시글 등록 /documents/create
  - 게시글 전체 조회 /documents
  - 게시글 상세 조회 /documents/{documentId}/read
  - 게시글 수정 /documents/{documentId}/edit
  - 게시글 삭제 /documents/{documentId}/delete

```
참고사항
* CSS 작성은 분리하는 것이 좋으나, HTML 내부에 작성하는 것도 허용합니다.
* Javascript (ES5, ES6), jQuery, XHR, ajax를 이용하여 구현하는 것도 허용합니다.
```

### 요건 1. 게시글 테이블 설계 및 DB 적용

게시글 테이블의 경우 (제목, 본문, 첨부파일, 조회수) 필드로 정의합니다.

- 해당 필드를 갖춘 Table을 생성하고 DB에 적용해야 합니다.
  - 제목 필드는 TextField로 구성하고, 공백 값이나 NULL 값이 들어갈 수 없습니다.
  - 본문 필드는 CharField로 구성하고, 공백 값이나 NULL 값이 들어갈 수 없습니다.
  - 첨부파일은 FileField로 구성하고, 값이 없어도 상관 없습니다.
  - 조회수는 IntegerField로 구성하고, 기본 값은 0으로 설정합니다.
  - Primary Key는 별도로 구성할 필요는 없습니다.

### 요건 2. 게시글 등록 기능 구현

게시물 등록 기능을 구현합니다.

- `project/document/templates/document/create.html` HTML을 작성하여 게시물 등록 FORM을 작성합니다.
- POST 방식으로 FORM 내용을 서버로 전달하여 게시물 테이블에 등록합니다.
- 게시물 등록이 정상적으로 완료됐다면 `/documents`로 Redirect 합니다.
- 게시물 등록이 정상적으로 처리되지 않았다면 `Exception`을 반환합니다.

| Method | URL |
|--|--|
| POST | /documents/create |

Exception:
- 제목, 본문을 기입하지 않은 경우 (400)

### 요건 3. 게시글 전체 조회 기능 구현

게시물 전체 조회 기능을 구현합니다.

- `project/document/templates/document/read.html` HTML을 작성하여 전체 게시글을 조회할 수 있는 페이지를 구현합니다.
- 전체 게시글 목록을 `table` 태그를 이용하여 렌더링합니다.
- `table`의 필드 순서는 [순번, 제목, 본문, 조회수, 옵션]로 구현합니다.
- `제목`을 클릭할 경우에 해당 게시글의 상세 조회 페이지로 이동하도록 구현합니다.
- `옵션` 항목에는 `수정 버튼`, `삭제 버튼` 두 버튼을 삽입하고, `수정 버튼`을 클릭할 경우에 해당 게시글의 수정 페이지, `삭제 버튼`을 클릭할 경우에 해당 게시글의 삭제 페이지로 이동하도록 구현합니다.
- 전체 게시글의 개수가 0개인 경우에는 `게시글이 없습니다.`라고 표시하도록 구현합니다.

| Method | URL |
|--|--|
| GET | /documents |


### 요건 4. 게시글 상세 조회 기능 구현

게시물 상세 조회 기능을 구현합니다.

- `project/document/templates/document/read_detail.html` HTML을 작성하여 상세 게시글을 조회할 수 있는 페이지를 구현합니다.
- [제목, 본문, 조회수, 첨부파일] 필드를 조회할 수 있도록 구현합니다.
- 첨부파일이 있는 경우에 클릭 시 다운로드 할 수 있도록 구현합니다.
- 게시글 상세 조회 시 해당 게시물의 조회수가 1 증가해야 합니다.

| Method | URL |
|--|--|
| GET | /documents/{documentId}/read |

Exception:
- 게시글을 찾을 수 없는 경우 (404)


### 요건 5. 게시글 수정 기능 구현

게시물 수정 기능을 구현합니다.

- `project/document/templates/document/edit.html` HTML을 작성하여 수정할 수 있는 페이지를 구현합니다.
- [제목, 본문, 첨부파일] 필드를 수정할 수 있습니다.
- 게시물 수정이 정상적으로 완료됐다면 해당 게시글 조회 페이지로 Redirect 합니다.
- 게시물 수정이 정상적으로 처리되지 않았다면 `Exception`을 반환합니다.

| Method | URL |
|--|--|
| POST | /documents/{documentId}/edit |

Exception:
- 제목, 본문을 기입하지 않은 경우 (400)
- 게시글을 찾을 수 없는 경우 (404)

### 요건 6. 게시글 삭제 기능 구현

게시물 삭제 기능을 구현합니다.

- `project/document/templates/document/delete.html` HTML을 작성하여 삭제할 수 있는 페이지를 구현합니다.
- 게시물 삭제가 정상적으로 처리됐다면 전체 게시글 조회 페이지로 Redirect합니다.
- 게시물 삭제가 정상적으로 처리되지 않았다면 `Exception`을 반환합니다.

| Method | URL |
|--|--|
| POST | /documents/{documentId}/delete |

Exception:
- 게시글을 찾을 수 없는 경우 (404)

### 요건 7. API 구현

#### API 응답 포멧

정상처리 및 오류처리에 대한 API 서버 공통 응답 포맷을 아래와 같이 정의합니다.

- 정상처리 및 오류처리 모두 success 필드를 포함합니다.
  - 정상처리라면 true, 오류처리라면 false 값을 출력합니다.
- 정상처리는 response 필드를 포함하고 error 필드는 null 입니다.
  - 응답 데이터가 단일 객체라면, response 필드는 JSON Object로 표현됩니다.
  - 응답 데이터가 스칼라 타입(string, number, boolean)이라면, response 필드는 string, number, boolean로 표현됩니다.
  - 응답 데이터가 Array라면, response 필드는 JSON Array로 표현됩니다.
- 오류처리는 error 필드를 포함하고 response 필드는 null 입니다. error 필드는 status, message 필드를 포함합니다.
  - status : HTTP Response status code 값과 동일한 값을 출력해야 합니다.
  - message : 오류 메시지가 출력됩니다.

#### API

- 공개용 API
  - 게시글 생성 POST /api/documents
  - 게시글 읽기 GET /api/documents/{documentId}
  - 게시글 삭제 DELETE /api/documents/{documentId}
  - 게시글 목록 GET /api/documents

#### 7-1. 게시글 생성

게시글을 생성합니다.

| method | path |
|--|--|
| POST | /api/documents |

Request Body:
``` json
{
  "제목": "게시글",
  "본문": "매우 긴 내용 ···",
  "첨부파일": "Blob of file",
}
```

Response Body:
``` json
{
  "success": true,
  "response": {
    "ID": "생성된 게시물의 ID"
  },
  "error": null
}
```

Exception:
- 제목, 본문을 기입하지 않은 경우 (400)

#### 7-2. 게시글 읽기

문서를 DB에서 읽어서 리턴합니다.

| Method | URL |
|--|--|
| GET | /api/documents/{documentId} |

Param:
- documentId: 문서 ID

Response Body:
``` json
{
  "success": true,
  "response": {
    "document": {
        "ID": "1",
        "제목": "게시글",
        "본문": "매우 긴 내용 ···",
        "첨부파일": "첨부파일의 URL",
        "조회수": "23",
      },
    }
  },
  "error": null
}
```

Exception:
- 게시글을 찾을 수 없는 경우 (404)

#### 7-3. 게시글 삭제

게시글을 삭제합니다.

| Method | URL |
|--|--|
| DELETE | /api/documents/{documentId} |

Response Body:
``` json
{
  "success": true,
  "response": true,
  "error": null
}
```

Exception:
- 게시글을 찾을 수 없는 경우 (404)

#### 7-4. 게시글 목록

모든 게시글을 DB에서 읽어서 API 응답 포맷 형태로 리턴합니다.

| Method | URL |
|--|--|
| GET | /api/documents |

Response Body:
``` json
{
  "success": true,
  "response": {
    "document": [
      {
        "ID": "1",
        "제목": "게시글",
        "본문": "매우 긴 내용 ···",
        "첨부파일": "첨부파일의 URL",
        "조회수": "23",
      },
      {
        "ID": "2",
        "제목": "게시글 2",
        "본문": "매우 긴 내용 ···",
        "첨부파일": "첨부파일의 URL",
        "조회수": "31",
      },
     ]
  },
  "error": null
}
```

--- 

# 3. 어플리케이션 개발

웹에서 개발된 게시글 조회, 등록, 수정, 삭제 기능을 동일하게 수행하는 어플리케이션을 개발하려고 합니다.

개발 요건을 잘 확인하고, 어플리케이션을 개발해 주세요.

## 개발 환경

- 개발 언어 및 프레임워크: React, React Native 0.64
- IDE : Visual Studio Code

```
참고사항
* 프로젝트 폴더는 problem_3을 이용해 주세요.
* Android (JAVA, Kotlin), iOS (Swift, Object-C) 등 다른 언어로 개발이 가능하다면 해당 언어로 개발하는 것도 허용합니다.
* 파일명과 폴더 구조는 자유롭게 결정하시어 개발하시면 됩니다.
```

---

### 요건 1. 게시글 전체 조회 기능

게시글 전체 조회 기능을 구현합니다.

- 게시글을 서버로부터 불러와, `List` 형태로 렌더링합니다.
- 게시글 클릭 시 해당 게시글의 상세 조회 페이지로 이동하도록 구현합니다.

### 요건 2. 게시글 상세 조회 기능

게시글 상세 조회 기능을 구현합니다.

- 제목, 본문, 첨부파일, 조회수를 조회할 수 있습니다.
- `삭제 버튼`, `수정 버튼` 두 버튼을 삽입하고, `삭제 버튼`을 클릭할 경우에 삭제 기능을 수행하도록, `수정 버튼`을 클릭할 경우에 수정 페이지로 이동하도록 구현합니다.

### 요건 3. 게시글 생성 기능

게시글 생성 기능을 구현합니다.

- `생성` 버튼을 삽입하고, `생성`을 클릭할 경웨 서버에 요청을 보내어 처리 결과를 사용자에게 `Alert`를 이용하여 안내합니다.
- 사용자가 `Alert`의 확인 버튼을 클릭하면 전체 조회 페이지로 이동하도록 구현합니다.
- 제목, 본문을 작성하지 않은 경우에 `Alert`나 `Toast`를 이용하여 사용자에게 안내해야 합니다.
- 생성 도중 서버에서 Exception이 발생했을 경우에 `Alert`나 `Toast`를 이용하여 오류 메세지를 출력해야 합니다.

### 요건 4. 게시글 삭제 기능

게시글 삭제 기능을 구현합니다.

- 삭제 도중 서버에서 Exception이 발생했을 경우에 `Alert`나 `Toast`를 이용하여 오류 메세지를 출력해야 합니다.

### 요건 5. 게시글 수정 기능

게시글 수정 기능을 구현합니다.

- 제목, 본문, 첨부파일를 수정할 수 있도록 구현합니다.
- `수정 완료` 버튼을 삽입하고, `수정 완료`를 클릭할 경우에 서버에 요청을 보내어 처리 결과를 사용자에게  `Alert`를 이용하여 안내합니다.
- 사용자가 `Alert`의 확인 버튼을 클릭하면 해당 게시글의 상세 조회 페이지로 이동하도록 구현합니다.

---

# 4. 인공지능

## 문제

Poker Hand 분류 문제로 S1, C1, S2, C2, S3, C3, S4, C4, S5, C5의 카드 정보를 바탕으로 Poker Hand를 예측하는 문제입니다.

자세한 문제 내용은 poker-hands.names 파일을 확인해 주세요.

```
참고사항
* 프로젝트 폴더는 problem_4 폴더를 이용해 주세요.
* 모든 데이터 셋은 problem_4 폴더 안에 있습니다.
```

## 결과
Poker Hand를 분류하는 머신러닝, 딥러닝 모델을 만들고 test.csv에 있는 데이터를 예측하여 sample_submission.csv와 같은 형태로 result.csv를 만들어 주세요.

## 데이터 셋 

- train.csv - 학습 데이터
- test.csv - 검사 데이터
- sample_submission.scv - 최종 결과 샘플 파일
- poker-hands.names - 데이터셋 컬럼 정보 및 설명

## 성능 평가
Softmax Regression 알고리즘에서 사용하는 평가 방법을 적용합니다. 100개 중에 10개를 맞췄다면 정확도는 0.1, 즉 10%가 됩니다.


