from src.page.abstract_page import AbstractPage
from dash import html
import dash_bootstrap_components as dbc


class DatasetSelection(AbstractPage):
    def get_page(self):
        return html.Div(
            [
                html.Hr(style={"height": "15px"}),
                html.H2(
                    "Dataset selection",
                    style={"color": "black", "fontSize": "50px"},
                ),
                html.H3(
                    "Select the dataset to visualise the predicted 3D structures from benchmarked models",
                    style={"color": "black", "fontSize": "20px"},
                ),
                html.Div(
                    [
                        dbc.RadioItems(
                            id="button-dataset",
                            className="btn-group",
                            inputClassName="btn-check",
                            labelClassName="btn btn-outline-primary fs-4",
                            labelCheckedClassName="active",
                            options=[
                                {"label": "RNAsolo", "value": "rnasolo"},
                                {"label": "RNA-Puzzles", "value": "rna_puzzles"},
                                {"label": "CASP-RNA", "value": "casp"},
                            ],
                            value="rna_puzzles",
                            style={
                                "background-color": "#1f447a",
                            },
                        ),
                    ],
                    style={
                        "display": "flex",
                        "justify-content": "center",
                        "align-items": "center",
                        "width": "100%",
                        "margin": "0 auto",
                        "padding": "20px",
                        "text-align": "center",
                    },
                ),
            ]
        )
