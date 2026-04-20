# Title:   Tools.Measure.Radius.CreateMeasureNote.Edge()
# Desc:    Create a Measure Note for Measure > Radius > Edge function
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.Measure.Radius.CreateMeasureNote.Edge
# ---
#Preapre model
Geometry.Part.Cylinder(iPartColor=6409934)
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

#Create a Measure Note
Tools.Measure.Radius.CreateMeasureNote.Edge(  # [hl:start]
  strNoteName="Radius1", 
  crEdge=Edge(1))  # [hl:end]
