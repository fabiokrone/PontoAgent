-- Criação da extensão para UUID
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Criação do schema
CREATE SCHEMA IF NOT EXISTS ponto;

-- Comentário no banco de dados
COMMENT ON DATABASE gestao_ponto IS 'Banco de dados para o Sistema Automatizado de Gestão de Ponto';