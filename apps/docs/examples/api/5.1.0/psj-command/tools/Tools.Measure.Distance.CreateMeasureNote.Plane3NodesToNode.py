# Title:   Tools.Measure.Distance.CreateMeasureNote.Plane3NodesToNode()
# Desc:    Create a Measure Note for Measure > Distance >  Plane(3Nodes)-Node function
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.Measure.Distance.CreateMeasureNote.Plane3NodesToNode
# ---
#Preapre model
Geometry.Part.Cube(iPartColor=6409934)
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

#Create a Measure Note
Tools.Measure.Distance.CreateMeasureNote.Plane3NodesToNode(  # [hl:start]
    strNoteName="Distance1", 
    crFirstNode=Node(35), 
    crSecondNode=Node(223), 
    crThirdNode=Node(437), 
    crFourthNode=Node(339))  # [hl:end]
