from dataclasses import dataclass, field
from typing import Dict, Any, Optional

@dataclass
class DocumentResult:
    """Modelo que representa o resultado do processamento de um documento."""
    type: str
    raw_text: str
    fields: Dict[str, Any] = field(default_factory=dict)
    confidence: float = 0.0
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "document_type": self.type,
            "extracted_fields": self.fields,
            "confidence_score": self.confidence,
            "content_summary": self.raw_text[:200] + "..." if len(self.raw_text) > 200 else self.raw_text
        }
