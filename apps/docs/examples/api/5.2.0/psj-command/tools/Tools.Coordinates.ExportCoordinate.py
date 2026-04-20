# Title:   Tools.Coordinates.ExportCoordinate()
# Desc:    Export local coordinates as Nastran bdf format.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/tools/Tools.Coordinates.ExportCoordinate
# ---
#Prepare model
Geometry.Part.Cube(iPartColor=6409934)

#Prepare coordinates
lcs1=Tools.Coordinates.ThreeNode(
    strName="CRect_1", 
    crlNodes=[Node(7, 6, 445)])

lcs2=Tools.Coordinates.ThreeNode(
    strName="CRect_2", 
    crlNodes=[Node(310, 317, 336)])

#Export coordinates

import os 
temp_path=JPT.GetAppPathInfo(JPT.PathType.TEMP_PATH)

Tools.Coordinates.ExportCoordinate(  # [hl:start]
    strlPath=os.path.join(temp_path,'exp-lcs.bdf'), 
    crlCS=[lcs1,lcs2])  # [hl:end]
