# Title:   Home.ExportGeometrySurface()
# Desc:    Export the file in Geometry Surface for Post format (*.stl)
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post-home/Home.ExportGeometrySurface
# ---
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16) 

# Export Geometry Surface for Post
exportFile = Home.ExportGeometrySurface(strFolderName="C:\\temp")  # [hl]
JPT.Debugger(exportFile)
