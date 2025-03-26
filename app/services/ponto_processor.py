# app/services/ponto_processor.py
from datetime import datetime, date, time, timedelta
from sqlalchemy.orm import Session
from sqlalchemy import func, and_, or_
from typing import Dict, List, Tuple

from app.models.batida import Batida
from app.models.servidor import Servidor
from app.models.feriado import Feriado
from app.models.justificativa import Justificativa

class ProcessaPonto:
    def __init__(self, db: Session):
        self.db = db
        self.jornada_diaria = timedelta(hours=8)
        
    def processar_batidas_importadas(self):
        """
        Processa todas as batidas recém-importadas para calcular horas trabalhadas,
        detectar inconsistências e notificar os servidores quando necessário
        """
        # Obtém todas as batidas importadas mas não processadas
        batidas = self.db.query(Batida).filter(
            Batida.processado == False
        ).all()
        
        # Agrupa as batidas por servidor e data
        batidas_por_servidor = {}
        for batida in batidas:
            key = (batida.servidor_id, batida.data_original)
            if key not in batidas_por_servidor:
                batidas_por_servidor[key] = []
            batidas_por_servidor[key].append(batida)
        
        # Para cada servidor e data, processa suas batidas
        for (servidor_id, data), batidas_dia in batidas_por_servidor.items():
            self._processar_batidas_dia(servidor_id, data, batidas_dia)
            
    def _processar_batidas_dia(self, servidor_id: int, data: date, batidas: List[Batida]):
        """
        Processa as batidas de um servidor em um dia específico
        """
        # Ordena as batidas por hora
        batidas_ordenadas = sorted(batidas, key=lambda b: b.hora_original)
        
        # Verifica se há batidas suficientes (mínimo 2 para entrada e saída)
        if len(batidas_ordenadas) < 2:
            self._registrar_inconsistencia(
                servidor_id, 
                data, 
                "Número insuficiente de batidas para o dia"
            )
            return
            
        # Verifica se é feriado ou fim de semana
        is_dia_especial = self._is_dia_especial(data)
        
        # Calcula horas trabalhadas
        horas_trabalhadas = self._calcular_horas_trabalhadas(batidas_ordenadas)
        
        # Calcula horas extras ou faltas
        if is_dia_especial:
            # Em dias especiais, todas as horas são consideradas extras
            horas_extras = horas_trabalhadas
            horas_faltantes = timedelta()
        else:
            # Em dias normais, compara com a jornada padrão
            diferenca = horas_trabalhadas - self.jornada_diaria
            horas_extras = max(diferenca, timedelta())
            horas_faltantes = max(-diferenca, timedelta())
        
        # Registra as horas calculadas no banco de dados
        self._registrar_horas_calculadas(
            servidor_id, 
            data, 
            horas_trabalhadas,
            horas_extras,
            horas_faltantes,
            is_dia_especial
        )
        
        # Marca as batidas como processadas
        for batida in batidas:
            batida.processado = True
            self.db.add(batida)
            
        self.db.commit()
    
    def _is_dia_especial(self, data: date) -> bool:
        """Verifica se a data é um feriado ou fim de semana"""
        # Verifica se é fim de semana
        if data.weekday() >= 5:  # 5=Sábado, 6=Domingo
            return True
            
        # Verifica se é feriado
        feriado = self.db.query(Feriado).filter(
            Feriado.data == data
        ).first()
        
        return feriado is not None
    
    def _calcular_horas_trabalhadas(self, batidas: List[Batida]) -> timedelta:
        """Calcula horas trabalhadas a partir das batidas"""
        total = timedelta()
        
        # Para cada par de batidas (entrada/saída), calcula a duração
        for i in range(0, len(batidas) - 1, 2):
            entrada = datetime.combine(batidas[i].data_original, batidas[i].hora_original)
            saida = datetime.combine(batidas[i+1].data_original, batidas[i+1].hora_original)
            
            # Se a saída for anterior à entrada, algo está errado
            if saida <= entrada:
                continue
                
            duracao = saida - entrada
            total += duracao
            
        return total
    
    def _registrar_horas_calculadas(self, servidor_id: int, data: date, 
                                   horas_trabalhadas: timedelta, 
                                   horas_extras: timedelta,
                                   horas_faltantes: timedelta,
                                   is_dia_especial: bool):
        """Registra as horas calculadas no banco de dados"""
        # Implemente conforme sua estrutura de banco de dados
        # Por exemplo, pode atualizar um relatório diário ou
        # criar registros específicos para controle de horas
        pass
    
    def _registrar_inconsistencia(self, servidor_id: int, data: date, descricao: str):
        """Registra inconsistência para posterior notificação ao servidor"""
        # Implemente conforme sua estrutura de banco de dados
        pass