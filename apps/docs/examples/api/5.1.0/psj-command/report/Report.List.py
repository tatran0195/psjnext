# Title:   Report.List()
# Desc:    Export the selected results to a CSV file or a universal format
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/report/Report.List
# ---
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)
Post.ShowContour(crPostJob=TSVPostJob(1), 
                lContourSettings=[PostContourSetting(postResultKey=PostResultKey(
                iAnalysisType=2, 
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
                    iAnalysisType=2, 
                    iResultSet=1, 
                    iTimeStep=1, 
                    strResultName="Displacement", 
                    strResultCompName="Translational"))
Post.EnableMiddleNodes()

# Make List report
reportList = Report.List(strPath="C:/temp/ReportList.csv",   # [hl:start]
                        crlTargets=[Part(3)], 
                        iOutput=1, 
                        bMidNode=True, 
                        listPostResultKey=[[2, 1, 1, 0], [2, 1, 2, 0], [2, 1, 3, 0], [2, 1, 4, 0], [2, 1, 5, 0]])  # [hl:end]
JPT.Debugger(reportList)
