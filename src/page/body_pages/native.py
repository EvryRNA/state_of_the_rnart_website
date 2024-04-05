from typing import Dict

from dash import Dash

from src.page.abstract_page import AbstractPage
from src.viz.viz_native import VizNative


class Native(AbstractPage):
    def __init__(
        self, native_paths: Dict, scores_dir: Dict, app: Dash, *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.challenge = "rna_puzzles"
        self.rna_name = "rp03"
        self.viz_native = VizNative(native_paths, scores_dir, app)

    def get_page(self):
        return self.viz_native.get_native_structure(self.challenge, self.rna_name)
