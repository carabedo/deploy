from flask import Flask, jsonify, request
app = Flask('Predictor de examenes')
#aclaramos la ruta del recurso y el tipo: (podriamos poner /modelos/listener)
@app.route('/',methods=['POST'])
#solo con esta linea, ya tenemos un recurso recibiendo requests en "127.0.0.1/".
#defino la funcion que manejarara el request
def predict():
    # obtengo los datos del request post.
    # notar que en este contexto request contiene la informacion 
    # que viene de la peticion externa (el metodo get_json lo transforma en un diccionario)
    data = request.get_json(force=True)
    try:
        a_vector = np.array(data['a']).astype('int')
        # Le damos forma de un diccionario para poder hacer el traspaso a json trivialmente
        a_2=a_vector**2
        #importante pasar a lista     
        resp={'response' : a_2.tolist() }
    except:
        print('no mandaron a')
        resp={'response' : 'no esta presente la variable a'}
       
        # en esta linea, transformamos el diccionario en json con jsonify (funcionalidad de flask)
        # y respondemos el request con un json mediante este return
        # este json es incorporado en el cuerpo de la respuesta
    return jsonify(resp)

app.run(host='0.0.0.0', port=5001)