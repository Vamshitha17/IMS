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
    cn.execute("SELECT * FROM CUSTOMER")
    data=[]
    for i in cn.fetchall():
        customer={}
        customer['customer_id']=i[0]
        customer['customer_name']=i[1]
        customer['customer_addr']=i[2]
        customer['customer_email']=i[3]
        data.append(customer)

    return render_template('showcustomers.html',data=data)

@app.route('/show-products')
def Product_show():
    cn=conn.cursor()
    cn.execute("SELECT * FROM PRODUCT")
    prd_data=[]
    for i in cn.fetchall():
        product={}
        product['product_id']=i[0]
        product['product_name']=i[1]
        product['price']=i[2]
        product['stock']=i[3]
        product['supplier_id']=i[4]

        prd_data.append(product)
    print(prd_data)
    return render_template('showproducts.html',data=prd_data)

@app.route('/show-orders')
def Order_show():
    cn=conn.cursor()
    cn.execute("SELECT * FROM ORDERS")
    ord_data=[]
    for i in cn.fetchall():
        order={}
        order['order_id']=i[0]
        order['product_id']=i[1]
        order['customer_id']=i[2]
        order['quantity']=i[3]
       

        ord_data.append(order)
    print(ord_data)
    return render_template('showorders.html',data=ord_data)

@app.route('/show-suppliers')
def Supplier_show():
    cn=conn.cursor()
    cn.execute("SELECT * FROM SUPPLIER")
    sup_data=[]
    for i in cn.fetchall():
        supplier={}
        supplier['supplier_id']=i[0]
        supplier['supplier_name']=i[1]
        supplier['supplier_addr']=i[2]
        supplier['supplier_email']=i[3]


        sup_data.append(supplier)
    print(sup_data)
    return render_template('showsuppliers.html',data=sup_data)

@app.route('/add-customer',methods =['GET','POST'])
def addcustomer():
    if request.method=='POST':
        cn=conn.cursor()
        CUSTOMER_NAME= request.form.get("name")
        CUSTOMER_ADDR= request.form.get("address")
        CUSTOMER_MAIL= request.form.get("email")
        cn.execute(F"INSERT INTO CUSTOMER (CUSTOMER_NAME,CUSTOMER_ADDR,CUSTOMER_MAIL) VALUES('{CUSTOMER_NAME}','{CUSTOMER_ADDR}','{CUSTOMER_MAIL}')")
        conn.commit()
        print('data inserted')
        return jsonify({'message':'successful'})
    else:
        return render_template('addcustomer.html')
    
@app.route('/add-product',methods =['GET','POST'])
def addproduct():
    if request.method=='POST':
        cn=conn.cursor()
        PRODUCT_NAME= request.form.get("name")
        PRICE= request.form.get("price")
        STOCK= request.form.get("stock")
        SUPPLIER_ID= request.form.get("supplier id")
        cn.execute(F"INSERT INTO PRODUCT (PRODUCT_NAME,PRICE,STOCK,SUPPLIER_ID) VALUES('{PRODUCT_NAME}','{PRICE}','{STOCK}','{SUPPLIER_ID}')")
        conn.commit()
        print('data inserted')
        return jsonify({'message':'successful'})
    else:
        return render_template('addproduct.html')
    
@app.route('/add-supplier',methods =['GET','POST'])
def addsupplier():
    if request.method=='POST':
        cn=conn.cursor()
        SUPPLIER_NAME= request.form.get("name")
        SUPPLIER_ADDR= request.form.get("address")
        SUPPLIER_MAIL= request.form.get("email")
        cn.execute(F"INSERT INTO SUPPLIER (SUPPLIER_NAME,SUPPLIER_ADDR,SUPPLIER_MAIL) VALUES('{SUPPLIER_NAME}','{SUPPLIER_ADDR}','{SUPPLIER_MAIL}')")
        conn.commit()
        print('data inserted')
        return jsonify({'message':'successful'})
    else:
        return render_template('addsupplier.html')
    
@app.route('/add-order',methods =['GET','POST'])
def addorder():
    if request.method=='POST':
        cn=conn.cursor()
        PRODUCT_ID= request.form.get("productid")
        CUSTOMER_ID= request.form.get("customerid")
        QUANTITY= request.form.get("quantity")
        cn.execute(F"INSERT INTO ORDERS (PRODUCT_ID,CUSTOMER_ID,QUANTITY) VALUES('{PRODUCT_ID}','{CUSTOMER_ID}','{QUANTITY}')")
        conn.commit()
        print('data inserted')
        return jsonify({'message':'successful'})
    else:
        return render_template('addorder.html')

@app.route('/update-customer',methods =['GET','POST'])
def updatecustomer():
    if request.method=='POST':
        cn=conn.cursor()
        CUSTOMER_ID= request.form.get("customerid")
        CUSTOMER_ADDR= request.form.get("address")
        CUSTOMER_MAIL= request.form.get("email")
        change = request.form.get('change')
        newvalue = request.form.get('newvalue')
        print(change,newvalue)

        cn.execute(f"UPDATE CUSTOMER SET {change} = '{newvalue}' where customer_id = '{CUSTOMER_ID}'")
        conn.commit()
        print('data inserted')
        return jsonify({'message':'successful'})
    else:
        return render_template('updatecustomer.html')
    
@app.route('/update-product',methods =['GET','POST'])
def updateproduct():
    if request.method=='POST':
        cn=conn.cursor()
        PRODUCT_ID=request.form.get("productid")
        PRODUCT_NAME= request.form.get("name")
        PRICE= request.form.get("price")
        STOCK= request.form.get("stock")
        SUPPLIER_ID= request.form.get("supplier id")
        change = request.form.get('change')
        newvalue = request.form.get('newvalue')
        print(change,newvalue)

        cn.execute(f"UPDATE PRODUCT SET {change} = '{newvalue}' where product_id = '{PRODUCT_ID}'")
        conn.commit()
        print('data inserted')
        return jsonify({'message':'successful'})
    else:
        return render_template('updateproduct.html')
    

@app.route('/update-order',methods =['GET','POST'])
def updateorder():
    if request.method=='POST':
        cn=conn.cursor()
        ORDER_ID=request.form.get("orderid")
        PRODUCT_ID= request.form.get("productid")
        CUSTOMER_ID= request.form.get("customerid")
        QUANTITY= request.form.get("quantity")
        change = request.form.get('change')
        newvalue = request.form.get('newvalue')
        print(change,newvalue)

        cn.execute(f"UPDATE ORDERS SET {change} = '{newvalue}' where order_id = '{ORDER_ID}'")
        conn.commit()
        print('data inserted')
        return jsonify({'message':'successful'})
    else:
        return render_template('updateorder.html')
    
@app.route('/update-supplier',methods =['GET','POST'])
def updatesupplier():
    if request.method=='POST':
        cn=conn.cursor()
        SUPPLIER_ID=request.form.get("supplierid")
        SUPPLIER_NAME= request.form.get("name")
        SUPPLIER_ADDR= request.form.get("address")
        SUPPLIER_MAIL= request.form.get("email")
        change = request.form.get("change")
        newvalue = request.form.get("newvalue")
    
        print("change","newvalue")

        cn.execute(f"UPDATE SUPPLIER SET {change} = '{newvalue}' where supplier_id = '{SUPPLIER_ID}'")
        conn.commit()
        print('data inserted')
        return jsonify({'message':'successful'})
    else:
        return render_template('updatesupplier.html')
    

        
@app.route('/delete-customers',methods =['GET','POST'])
def deletecustomer():
    if request.method=='POST':
        cn=conn.cursor()
        CUSTOMER_ID=request.form.get("customerid")
       
  
        cn.execute(f"DELETE FROM CUSTOMER WHERE customer_id = '{CUSTOMER_ID}'")
        conn.commit()
        print('data inserted')
        return jsonify({'message':'successful'})
    else:
        return render_template('deletecustomer.html')
    
@app.route('/delete-products',methods =['GET','POST'])
def deleteproduct():
    if request.method=='POST':
        cn=conn.cursor()
        PRODUCT_ID=request.form.get("productid")
       
  
        cn.execute(f"DELETE FROM PRODUCT WHERE product_id = '{PRODUCT_ID}'")
        conn.commit()
        print('data inserted')
        return jsonify({'message':'successful'})
    else:
        return render_template('deleteproduct.html')
    
@app.route('/delete-orders',methods =['GET','POST'])
def deleteorder():
    if request.method=='POST':
        cn=conn.cursor()
        ORDER_ID=request.form.get("orderid")
       
  
        cn.execute(f"DELETE FROM ORDERS WHERE order_id = '{ORDER_ID}'")
        conn.commit()
        print('data inserted')
        return jsonify({'message':'successful'})
    else:
        return render_template('deleteorder.html')
    
@app.route('/delete-suppliers',methods =['GET','POST'])
def deletesupplier():
    if request.method=='POST':
        cn=conn.cursor()
        SUPPLIER_ID=request.form.get("supplierid")
       
  
        cn.execute(f"DELETE FROM SUPPLIER WHERE supplier_id = '{SUPPLIER_ID}'")
        conn.commit()
        print('data inserted')
        return jsonify({'message':'successful'})
    else:
        return render_template('deletesupplier.html')

if __name__=='__main__':
    app.run()
