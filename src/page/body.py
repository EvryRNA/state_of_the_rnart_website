from typing import Dict

from src.enums.styles import NO_PADDING
from src.page.abstract_page import AbstractPage
import dash_mantine_components as dmc
from dash import html, Dash

from src.page.body_pages.animation import Animation
from src.page.body_pages.citation import Citation
from src.page.body_pages.dataset import Dataset
from src.page.body_pages.models import Models
from src.page.body_pages.native import Native
from src.page.body_pages.preds import Preds
from src.page.body_pages.title import Title
from src.page.body_pages.dataset_selection import DatasetSelection

STYLE_DIV = {**NO_PADDING, **{"width": "100%", "height": "100%"}}


class Body(AbstractPage):
    def __init__(
        self,
        native_paths: Dict,
        scores_dir: Dict,
        preds_paths: Dict,
        app: Dash,
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.all_elements = [
            Title(self.img_path),
            Animation(self.img_path),
            Dataset(self.img_path),
            DatasetSelection(self.img_path),
            Native(
                img_path=self.img_path,
                native_paths=native_paths,
                scores_dir=scores_dir,
                app=app,
            ),
            Preds(
                img_path=self.img_path,
                native_paths=native_paths,
                scores_dir=scores_dir,
                preds_paths=preds_paths,
                app=app,
            ),
            Models(self.img_path),
            Citation(self.img_path),
        ]

    def get_page(self):
        return html.Div(
            [
                dmc.Grid(
                    [
                        dmc.Col(html.Div(element.get_page()), span=12, style=STYLE_DIV)
                        for element in self.all_elements
                    ],
                    style=NO_PADDING,
                )
            ]
        )
