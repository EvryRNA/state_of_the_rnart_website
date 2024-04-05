from src.enums.colors import DARK_BLUE
from src.enums.links import TEXT_RNASOLO_CASE, TEXT_RNA_PUZZLES, TEXT_CASP_RNA
from src.page.abstract_page import AbstractPage
import dash_mantine_components as dmc
from dash import html

from src.page.utils.dash_utils import get_card


class Dataset(AbstractPage):
    def get_page(self):
        return dmc.Grid(
            children=[
                dmc.Col(html.Div(get_card(**info)), span=4)
                for info in [TEXT_RNASOLO_CASE, TEXT_RNA_PUZZLES, TEXT_CASP_RNA]
            ],
            justify="center",
            align="flex-start",
            gutter="xl",
            style={
                "backgroundColor": DARK_BLUE,
                "padding": "0px",
                "margin": "0 auto",
            },
        )
