def motor_decisao(insights):
    print("🤖 Tomando decisões...")
    decisoes = []
    top_produtos = insights.get("top_produtos", {})
    for produto, volume in top_produtos.items():
        if volume > 50:
            decisoes.append({
                "acao": "repor_estoque",
                "produto": produto
            })
    return decisoes

def executar_acoes(decisoes):
    print("⚡ Executando ações...")
    for d in decisoes:
        if d["acao"] == "repor_estoque":
            print(f"📦 Repor estoque: {d['produto']}")
