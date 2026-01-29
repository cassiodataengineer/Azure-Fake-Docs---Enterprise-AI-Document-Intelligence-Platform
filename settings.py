import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env se ele existir
load_dotenv()

def get_required_env(name: str) -> str:
    """Retorna o valor de uma variável de ambiente ou levanta erro se não existir."""
    value = os.getenv(name)
    if not value:
        raise EnvironmentError(f"A variável de ambiente obrigatória '{name}' não foi configurada.")
    return value

class Settings:
    # Configurações do Azure Document Intelligence
    AZURE_ENDPOINT = os.getenv("AZURE_ENDPOINT", "")
    AZURE_KEY = os.getenv("AZURE_KEY", "")
    
    # Configurações de Armazenamento (Opcional)
    AZURE_STORAGE_CONNECTION_STRING = os.getenv("AZURE_STORAGE_CONNECTION_STRING")
    CONTAINER_NAME = os.getenv("CONTAINER_NAME", "documents")
    
    @classmethod
    def validate(cls):
        """Valida se as configurações mínimas estão presentes."""
        if not cls.AZURE_ENDPOINT or not cls.AZURE_KEY:
            raise ValueError("AZURE_ENDPOINT e AZURE_KEY precisam estar configurados no arquivo .env")
