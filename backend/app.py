# from django.shortcuts import redirect
from flask import Flask, jsonify, request, redirect
from db.db import get_con, dict_factory
import datetime
import collections
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return 'This is a BingoBingo project.'

# 首頁顯示今日獎號
@app.route('/home', methods = ['GET'])
def bingoHome():

    # date = request.args.get('date').strftime('%Y-%m-%d') # 前端回傳date格式，例datetime.date(2022,4,29)
    date = '2022-04-29'

    con = get_con()
    con.row_factory = dict_factory
    cur = con.cursor()
    cur.execute('''
    SELECT id,date,time,num01,num02,num03,num04,num05,num06,num07,num08,num09,num10,num11,num12,num13,num14,num15,num16,num17,num18,num19,num20,odd_even
    FROM bingo
    WHERE date = '{}';
    '''.format(date))
    results = cur.fetchall()
    con.commit()
    cur.close()
    con.close()

    return jsonify(results)
    

@app.route('/analysis', methods = ['GET'])
def bingoAnalysis():

    '''
    --- 取得前端變數 ---
    '''
    print(request.args)
    req_json = request.get_json(force=True)
    years = req_json['year'] # 回傳一個list，包含使用者所選年份
    months = req_json['month'] # 回傳一個list，包含使用者所選月份
    days = req_json['day'] # 回傳一個list，包含使用者所選日期


    # years = request.args.getlist('year') # 回傳一個list，包含使用者所選年份
    # months = request.args.getlist('month') # 回傳一個list，包含使用者所選月份
    # days = request.args.getlist('day') # 回傳一個list，包含使用者所選日期
    # weekdays = request.args.getlist('weekday') # 回傳一個list，包含使用者所選星期

    # years = [2020, 2021,2022] # 回傳一個list，包含使用者所選年份
    # months = [1,2,3,4,5,6] # 回傳一個list，包含使用者所選月份
    # days = [1,2,28,29,30,31] # 回傳一個list，包含使用者所選日期
    # weekdays = request.args.getlist('weekday') # 回傳一個list，包含使用者所選星期

    dates = []
    for year in years:
        for month in months:
            for day in days:
                if month in (1,3,5,7,8,10,12):
                    dates.append('{}-{}-{}'.format(year, str(month).zfill(2), str(day).zfill(2)))
                elif month in (4,6,9,11):
                    if day <= 30:
                        dates.append('{}-{}-{}'.format(year, str(month).zfill(2), str(day).zfill(2)))
                elif month == 2:
                    if (year%4==0 and year%100!=0 and day<=29):
                        dates.append('{}-{}-{}'.format(year, str(month).zfill(2), str(day).zfill(2)))
                    elif (year%4==0 and year%100==0 and year%400==0 and day<=29):
                        dates.append('{}-{}-{}'.format(year, str(month).zfill(2), str(day).zfill(2)))
                    else:
                        if day <= 28:
                            dates.append('{}-{}-{}'.format(year, str(month).zfill(2), str(day).zfill(2)))

    '''
    --- DAO ---
    '''
    con = get_con()
    con.row_factory = dict_factory
    cur = con.cursor()
    cur.execute('''
    SELECT id,date,time,num01,num02,num03,num04,num05,num06,num07,num08,num09,num10,num11,num12,num13,num14,num15,num16,num17,num18,num19,num20,odd_even
    FROM bingo
    WHERE date IN {};
    '''.format(tuple(dates)) )
    results = cur.fetchall()
    con.commit()
    cur.close()
    con.close()

    '''
    --- 計算累積次數 ---
    '''
    
    response = {
            "num_freq" : {},
            "oddeven_freq" : {}
        }
    total_num = []
    total_oddeven = []
    for result in results:
        total_num.extend(list(result.values())[3:23])
        total_oddeven.extend(list(result.values())[23])
    
    print({k: v for k, v in sorted(dict(collections.Counter(total_num)).items(), key=lambda item:(item[1], item[0]), reverse=True)})
    response['num_freq'] = {k: v for k, v in sorted(dict(collections.Counter(total_num)).items(), key=lambda item:(item[1], item[0]), reverse=True)}
    response['oddeven_freq'] = {k: v for k, v in sorted(dict(collections.Counter(total_oddeven)).items(), key=lambda item:(item[1], item[0]), reverse=True)}
    
    return jsonify([response])


@app.route('/taiwanlottery')
def bingoRedirect():
    return redirect('https://www.taiwanlottery.com.tw/index_new.aspx')

app.run(debug = True)