from flask import Flask, jsonify, request

app = Flask('Servidor Get')
@app.route('/',methods=['GET'])

def hola():

    # obtengo los datos del request get.
    # notar que en este contexto request contiene la informacion 
    # que viene de la peticion externa (el metodo get_json lo transforma en un diccionario)
    data=request.args.to_dict()
    try:            
        resp='el cuadrado de a es : '+str(int(data['a'])*int(data['a']))
    except:
        resp='no se envio la variable a'
    return(resp)

app.run(host='0.0.0.0',  port=5002 )