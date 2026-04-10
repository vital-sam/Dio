def gerar_insights(df):
    print("📊 Gerando insights...")
    insights = {}
    if "product" in df.columns:
        insights["top_produtos"] = (
            df.groupby("product")["price"]
            .count()
            .sort_values(ascending=False)
            .head(5)
            .to_dict()
        )
    if "country" in df.columns:
        insights["top_por_pais"] = (
            df.groupby(["country", "product"])["price"]
            .count()
            .reset_index()
            .sort_values(["country", "price"], ascending=False)
            .to_dict(orient="records")
        )
    return insights
