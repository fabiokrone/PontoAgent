# app/core/config.py
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

class Settings:
    # Configurações da aplicação
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "Sistema Automatizado de Gestão de Ponto")
    API_PREFIX: str = os.getenv("API_PREFIX", "/api")
    CORS_ORIGINS: str = os.getenv("CORS_ORIGINS", "http://localhost,http://localhost:8000")
    
    # Configurações do banco de dados
    POSTGRES_USER: str = os.getenv("POSTGRES_USER", "postgres")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "postgres")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "gestao_ponto")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "db")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", "5432")
    
    # Montar URI do banco de dados
    DATABASE_URI: str = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

# Criar instância de configurações
settings = Settings()