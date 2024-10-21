import requests
import streamlit as st

url = 'http://localhost:3000/person'
headers = {
    'Content-Type': 'application/json',
}

r = requests.get(url=url, headers=headers)

if r.status_code ==  200:
    try: 
        data = r.json()
        st.write(data)
    except ValueError:
        st.write("json 형식 로드를 실패했습니다. text 형식으로 출력합니다.")
        st.wirte(r.text)
else:
    st.write(f"에러가 발생했습니다.")

