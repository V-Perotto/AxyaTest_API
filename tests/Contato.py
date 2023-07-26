import requests

class Contato:
    
    def __init__(self, base_url='http://localhost:5000'):
        self.base_url = base_url
    
    def create_contato(self, dados: dict):    
        """Create - Contato

        Args:
            dados (dict): <Nome>, <Sobrenome>, <Email>, <Telefone>

        Returns:
            dict: response.json()
        """
        url = f'{self.base_url}/contato/create'
        response = requests.post(url, json=dados)

        if response.status_code == 201 or response.status_code == 200:
            print('Contato criado com sucesso!')
            return response.json()
        elif response.status_code == 404:
            print('Contato não criado.')
        else:
            print('Erro ao criar o contato:', response.json())

    def read_contato(self, ID: int):
        """Read - Contato

        Args:
            ID (int): ID of Contato
        """
        url = f'{self.base_url}/contato/read/{ID}'
        response = requests.get(url, json={"ID": ID})

        if response.status_code == 200:
            print(f'Contato lido com sucesso!\n{response.json()}')
        elif response.status_code == 404:
            print('Contato não encontrado.')
        else:
            print(f'Erro ao ler o contato:\n{response.json()}')

    def update_contato(self, ID: int, dados: dict):
        """Update - Contato

        Args:
            ID (int): ID of Contato
            dados (dict): <Nome>, <Sobrenome>, <Email>, <Telefone>

        Returns:
            dict: response.json()
        """
        url = f'{self.base_url}/contato/update/{ID}'
        dados["ID"] = ID
        response = requests.put(url, json=dados)

        if response.status_code == 200:
            print('Contato atualizado com sucesso!')
            return response.json()
        elif response.status_code == 404:
            print('Contato não encontrado.')
        else:
            print(f'Erro ao atualizar o contato:\n{response.json()}')

    def delete_contato(self, ID: int):
        """Delete - Contato

        Args:
            ID (int): ID of Contato

        Returns:
            dict: response.json()
        """
        url = f'{self.base_url}/contato/delete/{ID}'
        response = requests.delete(url, json={"ID": ID})

        if response.status_code == 200:
            print('Contato deletado com sucesso!')
            return response.json()
        elif response.status_code == 404:
            print('Contato não deletado.')
        else:
            print(f'Erro ao deletar o contato:\n{response.json()}')

    def search_contato(self, nome: str):
        """Search - Contato

        Args:
            nome (str): <Nome>

        Returns:
            dict: response.json()
        """
        url = f'{self.base_url}/contato/search/{nome}'
        response = requests.get(url, json={"Nome": nome})

        if response.status_code == 200:
            print('Contatos encontrados com sucesso!')
            return response.json()
        elif response.status_code == 404:
            print('Contatos não encontrados.')
        else:
            print(f'Erro ao encontrar os contatos:\n{response.json()}')