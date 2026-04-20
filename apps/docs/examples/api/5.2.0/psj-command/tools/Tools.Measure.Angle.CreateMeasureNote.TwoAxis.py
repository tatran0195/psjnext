# Title:   Tools.Measure.Angle.CreateMeasureNote.TwoAxis()
# Desc:    Create a Measure Note for Measure > Angle > 2 Axes function
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.Measure.Angle.CreateMeasureNote.TwoAxis
# ---
#Preapre model
Geometry.Part.Cube(iPartColor=6409934)
Tools.Coordinates.ThreeNode(strName="CRect_1", crlNodes=[Node(6, 437, 472)])
Tools.Coordinates.ThreeNode(strName="CRect_2", crlNodes=[Node(370, 186, 170)])
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

#Create a Measure Note
Tools.Measure.Angle.CreateMeasureNote.TwoAxis(  # [hl:start]
  strNoteName="Angle1", 
  iAxis=0, 
  crCoordinateRef=Coord(2),
  iAxisRef=0, 
  crCoordinate=Coord(1))  # [hl:end]
