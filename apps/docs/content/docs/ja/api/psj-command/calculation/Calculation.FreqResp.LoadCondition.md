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

<!-- @since:5.1.0 @optional -->
### crTargetAnalysis

- Specify the target analysis. A new analysis is created if this parameter is set as None.
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### crCoordinate

- Specify the output coordinate system.
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### strName

- Specify the name of load condition to be created.
- The default value is "FRQLOAD1".

<!-- @since:5.1.0 @optional -->
### iLoadDirection

- Specify the direction of vibration.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### dlForce

- Specify the vector of vibration force.
- The default value is \[1,0,0].

<!-- @since:5.1.0 @optional -->
### dAmplitude

- Specify the amplitude of vibration force.
- The default value is 1.0.

<!-- @since:5.1.0 @optional -->
### dDelay

- Specify the value of time delay (seconds).
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### dPhase

- Specify the value of phase delay (angle).
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### bBf

- Specify whether to use frequency-dependent load as Table input.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### dBf

- Specify the value of frequency-dependent load (Bf).
- The default value is 1.0.

<!-- @since:5.1.0 @optional -->
### crBfCurve

- Specify the field data of frequency-dependent load.
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### bFf

- Specify whether to use frequency-dependent phase as Table input.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### dFf

- Specify the value of Frequency-dependent phase.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### crFfCurve

- Specify the field data of frequency-dependent phase.
- The default value is _None_.

<!-- @since:5.1.0 @optional -->
### bUnitLoad

- Specify whether to create a load and load case under the condition that each selected node is subjected to unit vibration.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### bCentrifugalForce

- Specify whether to use the centrifugal force.
- The default value is _False_.

<!-- @since:5.1.0 @required -->
### crlTargets

- Specify the selected nodes which can be assigned the load condition.

<!-- @since:5.1.0 @optional -->
### crEdit

- Specify an existing load condition
  - If this parameter is used, the specified load condition will be modified.
  - If it is left None, a new load condition will be created.
- The default value is _None_.

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
