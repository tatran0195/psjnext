# Title:   Tools.Measure.Distance.CreateMeasureNote.TwoNodes()
# Desc:    Create a Measure Note for Measure > Distance > Two Nodes function
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.Measure.Distance.CreateMeasureNote.TwoNodes
# ---
#Preapre model
Geometry.Part.Cube(iPartColor=6409934)
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

#Create a Measure Note
Tools.Measure.Distance.CreateMeasureNote.TwoNodes(  # [hl:start]
    strNoteName="Distance1", 
    crFirstNode=Node(7), 
    crSecondNode=Node(5))  # [hl:end]
