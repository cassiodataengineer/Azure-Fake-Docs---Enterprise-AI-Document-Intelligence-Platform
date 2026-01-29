# Azure Fake Docs — AI Document Intelligence Platform

[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/)
[![Azure](https://img.shields.io/badge/azure-document--intelligence-0089D6.svg)](https://azure.microsoft.com/)
[![Streamlit](https://img.shields.io/badge/ui-streamlit-FF4B4B.svg)](https://streamlit.io/)

Este repositório contém o projeto **Azure Fake Docs**, uma plataforma desenvolvida para automatizar a extração e classificação de dados em documentos não estruturados. Utilizando o serviço **Azure Document Intelligence**, o sistema transforma imagens e PDFs em dados estruturados (JSON) através de um pipeline de processamento inteligente.

## 🎯 Objetivo do Projeto

O foco principal é demonstrar a aplicação prática de serviços de IA da Azure em um ambiente com arquitetura modular e escalável. O projeto resolve o problema comum de triagem manual de documentos como notas fiscais, recibos e contratos, oferecendo uma interface amigável para o usuário final.

## 🏗️ Arquitetura do Sistema

A aplicação foi construída seguindo os princípios de **Clean Architecture**, garantindo separação de responsabilidades e facilidade de manutenção:

- **Frontend (UI):** Interface interativa construída com Streamlit.
- **Application Layer:** Orquestração do fluxo de negócio e casos de uso.
- **Domain Layer:** Contém a lógica de classificação, modelos de dados e parsers semânticos.
- **Infrastructure Layer:** Implementação da comunicação com a API REST do Azure Document Intelligence.

### Estrutura de Pastas
```text
src/
├── app.py                # Ponto de entrada (Streamlit)
├── application/          # Casos de uso
├── domain/               # Regras de negócio e modelos
├── services/             # Integrações externas (Azure)
└── config/               # Gestão de configurações
```

## 🚀 Funcionalidades

- **Ingestão de Documentos:** Upload de arquivos PDF, PNG e JPEG.
- **Classificação Automática:** Identificação do tipo de documento via análise de conteúdo.
- **Extração de Campos:** Captura de datas, valores e entidades específicas.
- **Normalização:** Saída padronizada em formato JSON para integração com outros sistemas.

## ⚙️ Configuração e Instalação

### Pré-requisitos
- Python 3.9 ou superior.
- Recurso do **Azure Document Intelligence** criado no portal Azure.

### Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/azure-fake-docs.git
   cd azure-fake-docs
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure as variáveis de ambiente:
   - Copie o arquivo `.env.example` para `.env`.
   - Preencha com seu `AZURE_ENDPOINT` e `AZURE_KEY`.

4. Execute a aplicação:
   ```bash
   streamlit run src/app.py
   ```

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python
- **IA/ML:** Azure Document Intelligence (AI Services)
- **Interface:** Streamlit
- **Integração:** Requests / REST API

## 📄 Documentação Técnica

Para uma visão aprofundada sobre as decisões de design, diagramas e detalhes de implementação, consulte a [Documentação Técnica]([./docs/ARCHITECTURE.md](https://github.com/cassiodataengineer/Azure-Fake-Docs---Enterprise-AI-Document-Intelligence-Platform/blob/main/ARCHITECTURE.md) 

---
Projeto desenvolvido como parte do desafio de projeto da **DIO**.
**Autor:** Cássio Campos
