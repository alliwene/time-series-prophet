from typing import List

import pandas as pd

import plotly.graph_objects as go
from plotly.subplots import make_subplots


def forecast_plot(
    df1: pd.DataFrame,
    df2: pd.DataFrame,
    date_col: str,
    pred: pd.Series,
    names: List[str],
    model_name: str,
    xaxis_title: str,
    yaxis_title: str,
):
    df1.set_index(date_col, inplace=True)
    df2.set_index(date_col, inplace=True)
    
    fig = make_subplots(rows=1, cols=1, vertical_spacing=0.05)

    fig.add_trace(
        go.Scatter(
            name=names[0],
            x=df1.index,
            y=df1["y"],
            marker=dict(size=10, color="blue"),
            textfont=dict(color="black", size=18, family="Times New Roman"),
        )
    )

    fig.add_trace(
        go.Scatter(
            name=names[1], x=df2.index, y=df2["y"], marker=dict(size=10, color="red")
        )
    )

    fig.add_trace(
        go.Scatter(
            name=names[2], x=df2.index, y=pred, marker=dict(size=10, color="green")
        )
    )

    fig.update_xaxes(
        rangeselector=dict(
            buttons=list(
                [
                    dict(count=1, label="1m", step="month", stepmode="backward"),
                    dict(count=6, label="6m", step="month", stepmode="backward"),
                    dict(count=1, label="YTD", step="year", stepmode="todate"),
                    dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(step="all"),
                ]
            )
        )
    )
    fig.update_layout(
        title={
            "text": f"{model_name} Model Plot",
            "y": 0.98,
            "x": 0.5,
            "xanchor": "center",
            "yanchor": "top",
            "font": {"size": 15},
        },
        xaxis_title=xaxis_title,
        yaxis_title=yaxis_title,
    )
    fig.update_layout(
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    names = set()
    fig.for_each_trace(
        lambda trace: trace.update(showlegend=False)
        if (trace.name in names)
        else names.add(trace.name)
    )

    fig.show()


if __name__ == "__main__":
    forecast_plot()
