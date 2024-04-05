import os

from src.page.abstract_page import AbstractPage
import dash_mantine_components as dmc
from dash import html


class Header(AbstractPage):
    def get_page(self):
        return dmc.Header(
            height=150,
            children=[
                dmc.Group(
                    position="apart",
                    children=[
                        html.A(
                            html.Img(
                                src=os.path.join(self.img_path, "logo_nav.svg"),
                                style={"height": "150px", "width": "auto"},
                            ),
                            href="./index.html",
                        ),
                        html.A(
                            html.Img(
                                src=os.path.join(self.img_path, "github.png"),
                                style={"height": "100px", "width": "auto"},
                            ),
                            href="https://github.com/EvryRNA/state_of_the_rnart_viz",
                            target="_blank",
                        ),
                    ],
                )
            ],
        )
