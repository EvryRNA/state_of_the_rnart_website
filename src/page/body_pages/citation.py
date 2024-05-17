from src.page.abstract_page import AbstractPage
import dash_mantine_components as dmc
from dash import html


class Citation(AbstractPage):
    def get_page(self):
        return html.Div(
            [
                html.H2(
                    "Citation",
                    style={
                        "text-align": "center",
                        "color": "black",
                        "font-size": "45px",
                    },
                ),
                dmc.Blockquote(
                    children=[
                        html.P(
                            "State-of-the-RNArt: benchmarking current methods for RNA 3D structure prediction."
                        ),
                        html.P(
                            "Clément Bernard, Guillaume Postic, Sahar Ghannay, Fariza Tahi"
                        ),
                    ],
                    cite="NAR Genomics and Bioinformatics, Volume 6, Issue 2, June 2024, lqae048, https://doi.org/10.1093/nargab/lqae048",
                    style={
                        "width": "50%",
                        "margin": "0 auto",
                        "font-size": "25px",
                        "text-align": "center",
                        "color": "black",
                        "background-color": "#d9e3f1",
                        "border-radius": "15px",
                        "font": "Abel",
                    },
                ),
            ]
        )
