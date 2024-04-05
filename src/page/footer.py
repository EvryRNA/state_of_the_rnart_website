import os

from src.enums.colors import HEADER_COLOR
from src.enums.links import CONTACT_US_FOOTER
from src.enums.styles import FOOTER_STYLE
from src.page.abstract_page import AbstractPage
from dash import html


class Footer(AbstractPage):
    def get_page(self):
        return html.Div(
            [
                html.Div(
                    "Sponsored by",
                    style={
                        **FOOTER_STYLE,
                        **{"color": "black", "font-size": "30px", "width": "30%"},
                    },
                ),
                html.Img(
                    src=os.path.join(self.img_path, "sponsor.png"),
                    style={**FOOTER_STYLE, **{"width": "70%", "height": "100%"}},
                ),
                html.H3(
                    "For questions about rights and access usage, contact Ms Tahi",
                    style={
                        "color": "black",
                        "text-align": "center",
                        "margin": "0 auto",
                        "font-size": "20px",
                    },
                ),
                CONTACT_US_FOOTER,
            ],
            style={
                "text-align": "center",
                "background-color": "white",
                "border": f"1px solid {HEADER_COLOR}",
                "background-color": HEADER_COLOR,
            },
        )
