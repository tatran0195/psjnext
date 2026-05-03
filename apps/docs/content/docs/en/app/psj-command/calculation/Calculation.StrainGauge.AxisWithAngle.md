---
title: "Calculation.StrainGauge.AxisWithAngle()"
description: "Display stress/strain data for an input rotation angle from the first defined axis on a plane consisting of two axes"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Calculation > StrainGauge > AxisWithAngle"
macro_link: "[CmdAddStrainGaugeAxisAngle](../../macro/calculation/CmdAddStrainGaugeAxisAngle)"
---

## Description

Display stress/strain data for an input rotation angle from the first defined axis on a plane consisting of two axes.

## Syntax

```psj
Calculation.StrainGauge.AxisWithAngle(...)
```

## Inputs

### `ilNodeIDs` @type(List\[Integer]) @default(\[])

- The IDs of the selected nodes.

### `iAxis1` @type(Integer) @default(0)

- The first axis from maximum principal stress, minimum principal stress, and middle principal stress.

### `iAxis2` @type(Integer) @default(1)

- The second axis from the minimum principal stress and the middle principal stress.

### `dAngle` @type(Double) @default(0.0)

- The value of rotation angle.

### `dWidth` @type(Double) @default(0.0)

- The width of the selection when the node is picked.

### `dLength` @type(Double) @default(0.0)

- The length of the selection when the node is picked.

### `dAmendFactor` @type(Double) @default(1.0)

- The coefficient for correction that is used for strain analysis results.

### `strGaugeName` @type(String) @default("")

- The gauge name.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {27}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)
# Plot the result
Post.ShowContour(crPostJob=TSVPostJob(1), 
                lContourSettings=[PostContourSetting(postResultKey=PostResultKey(
                iAnalysisType=2, 
                iResultSet=1, 
                iTimeStep=2, 
                strResultName="Strain", 
                strResultCompName="Solid Max Principal Strain", 
                iResultPos=4), 
                postDataOp=PostDataOp(
                iResultLocation=1, 
                iOptionCoord=1, 
                iOptionConversion=1, 
                iOptionContinuous=8))])
Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                    postResultKey=PostResultKey(
                    iAnalysisType=2, 
                    iResultSet=1, 
                    iTimeStep=2, 
                    strResultName="Strain", 
                    strResultCompName="Solid Max Principal Strain"))

# StrainGauge > AxisWithAngle
Calculation.StrainGauge.AxisWithAngle(ilNodeIDs=[110, 113], dAngle=30.0, dWidth=0.005, dLength=0.01)
```
