# Documentação Técnica e Arquitetura

Este documento detalha as decisões técnicas e a estrutura interna do projeto **Azure Fake Docs**.

## 1. Visão Geral Técnica

O sistema foi projetado para ser um pipeline de processamento de documentos assíncrono. A escolha da arquitetura em camadas visa permitir que o serviço de IA (Azure) possa ser substituído ou atualizado sem impactar a lógica de negócio ou a interface do usuário.

## 2. Componentes Principais

### 2.1. Azure Document Intelligence Service
Localizado em `src/services/`, este componente encapsula a complexidade da API REST da Azure. Ele gerencia:
- Autenticação via chaves de API.
- Envio de binários.
- Mecanismo de *polling* (aguardar o processamento assíncrono da Azure).

### 2.2. Document Classifier
O classificador (`src/domain/document_classifier.py`) utiliza uma abordagem baseada em heurísticas e palavras-chave para identificar o tipo de documento. Em uma evolução do projeto, este componente poderia ser substituído por um modelo de NLP (Natural Language Processing) mais avançado.

### 2.3. Smart Parser
O parser (`src/domain/parsers.py`) é responsável por transformar o conteúdo bruto retornado pela Azure em um objeto `DocumentResult`. Ele aplica regras de extração específicas (como Regex) dependendo da classe do documento identificada.

## 3. Fluxo de Execução

1. **Upload:** O usuário carrega o arquivo no Streamlit.
2. **Orquestração:** O `DocumentUseCase` recebe os bytes do arquivo.
3. **Análise:** O `AzureDocumentService` envia para a nuvem e recebe o JSON bruto.
4. **Parsing:** O `DocumentParser` analisa o texto, classifica como (Invoice/Receipt/Contract) e extrai os campos relevantes.
5. **Resposta:** O objeto estruturado retorna para a UI para exibição.

## 4. Decisões de Design

- **Uso de Dataclasses:** Para garantir tipagem e estrutura clara nos modelos de domínio.
- **Injeção de Dependência (Simulada):** O uso de classes de serviço facilita testes unitários futuros.
- **Tratamento de Erros:** Implementado na camada de aplicação e UI para garantir que falhas na API da Azure não quebrem a experiência do usuário.

## 5. Possíveis Evoluções

- **Persistência:** Integração com Azure Blob Storage para salvar os documentos originais.
- **Banco de Dados:** Armazenamento dos metadados extraídos em um Azure SQL ou Cosmos DB.
- **LLM Integration:** Uso de Azure OpenAI para extração de dados complexos que fogem de padrões de Regex.
- **Containerização:** Criação de um Dockerfile para facilitar o deploy em Azure App Service.
