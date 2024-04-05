import os
from typing import Dict

import dash
import flask
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

from src.enums.styles import NO_PADDING
from src.page.footer import Footer
from src.page.header import Header
from src.page.body import Body


class DashHelper:
    def __init__(
        self,
        app,
        native_paths: Dict,
        scores_dir: Dict,
        preds_paths: Dict,
        img_path: str,
    ):
        """
        :param app: Dash app
        :param native_path: path to the native structures
        :param scores_dir: path to the scores
        :param preds_path: path to the predicted structures
        :param img_path: path where are stored the different images
        """
        self.app = app
        self.native_paths = native_paths
        self.scores_dir = scores_dir
        self.preds_paths = preds_paths
        self.img_path = img_path

    def run(self):
        content = [
            Header(self.img_path).get_page(),
            Body(
                img_path=self.img_path,
                native_paths=self.native_paths,
                scores_dir=self.scores_dir,
                preds_paths=self.preds_paths,
                app=self.app,
            ).get_page(),
            Footer(self.img_path).get_page(),
        ]
        self.app.layout = dmc.Container(content, fluid=True, style=NO_PADDING)
        return self.app


server = flask.Flask(__name__)

app = dash.Dash(
    external_stylesheets=[dbc.themes.MORPH],
    suppress_callback_exceptions=True,
    server=server,
)
DATA_PREFIX = "data"

params = {
    "app": app,
    "native_paths": {
        name: os.path.join(DATA_PREFIX, name, "native")
        for name in ["rna_puzzles", "casp", "rnasolo"]
    },
    "scores_dir": {
        name: os.path.join(DATA_PREFIX, name, "scores")
        for name in ["rna_puzzles", "casp", "rnasolo"]
    },
    "preds_paths": {
        name: os.path.join(DATA_PREFIX, name, "aligned")
        for name in ["rna_puzzles", "casp", "rnasolo"]
    },
    "img_path": os.path.join("assets", "img"),
}

dash_helper = DashHelper(**params)
app = dash_helper.run()
if __name__ == "__main__":
    app.run_server(debug=True)
