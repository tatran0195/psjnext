# Title:   Tools.Measure.Radius.CreateMeasureNote.ThreeNodes()
# Desc:    Create a Measure Note for Measure > Radius > 3 Nodes function
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.Measure.Radius.CreateMeasureNote.ThreeNodes
# ---
#Preapre model
Geometry.Part.Cylinder(iPartColor=6409934)
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

#Create a Measure Note
Tools.Measure.Radius.CreateMeasureNote.ThreeNodes(  # [hl:start]
  strNoteName="Radius1", 
  crFirstNode=Node(70), 
  crSecondNode=Node(46), 
  crThirdNode=Node(16))  # [hl:end]
