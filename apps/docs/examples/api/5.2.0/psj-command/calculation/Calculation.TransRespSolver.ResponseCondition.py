# Title:   Calculation.TransRespSolver.ResponseCondition()
# Desc:    Output the result of the response point for transient response (Solver)
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/calculation/Calculation.TransRespSolver.ResponseCondition
# ---
# Prepare result model
inputPath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Command\\PostSample\\freq-solver\\103.bdf"
outputFolder = "C:\\temp"
JPT.RunSunShine(inputPath,outputFolder,2,1,False,True,False)

Home.ImportResults.Nastran(strPath = outputFolder + "\\103.op2", dFaceAngle=60.16, dEdgeAngle=60.16) 

# Create Transient Analysis Load - Solver
Calculation.TransRespSolver.LoadCondition(strName="TRNLoad_1", 
                                        iLoadDirection=2, 
                                        dlForce=[0.0, 0.0, 10.0], 
                                        dAmplitude=10.0, 
                                        crlTargets=[Node(514)])

# Create Transient Analysis Response - Solver
respCondition = Calculation.TransRespSolver.ResponseCondition(crTargetAnalysis=PostTransAnalysisSolver(1),   # [hl:start]
                                                            bDampingFactor=False, 
                                                            dDampingFactor=0.02, 
                                                            iCurveStyle=2, 
                                                            dStyleParamMid=20.0, 
                                                            dStyleParamBot=5000.0, 
                                                            strlResultNames=["TZ"], 
                                                            strDBFileName="103", 
                                                            strDBVersion="1", 
                                                            strMethodId="2", 
                                                            strPath="C:/temp/111.bdf", 
                                                            crlTargets=[Node(517)])  # [hl:end]
JPT.Debugger(respCondition) # for checking the return value
