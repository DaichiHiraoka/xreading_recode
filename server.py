from fastapi import FastAPI
import pyodbc
import datetime

app = FastAPI()

# データベース接続文字列
con_str = 'Driver={{Microsoft Access Driver (*.mdb, *.accdb)}};Dbq={0};'.format(r"C:\Users\ok230195\PycharmProjects\Xreading_record\Xreading.accdb")


def get_db_connection():
    conn = pyodbc.connect(con_str)
    return conn


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/sum/all")
async def sum_reading_word():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM([単語数]) FROM [2年前期達成状況]")
    result = cursor.fetchone()
    sum_all = result[0] if result[0] is not None else 0
    conn.close()
    return {"sumall": f"合計 {int(sum_all)}単語"}


@app.get("/sum/weeks")
async def anyweeks_reading_word():
    conn = get_db_connection()
    cursor = conn.cursor()
    print(datetime.datetime.now())
    cursor.execute("SELECT SUM([単語数]) FROM [2年前期達成状況] where [読んだ週]　= 1")
    result = cursor.fetchone()
    sum_weeks = result[0] if result[0] is not None else 0
    conn.close()
    return {"sumweeks": f"合計 {int(sum_weeks)}単語"}
