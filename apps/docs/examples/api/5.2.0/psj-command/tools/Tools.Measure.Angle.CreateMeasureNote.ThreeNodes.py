# Title:   Tools.Measure.Angle.CreateMeasureNote.ThreeNodes()
# Desc:    Create a Measure Note for Measure > Angle > 3 Nodes function
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.Measure.Angle.CreateMeasureNote.ThreeNodes
# ---
#Preapre model
Geometry.Part.Cube(iPartColor=6409934)
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

#Create a Measure Note
Tools.Measure.Angle.CreateMeasureNote.ThreeNodes(  # [hl:start]
    strNoteName="Angle1", 
    crFirstNode=Node(410),   # [hl:end]
    crSecondNode=Node(406), 
    crThirdNode=Node(370))
