# Title:   Tools.Measure.EditStyle()
# Desc:    Edit style of the specified measure note
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.Measure.EditStyle
# ---
#Preapre model
Geometry.Part.Cube(iPartColor=6409934)
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

#Create a Measure Note
Tools.Measure.Distance.CreateMeasureNote.TwoNodes(
  strNoteName="Distance1", 
  crFirstNode=Node(473), 
  crSecondNode=Node(439))

#Edit the style of the Measure Note
Tools.Measure.EditStyle(  # [hl:start]
  crlMeasureNote=[MeasureNote(1)], 
  iFontColor=255, 
  iBackgroundColor=15794175,
  iOutlineWidth=3, 
  iArrowWidth=2, 
  iArrowColor=255, 
  iArrowType=1, 
  iTitleType=1)  # [hl:end]
