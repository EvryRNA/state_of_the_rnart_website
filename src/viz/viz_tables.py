from typing import List
import os
import pandas as pd
from dash import dash_table
from src.enums.enums import (NAMES_CLEAN, REPLACE_METRICS_AND_SCORES, METRICS, ENERGIES)
from dash import Dash, dcc, html, Input, Output, callback

class VizTables:
    def __init__(self, csv_folder: str):
        self.csv_folder = csv_folder
        self.counter = 0
        self.current_value = None

    def clean_df(self, df):
        """
        Add Model name, clean the names, change the metrics names
        """
        df["Model name"] = df.index
        new_order = ["Model name"] + [x for x in df.columns if x != "Model name"]
        df = df[new_order]
        df["Model name"] = df["Model name"].apply(self.clean_name)
        df.rename(columns=REPLACE_METRICS_AND_SCORES, inplace=True)
        df = df[df["Model name"].notnull()]
        df = df.round(2)
        return df

    def clean_name(self, name):
        name = name.replace("normalized_", "")
        split_name = name.split("_")
        new_name = NAMES_CLEAN[split_name[0]]
        if len(split_name) <= 2:
            return new_name
        else:
            return new_name + f" (Prediction {split_name[-1].replace('.pdb', '')})"

    def _plot_csv(self, rna_challenge: str, scores: List, name: str):
        df = pd.read_csv(os.path.join(self.csv_folder, f"{rna_challenge}.csv"), index_col=0)
        df = self.clean_df(df)
        df = df[["Model name"] + scores]
        output = dash_table.DataTable(
                columns=[{'name': col, 'id': col} for col in df.columns],
                data=df.to_dict('records'),
                style_header={'backgroundColor': '#4782a9', 'color': 'white'},
                style_cell={
                    'backgroundColor': '#b5c9da',
                    'color': 'black',
                    'textAlign': 'center'
                },
                style_data={'border': '1px solid white'},
            )
        output = html.Div(
            children=[
                html.Div(output, id = f"data_table_{name}"),
            ],
            style={"margin": "0 auto", "width": "100%", }
        )
        return output


    def plot_csv_metrics(self, rna_challenge: str):
        return self._plot_csv(rna_challenge, METRICS, "Metrics")

    def plot_csv_energies(self, rna_challenge: str):
        return self._plot_csv(rna_challenge, ENERGIES, "Scoring functions")

    def update_table(self, value):
        if self.counter > 1 and value == "rp03":
            new_value = self.current_value
        else:
            self.current_value = value
            new_value = self.current_value
        self.counter+=1
        return self.plot_csv_metrics(new_value), self.plot_csv_energies(new_value)