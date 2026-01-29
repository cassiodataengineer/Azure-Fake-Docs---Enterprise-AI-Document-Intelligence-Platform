import re
from typing import Dict, Any
from .document_classifier import DocumentClassifier
from .models import DocumentResult

class DocumentParser:
    """Extrai campos específicos dependendo do tipo de documento identificado."""
    
    @staticmethod
    def parse(analyze_result: dict) -> DocumentResult:
        content = analyze_result.get("analyzeResult", {}).get("content", "")
        doc_type = DocumentClassifier.classify(content)
        
        fields = {}
        if doc_type == "invoice":
            fields = DocumentParser._parse_invoice(content)
        elif doc_type == "receipt":
            fields = DocumentParser._parse_receipt(content)
        elif doc_type == "contract":
            fields = DocumentParser._parse_contract(content)
            
        return DocumentResult(
            type=doc_type,
            raw_text=content,
            fields=fields
        )

    @staticmethod
    def _parse_invoice(text: str) -> Dict[str, Any]:
        # Exemplo de extração via regex simples (em produção usaria modelos da Azure específicos)
        return {
            "category": "Fiscal",
            "detected_date": DocumentParser._regex_find(text, r"(\d{2}/\d{2}/\d{4})"),
            "total_value": DocumentParser._regex_find(text, r"(?:R\$|Total)\s*([\d.,]+)")
        }

    @staticmethod
    def _parse_receipt(text: str) -> Dict[str, Any]:
        return {
            "category": "Comercial",
            "merchant": DocumentParser._regex_find(text, r"(?:Estabelecimento|Local):\s*(.*)"),
            "amount": DocumentParser._regex_find(text, r"(?:Valor|Pago):\s*([\d.,]+)")
        }

    @staticmethod
    def _parse_contract(text: str) -> Dict[str, Any]:
        return {
            "category": "Jurídico",
            "parties": "Identificação de partes pendente",
            "date": DocumentParser._regex_find(text, r"assinado em\s*(\d{2}/\d{2}/\d{4})")
        }

    @staticmethod
    def _regex_find(text: str, pattern: str) -> Any:
        match = re.search(pattern, text, re.IGNORECASE)
        return match.group(1).strip() if match else "Não encontrado"
