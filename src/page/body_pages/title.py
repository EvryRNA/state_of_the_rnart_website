from src.enums.colors import DARK_BLUE
from src.enums.links import MORE_INFORMATION_TITLE
from src.enums.styles import NO_PADDING
from src.page.abstract_page import AbstractPage
from dash import html
import os

from src.page.utils.dash_utils import get_button


class Title(AbstractPage):
    def get_page(self):
        content = html.Div(
            children=[
                html.Img(
                    src=os.path.join(self.img_path, "logo.svg"),
                    style={"width": "50%", "padding-top": "-100px"},
                ),
                get_button(
                    text="More information",
                    href=MORE_INFORMATION_TITLE,
                    button_color=DARK_BLUE,
                ),
            ],
            style=NO_PADDING,
        )
        return content
