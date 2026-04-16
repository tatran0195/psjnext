# Title:   Tools.Measure.Mass.CreateMeasureNote.Property()
# Desc:    Create a Measure Note for Measure > Mass > By Property
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.Measure.Mass.CreateMeasureNote.Property
# ---
#Preapre model
Geometry.Part.Cube(ilAxialNodes=[4, 4, 4], iPartColor=14903267)
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

Meshing.SolidMeshing(
  crlParts=[Part(1)], 
  bTet10=True,
  dGradingFactor=1.05,
  dStretchLimit=0.1, 
  iSpeedVsQual=1, 
  iRegion=1, 
  bSafeMode=False, 
  iParallel=8, 
  bInternalMeshOnly=False,
  iPartColor=65280)

Properties.Material.Add(
  strMaterialName="Copper_Alloy", 
  dictMaterialProperty={
    'Density': {
      'density': {'DENSITY': [8300.0]}}, 
    'Elastic': {
      'elastic': {
        'YOUNGS_MODULUS': [110000000000.0], 
        'POISSONS_RATIO': [0.34]}}, 
    }, iMaterialID=1, iMaterialColor=7901428)

Properties.Solid(
  crlTargets=[Part(1)], 
  strName="SolidProperty_1",
  iPropertyColor=16131973, 
  crMaterial=Material(1), 
  iCordM=-2, 
  dDynaRemeshVal1=DFLT_DBL, 
  dDynaRemeshVal2=DFLT_DBL, 
  dDispHG=DFLT_DBL, iFLG=-1)

#Create a Measure Note
Tools.Measure.Mass.CreateMeasureNote.Property(  # [hl:start]
  strNoteName="Mass1", 
  crlParts=[Part(1)])
