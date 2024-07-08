import streamlit as st
import pyodbc
import requests as req

from calc_date import now_weeks

con_str = 'Driver={{Microsoft Access Driver (*.mdb, *.accdb)}};Dbq={0};'.format(r"C:\Users\ok230195\PycharmProjects\Xreading_recode\Xreading.accdb")
conn = pyodbc.connect(con_str)
cur = conn.cursor()

st.title('Xreading Record')

now_week = now_weeks("2024/04/15")

with st.form('English Communication Xreading Record'):
    book_name = st.text_input('Enter Book Name')
    book_word_count = st.text_input('book_word_count')
    submit = st.form_submit_button('Submit')

if submit:
    st.text(f"以下の内容で記録します\n題名:{book_name}\n文字数:{book_word_count}")
    cur.execute("INSERT INTO [2年前期達成状況] (本の名前, 単語数, 読んだ週)VALUES (?, ?, ?)", (book_name, int(book_word_count), now_week))
    conn.commit()
    st.success("記録しました")
    print("success")
# FastAPIのエンドポイントURL
api_url = "http://127.0.0.1:8000"

# 全ての読んだ単語数の合計を取得
submit_all = st.button('Get Total Reading Words')
if submit_all:
    response = req.get(f"{api_url}/sum/all")
    if response.status_code == 200:
        total_words = response.json().get("sumall", "Error")
        st.write(total_words)
    else:
        st.write("Failed to get data from API.")

with st.form('週ごとの達成数を検索'):
    weeks = st.text_input('Enter weeks')
    submit_weeks = st.form_submit_button('Submit')
    # 週ごとの読んだ単語数の合計を取得
    if submit_weeks:
        response = req.get(f"{api_url}/sum/{weeks}")
        if response.status_code == 200:
            weekly_words = response.json().get("sumweeks", "Error")
            st.write(weekly_words)
        else:
            st.write("Failed to get data from API.")
cur.close()
conn.close()
