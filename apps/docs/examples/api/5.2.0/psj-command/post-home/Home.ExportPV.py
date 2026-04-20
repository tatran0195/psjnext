# Title:   Home.ExportPV()
# Desc:    Output the results to PV files according to three types of elements, or materials, or properties
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post-home/Home.ExportPV
# ---
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16) 
Post.ShowContour(crPostJob=TSVPostJob(1), 
                lContourSettings=[PostContourSetting(
                    postResultKey=PostResultKey(
                        iAnalysisType=1, 
                        iResultSet=1, 
                        iTimeStep=1, 
                        strResultName="Displacement", 
                        strResultCompName="Translational", 
                        iResultPos=1), 
                    postDataOp=PostDataOp(
                        iResultLocation=1, 
                        iOptionCoord=1))])
Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                    postResultKey=PostResultKey(
                        iAnalysisType=1, 
                        iResultSet=1, 
                        iTimeStep=1, 
                        strResultName="Displacement", 
                        strResultCompName="Translational"))
Tools.Group.CreateGroup(strGroupName="Element3DGroup", crlTargets=[ROElem(479, 477, 480, 478)])

# Export PV
exportFile = Home.ExportPV(iGroupType=1, strFileName="C:/temp/ExportPV.tsv")  # [hl]
JPT.Debugger(exportFile)
