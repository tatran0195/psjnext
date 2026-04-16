# Title:   Tools.Measure.Area.CreateMeasureNote.Part()
# Desc:    Create a Measure Note for Measure > Area > Part
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.Measure.Area.CreateMeasureNote.Part
# ---
#Preapre model
Geometry.Part.Cube(iPartColor=6409934)
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

#Create a Measure Note
Tools.Measure.Area.CreateMeasureNote.Part(  # [hl:start]
  strNoteName="Area1", 
  crlParts=[Part(1)])  # [hl:end]
