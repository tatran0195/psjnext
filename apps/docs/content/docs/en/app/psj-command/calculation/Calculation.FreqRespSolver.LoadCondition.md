---
title: "Calculation.FreqRespSolver.LoadCondition()"
description: "Set the steady-state excitation input for frequency response (Solver)"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Calculation > FreqRespSolver > LoadCondition"
macro_link: "[DYNAMIC_FREQ_ANALYSIS_LOAD_SOLVER](../../macro/calculation/DYNAMIC_FREQ_ANALYSIS_LOAD_SOLVER)"
---

## Description

Set the steady-state excitation input for frequency response (Solver).

## Syntax

```psj
Calculation.FreqRespSolver.LoadCondition(...)
```

## Inputs

### `iAnalysisType` @type(Integer) @default(0)

- The analysis type.

### `crTargetAnalysis` @type(Cursor) @default(None)

- The target analysis. A new analysis is created if this parameter is set as None.

### `crCoordinate` @type(Cursor) @default(None)

- The output coordinate system.

### `strName` @type(String) @default("FRQLOAD")

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

### `crlTargets` @type(List\[Cursor]) @default(\[])

- The selected nodes which can be assigned the load condition.

### `iLoadType` @type(Integer) @default(0)

- The load type.
  - 0: Force
  - 1: Displacement
  - 2: Velocity
  - 3: Acceleration

### `crEdit` @type(Cursor) @default(None)

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
loadCondition = Calculation.FreqRespSolver.LoadCondition(strName="FRQLoad_1", 
                                                        iLoadDirection=2, 
                                                        dlForce=[0.0, 0.0, 10.0], 
                                                        dAmplitude=10.0, 
                                                        crlTargets=[Node(514)])
JPT.Debugger(loadCondition) # for checking the return value
```
