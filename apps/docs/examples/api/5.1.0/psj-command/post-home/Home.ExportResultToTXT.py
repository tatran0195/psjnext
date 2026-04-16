# Title:   Home.ExportResultToTXT()
# Desc:    Export the selected result file to text format (*.txt)
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/post-home/Home.ExportResultToTXT
# ---
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16) 

# Export result to txt
exportFile = Home.ExportResultToTXT(strFileName="C:/temp/ExportTXT.txt",   # [hl:start]
                                    iSpliterType=1, 
                                    crlJobs=[TSVPostJob(1, 1)], 
                                    ilAnalysisTypes=[1, 1], 
                                    ilResultSets=[1, 1], 
                                    ilTimeSteps=[1, 1], 
                                    ilResultTypes=[3, 4], 
                                    ilResultPos=[1, 1], 
                                    strlResultNames=["", ""], 
                                    strlCompNames=["", ""], 
                                    strlNames=["RX", "RY"], 
                                    strlTypes=["TYPE_VIRTUAL_RESULT_ITEM", "TYPE_VIRTUAL_RESULT_ITEM"], 
                                    crlEdit=[Unknown(0, 0)])  # [hl:end]
JPT.Debugger(exportFile )
