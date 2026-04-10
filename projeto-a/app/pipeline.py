from app.etl import extrair_dados, transformar_dados
from app.insights import gerar_insights
from app.decision import motor_decisao, executar_acoes

def pipeline_diario():
    print("🔄 Iniciando pipeline...")
    dados = extrair_dados()
    dados_limpos = transformar_dados(dados)
    insights = gerar_insights(dados_limpos)
    decisoes = motor_decisao(insights)
    executar_acoes(decisoes)
    print("✅ Pipeline finalizado.")
