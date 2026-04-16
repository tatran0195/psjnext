# Title:   Tools.Measure.Distance.CreateMeasureNote.Edge()
# Desc:    Create a Measure Note for Measure > Distance > Edge function
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.Measure.Distance.CreateMeasureNote.Edge
# ---
#Preapre model
Geometry.Part.Cube(iPartColor=6409934)
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

#Create a Measure Note
Tools.Measure.Distance.CreateMeasureNote.Edge(  # [hl:start]
    strNoteName="Distance1", 
    crEdge=Edge(14))  # [hl:end]
