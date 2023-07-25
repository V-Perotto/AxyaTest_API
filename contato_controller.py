from config import api
        
@api.route("/contatos/<int:contato_id>", methods=["GET"])
def read(contato_id):
    """
        A API deve receber uma solicitação com o ID de um contato e retornar as informações detalhadas do contato.
    """
    return "read"

@api.route("/contatos/<int:contato_id>", methods=["POST"])
def update(contato_id):
    """
        A API deve receber uma solicitação com o ID do contato a ser atualizado e os campos a serem modificados (nome, email e telefone).
    """
    return "update" 

@api.route("/contatos/<int:contato_id>", methods=['DELETE'])
def delete(contato_id):
    """
        A API deve receber uma solicitação com o ID de um contato e permitir a exclusão do mesmo.
    """
    return "delete" 

@api.route("/contatos/", methods=["GET"])
def search():
    """
        A API deve receber parte de um nome e retornar os possiveis para aquele contato pesquisado.
    """
    return "search" 