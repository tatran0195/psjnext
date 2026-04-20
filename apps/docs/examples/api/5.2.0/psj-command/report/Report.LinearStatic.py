# Title:   Report.LinearStatic()
# Desc:    Search for parts (components) whose displayed static analysis results are outside the result thresholds set for parts and materials, captures images and automatically pastes them into Microsoft Office PowerPoint
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/report/Report.LinearStatic
# ---
# Prepare Post model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\101_solid.op2"
Home.ImportResults.Nastran(strPath= samplePath, dFaceAngle=60.16, dEdgeAngle=60.16, bReadLoadAndConstraint=True, 
                            bReadConnection=True, bCreateResultsAtMidNode=True)

# Make Linear Static report
reportLinearStatic = Report.LinearStatic(iCalculateValue=1,   # [hl:start]
                                        listPartInformation=[
                                        General_Report_LinearStatic_Data(
                                            strPartName="All", 
                                            strPropName="-", 
                                            strMatName="-", 
                                            dValue=0.000000), 
                                        General_Report_LinearStatic_Data(
                                            strPartName="Part - PSOLID (1)", 
                                            strPropName="PSOLID (1)", 
                                            strMatName="MAT (1)", 
                                            dValue=0.000000), 
                                        General_Report_LinearStatic_Data(
                                            strPartName="Part - PSOLID (2)", 
                                            strPropName="PSOLID (2)", 
                                            strMatName="MAT (1)", 
                                            dValue=0.000000), 
                                        General_Report_LinearStatic_Data(
                                            strPartName="Part - PSOLID (3)", 
                                            strPropName="PSOLID (3)", 
                                            strMatName="MAT (1)", 
                                            dValue=0.000000), 
                                        General_Report_LinearStatic_Data(
                                            strPartName="Part - PSOLID (4)", 
                                            strPropName="PSOLID (4)", 
                                            strMatName="MAT (1)", 
                                            dValue=0.000000), 
                                        General_Report_LinearStatic_Data(
                                            strPartName="Part - PSOLID (5)", 
                                            strPropName="PSOLID (5)", 
                                            strMatName="MAT (1)", 
                                            dValue=0.000000), 
                                        General_Report_LinearStatic_Data(
                                            strPartName="Part - PSOLID (6)", 
                                            strPropName="PSOLID (6)", 
                                            strMatName="MAT (1)", 
                                            dValue=0.000000)], 
                                            bExportPPT=True)  # [hl:end]
JPT.Debugger(reportLinearStatic)
