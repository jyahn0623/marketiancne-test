# 마케시안씨앤이 과제 테스트

게시글을 조회하고, 등록하고, 삭제하고, 수정할 수 있는 기능을 만들어 보려고 합니다.

개발 요건을 잘 확인하고, 게시글 기능을 완성해 주세요.

과제 테스트를 완료한 후 github에 업로드하여 주소를 jyahn@marketian.co.kr으로 보내주세요.

## 개발 환경

- 개발 언어: Python 3.6+
- 서버 프레임워크: django 2.2
- 데이터베이스 및 라이브러리: sqlite3
- IDE : Visual Studio Code

---

## URL 설정

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
