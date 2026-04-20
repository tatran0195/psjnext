# Title:   Tools.ResultToLoad()
# Desc:    Export the selected result name to solver information (as solver keyword card) for the selected entities. Depending on selection of convert load type, the analysis result will be exported to solver card information respectively.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post-tools/Tools.ResultToLoad
# ---
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\Post\\Static_Renkon.op2"
Home.ImportResults.Nastran(strPath= samplePath, dFaceAngle=60.16, dEdgeAngle=60.16, bReadLoadAndConstraint=True, 
                            bReadConnection=True, bCreateResultsAtMidNode=True)
Post.ShowContour(crPostJob=TSVPostJob(1), 
                lContourSettings=[PostContourSetting(postResultKey=PostResultKey(
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

# Result to load
sampleFile = Tools.ResultToLoad(crlTargets=[Face(10)],   # [hl:start]
                                postStepItem=POST_STEP_ITEM(
                                    iAnalysisType=1, 
                                    iResultSet=1, 
                                    iTimeStep=1), 
                                vecResultLoad=[RESULT_LOAD(
                                    iVrType=6, 
                                    strResultName="Displacement", 
                                    strLoadName="Enforced Displacement")], 
                                strExportPath="C:/temp/ResultToLoadFile")  # [hl:end]
JPT.Debugger(sampleFile)
