import requests
import json

# API 엔드포인트 URL
url = 'http://localhost:5000/auth/register'  # 적절한 호스트와 포트로 수정하세요

# 요청에 사용할 데이터 (JSON 형식)
data = {
    'username': 'newuser',
    'password': 'newpassword'
}

# JSON 형식으로 데이터를 전송하기 위해 headers 설정
headers = {
    'Content-Type': 'application/json'
}

# POST 요청 보내기
response = requests.post(url, headers=headers, data=json.dumps(data))

# 응답 결과 출력
print(response.status_code)  # 응답 상태 코드
print(response.json())       # 응답 JSON 데이터 (msg 등)