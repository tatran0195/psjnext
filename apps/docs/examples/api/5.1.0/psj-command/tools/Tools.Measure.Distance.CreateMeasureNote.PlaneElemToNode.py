# Title:   Tools.Measure.Distance.CreateMeasureNote.PlaneElemToNode()
# Desc:    Create a Measure Note for Measure > Distance > Plane(Elem)-Node function
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.Measure.Distance.CreateMeasureNote.PlaneElemToNode
# ---
#Preapre model
Geometry.Part.Cube(iPartColor=6409934)
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

#Create a Measure Note
Tools.Measure.Distance.CreateMeasureNote.PlaneElemToNode(  # [hl:start]
  strNoteName="Distance1", 
  crNode=Node(185), 
  crElement=Elem(544))  # [hl:end]

