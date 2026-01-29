import requests
import time
from config.settings import Settings

class AzureDocumentService:
    """Gerencia a comunicação com a API do Azure Document Intelligence."""
    
    def __init__(self):
        self.endpoint = Settings.AZURE_ENDPOINT
        self.key = Settings.AZURE_KEY
        self.api_version = "2023-07-31"

    def analyze_document(self, file_bytes: bytes, model_id: str = "prebuilt-document") -> dict:
        """Envia o documento para análise e aguarda o resultado."""
        url = f"{self.endpoint}/documentintelligence/documentModels/{model_id}:analyze?api-version={self.api_version}"
        
        headers = {
            "Ocp-Apim-Subscription-Key": self.key,
            "Content-Type": "application/octet-stream"
        }

        # Inicia a análise
        response = requests.post(url, headers=headers, data=file_bytes)
        if response.status_code != 202:
            raise Exception(f"Erro ao iniciar análise: {response.text}")

        # URL para consultar o status da operação
        operation_url = response.headers["Operation-Location"]
        
        # Polling para obter o resultado
        while True:
            result_response = requests.get(operation_url, headers=headers)
            result = result_response.json()
            
            status = result.get("status")
            if status == "succeeded":
                return result
            elif status == "failed":
                raise Exception(f"Falha no processamento do documento: {result}")
            
            # Aguarda antes da próxima consulta
            time.sleep(2)
