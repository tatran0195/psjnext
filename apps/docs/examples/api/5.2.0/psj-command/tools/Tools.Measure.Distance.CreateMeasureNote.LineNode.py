# Title:   Tools.Measure.Distance.CreateMeasureNote.LineNode()
# Desc:    Create a Measure Note for Measure > Distance > Line[Two Nodes]-Node function.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.Measure.Distance.CreateMeasureNote.LineNode
# ---
#Preapre model
Geometry.Part.Cube(iPartColor=6409934)
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

#Create a Measure Note
Tools.Measure.Distance.CreateMeasureNote.LineNode(  # [hl:start]
    strNoteName="Distance1", 
    crFirstNode=Node(88), 
    crSecondNode=Node(473), 
    crThirdNode=Node(431))  # [hl:end]

