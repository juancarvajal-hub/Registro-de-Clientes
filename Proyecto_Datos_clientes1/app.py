from flask import Flask, render_template, request, redirect, url_for
import csv
import os
from datetime import datetime
import threading

app = Flask(__name__)

# Carpeta base donde se guardan los datos
BASE_DIR = os.path.join('data', 'clientes')

@app.route('/')
def index():
    return render_template('formulario.html')

@app.route('/guardar', methods=['POST'])
def guardar():
    datos = request.form.to_dict()
    fecha_hoy = datetime.now().strftime('%Y-%m-%d')
    datos_con_fecha = {'fecha': fecha_hoy, **datos}

    carpeta_dia = os.path.join(BASE_DIR, fecha_hoy)
    os.makedirs(carpeta_dia, exist_ok=True)

    archivo_csv = os.path.join(carpeta_dia, 'clientes.csv')
    archivo_nuevo = not os.path.exists(archivo_csv)

    with open(archivo_csv, mode='a', newline='', encoding='utf-8-sig') as archivo:
        writer = csv.DictWriter(archivo, fieldnames=list(datos_con_fecha.keys()), delimiter=';')
        if archivo_nuevo:
            writer.writeheader()
        writer.writerow(datos_con_fecha)

    return redirect(url_for('index'))

# Nueva ruta para cerrar el servidor
@app.route('/cerrar', methods=['POST'])
def cerrar():
    def detener_servidor():
        func = request.environ.get('werkzeug.server.shutdown')
        if func:
            func()

    threading.Thread(target=detener_servidor).start()
    return "<h3>Servidor detenido correctamente. Ya puedes cerrar esta pestaña.</h3>"

if __name__ == '__main__':
    app.run(debug=True)