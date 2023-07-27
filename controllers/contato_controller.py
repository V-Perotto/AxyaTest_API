from flask import Blueprint, request, jsonify
from models.Database import Database

contato = Blueprint("contato", __name__, root_path="./")

@contato.route('/create', methods=['POST'])
def create_contato():
    try:
        data = request.json
        nome = data['Nome']
        sobrenome = data['Sobrenome']
        email = data['Email']
        telefone = data['Telefone']

        conn, cursor = Database().get_connection_and_cursor()

        query = """INSERT INTO contato (Nome, Sobrenome, Email, Telefone) VALUES (%s, %s, %s, %s)"""
        values = (nome, sobrenome, email, telefone)
        cursor.execute(query, values)
        ID = cursor.lastrowid

        Database().commit_and_close(conn, cursor)

        return jsonify({'ID': ID}), 201
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@contato.route('/read/<int:id>', methods=['GET'])
def read_contato(id):
    try:
        conn, cursor = Database().get_connection_and_cursor()

        query = """SELECT * FROM contato WHERE id = %s"""
        cursor.execute(query, (id,))
        contato = cursor.fetchone()

        Database().close(conn, cursor)

        if contato:
            contato_dict = {
                'id': contato[0],
                'nome': contato[1],
                'sobrenome': contato[2],
                'email': contato[3],
                'telefone': contato[4]
            }
            return jsonify(contato_dict)
        else:
            return jsonify({'message': 'Contato não encontrado'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@contato.route('/update/<int:id>', methods=['PUT'])
def update_contato(id):
    try:
        data = request.json
        nome = data.get('Nome')
        email = data.get('Email')
        telefone = data.get('Telefone')

        conn, cursor = Database().get_connection_and_cursor()

        query = "SELECT * FROM contato WHERE id = %s"
        cursor.execute(query, (id,))
        contato = cursor.fetchone()

        if not contato:
            Database().close(conn, cursor)
            return jsonify({'message': 'Contato não encontrado'}), 404

        update_query = "UPDATE contato SET "
        update_values = []
        if nome:
            update_query += "Nome = %s, "
            update_values.append(nome)
        if email:
            update_query += "Email = %s, "
            update_values.append(email)
        if telefone:
            update_query += "Telefone = %s, "
            update_values.append(telefone)

        update_query = update_query.rstrip(', ') + " WHERE id = %s"
        update_values.append(id)
        cursor.execute(update_query, tuple(update_values))

        Database().commit_and_close(conn, cursor)

        return jsonify({'message': 'Contato atualizado com sucesso'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@contato.route('/delete/<int:id>', methods=['DELETE'])
def delete_contato(id):
    try:
        conn, cursor = Database().get_connection_and_cursor()

        query = "SELECT * FROM contato WHERE id = %s"
        cursor.execute(query, (id,))
        contato = cursor.fetchone()

        if not contato:
            Database().close(conn, cursor)
            return jsonify({'message': 'Contato não encontrado'}), 404

        delete_query = "DELETE FROM contato WHERE id = %s"
        cursor.execute(delete_query, (id,))

        Database().commit_and_close(conn, cursor)

        return jsonify({'message': 'Contato deletado com sucesso'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@contato.route('/search/<string:search_string>', methods=['GET'])
def search_contatos(search_string):
    try:
        conn, cursor = Database().get_connection_and_cursor()

        query = "SELECT * FROM contato WHERE nome LIKE %s"
        cursor.execute(query, ('%' + search_string + '%',))
        contatos = cursor.fetchall()

        Database().close(conn, cursor)

        if contatos:
            contatos_list = []
            for contato in contatos:
                contato_dict = {
                    'ID': contato[0],
                    'Nome': contato[1],
                    'Sobrenome': contato[2],
                    'Email': contato[3],
                    'Telefone': contato[4]
                }
                contatos_list.append(contato_dict)
            return jsonify(contatos_list)
        else:
            return jsonify({'message': 'Nenhum contato encontrado'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 500