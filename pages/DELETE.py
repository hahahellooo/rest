import streamlit as st
import requests

user_id=st.text_input("id: ")
headers = {
    'Content-Type': 'application/json',
}

if user_id:
    url = f'http://localhost:3000/person/{user_id}'

    r = requests.delete(url=url, headers=headers)
    st.write("삭제완료")
    if r.status_code ==200:
        url = 'http://localhost:3000/person'
        r = requests.get(url=url, headers=headers)
        data = r.json()
        st.write(data)
    else:
        st.write(f"삭제 요청 처리 중 오류 발생: 상태코드{r.status_code}")
else:
    st.write("id를 입력해주세요")
