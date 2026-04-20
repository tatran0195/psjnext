# Title:   Calculation.AcousticAnalysis.PanelContribution()
# Desc:    Create a plot line for each panel property based on Actran's element contribution results
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/calculation/Calculation.AcousticAnalysis.PanelContribution
# ---
# Please set path to your sample Nastran Vibro-Acoustic file.
filePath="C:/Temp/Sample.op2"

# Prepare result model
Home.ImportResults.Nastran(strPath=filePath, dFaceAngle=60.16, dEdgeAngle=60.16, bIsVibro=True)

# AcousticAnalysis.PanelContribution
Calculation.AcousticAnalysis.PanelContribution(ilLoadCases=[201],   # [hl:start]
                                                crlProperties=[Property2DShell(50000), 
                                                Property3DSolid(20000, 40000)], 
                                                iAreaUnit=0)
Calculation.AcousticAnalysis.PanelContributionCreateGraph(crlLoadCases=[PostActranLoadCase(1, 2, 3, 4)])  # [hl:end]
