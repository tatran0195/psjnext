---
title: "Calculation.TransResp.LoadCondition()"
description: "Set the arbitrary excitation input for transient response"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Calculation > TransResp > LoadCondition"
macro_link: "[DYNAMIC_TRANS_ANALYSIS_LOAD](../../macro/calculation/DYNAMIC_TRANS_ANALYSIS_LOAD)"
---

## Description

Set the arbitrary excitation input for transient response.

## Syntax

```psj
Calculation.TransResp.LoadCondition(...)
```

## Inputs

### `crTargetAnalysis` @type(Cursor) @default(None)

- The target analysis. A new analysis is created if this parameter is set as None.

### `crCoordinate` @type(Cursor) @default(None)

- The coordinate system.

### `strName` @type(String) @default("TRNLoad1")

- The name of load condition to be created.

### `iLoadType` @type(Integer) @default(0)

- The load type.
  - 0: Table(TLOAD1)
  - 1: Cosine(TLOAD2)

### `iLoadDirection` @type(Integer) @default(0)

- The direction of vibration.
  - 0: X
  - 1: Y
  - 2: Z
  - 3: RX
  - 4: RY
  - 5: RZ
  - 6: Normal

### `dlForce` @type(List\[Double]) @default(\[1,0,0])

- The vector of vibration force.

### `dAmplitude` @type(Double) @default(1.0)

- The amplitude of vibration load.

### `dDelay` @type(Double) @default(0.0)

- The value of time delay (seconds).

### `dPhase` @type(Double) @default(0.0)

- The value of phase delay (angle) in load type Cosine(TLOAD2).

### `bFt` @type(Boolean) @default(False)

- Whether to use the time history load as inputted value or table.

### `dFt` @type(Double) @default(1.0)

- The value of the time history load.

### `crFtCurve` @type(Cursor) @default(None)

- The field data of the time history load.

### `dT1` @type(Double) @default(0.0)

- The vibration start time of load type Cosine(TLOAD2).

### `dT2` @type(Double) @default(1.0)

- The vibration end time of load type Cosine(TLOAD2).

### `dFrequency` @type(Double) @default(0.0)

- The value of frequency in load type Cosine(TLOAD2).

### `dExponent` @type(Double) @default(0.0)

- The value of exponential function in load type Cosine (TLOAD2).

### `dPower` @type(Double) @default(0.0)

- The value of growth factor in load type Cosine (TLOAD2).

### `crlTargets` @type(List\[Cursor]) @required

- The selected nodes which can be assigned the load condition.

### `crEdit` @type(Cursor) @default(None)

- An existing Load condition
  - If this parameter is used, the specified Load condition will be modified.
  - If it is left None, a new Load condition will be created.

## Return Code

A _Cursor_ specifying the created transient load condition.

## Sample Code

```psj {6-8}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\plate_eigen.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# Create a load condition
loadcondition = Calculation.TransResp.LoadCondition(strName="TRNLoad_2", iLoadType=1, iLoadDirection=2, 
                                                    dlForce=[0.0, 0.0, 10.0], dAmplitude=10, dT1=0.1, 
                                                    dT2=0.5, dFrequency=10.0, crlTargets=[Node(1516)])
JPT.Debugger(loadcondition)
```
