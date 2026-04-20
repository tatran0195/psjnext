# Title:   Calculation.AcousticAnalysis.ActranPltImport()
# Desc:    Create intensity from the sound pressure and particle velocity results
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/calculation/Calculation.AcousticAnalysis.ActranPltImport
# ---
#Please set path to your sample actran file.
filePath="C:/Temp/Sample.plt"

plt = Calculation.AcousticAnalysis.ActranPltImport(strPath=filePath)  # [hl]
JPT.Debugger(plt)
