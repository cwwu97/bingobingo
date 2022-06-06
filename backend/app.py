# from django.shortcuts import redirect
from flask import Flask, jsonify, request, redirect
from db.db import get_con, dict_factory
from db.db_bigtable import get_bigtable
import datetime
import collections
from flask_cors import CORS
from google.cloud.bigtable.row_set import RowSet

app = Flask(__name__)
CORS(app)

@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Headers'] = '*'
    header['Access-Control-Allow-Methods'] = '*'
    header['Content-type'] = 'application/json'
    return response

@app.route('/')
def index():
    return 'This is a BingoBingo project.'


# 使用bigtable
@app.route('/home', methods = ['GET'])
def bingoHome():

    # date = request.args.get('date').strftime('%Y-%m-%d') # 前端回傳date格式，例datetime.date(2022,4,29)
    # date = datetime.datetime.now().strftime('%Y-%m-%d')
    date = '2022-04-29'
    client, instance, table = get_bigtable()
    column_family_id = "lotteryresult"
    prefix = "{}#".format(date)
    end_key = prefix[:-1] + chr(ord(prefix[-1]) + 1)
    row_set = RowSet()
    row_set.add_row_range_from_keys(prefix.encode("utf-8"), end_key.encode("utf-8"))
    rows = table.read_rows(row_set=row_set)  
    results = []  
    for row in rows:
        result = {
            "id":int(row.cells[column_family_id]['id'.encode()][0].value.decode("utf-8")),
            "date":str(row.cells[column_family_id]['date'.encode()][0].value.decode("utf-8")),
            "time":str(row.cells[column_family_id]['time'.encode()][0].value.decode("utf-8")),
            "num01":int(row.cells[column_family_id]['num01'.encode()][0].value.decode("utf-8")),
            "num02":int(row.cells[column_family_id]['num02'.encode()][0].value.decode("utf-8")),
            "num03":int(row.cells[column_family_id]['num03'.encode()][0].value.decode("utf-8")),
            "num04":int(row.cells[column_family_id]['num04'.encode()][0].value.decode("utf-8")),
            "num05":int(row.cells[column_family_id]['num05'.encode()][0].value.decode("utf-8")),
            "num06":int(row.cells[column_family_id]['num06'.encode()][0].value.decode("utf-8")),
            "num07":int(row.cells[column_family_id]['num07'.encode()][0].value.decode("utf-8")),
            "num08":int(row.cells[column_family_id]['num08'.encode()][0].value.decode("utf-8")),
            "num09":int(row.cells[column_family_id]['num09'.encode()][0].value.decode("utf-8")),
            "num10":int(row.cells[column_family_id]['num10'.encode()][0].value.decode("utf-8")),
            "num11":int(row.cells[column_family_id]['num11'.encode()][0].value.decode("utf-8")),
            "num12":int(row.cells[column_family_id]['num12'.encode()][0].value.decode("utf-8")),
            "num13":int(row.cells[column_family_id]['num13'.encode()][0].value.decode("utf-8")),
            "num14":int(row.cells[column_family_id]['num14'.encode()][0].value.decode("utf-8")),
            "num15":int(row.cells[column_family_id]['num15'.encode()][0].value.decode("utf-8")),
            "num16":int(row.cells[column_family_id]['num16'.encode()][0].value.decode("utf-8")),
            "num17":int(row.cells[column_family_id]['num17'.encode()][0].value.decode("utf-8")),
            "num18":int(row.cells[column_family_id]['num18'.encode()][0].value.decode("utf-8")),
            "num19":int(row.cells[column_family_id]['num19'.encode()][0].value.decode("utf-8")),
            "num20":int(row.cells[column_family_id]['num20'.encode()][0].value.decode("utf-8")),
            "odd_even":str(row.cells[column_family_id]['oddeven'.encode()][0].value.decode("utf-8"))
        }
        results.append(result)
    # print(results)
    return jsonify(results)

@app.route('/analysis', methods = ['GET'])
def bingoAnalysis():

    '''
    --- 取得前端變數 ---
    '''
    years = eval(request.args.get('arg'))['year'] # 回傳一個list，包含使用者所選年份
    months = eval(request.args.get('arg'))['month'] # 回傳一個list，包含使用者所選月份
    days = eval(request.args.get('arg'))['day'] # 回傳一個list，包含使用者所選日期
    # weekdays = eval(request.args.get('arg'))['weekday'] # 回傳一個list，包含使用者所選星期

    # years = [2020] # 回傳一個list，包含使用者所選年份
    # months = [4] # 回傳一個list，包含使用者所選月份
    # days = [30] # 回傳一個list，包含使用者所選日期
    # weekdays = ['一','四'] # 回傳一個list，包含使用者所選星期

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
    # if len(dates) == 1:
    #     dates.append(0)

    '''
    --- DAO ---
    '''
    client, instance, table = get_bigtable()
    column_family_id = "lotteryresult"
    results = []
    for date in dates:
        prefix = "{}#".format(date)
        # print(prefix)
        end_key = prefix[:-1] + chr(ord(prefix[-1]) + 1)
        row_set = RowSet()
        row_set.add_row_range_from_keys(prefix.encode("utf-8"), end_key.encode("utf-8"))

        rows = table.read_rows(row_set=row_set)    
        for row in rows:
            result = {
                "num01":int(row.cells[column_family_id]['num01'.encode()][0].value.decode("utf-8")),
                "num02":int(row.cells[column_family_id]['num02'.encode()][0].value.decode("utf-8")),
                "num03":int(row.cells[column_family_id]['num03'.encode()][0].value.decode("utf-8")),
                "num04":int(row.cells[column_family_id]['num04'.encode()][0].value.decode("utf-8")),
                "num05":int(row.cells[column_family_id]['num05'.encode()][0].value.decode("utf-8")),
                "num06":int(row.cells[column_family_id]['num06'.encode()][0].value.decode("utf-8")),
                "num07":int(row.cells[column_family_id]['num07'.encode()][0].value.decode("utf-8")),
                "num08":int(row.cells[column_family_id]['num08'.encode()][0].value.decode("utf-8")),
                "num09":int(row.cells[column_family_id]['num09'.encode()][0].value.decode("utf-8")),
                "num10":int(row.cells[column_family_id]['num10'.encode()][0].value.decode("utf-8")),
                "num11":int(row.cells[column_family_id]['num11'.encode()][0].value.decode("utf-8")),
                "num12":int(row.cells[column_family_id]['num12'.encode()][0].value.decode("utf-8")),
                "num13":int(row.cells[column_family_id]['num13'.encode()][0].value.decode("utf-8")),
                "num14":int(row.cells[column_family_id]['num14'.encode()][0].value.decode("utf-8")),
                "num15":int(row.cells[column_family_id]['num15'.encode()][0].value.decode("utf-8")),
                "num16":int(row.cells[column_family_id]['num16'.encode()][0].value.decode("utf-8")),
                "num17":int(row.cells[column_family_id]['num17'.encode()][0].value.decode("utf-8")),
                "num18":int(row.cells[column_family_id]['num18'.encode()][0].value.decode("utf-8")),
                "num19":int(row.cells[column_family_id]['num19'.encode()][0].value.decode("utf-8")),
                "num20":int(row.cells[column_family_id]['num20'.encode()][0].value.decode("utf-8")),
                "odd_even":str(row.cells[column_family_id]['oddeven'.encode()][0].value.decode("utf-8"))
            }
            results.append(result)

    response = {
            "num_freq" : {},
            "oddeven_freq" : {}
        }
    total_num = []
    total_oddeven = []
    for result in results:
        total_num.extend(list(result.values())[:19])
        total_oddeven.extend(list(result.values())[20:])
    
    # print({k: v for k, v in sorted(dict(collections.Counter(total_num)).items(), key=lambda item:(item[1], item[0]), reverse=True)})
    toChar = lambda x: {'odd-small': '小單', 'odd': '單', 'fair':'和', 'even':'雙', 'even-small':'小雙'}.get(x, '無開獎')
    response['num_freq'] = {k: v for k, v in sorted(dict(collections.Counter(total_num)).items(), key=lambda item:(item[1], item[0]), reverse=True)}
    response['oddeven_freq'] = {toChar(k): v for k, v in sorted(dict(collections.Counter(total_oddeven)).items(), key=lambda item:(item[1], item[0]), reverse=True)}
    # print(response)
    return jsonify([response])

    lambda x: {'odd-small': '小單', 'odd': '單', 'fair':'和', 'even':'雙', 'even-small':'小雙'}.get(x, '無開獎')
    
"""
# 使用sqlite3
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
    years = eval(request.args.get('arg'))['year'] # 回傳一個list，包含使用者所選年份
    months = eval(request.args.get('arg'))['month'] # 回傳一個list，包含使用者所選月份
    days = eval(request.args.get('arg'))['day'] # 回傳一個list，包含使用者所選日期
    # weekdays = eval(request.args.get('arg'))['weekday'] # 回傳一個list，包含使用者所選星期

    # years = [2022] # 回傳一個list，包含使用者所選年份
    # months = [1] # 回傳一個list，包含使用者所選月份
    # days = [30] # 回傳一個list，包含使用者所選日期
    # weekdays = ['一','四'] # 回傳一個list，包含使用者所選星期

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
    if len(dates) == 1:
        dates.append(0)

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
    '''.format(tuple(dates)))
    results = cur.fetchall()
    con.commit()
    cur.close()
    con.close()
    # print(results)
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
    
    # print({k: v for k, v in sorted(dict(collections.Counter(total_num)).items(), key=lambda item:(item[1], item[0]), reverse=True)})
    response['num_freq'] = {k: v for k, v in sorted(dict(collections.Counter(total_num)).items(), key=lambda item:(item[1], item[0]), reverse=True)}
    response['oddeven_freq'] = {k: v for k, v in sorted(dict(collections.Counter(total_oddeven)).items(), key=lambda item:(item[1], item[0]), reverse=True)}
    
    return jsonify([response])


@app.route('/taiwanlottery')
def bingoRedirect():
    return redirect('https://www.taiwanlottery.com.tw/index_new.aspx')
"""

if __name__ == "__main__":
    app.run(host = '0.0.0.0', debug = True)