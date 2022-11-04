from flask import Flask,render_template,request,redirect
from flask_mysqldb import MySQL


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'sql541.main-hosting.eu'
app.config['MYSQL_USER'] = 'u109726298_root_denzel'
app.config['MYSQL_PASSWORD'] = 'Abc12345@'
app.config['MYSQL_DB'] = 'u109726298_bd_denzel'
mysql = MySQL(app)

@app.route("/")
def objetos():
    cur = mysql.connection.cursor()
    cur.execute('select * from productos')
    rv = cur.fetchall()
    return render_template("productos.html",objeto=rv)

@app.get("/crear")
def create():
    return render_template("create.html")

@app.post("/crear")
def crear():
    if request.method == "POST":
        nombre = request.form["nombre"]
        descrip = request.form["descripcion"]
        precio = request.form["precio"]
        con = mysql.connection.cursor()
        con.execute("insert into productos(nombre,descripcion,precio) values(%s,%s,%s)",(nombre,descrip,precio))
        mysql.connection.commit()
        
        
    return redirect('/')
@app.get("/eliminar/<delete>")
def eliminar(delete):
    if request.method == "GET":
         id = delete
         con = mysql.connection.cursor()
         con.execute("delete from productos where token=%s",(id))
         mysql.connection.commit()      

    return redirect("/")

@app.get("/actualizar/<token>")
def actualizar(token):
        if request.method=="GET":
              cur = mysql.connection.cursor()
              cur.execute("select * from productos where token=%s",[token])
              rv = cur.fetchone()
    
        return render_template("update.html",objeto=rv)
@app.post("/actualizar")
def actualizate():
    if request.method == "POST":
        nombre = request.form["nombre"]
        descrip = request.form["descripcion"]
        precio = request.form["precio"]
        token = request.form["token"]
        con = mysql.connection.cursor()
        con.execute("update productos set nombre=%s,descripcion=%s,precio=%s where token=%s",(nombre,descrip,precio,token))
        mysql.connection.commit()
    return redirect("/")

        

if __name__ == '__main__':
    
    app.run(port=3000, debug=True,)