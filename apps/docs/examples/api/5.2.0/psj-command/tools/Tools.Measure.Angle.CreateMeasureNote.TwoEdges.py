# Title:   Tools.Measure.Angle.CreateMeasureNote.TwoEdges()
# Desc:    Create a Measure Note for Measure > Angle > 2 Edges function
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.Measure.Angle.CreateMeasureNote.TwoEdges
# ---
#Preapre model
Geometry.Part.Cube(iPartColor=6409934)
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

#Create a Measure Note
Tools.Measure.Angle.CreateMeasureNote.TwoEdges(  # [hl:start]
    strNoteName="Angle1",
    crFirstEdge=Edge(9), 
    crSecondEdge=Edge(13))  # [hl:end]
