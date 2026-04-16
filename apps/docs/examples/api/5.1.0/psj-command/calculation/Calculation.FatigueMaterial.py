# Title:   Calculation.FatigueMaterial()
# Desc:    Load the fatigue limit diagrams for each material
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/calculation/Calculation.FatigueMaterial
# ---
# Please prepare the input files for Durability > Fatigue Material calculation
op2_path = ".../FatigueMaterial.op2"
csv_path = [".../FatigueMaterial.csv"]
# Import result model
Home.ImportResults.Nastran(
    strPath=op2_path, 
    bReadLoadAndConstraint=True, 
    bReadConnection=True, 
    bCreateResultsAtMidNode=True)

# Durability > Fatigue Material
ret = Calculation.FatigueMaterial(  # [hl]
    strlFilePaths=csv_path)  # [hl]
print(ret)
