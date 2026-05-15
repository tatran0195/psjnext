---
title: "Calculation.TransResp.OpenAnalysis()"
description: "Load the results of a transient response analysis (*.tsdv)"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Calculation > TransResp > OpenAnalysis"
macro _link: "[CmdSaveOpenTsdv](../../macro/calculation/CmdSaveOpenTsdv)"
---

## Description

Load the results of a transient response analysis (\*.tsdv).

## Syntax

```psj
Calculation.TransResp.OpenAnalysis(...)
```

## Inputs

<!-- @since:5.1.0 @required -->
### strPath

- Specify the path of file will be opened.

<!-- @since:5.1.0 @optional -->
### bBdfMode

- Specify whether to use BDF mode.
- The default value is _False_.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {31}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\plate _eigen.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# Create a load condition
loadcondition = Calculation.TransResp.LoadCondition(strName="TRNLoad _2", iLoadType=1, iLoadDirection=2, 
                                                    dlForce=[0.0, 0.0, 10.0], dAmplitude=10, dT1=0.1, 
                                                    dT2=0.5, dFrequency=10.0, crlTargets=[Node(1516)])

# Create a loadcase
loadcase = Calculation.TransResp.LoadCaseCondition(crTargetAnalysis=PostTransAnalysis(1), 
                                                    strName="LoadCase _1", 
                                                    crlSelectedLoad=[PostTransLoad(1)], 
                                                    dlTargetFactor=[1.0])

# Create response condition
Calculation.TransResp.ResponseCondition(crTargetAnalysis=PostTransAnalysis(1), dDampingFactor=0.02, 
                                        iCurveStyle=0, dStyleParamMid=80.0, dStyleParamBot=0.0125, 
                                        strlResultNames=["TZ"], crlTargets=[Node(1516, 1016)])

# Save Analysis
Calculation.TransResp.SaveAnalysis(strPath="C:/temp/TransRespAnalysis.tsdv", 
                                    crlTargets=[PostTransAnalysis(1)])

# Close current document and import the result file again
JPT.CloseDocumentByName("plate _eigen")
JPT.CreateNewDocument()
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# Open the saved analysis
openFile = Calculation.TransResp.OpenAnalysis(strPath="C:/temp/TransRespAnalysis.tsdv")
JPT.Debugger(openFile)
```
