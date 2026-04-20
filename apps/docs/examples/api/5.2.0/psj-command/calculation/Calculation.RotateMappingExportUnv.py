# Title:   Calculation.RotateMappingExportUnv()
# Desc:    Save the mapped result to file (*unv).
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/calculation/Calculation.RotateMappingExportUnv
# ---
# Please set path to your sample universal file and the exported file.
filePath="C:/Temp/Sample.unv"
exportPath = "C:/Temp/Unv_Export.unv"

# Import result file
Home.ImportResults.Universal(filePath)

# Rotate mapping
Calculation.RotateMapping(dAngleInterval=90.0, iRotateAxis=1, crTarget=Part(1))
# Export Unv file
Calculation.RotateMappingExportUnv(strPath=exportPath,   # [hl:start]
                                    veclResultSet=[[105, 1001, 0], [105, 1001, 1], [105, 1001, 2], [105, 1001, 3]], 
                                    ilComponentUnv=[0, 2, 5, 1, 4, 3])  # [hl:end]
