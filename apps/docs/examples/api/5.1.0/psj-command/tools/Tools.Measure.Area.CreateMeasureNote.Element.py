# Title:   Tools.Measure.Area.CreateMeasureNote.Element()
# Desc:    Create a Measure Note for Measure > Area > Element
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.Measure.Area.CreateMeasureNote.Element
# ---
#Preapre model
Geometry.Part.Cube(iPartColor=6409934)
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

#Create a Measure Note
Tools.Measure.Area.CreateMeasureNote.Element(  # [hl:start]
    strNoteName="Area1", 
    crlElements=[Elem(233, 216, 215, 197, 198, 180)])  # [hl:end]
