# Title:   Calculation.FFTAnalysis.CopyCondition()
# Desc:    Create a copy of the specified FFT condition
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/calculation/Calculation.FFTAnalysis.CopyCondition
# ---
# This code needs PostFFTCondition by using 
# Calculation.FFTAnalysis.SetCondition. 
# i.e.
# firstBore=Calculation.FFTAnalysis.SetCondition(...)
  # [hl]
Calculation.FFTAnalysis.CopyCondition(crPostFFTCondition=firstBore)
