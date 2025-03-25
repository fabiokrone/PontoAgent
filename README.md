# Sistema Automatizado de Gestão de Ponto

Um sistema inteligente para gestão e conferência automatizada de ponto, com comunicação via WhatsApp e email, usando agentes Crew AI para processamento de dados.

## Descrição

O Sistema Automatizado de Gestão de Ponto é uma solução completa para automatizar a conferência de batidas de ponto, validar inconsistências, gerenciar justificativas via WhatsApp/email e gerar relatórios para aprovação dos gestores. O sistema utiliza agentes inteligentes (Crew AI) para processar os dados e facilitar o fluxo de trabalho.

## Arquitetura

- **Backend**: FastAPI
- **Banco de dados**: PostgreSQL
- **Comunicação**: Integração WhatsApp via Evolution API e serviço de email
- **Processamento**: Agentes Crew AI para tarefas específicas
- **Implantação**: Docker para containerização

## Funcionalidades Principais

- Importação de arquivos CSV/Excel de batidas de ponto
- Conferência automatizada com detecção de inconsistências
- Comunicação com colaboradores e gestores via WhatsApp
- Fluxo simplificado de aprovação de justificativas
- Geração e envio automático de relatórios

## Pré-requisitos

- Docker e Docker Compose
- Git

## Instalação e Configuração

1. Clone o repositório:
   ```bash
   git clone [URL_DO_REPOSITÓRIO]
   cd PontoAgent
   ```

2. Crie o arquivo de variáveis de ambiente:
   ```bash
   cp .env.example .env
   ```
   Configure as variáveis no arquivo `.env` conforme necessário.

3. Construa e inicie os containers Docker:
   ```bash
   docker-compose build
   docker-compose up -d
   ```

4. Acesse a aplicação em:
   - API: http://localhost:8000
   - Documentação API: http://localhost:8000/api/v1/docs
   - PGAdmin: http://localhost:5050

## Estrutura do Projeto

```
PontoAgent/
├── app/                      # Código da aplicação
├── docker/                   # Arquivos de configuração Docker
│   ├── app/                  # Dockerfile da aplicação
│   └── postgres/             # Scripts de inicialização do banco de dados
├── docker-compose.yml        # Configuração dos serviços Docker
├── requirements.txt          # Dependências Python
└── .env                      # Variáveis de ambiente
```

## Desenvolvimento

Para desenvolver novas funcionalidades:

1. As alterações em arquivos Python são automaticamente aplicadas graças ao hot-reload.
2. Para instalar novas dependências, adicione-as ao `requirements.txt` e reconstrua a imagem:
   ```bash
   docker-compose build
   docker-compose up -d
   ```
3. Para acessar o shell da aplicação:
   ```bash
   docker-compose exec app bash
   ```

## Licença

[Especifique a licença do projeto]

## Contato

[Adicione informações de contato]