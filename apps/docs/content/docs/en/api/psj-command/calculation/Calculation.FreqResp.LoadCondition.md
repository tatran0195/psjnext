---
title: "Calculation.FreqResp.LoadCondition()"
description: "Set the steady-state excitation input for frequency response"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Calculation > FreqResp > LoadCondition"
macro _link: "[DYNAMIC _FREQ _ANALYSIS _LOAD](../../macro/calculation/DYNAMIC _FREQ _ANALYSIS _LOAD)"
---

## Description

Set the steady-state excitation input for frequency response.

## Syntax

```psj
Calculation.FreqResp.LoadCondition(...)
```

## Inputs

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crTargetAnalysis`

- The target analysis. A new analysis is created if this parameter is set as None.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crCoordinate`

- The output coordinate system.

<!-- @since:5.1.0 @type:String @optional @default:"FRQLOAD1" -->
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

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bUnitLoad`

- Whether to create a load and load case under the condition that each selected node is subjected to unit vibration.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bCentrifugalForce`

- Whether to use the centrifugal force.

<!-- @since:5.1.0 @type:List[Cursor] @required -->
### `crlTargets`

- The selected nodes which can be assigned the load condition.

<!-- @since:5.1.0 @type:Cursor @optional @default:None -->
### `crEdit`

- An existing load condition
  - If this parameter is used, the specified load condition will be modified.
  - If it is left None, a new load condition will be created.

## Return Code

A _Cursor_ specifying the created frequency load condition.

## Sample Code

```psj {6-7}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\plate _eigen.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# Create a load condition
loadCondition = Calculation.FreqResp.LoadCondition(strName="FRQLoad _1", iLoadDirection=2, dlForce=[0.0, 0.0, 10.0], 
                                                    dAmplitude=10.0, crlTargets=[Node(1516)])
JPT.Debugger(loadCondition)
```
