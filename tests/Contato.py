import requests
from logger.Logger import Logger

logger = Logger()

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
            logger.log_info('Contato criado com sucesso!', status=response.status_code, response=response.json())
            return response.json()
        elif response.status_code == 404:
            logger.log_error('Contato não criado.', status=response.status_code, response=response.json())
        else:
            logger.log_critical('Erro ao criar o contato', status=response.status_code, response=response.json())

    def read_contato(self, ID: int):
        """Read - Contato

        Args:
            ID (int): ID of Contato
        """
        url = f'{self.base_url}/contato/read/{ID}'
        response = requests.get(url, json={"ID": ID})

        if response.status_code == 200:
            logger.log_info("Contato lido com sucesso!", status=response.status_code, response=response.json())
        elif response.status_code == 404:
            logger.log_error('Contato não encontrado.', status=response.status_code, response=response.json())
        else:
            logger.log_critical("Erro ao ler o contato", status=response.status_code, response=response.json())

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
            logger.log_info('Contato atualizado com sucesso!', status=response.status_code, response=response.json())
            return response.json()
        elif response.status_code == 404:
            logger.log_error('Contato não encontrado.', status=response.status_code, response=response.json())
        else:
            logger.log_critical("Erro ao atualizar o contato", status=response.status_code, response=response.json())

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
            logger.log_info('Contato deletado com sucesso!', status=response.status_code, response=response.json())
            return response.json()
        elif response.status_code == 404:
            logger.log_error('Contato não deletado.', status=response.status_code, response=response.json())
        else:
            logger.log_critical("Erro ao deletar o contato", status=response.status_code, response=response.json())

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
            logger.log_info('Contatos encontrados com sucesso!', status=response.status_code, response=response.json())
            return response.json()
        elif response.status_code == 404:
            logger.log_error('Contatos não encontrados.', status=response.status_code, response=response.json())
        else:
            logger.log_critical("Erro ao encontrar os contatos", status=response.status_code, response=response.json())