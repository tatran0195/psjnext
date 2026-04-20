# Title:   Tools.Measure.Distance.CreateMeasureNote.EdgeNode()
# Desc:    Create a Measure Note for Measure > Distance > Edge-Node function.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.Measure.Distance.CreateMeasureNote.EdgeNode
# ---
#Preapre model
Geometry.Part.Cube(iPartColor=6409934)
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

#Create a Measure Note
Tools.Measure.Distance.CreateMeasureNote.EdgeNode(  # [hl:start]
  strNoteName="MyDistance", 
  crNode=Node(36), 
  crEdge=Edge(18))  # [hl:end]
