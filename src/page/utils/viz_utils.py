from typing import Any

from dash_bio.utils import PdbParser, create_mol3d_style

import dash_bio

from src.enums.viz_enums import STYLE_3D


def get_color_scheme(
    data: Any,
    is_native: bool,
    native_color: str = "#ec8023",
    pred_color: str = "#275390",
):
    chains = list(set([atom.get("chain", 65) for atom in data.get("atoms", {})]))
    orders = [ord(id) for id in chains]
    max_order = max(orders)
    index_max = max_order + 1 if is_native else max_order
    if is_native:
        color_scheme = {
            chr(chain_id).upper(): native_color for chain_id in range(65, index_max)
        }
    else:
        color_scheme = {
            chr(chain_id).upper(): pred_color for chain_id in range(65, index_max)
        }
        color_scheme[chr(max_order).upper()] = native_color
    if "1" in chains and "A" in chains:
        color_scheme["1"] = native_color
        color_scheme["A"] = pred_color
    color_scheme["0"] = native_color
    return color_scheme


def get_viz_3d_data(
    in_path: str,
    width=350,
    height=350,
    is_native: bool = False,
    background_color: str = "#c4e4ff",
):
    parser = PdbParser(in_path)
    data = parser.mol3d_data()
    styles = create_mol3d_style(
        data["atoms"],
        visualization_type="cartoon",
        color_element="chain",
        color_scheme=get_color_scheme(data, is_native),
    )
    c_style = STYLE_3D.copy()
    c_style = {
        **c_style,
        **{"width": width, "height": height, "background-color": background_color},
    }
    if is_native:
        content = dash_bio.Molecule3dViewer(
            modelData=data,
            styles=styles,
            backgroundOpacity=0.2,
            backgroundColor=background_color,
            width=width,
            height=height,
            style=c_style,
            zoom={"factor": 1.2},
        )
    else:
        content = dash_bio.Molecule3dViewer(
            modelData=data,
            styles=styles,
            backgroundOpacity=0.2,
            width=width,
            height=height,
            style=c_style,
            zoom={"factor": 1.2},
        )
    return content
