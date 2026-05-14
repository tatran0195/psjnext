---
title: "Calculation.FreqRespSolver.LoadCondition()"
description: "Set the steady-state excitation input for frequency response (Solver)"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Calculation > FreqRespSolver > LoadCondition"
macro _link: "[DYNAMIC _FREQ _ANALYSIS _LOAD _SOLVER](../../macro/calculation/DYNAMIC _FREQ _ANALYSIS _LOAD _SOLVER)"
---

## Description

Set the steady-state excitation input for frequency response (Solver).

## Syntax

```psj
Calculation.FreqRespSolver.LoadCondition(...)
```

## Inputs

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iAnalysisType`

- The analysis type.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crTargetAnalysis`

- The target analysis. A new analysis is created if this parameter is set as None.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crCoordinate`

- The output coordinate system.

<!-- @since:5.1.0 @type:String @optional @default:"FRQLOAD" -->
### `strName`

- The name of load condition to be created.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iLoadDirection`

- The direction of vibration.

<!-- @since:5.1.0 @type:List[Double] @optional @default:[1,0,0] -->
### `dlForce`

- The vector of vibration force.

<!-- @since:5.1.0 @type:Double @optional @default:1.0 -->
### `dAmplitude`

- The amplitude of vibration force.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dDelay`

- The value of time delay (seconds).

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dPhase`

- The value of phase delay (angle).

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bBf`

- Whether to use frequency-dependent load as Table input.

<!-- @since:5.1.0 @type:Double @optional @default:1.0 -->
### `dBf`

- The value of frequency-dependent load (Bf).

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crBfCurve`

- The field data of frequency-dependent load.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bFf`

- Whether to use frequency-dependent phase as Table input.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dFf`

- The value of Frequency-dependent phase.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crFfCurve`

- The field data of frequency-dependent phase.

<!-- @since:5.1.0 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The selected nodes which can be assigned the load condition.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iLoadType`

- The load type.
  - 0: Force
  - 1: Displacement
  - 2: Velocity
  - 3: Acceleration

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crEdit`

- An existing load condition
  - If this parameter is used, the specified load condition will be modified.
  - If it is left None, a new load condition will be created.

## Return Code

A _Cursor_ specifying the created frequency load condition (Solver).

## Sample Code

```psj {6-10}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Command\\PostSample\\freq-solver\\103.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# Create Frequency Analysis Load - Solver
loadCondition = Calculation.FreqRespSolver.LoadCondition(strName="FRQLoad _1", 
                                                        iLoadDirection=2, 
                                                        dlForce=[0.0, 0.0, 10.0], 
                                                        dAmplitude=10.0, 
                                                        crlTargets=[Node(514)])
JPT.Debugger(loadCondition) # for checking the return value
```
