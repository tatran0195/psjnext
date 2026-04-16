# Title:   Calculation.TransResp.LoadCaseCondition()
# Desc:    Create a load case for transient response analysis
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/calculation/Calculation.TransResp.LoadCaseCondition
# ---
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\plate_eigen.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# Create a load condition
loadcondition = Calculation.TransResp.LoadCondition(strName="TRNLoad_2", iLoadType=1, iLoadDirection=2, 
                                                    dlForce=[0.0, 0.0, 10.0], dAmplitude=10, dT1=0.1, 
                                                    dT2=0.5, dFrequency=10.0, crlTargets=[Node(1516)])

# Create a loadcase
loadcase = Calculation.TransResp.LoadCaseCondition(crTargetAnalysis=PostTransAnalysis(1), strName="LoadCase_1",  # [hl:start]
                                                 crlSelectedLoad=[PostTransLoad(1)], dlTargetFactor=[1.0])  # [hl:end]
JPT.Debugger(loadcase)
