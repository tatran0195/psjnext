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

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crTargetAnalysis`

- The target job to be processed.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crCoordinate`

- The output coordinate system.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bAllModesUsed`

- Whether to use all modes.

<!-- @since:5.1.0 @type:List[String] @optional @default:[] -->
### `strlModesSelected`

- The selected modes using for response calculation. This option was used if bAllModesUsed is _False_.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bDampingFactor`

- Whether to use damping factor for calculation.

<!-- @since:5.1.0 @type:Double @optional @default:0.01 -->
### `dDampingFactor`

- The value of damping factor.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crDampingFactor`

- The field data of damping factor.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iCurveStyle`

- The style of time range for the calculation.
  - 0: Start + StepNumber + StepSize
  - 1: Start + StepSize + End
  - 2: Start + StepNumber + End

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dStyleParamTop`

- The analysis start value of the selected curve style.

<!-- @since:5.1.0 @type:Double @optional @default:1.0 -->
### `dStyleParamMid`

- The step size value of the selected curve style.

<!-- @since:5.1.0 @type:Double @optional @default:1.0 -->
### `dStyleParamBot`

- The analysis end value of the selected curve style.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bIncludeEigenValue`

- Whether to plot the frequency of eigen value.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bCreateNewResult`

- Whether to create new results (displacement and stress) for the entire model.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iResultType`

- The result type to be calculated.
  - 0: Displacement
  - 1: Velocity
  - 2: Acceleration
  - 3: Stress (Solid)
  - 4: Stress (Shell)
  - 5: Disp. + Stress. This result type was displayed when bCreateNewResult = _True_.

<!-- @since:5.1.0 @type:List[String] @optional @default:["TX"] -->
### `strlResultNames`

- The component results according to the selected result type.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iResultPosition`

- The output position of the result.
  - 0: On Node
  - 1: On Element
  - 2: On Element Node

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strDBFileName`

- The SunShine DB file (\*.mdb).

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strDBVersion`

- The DB version.

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strMethodId`

- The method ID.

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strSPCID`

- The SPC ID.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iResidualVector`

- The residual vector option.
  - 0: No
  - 1: Yes
  - 2: Blank

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strPath`

- The directory path used to store the result data (\*.bdf file).

<!-- @since:5.1.0 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The target to calculate the response. The target is node or solid element.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crEdit`

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
