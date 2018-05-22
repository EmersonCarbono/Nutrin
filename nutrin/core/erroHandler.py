from flask import  jsonify, render_template
from core import app, response

@app.errorhandler(500)
def Error500(error):
    response["Mensagem"] = " Tivemos um Problema logo sera resolvido "
    response["Status"] = "Error: {}".format(error)
    response["Dados"] = " "
    return jsonify(response)
    
@app.errorhandler(404)
def Error404(error):
    response["Mensagem"] = "Ops, pagina não encontrada "
    response["Status"] = "",
    response["Dados"] = error
    return render_template('erro/404.html', response=response)

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
    


    
