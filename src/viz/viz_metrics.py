from typing import List

import pandas as pd

import plotly.express as px

from src.enums.viz_enums import METRICS, DESC_METRICS, OLD_TO_NEW, TO_NORMALISED_METRICS


class VizMetrics:

    def plot(self, score_path: str, inverse_metrics: List = TO_NORMALISED_METRICS ):
        df = pd.read_csv(score_path, index_col=0)
        names = [x.replace("normalized_", "").split("_")[0] for x in list(df.index)]
        df.index = names
        metrics = [metric for metric in METRICS if metric in df.columns]
        df = df.loc[:,metrics]
        # Normalise the columns of the df by max min scaler
        inv_metrics = [metric for metric in inverse_metrics if metric in df.columns]
        df[inv_metrics] = (df[inv_metrics] - df[inv_metrics].min()) \
                                  / (df[inv_metrics].max() - df[inv_metrics].min())
        desc_metrics = [metric for metric in DESC_METRICS if metric in df.columns]
        df[desc_metrics] = 1 - df[desc_metrics]
        df = df.rename(OLD_TO_NEW)
        fig = px.imshow(df, color_continuous_scale=px.colors.sequential.Viridis)
        fig = self._clean_fig(fig)
        return fig

    def _clean_fig(self, fig):
        fig.update_annotations(font_size=20)
        params_axes = dict(
            showgrid=True,
            gridcolor="grey",
            linecolor="black",
            zeroline=False,
            linewidth=1,
            showline=True,
            mirror=True,
            gridwidth=1,
            griddash="dot",
            tickson="boundaries",
        )
        fig.update_yaxes(**params_axes)
        fig.update_xaxes(**params_axes)
        fig.update_layout(
            dict(plot_bgcolor="white"), margin=dict(l=10, r=5, b=10, t=20)
        )
        param_marker = dict(
            opacity=1, line=dict(width=0.5, color="DarkSlateGrey"), size=6
        )
        fig.update_traces(marker=param_marker, selector=dict(mode="markers"))
        fig.update_layout(
            font=dict(
                family="Computer Modern",
                size=20,
            )
        )
        fig.update_xaxes(tickangle=45)
        return fig