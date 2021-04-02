"""plotPlotly.py
Plotting functions that requrire the plotly library to be installed
"""
import plotly.graph_objects as go
import plotly.express as px

def histBase(df, x, y, filename="standard"):
    """
    Input a dataframe object and a single x value (key value of the x label)
    and either 1 or more samples for Y so that a histogram can be created
    with x-axis - x and y as samples
    """
    subs = df.groupby(x).sum()[y]
    fig = go.Figure()
    for key in subs.columns:
        fig.add_trace(go.Bar(
            x=subs[key].index,
            y=subs[key].to_numpy(),
            name=key
        )
                      )
        fig.update_layout(barmode='stack', title=x)

    return fig

