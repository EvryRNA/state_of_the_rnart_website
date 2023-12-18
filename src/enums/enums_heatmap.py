METRICS_ALL = [
    "RMSD",
    "P-VALUE",
    "INF-ALL",
    "INF-WC",
    "INF-NWC",
    "INF-STACK",
    "DI",
    "MCQ",
    "TM-SCORE",
    "GDT-TS",
    "BARNABA-eRMSD",
    "CLASH",
]

METRICS = [
    "RMSD",
    "INF-ALL",
    "DI",
    "INF-WC",
    "P-VALUE",
    "TM-SCORE",
    "GDT-TS",
    "εRMSD",
    "lDDT",
    "INF-STACK",
    "INF-NWC",
    "MCQ",
    "tm-score-ost",
    "TM-score",
    "QS-score",
]
SUB_METRICS = ["RMSD", "P-VALUE", "DI", "εRMSD", "TM-score", "GDT-TS", "INF-ALL", "lDDT"]
ALL_MODELS = [
    "mcsym",
    "ifoldrna",
    "vfold",
    "vfoldpipeline",
    "rnacomposer",
    "simrna",
    "3drna",
    "isrna",
    "rnajp",
    "rhofold",
    "trrosettarna",
]
# Higher is better
ASC_METRICS = ["INF-ALL", "TM-score", "GDT-TS", "lDDT"]
# Lower is better
DESC_METRICS = ["RMSD", "P-VALUE", "DI", "εRMSD"]
PAPER_METRICS = ["DI", "P-VALUE", "TM-score", "GDT-TS"]
PAPER_SUP_METRICS = ["RMSD", "εRMSD", "INF-ALL", "lDDT"]


RNA_NAMES = [
    "rp03",
    "rp04",
    "rp05",
    "rp06",
    "rp07",
    "rp08",
    "rp09",
    "rp11",
    "rp12",
    "rp13",
    "rp14b",
    "rp14f",
    "rp16",
    "rp17",
    "rp18",
    "rp21",
    "rp23",
    "rp24",
    "rp25",
    "rp29",
    "rp32",
    "rp34",
]
MODELS_TO_GROUP = {
    "MC-Sym": "Template-based",
    "iFoldRNA": "Ab initio",
    "Vfold3D": "Template-based",
    "Vfold-Pipeline": "Template-based",
    "RNAComposer": "Template-based",
    "3dRNA": "Template-based",
    "IsRNA1": "Ab initio",
    "RNAJP": "Ab initio",
    "RhoFold": "Deep learning",
    "trRosettaRNA": "Deep learning",
}
ORDER_MODELS = list(MODELS_TO_GROUP.keys())
MODELS = list(MODELS_TO_GROUP.keys())
COLORS = {"Template-based": "#e0aa74", "Ab initio": "#A6CF98", "Deep learning": "#4999f7"}
OLD_TO_NEW = {
    "BARNABA-eRMSD": "εRMSD",
    "rnacomposer": "RNAComposer",
    "isrna": "IsRNA1",
    "3drna": "3dRNA",
    "rhofold": "RhoFold",
    "ifoldrna": "iFoldRNA",
    "vfold": "Vfold3D",
    "eprna": "epRNA",
    "rp14_free": "rp14f",
    "rp14_bound": "rp14b",
    "lddt": "lDDT",
    "trrosettarna": "trRosettaRNA",
    "mcsym": "MC-Sym",
    "vfoldpipeline": "Vfold-Pipeline",
    "rnajp": "RNAJP",
}
