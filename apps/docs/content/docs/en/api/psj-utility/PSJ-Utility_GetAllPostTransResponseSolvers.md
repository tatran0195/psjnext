---
title: "JPT.GetAllPostTransResponseSolvers()"
description: "Get all the information of all existing Transient responses (Solver)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Get all the information of all existing Transient responses (Solver).

## Syntax

```psj
JPT.GetAllPostTransResponseSolvers()
```

## Inputs

This utility function does not require any input value.

## Return Code

A _[DPostResponse](../data-type/psj-utility/post-utility/post-built-in-types/DPostResponse)_ object containing all the information of all the existing Transient Responses (Solver).

## Sample Code

```psj {29}
# Prepare result model
inputPath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Command\\PostSample\\freq-solver\\103.bdf"
outputFolder = "C:\\temp"
JPT.RunSunShine(inputPath,outputFolder,2,1,False,True,False)

Home.ImportResults.Nastran(strPath = outputFolder + "\\103.op2", dFaceAngle=60.16, dEdgeAngle=60.16) 

# Create Transient Analysis Load - Solver
Calculation.TransRespSolver.LoadCondition(strName="TRNLoad _1", 
                                        iLoadDirection=2, 
                                        dlForce=[0.0, 0.0, 10.0], 
                                        dAmplitude=10.0, 
                                        crlTargets=[Node(514)])

# Create Transient Analysis Response - Solver
respCondition = Calculation.TransRespSolver.ResponseCondition(crTargetAnalysis=PostTransAnalysisSolver(1), 
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
                                                            crlTargets=[Node(517)])
# Get all Post Transient Response (Solver)
listResponses = JPT.GetAllPostTransResponseSolvers()
JPT.Debugger(listResponses)
for response in listResponses:
    print(response.name)
    print(response.type)
    print(response.id)
    JPT.Debugger(response.targetAnalysis)
    JPT.Debugger(response.resultCurve)
```
