class DocumentClassifier:
    """Classifica o tipo de documento com base no conteúdo textual extraído."""
    
    @staticmethod
    def classify(text: str) -> str:
        text_lower = text.lower()
        
        # Lógica de classificação baseada em palavras-chave comuns
        if any(k in text_lower for k in ["nota fiscal", "nfe", "danfe", "invoice"]):
            return "invoice"
        elif any(k in text_lower for k in ["recibo", "receipt", "comprovante", "merchant"]):
            return "receipt"
        elif any(k in text_lower for k in ["contrato", "agreement", "cláusula", "foro"]):
            return "contract"
        else:
            return "generic_document"
