import os

from src.enums.colors import DARK_BLUE
from src.enums.styles import ANIMATION_STYLE
from src.page.abstract_page import AbstractPage
from dash import html


class Animation(AbstractPage):
    def get_page(self):
        return html.Div(
            children=[
                html.Div(
                    id="top-div",
                    style={
                        "background-color": "white",
                        "height": "50%",
                        "width": "auto",
                    },
                ),
                html.Img(
                    src=os.path.join(self.img_path, "video3d.gif"),
                    style=ANIMATION_STYLE,
                ),
                html.Div(
                    id="bottom-div",
                    style={
                        "background-color": DARK_BLUE,
                        "height": "50%",
                        "width": "100%",
                    },
                ),
            ],
            style={
                "position": "relative",
                "height": "600px",
                "box-sizing": "border-box",
            },
        )
