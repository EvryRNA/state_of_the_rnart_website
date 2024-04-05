import os
from typing import Dict
from dash import dcc, html, ctx, no_update
import dash_bootstrap_components as dbc
import dash
import dash_molstar
from dash_molstar.utils import molstar_helper

from src.enums.colors import GRAY
from src.enums.styles import STYLE_H, BUTTON_STYLE
from src.enums.viz_enums import RNA_CHALLENGES_LENGTH, CASP_RNA_CHALLENGES_LENGTH
from src.viz.viz_metrics import VizMetrics


class VizNative:
    def __init__(self, native_paths: Dict, scores_dir: Dict, app):
        self.native_paths = native_paths
        self.scores_dir = scores_dir
        self.all_challenges = self.get_all_challenges(native_paths)
        self.benchmark = None
        app.callback(
            dash.dependencies.Output("native_structure", "data"),
            dash.dependencies.Output("title_challenge", "children"),
            dash.dependencies.Output("dropdown_challenges", "options"),
            dash.dependencies.Output("dropdown_challenges", "value"),
            dash.dependencies.Output("metrics", "children"),
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
            dropdown = self.all_challenges.get(benchmark)
            value = rna_name
        else:
            dropdown, value = no_update, no_update
        content, title = self.get_updatable_elements(benchmark, rna_name)
        native_path = os.path.join(self.native_paths.get(benchmark), f"{rna_name}.pdb")
        content = molstar_helper.parse_molecule(native_path)
        table = self.get_plot_table(benchmark, rna_name)
        return content, title, dropdown, value, table

    def get_all_challenges(self, native_paths: Dict):
        all_challenges = {}
        for benchmark, path in native_paths.items():
            if benchmark == "rna_puzzles":
                c_challenges = list(RNA_CHALLENGES_LENGTH.keys())
            elif benchmark == "casp":
                c_challenges = list(CASP_RNA_CHALLENGES_LENGTH.keys())
            else:
                c_challenges = [
                    rna_name.replace(".pdb", "") for rna_name in os.listdir(path)
                ]
            all_challenges[benchmark] = c_challenges
        return all_challenges

    def show_native(self, benchmark: str, rna_name: str):
        return [
            html.Div(
                children=[self.get_native_structure(benchmark, rna_name)],
            ),
        ]

    def get_updatable_elements(
        self, benchmark: str, rna_name: str, is_first: bool = False
    ):
        native_path = os.path.join(self.native_paths.get(benchmark), f"{rna_name}.pdb")
        content = self.get_viz_molstar(native_path, is_first)
        content = html.Div(content)
        title = html.H2(f"Challenge {rna_name}", style=STYLE_H, id="title_challenge")
        return content, title

    def get_viz_molstar(self, native_path: str, is_first: bool = False):
        if is_first:
            data = molstar_helper.parse_molecule(native_path)
            content = dash_molstar.MolstarViewer(
                data=data,
                id="native_structure",
                style={
                    "width": "500px",
                    "height": "500px",
                    "backgroundColor": "#d9e3f1",
                    "color": "red",
                    "margin": "0 auto",
                    "text-align": "center",
                },
            )
        else:
            content = dash_molstar.MolstarViewer(
                id="native_structure",
                style={
                    "width": "500px",
                    "height": "500px",
                    "backgroundColor": "#d9e3f1",
                    "color": "red",
                    "margin": "0 auto",
                    "text-align": "center",
                },
            )
        return content

    def _get_dropdown(self, benchmark: str):
        dropdown = dcc.Dropdown(
            options=self.all_challenges.get(benchmark),
            value=self.all_challenges.get(benchmark)[0],
            clearable=False,
            placeholder="Select a RNA",
            persistence=False,
            id="dropdown_challenges",
            style={
                "background-color": GRAY,
                "border-radius": "15px",
            },
        )
        return dropdown

    def get_dropdown(self, benchmark: str):
        return html.Div(
            self._get_dropdown(benchmark),
            style={
                "width": "15%",
                "margin": "0 auto",
                "height": "50px",
                "border-radius": "10px",
                "fontSize": "30px",
                "color": "black",
            },
        )

    def get_plot_table(self, benchmark: str, rna_name: str):
        fig = VizMetrics().plot(
            os.path.join(self.scores_dir.get(benchmark), f"{rna_name}.csv")
        )
        output = html.Div(
            dcc.Graph(figure=fig), style={"background-color": "white"}, id="metrics"
        )
        return output

    def get_native_structure(self, benchmark: str, rna_name: str):
        content, title = self.get_updatable_elements(benchmark, rna_name, is_first=True)
        table = self.get_plot_table(benchmark, rna_name)
        dropdown = self.get_dropdown(benchmark)
        children = [
            html.H2(
                "RNA challenge selection", style={"fontSize": "40px", "color": "black"}
            ),
            html.Hr(style={"height": "10px"}),
            dropdown,
            html.Hr(style={"height": "20px"}),
            dbc.Row(
                justify="center",
                children=[
                    dbc.Col(
                        [
                            title,
                            html.H3(
                                "Native structure",
                                style={
                                    **STYLE_H,
                                    "fontSize": "20px",
                                    "padding": "0 20px",
                                },
                            ),
                            content,
                            html.Button(
                                "Download",
                                n_clicks=0,
                                style={
                                    **BUTTON_STYLE,
                                    **{
                                        "color": "white",
                                        "background-color": "#1f447a",
                                    },
                                },
                            ),
                        ],
                        width=6,
                    ),
                    dbc.Col(
                        [
                            html.H2(
                                "Normalised metrics",
                                style={
                                    **STYLE_H,
                                    "fontSize": "30px",
                                    "padding": "0 20px",
                                },
                            ),
                            html.H2(
                                "Each metric is normalised by the maximum value of the metric. The descending "
                                "metrics are inversed to set all better metrics to 1.0. Descending metrics are: "
                                "RMSD, P-VALUE, DI, εRMSD, and MCQ.\n White values mean missing values.",
                                style={
                                    **STYLE_H,
                                    "fontSize": "15px",
                                    "padding": "0 20px",
                                    "width": "70%",
                                    "margin": "0 auto",
                                },
                            ),
                            table,
                        ],
                        width=5,
                    ),
                ],
            ),
        ]
        div = html.Div(
            children=children,
            style={
                "width": "77%",
                "background-color": "white",
                "margin": "0 auto",
            },
        )
        return div
