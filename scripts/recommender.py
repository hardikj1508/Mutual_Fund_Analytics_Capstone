import pandas as pd

funds = pd.read_csv("../notebooks/fund_scorecard.csv")

def recommend(risk_level):

    if risk_level == "Low":
        recommendations = funds.sort_values(
            "sharpe_ratio",
            ascending=False
        ).head(3)

    elif risk_level == "Moderate":
        recommendations = funds.sort_values(
            "sharpe_ratio",
            ascending=False
        ).head(3)

    else:
        recommendations = funds.sort_values(
            "sharpe_ratio",
            ascending=False
        ).head(3)

    return recommendations

print("Top Funds:")

print(
    recommend("High")
)