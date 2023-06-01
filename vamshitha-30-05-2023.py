import pyodbc

from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

server ='SHIRISHA\SQLEXPRESS'
database ='newims'
driver ='{SQL Server}'

connecting_string = f'DRIVER={driver};SERVER={server};DATABASE={database};trusted_connection=YES'

conn = pyodbc.connect(connecting_string)

cn=conn.cursor()

cn.execute("select * from customer")
print(cn.fetchall())

##cn.execute("insert into customer(customer_name,customer_addr,customer_email) values('PQR','HYD','PQR@GMAIL.COM')")
##conn.commit()


customer_name='ABC'
customer_addr='jgtl'
customer_email='ABC@GMAIL.COM'
cn.execute(f"insert into customer(customer_name,customer_addr,customer_email) values('{customer_name}','{customer_addr}','{customer_email}')")
conn.commit()

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/show-customers')
def customer_show():
    cn=conn.cursor()
    cn.execute("select * from customer")
    data=[]
    for i in cn.fetchall():
        customer = {}
        customer['customer_id'] = i[0]
        customer['customer_name'] = i[1]
        customer['customer_addr'] = i[2]
        customer['customer_email'] = i[3]
        data.append(customer)
    print(data)
    return render_template('showcustomers.html',data = data)
    @app.route('/')
def home():
    return render_template('index.html')
@app.route('/show-products')
def product_show():
    cn=conn.cursor()
    cn.execute("select * from product")
    data=[]
    for i in cn.fetchall():
        product = {}
        product['product_id'] = i[0]
        product['product_name'] = i[1]
        product['product_stock'] = i[2]
        product['product_price'] = i[3]
        product['product_supplierid'] = i[3]
        data.append(product)
    print(data)
    return render_template('showproducts.html',data = data)
    



if __name__ == '__main__':
    app.run()
