from datetime import datetime

def now_weeks(date_string):
    # 指定の日付をdatetimeオブジェクトに変換
    specified_date = datetime.strptime(date_string, '%Y/%m/%d')

    # 現在の日付を取得
    current_date = datetime.now()

    # 日付の差分を計算
    delta = current_date - specified_date

    # 週数を計算
    weeks_since = delta.days // 7

    return weeks_since