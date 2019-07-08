
import sqlite3 as db
import pandas as pd
from pandas import DataFrame,Series

#Name of Excel xlsx file.  SQLite database will have the same name and

#dbファイル名を指定
filename = "HCM" 

#dbコネクターを作成する
con = db.connect(filename + ".db",isolation_level=None)

#Excel内容を読込み
wb = pd.read_excel(filename + '.xlsx',sheetname=None,index=False)

#シートが多数ある場合、ループして、シート名がテーブル名に変換する
for sheet in wb:
    #dbが既に存在する場合、リープレスする。
    #wb[sheet].to_sql(sheet,con,if_exists = 'replace')
    #インデックスを無効にするため
    wb[sheet].to_sql(sheet,con,if_exists = 'append',index = False)

    ##インデックスを作成するため
    #wb[sheet].to_sql(sheet,con,if_exists = 'replace')

#dbへ書込み
con.commit()

#コネクターを終了する
con.close()