from flask import  jsonify
from core import app,response


@app.errorhandler(500)
def Error500(error):
    response["Mensagem"] = " Tivemos um Problema logo sera resolvido "
    response["Status"] = "Error: {}".format(error)
    response["Dados"] = " "
    return jsonify(response)
    
@app.errorhandler(404)
def Error404(error):
    response["Mensagem"] = " Recurso Invalida "
    response["Status"] = "Error: {}".format(error)
    response["Dados"] = " "
    return jsonify(response)

@app.errorhandler(400)
def Error400(error):
    response["Mensagem"] = " Requisição Invalida "
    response["Status"] = "Error: {}".format(error)
    response["Dados"] = ""
    return jsonify(response)

@app.errorhandler(403)
def Error403(error):
    response["Mensagem"] = " Acesso Negado "
    response["Status"] = "Error: {}".format(error)
    response["Dados"] = ""
    return jsonify(response)
    


    
