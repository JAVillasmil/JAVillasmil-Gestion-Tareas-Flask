from flask import Flask, render_template, request, redirect, url_for
from models import Tarea
from datetime import datetime,date
import db

app = Flask(__name__)

@app.route("/") #ruta de origen
def home():
    todas_las_tareas = db.session.query(Tarea).all()
    return render_template("index.html", lista_de_tareas=todas_las_tareas)

@app.route("/crear_tarea", methods=["POST"]) #creado de nueva tarea
def crear():
    categoria = request.form["categoria_tarea"] #condicional para evitar nulo en categoria
    if categoria == "":
        categoria = "N/A"
    else:
        categoria = request.form["categoria_tarea"] #condicional para evitar nulo en tarea
    fecha = request.form["fecha_tarea"]
    if  fecha == "":  #condicional para evitar nulo en fecha
        fecha = datetime.now()
        fecha = (fecha.strftime("%d/%m/%Y"))
    else:
        fecha = request.form["fecha_tarea"] #adapatacion de formato fechas a d/m/y
        fecha = fecha.replace("-","/")
        fecha = datetime.strptime(fecha,"%Y/%m/%d")
        fecha = fecha.strftime("%d/%m/%Y")
    contenido = request.form["contenido_tarea"]
    if contenido == "":
        contenido = "No Asignada"
    else:
        contenido = request.form["contenido_tarea"]
    tarea = Tarea(contenido=contenido, hecha=False , categoria=categoria, fecha=fecha) #ensamblado de tarea
    db.session.add(tarea)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/eliminar-tarea/<id>") #eliminado de tarea por id
def eliminar(id):
    tarea = db.session.query(Tarea).filter_by(id_tarea=id).delete()
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/tarea-hecha/<id>") #cambio a verdadero el hecho
def hecha(id):
    tarea = db.session.query(Tarea).filter_by(id_tarea=id).first()
    tarea.hecha = not(tarea.hecha)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/tarea-editar/<id>") #extracion de datos de editado, y cambio a pantalla de editado
def editar(id):
    tarea_edi = db.session.query(Tarea).filter_by(id_tarea=id).first()
    print(id)
    db.session.commit()
    return render_template("editar.html", lista_de_tareas=tarea_edi, id_tarea=id)

@app.route("/redic/", methods=["POST"]) #pantalla de editado / enviado de datos actuales, y solicitud de los nuevos datos
def redic():
    ide = request.form["id_tarea"]
    ide = int(ide) #extracion de informacion del dato
    tarea_edi = db.session.query(Tarea).filter_by(id_tarea=ide).first() #seleccion de tarea a editar
    contenido = request.form["contenido_tarea"] #contenido nuevo
    contenido_d = request.form["contenido_tarea_d"] #contenido antiguo
    if contenido == "": #condicional para contenido
        contenido = contenido_d
    tarea_edi.contenido = contenido #asignacion de contenido
    categoria = request.form["categoria_tarea"] #tarea nueva
    categoria_d = request.form["categoria_tarea_d"] #tarea antigua
    if categoria == "": #condicional de categoria
        categoria = categoria_d
    tarea_edi.categoria = categoria #asignacion de categoria
    fecha = request.form["fecha_tarea"] #fecha nueva
    fecha_d = request.form["fecha_tarea_d"] #fecha antigua
    if fecha != "":
        fecha = request.form["fecha_tarea"]  # adapatacion de formato fechas a d/m/y
        fecha = fecha.replace("-", "/")
        fecha = datetime.strptime(fecha, "%Y/%m/%d")
        fecha = fecha.strftime("%d/%m/%Y")
        tarea_edi.fecha = fecha #asignacion de fecha para editar
    if fecha =="": #condicional de fecha
        fecha = fecha_d
    db.session.commit() #guardado de los cambios en la bd
    return redirect(url_for("home")) #vuelta a la pagina principal

if __name__ == "__main__":
    db.Base.metadata.create_all(db.engine) #funcion de crear base de datos
    app.run(debug=True)