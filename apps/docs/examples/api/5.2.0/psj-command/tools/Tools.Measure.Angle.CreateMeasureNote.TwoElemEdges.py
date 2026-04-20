# Title:   Tools.Measure.Angle.CreateMeasureNote.TwoElemEdges()
# Desc:    Create a Measure Note for Measure > Angle > 2 Elem Edges function
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.Measure.Angle.CreateMeasureNote.TwoElemEdges
# ---
#Preapre model
Geometry.Part.Cube(iPartColor=6409934)
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

#Create a Measure Note
Tools.Measure.Angle.CreateMeasureNote.TwoElemEdges(  # [hl:start]
  strNoteName="Angle1", 
  crFirstPairFirstNode=Node(371), 
  crFirstPairSecondNode=Node(380), 
  crSecondPairFirstNode=Node(379), 
  crSecondPairSecondNode=Node(380))  # [hl:end]
