---
title: "Calculation.TransResp.LoadCondition()"
description: "Set the arbitrary excitation input for transient response"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Calculation > TransResp > LoadCondition"
macro _link: "[DYNAMIC _TRANS _ANALYSIS _LOAD](../../macro/calculation/DYNAMIC _TRANS _ANALYSIS _LOAD)"
---

## Description

Set the arbitrary excitation input for transient response.

## Syntax

```psj
Calculation.TransResp.LoadCondition(...)
```

## Inputs

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crTargetAnalysis`

- The target analysis. A new analysis is created if this parameter is set as None.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crCoordinate`

- The coordinate system.

<!-- @since:5.1.0 @type:String @optional @default:"TRNLoad1" -->
### `strName`

- The name of load condition to be created.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iLoadType`

- The load type.
  - 0: Table(TLOAD1)
  - 1: Cosine(TLOAD2)

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

- The amplitude of vibration load.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dDelay`

- The value of time delay (seconds).

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dPhase`

- The value of phase delay (angle) in load type Cosine(TLOAD2).

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bFt`

- Whether to use the time history load as inputted value or table.

<!-- @since:5.1.0 @type:Double @optional @default:1.0 -->
### `dFt`

- The value of the time history load.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crFtCurve`

- The field data of the time history load.

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
### `dExponent`

- The value of exponential function in load type Cosine (TLOAD2).

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dPower`

- The value of growth factor in load type Cosine (TLOAD2).

<!-- @since:5.1.0 @type:List[Cursor] @required -->
### `crlTargets`

- The selected nodes which can be assigned the load condition.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crEdit`

- An existing Load condition
  - If this parameter is used, the specified Load condition will be modified.
  - If it is left None, a new Load condition will be created.

## Return Code

A _Cursor_ specifying the created transient load condition.

## Sample Code

```psj {6-8}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\plate _eigen.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# Create a load condition
loadcondition = Calculation.TransResp.LoadCondition(strName="TRNLoad _2", iLoadType=1, iLoadDirection=2, 
                                                    dlForce=[0.0, 0.0, 10.0], dAmplitude=10, dT1=0.1, 
                                                    dT2=0.5, dFrequency=10.0, crlTargets=[Node(1516)])
JPT.Debugger(loadcondition)
```
