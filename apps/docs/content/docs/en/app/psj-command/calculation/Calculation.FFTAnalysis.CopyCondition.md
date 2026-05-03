---
title: "Calculation.FFTAnalysis.CopyCondition()"
description: "Create a copy of the specified FFT condition"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Calculation > FFTAnalysis > CopyCondition"
macro_link: ""
---

## Description

Create a copy of the specified FFT condition.

## Syntax

```psj
Calculation.FFTAnalysis.CopyCondition(...)
```

## Inputs

### `crPostFFTCondition` @type(Cursor) @required

- FFT Condition.

## Return Code

- A _Boolean_ specifying whether the function succeeded or not.
  - True: Succeeded.
  - False: Failed.

## Sample Code

```psj {5}
# This code needs PostFFTCondition by using 
# Calculation.FFTAnalysis.SetCondition. 
# i.e.
# firstBore=Calculation.FFTAnalysis.SetCondition(...)

Calculation.FFTAnalysis.CopyCondition(crPostFFTCondition=firstBore)
```
