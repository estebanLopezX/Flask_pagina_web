from flask import Flask, redirect, render_template, url_for
from cliente_dao import ClienteDAO
from cliente import Cliente
from cliente_forma import ClienteForma


app = Flask(__name__)
app.config['SECRET_KEY'] = 'holaMundo123'

titulo_app = 'Zona Fit GYM'


@app.route('/') #url: http://localhost:5000/
@app.route('/index.html') # url: http://localhost:5000/index.html
def inicio():
    app.logger.debug('Se ha accedido a la página de inicio')
    clientes_db = ClienteDAO.seleccionar()
    # Creamos un objeto de cliente form vacio 
    cliente = Cliente()
    # Cliente forma es para llenar el formmulario 
    cliente_forma = ClienteForma(obj=cliente)
    return render_template('index.html', titulo=titulo_app, clientes=clientes_db, forma=cliente_forma)


@app.route('/guardar', methods=['POST'])
def guardar():
    cliente_forma = ClienteForma()
    print(cliente_forma.errors)
    cliente = Cliente()
    cliente_forma.populate_obj(cliente)
    print('entro al if ')
    if not cliente.id:
        print('Insertando cliente')
        ClienteDAO.insertar(cliente)
    else:
        print('Actualizando cliente')
        ClienteDAO.actualizar(cliente)

    return redirect(url_for('inicio'))

@app.route('/limpiar')
def limpiar():
    return redirect(url_for('inicio'))


@app.route('/editar/<int:id>')
def editar(id):
    if id is not None:
        print(f'Editando cliente con id: {id}')
    cliente = ClienteDAO.seleccionar_por_id(id)
    clienteForma = ClienteForma(obj=cliente)
    clientes_db = ClienteDAO.seleccionar()
    return render_template('index.html', titulo=titulo_app, forma = clienteForma, clientes=clientes_db)



@app.route('/eliminar/<int:id>', methods=['POST', 'GET'])
def eliminar(id):
    cliente = ClienteDAO.seleccionar_por_id(id)
    if cliente:        
        ClienteDAO.eliminar(cliente)
    return redirect(url_for('inicio'))



if __name__ == '__main__':
    app.run(debug=True)