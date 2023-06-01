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


#customer_name='ABC'
#customer_addr='jgtl'
#customer_email='ABC@GMAIL.COM'
#cn.execute(f"insert into customer(customer_name,customer_addr,customer_email) values('{customer_name}','{customer_addr}','{customer_email}')")
#conn.commit()

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
@app.route('/show-suppliers')
def suppliers_show():
    cn=conn.cursor()
    cn.execute("select * from supplier")
    data=[]
    for i in cn.fetchall():
        supplier = {}
        supplier['supplier_id'] = i[0]
        supplier['supplier_name'] = i[1]
        supplier['supplier_addr'] = i[2]
        supplier['supplier_email'] = i[3]
        data.append(supplier)
    print(data)
    return render_template('showsuppliers.html',data = data)
@app.route('/show-ORDERS')
def ORDERS_show():
    cn=conn.cursor()
    cn.execute("select * from ORDERS")
    data=[]
    for i in cn.fetchall():
        ORDERS = {}
        ORDERS['ORDER_id'] = i[0]
        ORDERS['PRODUCT_ID'] = i[1]
        ORDERS['CUSTOMER_ID'] = i[2]
        ORDERS['ORDER_QUANTITY'] = i[3]
        data.append(ORDERS)
    print(data)
    return render_template('SHOWORDERS.html',data = data)

@app.route('/add-customer',methods = ['GET','POST']) 
def addcustomer():
    if request.method=='POST':
        cn=conn.cursor()
        customer_name = request.form.get("name")
        customer_addr = request.form.get("address")
        customer_email = request.form.get("email")
        cn.execute(f"insert into customer(customer_name,customer_addr,customer_email) values('{customer_name}','{customer_addr}','{customer_email}')")
        conn.commit()
        print('Data has been inserted')
        return jsonify({'message':'sucessfull'})
    else:
        return render_template('addcustomer.html')

@app.route('/update-customer',methods = ['GET','POST']) 
def updatecustomer():
    if request.method=='POST':
        cn=conn.cursor()
        customer_id = request.form.get("customer_id")
        change= request.form.get("change")
        newvalue = request.form.get('newvalue')
        print(customer_id,change,newvalue)
        cn.execute(f"update customer set {change} = '{newvalue}' where customer_id = '{customer_id}'")
        conn.commit()
        print('Data has been updated')
        return jsonify({'message':'sucessfull'})
    else:
        return render_template('updatecustomer.html')

@app.route('/delete-customer',methods = ['GET','POST']) 
def deletecustomer():
    if request.method=='POST':
        cn=conn.cursor()
        customer_id = request.form.get("customer_id")
        cn.execute(f"delete from customer where customer_id = '{customer_id}')")
        conn.commit()
        print('Data has been inserted')
        return jsonify({'message':'sucessfull'})
    else:
        return render_template('deletecustomer.html')


@app.route('/add-suppliers',methods = ['GET','POST']) 
def addsuppliers():
    if request.method=='POST':
        cn=conn.cursor()
        supplier_name = request.form.get("name")
        supplier_addr = request.form.get("address")
        supplier_email = request.form.get("email")
        cn.execute(f"insert into SUPPLIER(supplier_name,supplier_addr,supplier_email) values('{supplier_name}','{supplier_addr}','{supplier_email}')")
        conn.commit()
        print('Data has been inserted')
        return jsonify({'message':'sucessfull'})
    else:
        return render_template('addsuppliers.html')

@app.route('/add-product',methods = ['GET','POST']) 
def addproduct():
    if request.method=='POST':
        print('TEST1')
        cn=conn.cursor()
        product_name = request.form.get("name")
        stock = request.form.get("stock")
        price = request.form.get("price")
        supplier_id = request.form.get("id")
        print('TEST2')
        cn.execute(f"insert into product(product_name,stock,price,supplier_id) values('{product_name}','{stock}','{price}','{supplier_id}')")
        conn.commit()
        print('Data has been inserted')
        return jsonify({'message':'sucessfull'})
    else:
        return render_template('addproduct.html')

@app.route('/update-product',methods = ['GET','POST'])
def updateproduct():
    if request.method=='POST':
        cn=conn.cursor()
        product_id = request.form.get("product_id")
        change= request.form.get("change")
        newvalue = request.form.get('newvalue')
        print(product_id,change,newvalue)
        cn.execute(f"update product set {change} = '{newvalue}' where product_id = '{product_id}'")
        conn.commit()
        print('Data has been updated')
        return jsonify({'message':'sucessfull'})
    else:
        return render_template('updateproduct.html')


@app.route('/update-orders',methods = ['GET','POST'])
def updateorders():
    if request.method=='POST':
        cn=conn.cursor()
        order_id = request.form.get("order_id")
        change= request.form.get("change")
        newvalue = request.form.get('newvalue')
        print(order_id,change,newvalue)
        cn.execute(f"update orders set {change} = '{newvalue}' where order_id = '{order_id}'")
        conn.commit()
        print('Data has been updated')
        return jsonify({'message':'sucessfull'})
    else:
        return render_template('updateorders.html')
@app.route('/update-supplier',methods = ['GET','POST'])
def updatesupplier():
    if request.method=='POST':
        cn=conn.cursor()
        supplier_id = request.form.get("supplier_id")
        change= request.form.get("change")
        newvalue = request.form.get('newvalue')
        print(order_id,change,newvalue)
        cn.execute(f"update supplier set {change} = '{newvalue}' where supplier_id = '{supplier_id}'")
        conn.commit()
        print('Data has been updated')
        return jsonify({'message':'sucessfull'})
    else:
        return render_template('updatesupplier.html')




@app.route('/delete-product',methods = ['GET','POST']) 
def deleteproduct():
    if request.method=='POST':
        cn=conn.cursor()
        product_id = request.form.get("product_id")
        cn.execute(f"delete from product where product_id='{product_id}')")
        conn.commit()
        print('Data has been deleteed')
        return jsonify({'message':'sucessfull'})
    else:
        return render_template('deleteproduct.html')


@app.route('/add-orders',methods = ['GET','POST']) 
def addorders():
    if request.method=='POST':
        cn=conn.cursor()
        product_id = request.form.get("id")
        customer_id = request.form.get("id")
        quantity = request.form.get("quantity")
        cn.execute(f"insert into orders(product_id,customer_id,quantity) values('{product_id}','{customer_id}','{quantity}')")
        conn.commit()
        print('Data has been inserted')
        return jsonify({'message':'sucessfull'})
    else:
        return render_template('addorders.html')




if __name__ == '__main__':
    app.run()
