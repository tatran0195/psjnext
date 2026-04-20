# Title:   Tools.Measure.Distance.CreateMeasureNote.TwoEdges()
# Desc:    Create a Measure Note for Measure > Distance > 2Edges function
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.Measure.Distance.CreateMeasureNote.TwoEdges
# ---
#Preapre model
Geometry.Part.Cube(iPartColor=6409934)
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

#Create a Measure Note
Tools.Measure.Distance.CreateMeasureNote.TwoEdges(  # [hl:start]
    strNoteName="Distance1", 
    crFirstEdge=Edge(11),
    crSecondEdge=Edge(17))  # [hl:end]
