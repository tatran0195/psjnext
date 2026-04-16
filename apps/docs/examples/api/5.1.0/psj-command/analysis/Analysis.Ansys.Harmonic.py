# Title:   Analysis.Ansys.Harmonic()
# Desc:    Export the Ansys Harmonic Structural solver file
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/analysis/Analysis.Ansys.Harmonic
# ---
Geometry.Part.Cube()

Analysis.Ansys.Harmonic("Job1", ansysAnalysisHarmonic=HARMONIC(bHarmonicOutputDisplacements=True),  # [hl:start]
    iLoadCaseId=1, strFileName="C:/Job1.dat")  # [hl:end]
