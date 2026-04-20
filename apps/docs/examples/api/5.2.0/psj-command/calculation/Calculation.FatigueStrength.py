# Title:   Calculation.FatigueStrength()
# Desc:    Calculate fatigue strength (safety factor, mean stress, stress amplitude) at any location
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/calculation/Calculation.FatigueStrength
# ---
# Please prepare the input files for Durability > Fatigue Strength calculation
op2_path = ".../FatigueStrength.op2"
csv_path = [".../FatigueMaterial.csv"]
# Import result model
Home.ImportResults.Nastran(
    strPath=op2_path, 
    bReadLoadAndConstraint=True, 
    bReadConnection=True, 
    bCreateResultsAtMidNode=True)

# Durability > Fatigue Material
Calculation.FatigueMaterial(
  strlFilePaths=csv_path)

# Durability > Fatigue Strength
fatigue_strength = Calculation.FatigueStrength(  # [hl:start]
  crlTargets=[Part(1)], 
  listPropAndMat=[CursorPair(Property3DSolid(1), PostFatigueMaterial(1))], 
  iResAngle=9, 
  strNewSubcaseName="Fatigue Strength", 
  iSubcaseID=9, 
  strCycleName="Case 1", 
  ilSelectedSubcases=[[1, 5, 5], [1, 6, 6], [1, 7, 7], [1, 8, 8]], 
  iCalculationType=1, 
  ilInitStressSubcases=[1, 5, 5], 
  ilTempSubcases=[1, 6, 6], 
  iStressRange=1)  # [hl:end]
print(fatigue_strength)
