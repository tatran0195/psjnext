---
title: "Calculation.FreqRespSolver.ResponseCondition()"
description: "Output the result of the response point for frequency response (Solver)"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Calculation > FreqRespSolver > ResponseCondition"
macro_link: "[DYNAMIC_FREQ_ANALYSIS_RESPONSE_SOLVER](../../macro/calculation/DYNAMIC_FREQ_ANALYSIS_RESPONSE_SOLVER)"
---

## Description

Output the result of the response point for frequency response (Solver).

## Syntax

```psj
Calculation.FreqRespSolver.ResponseCondition(...)
```

## Inputs

### `crTargetAnalysis` @type(Cursor) @default(None)

- The target job to be processed.

### `crCoordinate` @type(Cursor) @default(None)

- The output coordinate system.

### `bAllModesUsed` @type(Boolean) @default(True)

- Whether to use all modes.

### `strlModesSelected` @type(List\[String]) @default(\[])

- The selected modes using for response calculation. This option was used if bAllModesUsed i&#x73;_&#x46;alse_.

### `bDampingFactor` @type(Boolean) @default(True)

- Whether to use damping factor for calculation.

### `dDampingFactor` @type(Double) @default(0.01)

- The value of damping factor.

### `crDampingFactor` @type(Cursor) @default(None)

- The field data of damping factor.

### `iCurveStyle` @type(Integer) @default(1)

- The style of time range for the calculation.
  - 0: Start + StepNumber + StepSize
  - 1: Start + StepSize + End
  - 2: Start + StepNumber + End

### `dStyleParamTop` @type(Double) @default(0.0)

- The analysis start value of the selected curve style.

### `dStyleParamMid` @type(Double) @default(1.0)

- The step size value of the selected curve style.

### `dStyleParamBot` @type(Double) @default(1.0)

- The analysis end value of the selected curve style.

### `bIncludeEigenValue` @type(Boolean) @default(False)

- Whether to plot the frequency of eigen value.

### `bCreateNewResult` @type(Boolean) @default(False)

- Whether to create new results (displacement and stress) for the entire model.

### `iResultType` @type(Integer) @default(0)

- The result type to be calculated.
  - 0: Displacement
  - 1: Velocity
  - 2: Acceleration
  - 3: Stress (Solid)
  - 4: Stress (Shell)
  - 5: Disp. + Stress. This result type was displayed when bCreateNewResult =_True_.

### `strlResultNames` @type(List\[String]) @default(\["TX"])

- The component results according to the selected result type.

### `iResultPosition` @type(Integer) @default(0)

- The output position of the result.
  - 0: On Node
  - 1: On Element
  - 2: On Element Node

### `strDBFileName` @type(String) @default("")

- The SunShine DB file (\*.mdb).

### `strDBVersion` @type(String) @default("")

- The DB version.

### `strMethodId` @type(String) @default("")

- The method ID.

### `strSPCID` @type(String) @default("")

- The SPC ID.

### `iResidualVector` @type(Integer) @default(0)

- Residual vector option.
  - 0: No
  - 1: Yes
  - 2: Blank

### `strPath` @type(String) @default("")

- The directory path used to store the result data (\*.bdf file).

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The target to calculate the response. The target is node or solid element.

### `crEdit` @type(Cursor) @default(None)

- An existing response condition
  - If this parameter is used, the specified response condition will be modified.
  - If it is left None, a new response condition will be created.

## Return Code

A _Cursor_ specifying the created frequency response condition (solver).

## Sample Code

```psj {16-27}
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
respCondition = Calculation.FreqRespSolver.ResponseCondition(crTargetAnalysis=PostFreqAnalysisSolver(1), 
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
                                                            crlTargets=[Node(517)])
JPT.Debugger(respCondition) # for checking the return value
```
