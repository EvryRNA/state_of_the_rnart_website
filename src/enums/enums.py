NAMES_CLEAN = {
    "alphafold3": "AlphaFold3",
    "rnajp": "RNAJP",
    "vfoldpipeline": "VfoldPipeline",
    "trrosettarna": "trRosettaRNA",
    "rhofold": "RhoFold",
    "isrna": "IsRNA1",
    "simrna": None,
    "3drna": "3dRNA",
    "rnacomposer": "RNAComposer",
    "vfold": "Vfold3D",
    "mcsym": "MCSym",
    "ifoldrna": "iFoldRNA",
    "eprna": None,
}
STYLE_H = {
    "fontSize": "35px",
    "fontWeight": "bold",
    "border-radius": "1px",
    "color": "black",
}
STYLE_SCORE = {
    "fontSize": "25px",
    "color": "#0766AD",
    "border-radius": "1px",
}

STYLE_TITLE = {
    "fontSize": "70px",
    "fontWeight": "bold",
    "textAlign": "center",
    "color": "black",
}

TEXT_FIRST_CASE = {
    "H2": "RNA-Puzzles",
    "H3": "CASP-like competition that has collected RNA molecules since 2011. It is used as a test set to assess the robustness of predictive models.",
    "LINK": "https://www.rnapuzzles.org/",
    "IMAGE": "url('assets/img/rna_test.png')",
}
TEXT_SECOND_CASE = {
    "H2": "CASP-RNA",
    "H3": "CASP-RNA is a collaboration between CASP organizers and RNA-Puzzles. It is composed of 12 RNA molecules for the CASP15 competition.",
    "LINK": "https://predictioncenter.org/casp15/",
    "IMAGE": "url('assets/img/performance.png')",
}

BUTTON_STYLE = {
    "color": "inherit",
    "text-decoration": "none",
    "border": "black",
    "border-radius": "5px",
    "padding": "10px",
    "margin": "0 auto",
    "display": "block",
    "fontSize": "20px",
}

REPLACE_METRICS_AND_SCORES = {
    "INF-ALL": "INF",
    "RASP-ENERGY": "RASP",
    "BARNABA-eRMSD": "εRMSD",
    "BARNABA-eSCORE": "εSCORE",
    "DFIRE": "DFIRE-RNA",
}

METRICS = [
    "RMSD",
    "P-VALUE",
    "INF",
    "INF-WC",
    "INF-NWC",
    "DI",
    "MCQ",
    "GDT-TS",
    "CAD",
    "εRMSD",
    "lDDT",
    "TM-score",
]
ENERGIES = ["RASP", "DFIRE-RNA", "εSCORE", "rsRNASP"]
