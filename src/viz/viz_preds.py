from typing import List
import os
from typing import Dict
from dash import html, ctx
import dash_bootstrap_components as dbc
import dash

import pandas as pd
import numpy as np

from src.enums.styles import STYLE_SCORE, STYLE_H, BUTTON_STYLE
from src.enums.viz_enums import NAMES_CLEAN, OLD_TO_NEW, METRICS
from src.page.utils.viz_utils import get_viz_3d_data


class VizPreds:
    def __init__(self, native_paths: Dict, pred_paths: Dict, scores_dir: Dict, app):
        self.native_paths = native_paths
        self.pred_paths = pred_paths
        self.all_challenges = self.get_all_challenges(pred_paths)
        self.scores_dir = scores_dir
        self.names_to_path = self.get_names_to_path()
        self.all_methods = [x for x in list(NAMES_CLEAN.keys()) if x not in ["eprna"]]
        self.all_methods_index = {
            method: i for i, method in enumerate(self.all_methods)
        }
        app.callback(
            dash.dependencies.Output("3d_structures_shown", "children"),
            [
                dash.dependencies.Input("dropdown_challenges", "value"),
                dash.dependencies.Input("button-dataset", "value"),
            ],
            allow_duplicate=True,
            prevent_initial_call=True,
            suppress_callback_exceptions=True,
        )(self.update_dropdown)

    def update_dropdown(self, rna_name, benchmark):
        triggered_id = ctx.triggered_id
        if triggered_id == "button-dataset":
            rna_name = self.all_challenges.get(benchmark)[0]
        return self.get_plot(benchmark, rna_name)

    def get_names_to_path(self):
        names_to_path = {}
        for benchmark, challenges in self.all_challenges.items():
            c_paths = {}
            for challenge in challenges:
                c_paths[challenge] = {
                    method: os.path.join(self.pred_paths[benchmark], challenge, method)
                    for method in os.listdir(
                        os.path.join(self.pred_paths[benchmark], challenge)
                    )
                }
            names_to_path[benchmark] = c_paths
        return names_to_path

    def get_all_challenges(self, native_paths: Dict):
        all_challenges = {}
        for benchmark, path in native_paths.items():
            all_challenges[benchmark] = [
                rna_name.replace(".pdb", "") for rna_name in os.listdir(path)
            ]
        return all_challenges

    def get_plot(self, benchmark: str, rna_name: str):
        plot_3d = self.get_all_plots_3d(benchmark, rna_name)
        return html.Div(
            plot_3d,
            style={
                "width": "100%",
                "text-align": "center",
                "justify-content": "center",
                "margin": "0 auto",
            },
            id="3d_structures_shown",
        )

    def get_all_plots_3d(self, benchmark: str, rna_name: str):
        all_models = self.get_all_models(benchmark, rna_name)
        row = html.Div(
            [
                dbc.Row(html.Hr(style={"height": "15px"})),
                dbc.Row(
                    [
                        dbc.Col(content, style={"margin-bottom": "20px"})
                        for content in all_models
                    ]
                ),
            ],
            style={"width": "70%", "margin": "0 auto", "justify-content": "center"},
        )
        return row

    def get_all_models(self, benchmark: str, rna_challenge: str):
        """
        Return the different models for this challenge
        """
        scores, new_models = self.get_scores(benchmark, rna_challenge)
        content = [
            self.get_viz_3d(method_name, rna_challenge, benchmark, scores)
            for method_name in new_models
        ]
        return content

    def get_scores(self, benchmark: str, rna_challenge: str):
        scores = pd.read_csv(
            os.path.join(self.scores_dir.get(benchmark), f"{rna_challenge}.csv"),
            index_col=0,
        )
        new_models = [method for method in self.all_methods]
        for name in scores.index:
            method = name.replace("normalized_", "").split("_")[0]
            if method in self.all_methods_index:
                new_models[self.all_methods_index[method]] = name.replace(
                    "normalized_", ""
                )
        return scores, new_models

    def get_name_and_decoys(self, in_paths: List):
        """
        Return the name and the decoys as values of dictionary
        """
        output = {}
        for in_path in in_paths:
            if "eprna" in in_path:
                continue
            name_split = in_path.split("_")
            method = name_split[0]
            if len(name_split) == 2:
                suffix = name_split[1]
                output[method] = output.get(method, []) + [f"Prediction {suffix}"]
                if method in output[method]:
                    output[method].remove(method)
            else:
                output[method] = [method]
        return output

    def get_viz_3d(
        self, method_name: str, rna_challenge: str, benchmark: str, scores: pd.DataFrame
    ):
        if method_name.endswith(".pdb"):
            in_path = self.names_to_path[benchmark][rna_challenge][method_name]
            scores = scores.rename(OLD_TO_NEW, axis=1)
            text_scores = self.get_name_scores(in_path, scores)
            name = NAMES_CLEAN[method_name.split("_")[0]]
        else:
            in_path = os.path.join("data", "null_structure.pdb")
            text_scores = "No prediction"
            name = NAMES_CLEAN[method_name]
        output = self.get_data_styles(in_path, name, text_scores)
        return output

    def get_name_scores(self, in_path: str, scores_df: pd.DataFrame):
        """
        Finds the name from the scoring dataframe
        """
        basename = os.path.basename(in_path)
        original_name = "normalized_" + basename
        scores = scores_df.loc[original_name]
        metrics = [metric for metric in METRICS if metric in scores_df.columns]
        new_scores = scores.loc[metrics].to_dict()
        return new_scores

    def get_data_styles(self, in_path: str, method_name: str, scores: Dict):
        content = get_viz_3d_data(in_path, is_native=False)
        try:
            scores = [
                f"{key}:{value:.2f}"
                for key, value in scores.items()
                if not np.isnan(value)
            ]
            scores = " | ".join(scores)
        except AttributeError:
            scores = "No prediction"
        metrics = html.H3(
            scores,
            style={
                **STYLE_SCORE,
                **{"fontSize": "15px", "width": "70%", "margin": "0 auto"},
            },
        )
        children = [
            html.H3(method_name, style={**STYLE_H, "margin": "0 auto", "width": "70%"}),
            metrics,
        ]
        children.append(html.Div(content, id=in_path.replace(".pdb", "")))
        button = html.Button(
            "Download",
            n_clicks=0,
            style={
                **BUTTON_STYLE,
                **{
                    "color": "white",
                    "background-color": "#1f447a",
                    "margin-bottom": "50px",
                },
            },
        )
        children.append(button)
        div = html.Div(children=children, style={"margin": "0 auto"})
        return div
