---
title: "Calculation.Gururi.LoadCondition()"
description: "Set the frequency response steady-state excitation input for the Gururi"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Calculation > Gururi > LoadCondition"
macro_link: "[DYNAMIC_FREQ_ANALYSIS_LOAD](../../macro/calculation/DYNAMIC_FREQ_ANALYSIS_LOAD)"
---

## Description

Set the frequency response steady-state excitation input for the Gururi.

## Syntax

```psj
Calculation.Gururi.LoadCondition(...)
```

## Inputs

### `crTargetAnalysis` @type(Cursor) @default(None)

- The target analysis. A new analysis is created if this parameter is set as None.

### `crCoordinate` @type(Cursor) @default(None)

- The coordinate system.

### `strName` @type(String) @default("FRQLOAD1")

- The name of load condition to be created.

### `iLoadDirection` @type(Integer) @default(0)

- The direction of vibration.

### `dlForce` @type(List\[Double]) @default(\[1,0,0])

- The vector of vibration force.

### `dAmplitude` @type(Double) @default(1.0)

- The amplitude of vibration force.

### `dDelay` @type(Double) @default(0.0)

- The value of time delay (seconds).

### `dPhase` @type(Double) @default(0.0)

- The value of phase delay (angle).

### `bBf` @type(Boolean) @default(False)

- Whether to use frequency-dependent load as Table input.

### `dBf` @type(Double) @default(1.0)

- The value of frequency-dependent load (Bf).

### `crBfCurve` @type(Cursor) @default(None)

- The field data of frequency-dependent load.

### `bFf` @type(Boolean) @default(False)

- Whether to use frequency-dependent phase as Table input.

### `dFf` @type(Double) @default(0.0)

- The value of Frequency-dependent phase.

### `crFfCurve` @type(Cursor) @default(None)

- The field data of frequency-dependent phase.

### `bUnitLoad` @type(Boolean) @default(False)

- Whether to create a load and load case under the condition that each selected node is subjected to unit vibration.

### `bCentrifugalForce` @type(Boolean) @default(False)

- Whether to use the centrifugal force.

### `crlTargets` @type(List\[Cursor]) @required

- The selected nodes which can be assigned the load condition.

### `crEdit` @type(Cursor) @default(None)

- An existing load condition
  - If this parameter is used, the specified load condition will be modified.
  - If it is left None, a new load condition will be created.

## Return Code

A _Cursor_ specifying the created gururi load condition.

## Sample Code

```psj {8-10}
# Please set path to your result sample file
samplePath = "C:/Temp/Sample.op2"

# Prepare result model
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60, dEdgeAngle=60)

# Create a load condition
loadcondition = Calculation.Gururi.LoadCondition(strName="FRQLoad_1", iLoadDirection=2, 
                                                dlForce=[0.0, 0.0, 10.0], dAmplitude=10.0, 
                                                crlTargets=[Node(501)])
JPT.Debugger(loadcondition)
```
