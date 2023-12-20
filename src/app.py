from dash import Dash, dcc, html, Input, Output, callback, ctx
import dash
import dash_bootstrap_components as dbc
from src.viz.viz3d import Viz3D
from src.enums.enums import (STYLE_TITLE, TEXT_FIRST_CASE, TEXT_SECOND_CASE, BUTTON_STYLE)

from src.viz.viz_tables import VizTables
from src.viz.viz_heatmap import VizHeatmap

app = dash.Dash(external_stylesheets=[dbc.themes.MORPH], suppress_callback_exceptions=True)
server = app.server


class DashHelper:
    def __init__(self, app, native_path: str, rna_dir: str, scores_dir: str, casp_rna_native: str, casp_rna_dir: str):
        """
        :param native_path: path to native structures
        :param rna_dir: path to the aligned structures
        """
        self.app = app
        self.native_path = native_path
        self.rna_dir = rna_dir
        self.casp_rna_native = casp_rna_native
        self.casp_rna_dir = casp_rna_dir
        self.challenge = "rna_puzzles"
        self.viz3d = Viz3D(native_path, rna_dir, "rna_puzzles", self.app)
        self.viz_casp = Viz3D(casp_rna_native, casp_rna_dir, "casp", self.app)
        self.viz = self.get_viz()
        self.viz_table = VizTables(scores_dir)
        self.viz_heatmap = VizHeatmap(scores_dir)
        self.app.callback(dash.dependencies.Output('data_table_Metrics', 'children'),
                          dash.dependencies.Output('data_table_Scoring functions', 'children'),
                          dash.dependencies.Input('dropdown_challenges', 'value'),
                          suppress_callback_exceptions=True
                          )(self.viz_table.update_table)
        self.app.callback(dash.dependencies.Output('3d_structures_shown', 'children', allow_duplicate=True),
                          dash.dependencies.Output("title_challenge", "children"),
                          dash.dependencies.Input('button-rna_puzzles', 'n_clicks',),
                          dash.dependencies.Input('button-casp', 'n_clicks'),
                          prevent_initial_call=True, suppress_callback_exceptions=True
                          )(self.update_benchmark)
    def get_viz(self):
        if self.challenge == "rna_puzzles":
            viz = self.viz3d
        elif self.challenge == "casp":
            viz = self.viz_casp
        self.viz = viz
        return viz

    def get_first_page(self):
        content = html.Div(
            children = [
                html.Hr(style={"height": "15px"}),
                html.H1("RNA-Puzzles single-stranded benchmark", style=STYLE_TITLE),
                html.H3("RNA 3D structures visualisations", style={"color": "black"} ),
                html.Hr(style={"height": "15px"}),
            ],
        )
        return content


    def _get_separation(self, color = "white"):
        return html.Hr(style={"height": "5px"}) , html.Hr(style={"width": "100px", "background-color": color, "height": "2px",
                       "margin": "0 auto", }), html.Hr(style={"height": "2px"})


    def get_text_explanation(self, all_info, bg_color = "#4682A9", color = "white", button_color = "black"):
        content = html.Div(
            children = [
                html.Div(style= {"background-image": all_info.get("IMAGE"), "width": "50px", "height": "50px", "background-size": "cover", "background-position": "center", "margin": "0 auto"}),
                html.H2(all_info.get("H2"), style={"color": color, "fontSize": "30px", } ),
                *self._get_separation(color=color),
                html.H3(all_info.get("H3"),
                        style={"color": color, "width": "70%", "text-align": "center", "margin": "0 auto", "fontSize": "15",
                               "height": "120px"} ),
                *self._get_separation(color=color),
                html.Button(
                    html.A("More information", href=all_info.get("LINK"), style = {"color": "white" if color != "white" else "black", "text-decoration" : "none"}
                           ), style={"color": "inherit", "text-decoration" : "none", "background-color": button_color,
                                     "border": "black", "border-radius": "5px", "padding": "10px",
                                     "margin": "0 auto", "display": "block", "fontSize": "20px"},
                )
            ],
            style={"background-color": bg_color, "width": "100%", "margin": "0 auto", "padding": "20px", "text-align": "center",
                   "height": "450px"}
        )
        return content


    def get_table_metrics(self):
        return self.viz_table.plot_csv_metrics("rp03")


    def get_timeline(self):
        return html.Div(
            style={
                "background-image": "url('assets/img/timeline_all_papers.drawio.png')",
                "background-size": "100% 100%",
                # "background-position": "center",
                "background-repeat": "no-repeat",
                "width": "100%",
                "height": "1000px",
                "margin": "0 auto"  # Centers the image horizontally
            }
        )


    def get_first_cases(self):
        return dbc.Row([
            dbc.Col(self.get_text_explanation(TEXT_FIRST_CASE, button_color="#cedbe6"), width=6),
            dbc.Col(self.get_text_explanation(TEXT_SECOND_CASE, "#cedbe6", color="black",
                                          button_color="#4682A9"), width=6)
            ])


    def get_native_plot_dropdown(self):
        return html.Div(
            children = [
                html.Br(),
                self.get_button_choose_benchmark(),
                html.Div(
                    children=[html.Br(style={"height": "10px"}),
                              *self.viz.get_native_plot(),
                              html.Br()
                              ],
                ),
            ],
            style={"background-color": "#b5c9da", "width": "80%",
                   "text-align": "center", "justify-content": "center",
                   "margin": "0 auto", "border-radius": "5px", "padding": "20px"}
        )


    def get_layout_native(self):
        self.viz = self.get_viz()
        return html.Div(children = [
                               html.Br(),
                    self.get_native_plot_dropdown(),
                            html.Br(),
            html.Div(self.viz.get_all_plots_3d(), style={"width": "100%", "text-align": "center", "justify-content": "center", "margin": "0 auto"})],
           id = "3d_structures_shown",

        )

    def get_layout_native_casp(self):
        return [html.Div(
            children = [html.Br(style={"height": "10px"}),
                        *self.viz_casp.get_native_plot(),
                        html.Br()
                        ],
            style = {"background-color": "#b5c9da", "width": "100%",
                     "text-align": "center", "justify-content": "center",
                     "margin": "0 auto"}),
            html.Br(),
            html.Div(self.viz_casp.get_all_plots_3d(), style={"width": "100%", "text-align": "center", "justify-content": "center", "margin": "0 auto"})]

    def get_layout_tables(self):
        return [html.H2("Metrics", style={"color": "black", "fontSize": "40px"}),
            html.Div(self.viz_table.plot_csv_metrics("rp03"),
                 style={"width": "100%", "text-align": "center", "justify-content": "center",
                        "margin": "0 auto"}),
                html.H2("Scoring functions", style={"color": "black", "fontSize": "40px"}),
        html.Div(self.viz_table.plot_csv_energies("rp03"),
                 style={"width": "100%", "text-align": "center", "justify-content": "center",
                        "margin": "0 auto"})]

    def get_heatmap(self):
        fig = self.viz_heatmap.plot_heatmaps()
        return html.Div(dcc.Graph(figure = fig), style={"width": "100%", "text-align": "center", "justify-content": "center"},)

    def get_boxplot(self):
        fig = self.viz_heatmap.plot_box_plot()
        return html.Div(dcc.Graph(figure = fig), style={"width": "100%", "text-align": "center", "justify-content": "center"},)

    def get_button_choose_benchmark(self):
        return html.Div([
            html.H2("Choose a benchmark:", style={"color": "black", "fontSize": "35px"}),
            html.Div([
                html.Button("RNA-Puzzles", id="button-rna_puzzles", n_clicks=0,
                            style={**BUTTON_STYLE, **{"color": "black"}}),
                html.Button("CASP-RNA", id="button-casp", n_clicks=0, style={**BUTTON_STYLE, **{"color": "white", "background-color": "#4682A9"}}),
            ],
                style = {"display": "flex", "justify-content": "center", "align-items": "center", "width": "30%", "margin": "0 auto", "padding": "20px", "text-align": "center",}
            ),
            ])

    def update_benchmark(self, btn1, btn2):
        if "button-rna_puzzles" == ctx.triggered_id:
            self.challenge = "rna_puzzles"
            title = "RNA-Puzzles"
        elif "button-casp" == ctx.triggered_id:
            self.challenge = "casp"
            title = "CASP-RNA"
        return self.get_layout_native(), html.H2(f"{title} challenge", style={"color": "black", "fontSize": "30px"}, id="title_challenge"),

    def run(self):
        page_structure = [
            dbc.Row(self.get_first_page()),
            html.Br(),
            dbc.Row(self.get_first_cases()),
            html.Br(),
            self.get_layout_native(),
            html.Br(),
            *self.get_layout_tables(),
            dbc.Row([
                dbc.Col([ self.get_timeline()
                ], width=4),
                dbc.Col([self.get_heatmap()], width = 8)
            ]),
            self.get_boxplot(),
            ]


        self.app.layout = dbc.Container(
            id="root",
            children=page_structure,
            fluid=True,
            style={
                "background-color": "white",
            },
        )
        return self.app


if __name__ == "__main__":
    params = {"app": app,
              "native_path": "data/rna_puzzles/native",
              "rna_dir": "data/rna_puzzles/aligned",
              "scores_dir": "data/rna_puzzles/scores",
              "casp_rna_native": "data/casp_rna/native",
              "casp_rna_dir": "data/casp_rna/aligned",
              }
    dash_helper = DashHelper(**params)
    app = dash_helper.run()
    server = app.server
    app.run_server(debug=True, port=8050)