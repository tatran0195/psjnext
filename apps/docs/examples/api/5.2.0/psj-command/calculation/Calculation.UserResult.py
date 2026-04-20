# Title:   Calculation.UserResult()
# Desc:    Any desired result can be created and added to the document by treating the results as variables and passing them to functions.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/calculation/Calculation.UserResult
# ---
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# User result
result = Calculation.UserResult(crPostJob=TSVPostJob(1),   # [hl:start]
                                iResultVariableType=3, 
                                strResultName="Expr_1", 
                                iResultSet=2, 
                                listResultVariables=[RESULT_VARIABLE(crReferencePostJob=TSVPostJob(1), \
                                strName="C1", iAnalysisType=2, iResultSet=1, iTimeStep=1, iResultPos=1), \
                                RESULT_VARIABLE(crReferencePostJob=TSVPostJob(1), strName="C2", \
                                iAnalysisType=2, iResultSet=1, iTimeStep=1, iResultType=1, iResultPos=1)], 
                                bResultExpression=False, 
                                bContourExpression=True, 
                                strContourExpression="C1+C2")  # [hl:end]
JPT.Debugger(result)
