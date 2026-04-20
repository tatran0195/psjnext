# Title:   Calculation.FreqRespSolver.ResponseCondition()
# Desc:    Output the result of the response point for frequency response (Solver)
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/calculation/Calculation.FreqRespSolver.ResponseCondition
# ---
# Prepare result model
inputPath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Command\\PostSample\\freq-solver\\103.bdf"
outputFolder = "C:\\temp"
JPT.RunSunShine(inputPath,outputFolder,2,1,False,True,False)

Home.ImportResults.Nastran(strPath = outputFolder + "\\103.op2", dFaceAngle=60.16, dEdgeAngle=60.16) 

# Create Frequency Analysis Load - Solver
Calculation.FreqRespSolver.LoadCondition(strName="FRQLoad_1", 
                                        iLoadDirection=2, 
                                        dlForce=[0.0, 0.0, 10.0], 
                                        dAmplitude=10.0, 
                                        crlTargets=[Node(514)])

# Create Frequency Analysis Transient - Solver
respCondition = Calculation.FreqRespSolver.ResponseCondition(crTargetAnalysis=PostFreqAnalysisSolver(1),   # [hl:start]
                                                            bDampingFactor=False, 
                                                            dDampingFactor=0.02, 
                                                            iCurveStyle=2, 
                                                            dStyleParamMid=20.0, 
                                                            dStyleParamBot=50000.0, 
                                                            strlResultNames=["TZ"], 
                                                            strDBFileName="103", 
                                                            strDBVersion="1", 
                                                            strMethodId="2", 
                                                            strPath="C:/temp/113.bdf", 
                                                            crlTargets=[Node(517)])  # [hl:end]
JPT.Debugger(respCondition) # for checking the return value
