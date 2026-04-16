# Title:   Tools.Measure.Angle.CreateMeasureNote.TwoNodesAxis()
# Desc:    Create a Measure Note for Measure > Angle > 2 Nodes Axis function
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.Measure.Angle.CreateMeasureNote.TwoNodesAxis
# ---
#Preapre model
Geometry.Part.Cube(iPartColor=6409934)
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

#Create a Measure Note
Tools.Measure.Angle.CreateMeasureNote.TwoNodesAxis(  # [hl:start]
    strNoteName="Angle1", 
    crFirstNode=Node(107), 
    crSecondNode=Node(259))  # [hl:end]
