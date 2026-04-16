# Title:   Calculation.StressRecovery()
# Desc:    Recover stresses (strain) in arbitrary elements from the calculation results of RecurDyn
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/calculation/Calculation.StressRecovery
# ---
# Please prepare the result files with a compatible version of Sunshine.
op2_path = ".../StressRecovery.op2"
mdf_path = ".../StressRecovery.mdf"
sunshine_path = ".../tss.bat"
# Import result model
Home.ImportResults.Nastran(
  strPath=op2_path, 
  bReadLoadAndConstraint=True, 
  bReadConnection=True, 
  bCreateResultsAtMidNode=True)

# Durability > Stress Recovery
stress_recovery = Calculation.StressRecovery(  # [hl:start]
  crlTargets=[Part(3, 2)], 
  strMDFFilePath=mdf_path, 
  dlStep=[(0.138889, 2.36111), (7.91667, 10.1389)], 
  strSunShinePath=sunshine_path)  # [hl:end]
print(stress_recovery)
