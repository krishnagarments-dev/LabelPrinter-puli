import pyodbc
from datetime import datetime

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\\BESPOKE TSR\\MData.mdb;')

# Checking Product Stock
def check_stock(batcode):
    cursor = conn.cursor()
    cursor.execute(f"select nobstk,ncurstk from itembatch where citbatcode='{batcode}'")
    obstk,curstk = cursor.fetchall()[0]
    cursor.commit()
    cursor.close()
    print(obstk)
    print(curstk)
    return obstk,curstk

# Find in the database
def find_data(item_name):
    cursor = conn.cursor()
    code = []
    item = []
    pricing = []
    cursor.execute(f"select citcode,citname from item where citname LIKE '%{item_name}%'")
    for x,y in cursor.fetchall():
        code.append(x)
        item.append(y)
    
    for i in code:
        cursor.execute(f"select nsalerate from itembatch where citbatcode LIKE '%{i}%'")
        pricing.append(cursor.fetchall()[0][0])

    cursor.close()
    return code,item,pricing


# Find Item with rate
def find_data_wrate(item_name,item_rate):
    cursor = conn.cursor()
    code = []
    item = []
    rate_product = []
    a = []
    b = []
    r = []
    cursor.execute(f"select citcode,citname from item where citname LIKE '%{item_name}%'")
    for x,y in cursor.fetchall():
        a.append(x)
        b.append(y)
    

    for i in a:
        cursor.execute(f"select nsalerate,citbatcode from itembatch where citbatcode='{i}' and nsalerate LIKE {float(item_rate)}")
        try:
            rate,batcode = cursor.fetchone()
            rate_product.append(rate)
            r.append(batcode)
        except:
            pass
    
    for rm in r:
        try:
            cursor.execute(f"select citcode,citname from item where citcode LIKE '%{rm}%'")
            
            citcode,citname = cursor.fetchone()
            code.append(citcode)
            item.append(citname)
        except:
            pass

    cursor.close()
        

    return code,item,rate_product


# Load Item from code
def load_from_code(item_code):
    cursor = conn.cursor()
    cursor.execute(f"select ncurstk,nsalerate,nprrate from itembatch where citbatcode='{item_code}'")
    curstk, selling_rate, purchase_rate = cursor.fetchall()[0]
    cursor.commit()
    cursor.close()
    cursor = conn.cursor()
    cursor.execute(f"select citname,nigst from item where citcode='{item_code}'")
    item_name,ngst = cursor.fetchall()[0]
    cursor.commit()
    cursor.close()
    return curstk,selling_rate,purchase_rate,item_name,ngst
