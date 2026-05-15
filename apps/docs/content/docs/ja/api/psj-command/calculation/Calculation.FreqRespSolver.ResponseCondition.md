---
title: "Calculation.FreqRespSolver.ResponseCondition()"
description: "Output the result of the response point for frequency response (Solver)"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Calculation > FreqRespSolver > ResponseCondition"
macro _link: "[DYNAMIC _FREQ _ANALYSIS _RESPONSE _SOLVER](../../macro/calculation/DYNAMIC _FREQ _ANALYSIS _RESPONSE _SOLVER)"
---

## Description

Output the result of the response point for frequency response (Solver).

## Syntax

```psj
Calculation.FreqRespSolver.ResponseCondition(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### crTargetAnalysis

- Specify the target job to be processed.
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### crCoordinate

- Specify the output coordinate system.
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### bAllModesUsed

- Specify whether to use all modes.
- The default value is _True_.

<!-- @since:5.1.0 @optional -->
### strlModesSelected

- Specify the selected modes using for response calculation. This option was used if bAllModesUsed is _False_.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### bDampingFactor

- Specify whether to use damping factor for calculation.
- The default value is _True_.

<!-- @since:5.1.0 @optional -->
### dDampingFactor

- Specify the value of damping factor.
- The default value is 0.01.

<!-- @since:5.1.0 @optional -->
### crDampingFactor

- Specify the field data of damping factor.
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### iCurveStyle

- Specify the style of time range for the calculation.
  - 0: Start + StepNumber + StepSize
  - 1: Start + StepSize + End
  - 2: Start + StepNumber + End
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### dStyleParamTop

- Specify the analysis start value of the selected curve style.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### dStyleParamMid

- Specify the step size value of the selected curve style.
- The default value is 1.0.

<!-- @since:5.1.0 @optional -->
### dStyleParamBot

- Specify the analysis end value of the selected curve style.
- The default value is 1.0.

<!-- @since:5.1.0 @optional -->
### bIncludeEigenValue

- Specify whether to plot the frequency of eigen value.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### bCreateNewResult

- Specify whether to create new results (displacement and stress) for the entire model.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### iResultType

- Specify the result type to be calculated.
  - 0: Displacement
  - 1: Velocity
  - 2: Acceleration
  - 3: Stress (Solid)
  - 4: Stress (Shell)
  - 5: Disp. + Stress. This result type was displayed when bCreateNewResult = _True_.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### strlResultNames

- Specify the component results according to the selected result type.
- The default value is \["TX"].

<!-- @since:5.1.0 @optional -->
### iResultPosition

- Specify the output position of the result.
  - 0: On Node
  - 1: On Element
  - 2: On Element Node
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### strDBFileName

- Specify the SunShine DB file (\*.mdb).
- The default value is "".

<!-- @since:5.1.0 @optional -->
### strDBVersion

- Specify the DB version.
- The default value is "".

<!-- @since:5.1.0 @optional -->
### strMethodId

- Specify the method ID.
- The default value is "".

<!-- @since:5.1.0 @optional -->
### strSPCID

- Specify the SPC ID.
- The default value is "".

<!-- @since:5.1.0 @optional -->
### iResidualVector

- Specify residual vector option.
  - 0: No
  - 1: Yes
  - 2: Blank
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### strPath

- Specify the directory path used to store the result data (\*.bdf file).
- The default value is "".

<!-- @since:5.1.0 @optional -->
### crlTargets

- Specify the target to calculate the response. The target is node or solid element.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### crEdit

- Specify an existing response condition
  - If this parameter is used, the specified response condition will be modified.
  - If it is left None, a new response condition will be created.
- The default value is _None_.

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
Calculation.FreqRespSolver.LoadCondition(strName="FRQLoad _1", 
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
