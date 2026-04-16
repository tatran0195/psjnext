# Title:   Tools.Measure.Area.CreateMeasureNote.Face()
# Desc:    Create a Measure Note for Measure > Area > Face
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.Measure.Area.CreateMeasureNote.Face
# ---
#Preapre model
Geometry.Part.Cube(iPartColor=6409934)
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

#Create a Measure Note
Tools.Measure.Area.CreateMeasureNote.Face(  # [hl:start]
  strNoteName="Area1", 
  crlFaces=[Face(22)])  # [hl:end]
