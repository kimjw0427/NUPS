
## API 문서

### 기본 URL
```
http://<your-domain>/api
```

### 회원가입 및 로그인

#### 회원가입

- **URL:** `/auth/register`
- **Method:** `POST`
- **Body:**
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Response:**
  - 성공:
    ```json
    {
      "msg": "User created successfully"
    }
    ```
  - 실패:
    ```json
    {
      "msg": "Username already exists"
    }
    ```

#### 로그인

- **URL:** `/auth/login`
- **Method:** `POST`
- **Body:**
  ```json
  {
    "username": "string",
    "password": "string"
  }
  ```
- **Response:**
  - 성공:
    ```json
    {
      "access_token": "string"
    }
    ```
  - 실패:
    ```json
    {
      "msg": "Bad username or password"
    }
    ```

### 게시판

#### 게시글 생성

- **URL:** `/board/<category>`
- **Method:** `POST`
- **Headers:**
  - Authorization: `Bearer <JWT token>`
- **Body:**
  ```json
  {
    "title": "string",
    "content": "string"
  }
  ```
- **Response:**
  - 성공:
    ```json
    {
      "msg": "Post created successfully"
    }
    ```
  - 실패:
    ```json
    {
      "msg": "Invalid category"
    }
    ```

#### 게시글 조회

- **URL:** `/board/<category>`
- **Method:** `GET`
- **Query Parameters:**
  - `sort_by` (optional, default: `created_at`): 정렬 기준 필드 (e.g., `title`, `created_at`)
  - `order` (optional, default: `desc`): 정렬 순서 (`asc` 또는 `desc`)
  - `search` (optional, default: `""`): 검색어
- **Response:**
  ```json
  [
    {
      "id": "integer",
      "title": "string",
      "content": "string",
      "category": "string",
      "created_at": "datetime",
      "updated_at": "datetime",
      "user_id": "integer"
    }
  ]
  ```

#### 게시글 수정

- **URL:** `/board/<int:post_id>`
- **Method:** `PUT`
- **Headers:**
  - Authorization: `Bearer <JWT token>`
- **Body:**
  ```json
  {
    "title": "string",
    "content": "string"
  }
  ```
- **Response:**
  - 성공:
    ```json
    {
      "msg": "Post updated successfully"
    }
    ```
  - 실패:
    ```json
    {
      "msg": "Permission denied"
    }
    ```

#### 게시글 삭제

- **URL:** `/board/<int:post_id>`
- **Method:** `DELETE`
- **Headers:**
  - Authorization: `Bearer <JWT token>`
- **Response:**
  - 성공:
    ```json
    {
      "msg": "Post deleted successfully"
    }
    ```
  - 실패:
    ```json
    {
      "msg": "Permission denied"
    }
    ```

## 카테고리

`<category>` 값은 다음 중 하나여야 합니다:
- `자유게시판`
- `연구과제`
- `뉴스`

각 카테고리는 독립적으로 운영됩니다.
