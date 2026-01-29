import streamlit as st
import sys
import os

# Adiciona o diretório src ao path para facilitar imports
sys.path.append(os.path.join(os.path.dirname(__file__)))

from application.document_use_case import DocumentUseCase
from config.settings import Settings

# Configuração da página
st.set_page_config(page_title="Azure Fake Docs", page_icon="📄", layout="wide")

def main():
    st.title("📄 Azure Fake Docs")
    st.markdown("---")
    st.sidebar.header("Configurações")
    
    # Verificação de credenciais
    if not Settings.AZURE_KEY or not Settings.AZURE_ENDPOINT:
        st.sidebar.error("⚠️ Credenciais da Azure não encontradas no .env")
        st.info("Por favor, configure o arquivo `.env` com suas chaves da Azure para começar.")
        return

    st.sidebar.success("✅ Conectado à Azure")

    st.write("### Upload de Documento")
    st.write("Envie uma nota fiscal, recibo ou contrato para extração inteligente de dados.")

    uploaded_file = st.file_uploader(
        "Escolha um arquivo", 
        type=["pdf", "jpg", "jpeg", "png"],
        help="Suporta PDF e imagens de documentos."
    )

    if uploaded_file is not None:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Pré-visualização")
            if uploaded_file.type == "application/pdf":
                st.info("Visualização de PDF não disponível diretamente, mas o arquivo foi carregado.")
            else:
                st.image(uploaded_file, use_container_width=True)

        with col2:
            st.subheader("Processamento AI")
            if st.button("Analisar Documento"):
                with st.spinner("Aguardando resposta do Azure Document Intelligence..."):
                    try:
                        use_case = DocumentUseCase()
                        result = use_case.execute(uploaded_file.read())
                        
                        st.success("Processamento concluído!")
                        
                        # Exibição dos resultados estruturados
                        st.metric("Tipo Identificado", result.type.upper())
                        
                        st.write("#### Dados Extraídos")
                        st.json(result.to_dict())
                        
                        with st.expander("Ver Texto Bruto"):
                            st.text(result.raw_text)
                            
                    except Exception as e:
                        st.error(f"Ocorreu um erro: {str(e)}")

if __name__ == "__main__":
    main()
