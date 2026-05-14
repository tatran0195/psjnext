---
title: "Calculation.TransRespSolver.LoadCondition()"
description: "Set the arbitrary excitation input for transient response (Solver)"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Calculation > TransRespSolver > LoadCondition"
macro _link: ""
---

## Description

Set the arbitrary excitation input for transient response (Solver).

## Syntax

```psj
Calculation.TransRespSolver.LoadCondition(...)
```

## Inputs

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crTargetAnalysis`

- The target analysis. A new analysis is created if this parameter is set as None.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crCoordinate`

- The output coordinate system.

<!-- @since:5.1.0 @type:String @optional @default:"TRNLoad" -->
### `strName`

- The name of load condition to be created.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iLoadType`

- The load type.
  - 0: Table(TLOAD1)
  - 1: Cosine(TLOAD2)

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iResultType`

- The result type.
  - 0: Force
  - 1: Displacement
  - 2: Velocity
  - 3: Acceleration

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iLoadDirection`

- The direction of vibration.
  - 0: X
  - 1: Y
  - 2: Z
  - 3: RX
  - 4: RY
  - 5: RZ
  - 6: Normal

<!-- @since:5.1.0 @type:List[Double] @optional @default:[1,0,0] -->
### `dlForce`

- The vector of vibration force.

<!-- @since:5.1.0 @type:Double @optional @default:1.0 -->
### `dAmplitude`

- The amplitude of vibration force.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dInitialDisplacement`

- The initial displacement.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dInitialVelocity`

- The initial displacement.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dT1`

- The vibration start time of load type Cosine(TLOAD2).

<!-- @since:5.1.0 @type:Double @optional @default:1.0 -->
### `dT2`

- The vibration end time of load type Cosine(TLOAD2).

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dFrequency`

- The value of frequency in load type Cosine(TLOAD2).

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dPhase`

- The value of phase delay (angle) in load type Cosine(TLOAD2)

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dExponent`

- The value of exponential function in load type Cosine (TLOAD2).

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dPower`

- The value of growth factor in load type Cosine (TLOAD2).

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bFt`

- Whether to use the time history load as inputted value or table.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dFt`

- The value of the time history load.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crFtCurve`

- The field data of the time history load.

<!-- @since:5.1.0 @type:List[Cursor] @optional @default:[] -->
### `crlTargets`

- The selected nodes which can be assigned the load condition.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crEdit`

- An existing Load condition
  - If this parameter is used, the specified Load condition will be modified.
  - If it is left None, a new Load condition will be created.

## Return Code

A _Cursor_ specifying the created transient load condition (Solver).

## Sample Code

```psj {6-10}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Command\\PostSample\\freq-solver\\103.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# Create Transient Analysis Load - Solver
loadCondition = Calculation.TransRespSolver.LoadCondition(strName="TRNLoad _1", 
                                                        iLoadDirection=2, 
                                                        dlForce=[0.0, 0.0, 10.0], 
                                                        dAmplitude=10.0, 
                                                        crlTargets=[Node(514)])
JPT.Debugger(loadCondition) # for checking the return value
```
