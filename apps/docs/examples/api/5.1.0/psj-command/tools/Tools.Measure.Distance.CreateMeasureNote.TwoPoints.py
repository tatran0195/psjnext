# Title:   Tools.Measure.Distance.CreateMeasureNote.TwoPoints()
# Desc:    Create a Measure Note for Measure > Distance > Two Points function
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.Measure.Distance.CreateMeasureNote.TwoPoints
# ---
#Preapre model
Geometry.Part.Cube(iPartColor=6409934)
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

#Create a Measure Note
Tools.Measure.Distance.CreateMeasureNote.TwoPoints(  # [hl:start]
  strNoteName="Distance1", 
  dlFirstPoint=[0.007, 0.0036, 0.01], 
  dlSecondPoint=[0.001, 0.005, 0.01])  # [hl:end]
