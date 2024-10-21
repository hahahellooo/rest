import streamlit as st
import requests
import json

firstname = st.text_input("firstname: ")
lastname =st.text_input("lastname: ")
user_id = st.text_input("id: ")
headers = {
    'Content-Type': 'application/json',
}
url = 'http://localhost:3000/person'


if firstname and lastname:
    data = {"firstName": firstname, "lastName": lastname, "id":user_id}
    r = requests.post(url=url, headers=headers, json=data)
    st.write("삽입 완료")
    if r.status_code ==201:
        r = requests.get(url=url, headers=headers)
        d = r.json()
        st.write(d)
    else:
        st.write(f"오류가 발생했습니다. 오류 코드 {r.status_code}")
else:
    st.write("firstname, lastname, id를 입력해주세요")
