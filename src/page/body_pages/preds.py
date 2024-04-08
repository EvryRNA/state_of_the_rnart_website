from typing import Dict

from dash import Dash

from src.page.abstract_page import AbstractPage
from src.viz.viz_preds import VizPreds


class Preds(AbstractPage):
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
        self.challenge = "rna_puzzles"
        self.rna_name = "rp03"
        self.viz_preds = VizPreds(
            native_paths=native_paths,
            pred_paths=preds_paths,
            scores_dir=scores_dir,
            app=app,
        )

    def get_page(self):
        return self.viz_preds.get_plot(self.challenge, self.rna_name)
