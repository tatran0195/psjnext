# Title:   Calculation.Subcase.RelativeOffset()
# Desc:    Create a subcase of relative displacement with zero displacement for any selected nodal ID
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/calculation/Calculation.Subcase.RelativeOffset
# ---
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# Subcase.RelativeOffset
relativeOffset = Calculation.Subcase.RelativeOffset(iAnalysisType=2, iTimeStep=1, iNodeID=133, iSubcaseID=11, \  # [hl:start]
                                                    strSubcaseName="Relative Offset 11  Subcase 1")  # [hl:end]
JPT.Debugger(relativeOffset)
Post.ShowContour(crPostJob=TSVPostJob(1), 
                lContourSettings=[PostContourSetting(postResultKey=PostResultKey(iAnalysisType=2, \
                iResultSet=1, iTimeStep=11, strResultName="Displacement", strResultCompName="Translational", \
                iResultPos=1), postDataOp=PostDataOp(iResultLocation=1, iOptionCoord=1))])
