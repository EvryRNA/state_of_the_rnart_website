from dash import html

from src.enums.colors import PURPLE, DARK_BLUE, BLUE

MORE_INFORMATION_TITLE = "https://www.biorxiv.org/content/10.1101/2023.12.22.573067v2"
CONTACT_US_FOOTER = html.A("fariza.tahi@univ-evry.fr", href="mailto:fariza.tahi@univ-evry.fr")
TEXT_RNASOLO_CASE = {
    "title": "RNAsolo",
    "text": "Non redundant dataset of 29 RNAs obtained from RNAsolo and Rfam databases. It is used as a distinct dataset to compare performances of models.",
    "link": "https://rnasolo.cs.put.poznan.pl/",
    "img_path": "assets/img/rnasolo.png",
    "nb_rna": "29 RNA",
    "color": DARK_BLUE
}
TEXT_RNA_PUZZLES = {
    "title": "RNA-Puzzles",
    "text": "CASP-like competition that has collected RNA molecules since 2011. It is used as a test set to assess the robustness of predictive models.",
    "link": "https://www.rnapuzzles.org/",
    "img_path": "assets/img/rna_test.png",
    "color": PURPLE,
    "nb_rna": "22/40 RNA",
}
TEXT_CASP_RNA = {
    "title": "CASP-RNA",
    "text": "CASP-RNA is a collaboration between CASP organizers and RNA-Puzzles. It is composed of 12 RNA molecules for the CASP15 competition.",
    "link": "https://predictioncenter.org/casp15/",
    "img_path": "assets/img/performance.png",
    "color": BLUE,
    "nb_rna": "8/12 RNA",
}
TIMELINE_TEXT = {
    "MC-Sym": {
        "title": "MC-Sym",
        "text": "MC-Sym uses secondary structure elements (SSEs), with nucleotide cycle modulus"+
                "as blocks. It relies on a representation of nucleotide relationships"+
                "named nucleotide cyclic motif (NCM), incorporating more context-dependent information.",
        "year": "2008",
        "input": "Raw sequence, Secondary sequence",
        "method": "Ab initio",
        "paper": "https://www.nature.com/articles/nature06684",
        "code": "https://www.major.iric.ca/MC-Pipeline/",
        "web_server": "https://www.major.iric.ca/MC-Sym/",
    },
    "Vfold3D": {
        "title": "Vfold3D",
        "text": "Vfold3D constructs 3D structures from fragment databases. It uses the lowest "
                "free energy secondary structures converted to known fragments.",
        "year": "2011",
        "input": "Raw sequence, Secondary sequence",
        "method": "Template-based",
        "paper": "https://pubs.acs.org/doi/10.1021/jp112059y",
        "code": "http://rna.physics.missouri.edu/vfold_software_download/vfold3D_download.html",
        "web_server": "http://rna.physics.missouri.edu/vfold3D/"
    },
    "RNAComposer": {
        "title": "RNAComposer",
        "text": "RNAComposer uses a database with fragment mapping 2D elements to 3D motifs "
                "before using refinement. It uses SSEs as blocks for the fragment reconstruction.",
        "year": "2012",
        "input": "Raw sequence, Secondary sequence",
        "method": "Template-based",
        "paper": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3413140/",
        "code": "",
        "web_server": "https://rnacomposer.cs.put.poznan.pl/"
    },
    "3dRNA": {
        "title": "3dRNA",
        "text": "3dRNA uses a fragment assembly approach guided by a scoring function, "
                "3dRNAScore, where the SSEs considered are improved by more base pairs from connected stems.",
        "year": "2012",
        "input": "Raw sequence, Secondary sequence",
        "method": "Template-based",
        "paper": "https://pubmed.ncbi.nlm.nih.gov/23071898/",
        "code": "",
        "web_server": "http://biophy.hust.edu.cn/new/3dRNA"
    },
    "SimRNA": {
        "title": "SimRNA",
        "text": "SimRNA uses Monte Carlo steps with a five-bead nucleotide approach "
                "guided by an energy that considers local and non-local terms",
        "year": "2016",
        "input": "Raw sequence, Secondary sequence",
        "method": "Ab initio",
        "paper": "https://pubmed.ncbi.nlm.nih.gov/26687716/",
        "code": "https://genesilico.pl/software/stand-alone/simrna",
        "web_server": "https://genesilico.pl/SimRNAweb"
    },
    "IsRNA1": {
        "title": "IsRNA1",
        "text": "IsRNA1 is a coarse-grained method with five-bead per nucleotide to "
                "predict noncanonical base pairs",
        "year": "2021",
        "input": "Raw sequence, Secondary sequence",
        "method": "Ab initio",
        "paper": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8064582/",
        "code": "http://rna.physics.missouri.edu/vfold_software_download/vfold3D_download.html",
        "web_server": "http://rna.physics.missouri.edu/IsRNA/index.html"
    },
    "RhoFold": {
        "title": "RhoFold",
        "text": "RhoFold is a preprint work with an end-to-end differentiable approach for "
                "predicting RNA 3D structures. The model’s input is the MSA, "
                "and features are extracted with a pre-trained model RNA-FM.",
        "year": "2022",
        "input": "MSA",
        "method": "Deep Learning",
        "paper": "https://arxiv.org/abs/2207.01586",
        "code": "https://github.com/RFOLD/RhoFold",
        "web_server": "https://proj.cse.cuhk.edu.hk/aihlab/rhofold/"
    },
    "trRosettaRNA": {
        "title": "trRosettaRNA",
        "text": "trRosettaRNA uses MSA and secondary structure (predicted by SPOT-RNA) as inputs. "
                "The network architecture is inspired by AlphaFold2 Evoformer block and thus uses transformer networks.",
        "year": "2022",
        "input": "Raw sequence, MSA",
        "method": "Deep Learning",
        "paper": "https://www.nature.com/articles/s41467-023-42528-4",
        "code": "https://yanglab.qd.sdu.edu.cn/trRosettaRNA/download/",
        "web_server": "https://yanglab.qd.sdu.edu.cn/trRosettaRNA/"
    },
    "Vfold-Pipeline": {
        "title": "Vfold-Pipeline",
        "text": "Vfold-Pipeline uses Vfold2D to predict the secondary structure and then "
                "uses either Vfold3D or VfoldLA for the final 3D structure prediction.",
        "year": "2022",
        "input": "Raw sequence, Secondary sequence",
        "method": "Template-based",
        "paper": "https://pubmed.ncbi.nlm.nih.gov/35758624/",
        "code": "http://rna.physics.missouri.edu/vfold_software_download/vfoldpipeline_download.html",
        "web_server": "http://rna.physics.missouri.edu/vfoldPipeline/index.html"
    },
    "RNAJP": {
        "title": "RNAJP",
        "text": "RNAJP uses a coarse-grained approach at both atom and helix levels. "
                "It represents a nucleotide with five beads, and uses an energy function that "
                "helps manipulating helices and loops.",
        "year": "2023",
        "input": "Raw sequence, Secondary sequence",
        "method": "Ab initio",
        "paper": "https://pubmed.ncbi.nlm.nih.gov/36864729/",
        "code": "http://rna.physics.missouri.edu/RNAJP/index.html",
        "web_server": ""
    },
}

NATIVE_PREFIX_LINK = "https://github.com/EvryRNA/state_of_the_rnart_website/blob/main/src/data"
PREDS_PREFIX_LINK = "https://github.com/EvryRNA/state_of_the_rnart_website/blob/main/src"
