# Title:   Assembly.RightClick.ExportMeasureNote()
# Desc:    Export content of measure notes to csv files.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/assembly/Assembly.RightClick.ExportMeasureNote
# ---
import os

#Preapre model
Geometry.Part.Cube(iPartColor=6409934)
JPT.DisableScreenAnimation()
JPT.ViewFitToModel()

#Create a Measure Note
Tools.Measure.Distance.CreateMeasureNote.TwoNodes(
    strNoteName="Distance1", 
    crFirstNode=Node(7), 
    crSecondNode=Node(5))

path_to_temp=JPT.GetAppPathInfo(JPT.PathType.TEMP_PATH)

Assembly.RightClick.ExportMeasureNote(  # [hl:start]
    crlTargets=[MeasureNote(1)], 
    strlPaths=[os.path.join(path_to_temp,"Distance.csv")], 
    iEncode=0, 
    bWithBOM=True)  # [hl:end]
