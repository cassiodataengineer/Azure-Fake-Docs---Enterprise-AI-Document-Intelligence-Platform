from services.azure_document_service import AzureDocumentService
from domain.parsers import DocumentParser
from domain.models import DocumentResult

class DocumentUseCase:
    """Orquestra o fluxo de processamento de um documento."""
    
    def __init__(self):
        self.azure_service = AzureDocumentService()
        self.parser = DocumentParser()

    def execute(self, file_bytes: bytes) -> DocumentResult:
        """Executa o pipeline completo: Envio -> Extração -> Parsing."""
        # 1. Envia para o Azure
        raw_result = self.azure_service.analyze_document(file_bytes)
        
        # 2. Processa e classifica o resultado
        processed_doc = self.parser.parse(raw_result)
        
        return processed_doc
