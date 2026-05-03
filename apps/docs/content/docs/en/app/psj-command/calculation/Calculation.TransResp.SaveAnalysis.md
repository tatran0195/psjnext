---
title: "Calculation.TransResp.SaveAnalysis()"
description: "Save the results of a transient response analysis (*.tsdv)"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Calculation > TransResp > SaveAnalysis"
macro_link: "[SaveMPCResultToCSV](../../macro/calculation/SaveMPCResultToCSV)"
---

## Description

Save the results of a transient response analysis (\*.tsdv).

## Syntax

```psj
Calculation.TransResp.SaveAnalysis(...)
```

## Inputs

### `strPath` @type(String) @required

- The path of file to be saved.

### `crlTargets` @type(List\[Cursor]) @required

- The specified analysis targets to be saved.

### `bBdfMode` @type(Boolean) @default(False)

- Whether to use the BDF mode.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {17-18}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\plate_eigen.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)
# Create a load condition
loadcondition = Calculation.TransResp.LoadCondition(strName="TRNLoad_2", iLoadType=1, iLoadDirection=2, 
                                                    dlForce=[0.0, 0.0, 10.0], dAmplitude=10, dT1=0.1, 
                                                    dT2=0.5, dFrequency=10.0, crlTargets=[Node(1516)])
# Create a loadcase
loadcase = Calculation.TransResp.LoadCaseCondition(crTargetAnalysis=PostTransAnalysis(1), 
                                                    strName="LoadCase_1", crlSelectedLoad=[PostTransLoad(1)], 
                                                    dlTargetFactor=[1.0])
# Create response condition
Calculation.TransResp.ResponseCondition(crTargetAnalysis=PostTransAnalysis(1), dDampingFactor=0.02, 
                                        iCurveStyle=0, dStyleParamMid=80.0, dStyleParamBot=0.0125, 
                                        strlResultNames=["TZ"], crlTargets=[Node(1516, 1016)])
# Save Analysis
saveFile = Calculation.TransResp.SaveAnalysis(strPath="C:/temp/TransRespAnalysis.tsdv", 
                                                crlTargets=[PostTransAnalysis(1)])
JPT.Debugger(saveFile)
```
