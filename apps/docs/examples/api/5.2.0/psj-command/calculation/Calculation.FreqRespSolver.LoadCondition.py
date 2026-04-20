# Title:   Calculation.FreqRespSolver.LoadCondition()
# Desc:    Set the steady-state excitation input for frequency response (Solver)
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/calculation/Calculation.FreqRespSolver.LoadCondition
# ---
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Command\\PostSample\\freq-solver\\103.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# Create Frequency Analysis Load - Solver
loadCondition = Calculation.FreqRespSolver.LoadCondition(strName="FRQLoad_1",   # [hl:start]
                                                        iLoadDirection=2, 
                                                        dlForce=[0.0, 0.0, 10.0], 
                                                        dAmplitude=10.0, 
                                                        crlTargets=[Node(514)])  # [hl:end]
JPT.Debugger(loadCondition) # for checking the return value
