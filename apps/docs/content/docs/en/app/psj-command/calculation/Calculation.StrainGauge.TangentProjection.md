---
title: "Calculation.StrainGauge.TangentProjection()"
description: "Display the tangential strain at each node"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Calculation > StrainGauge > TangentProjection"
macro_link: "[CmdAddStrainGaugeTangentProject](../../macro/calculation/CmdAddStrainGaugeTangentProject)"
---

## Description

Display the tangential strain at each node.

## Syntax

```psj
Calculation.StrainGauge.TangentProjection(...)
```

## Inputs

### `ilNodeIDs` @type(List\[Integer]) @default(\[])

- The IDs of the selected nodes.

### `dWidth` @type(Double) @default(0.0)

- The width of the selection when the node is picked.

### `dLength` @type(Double) @default(0.0)

- The length of the selection when the node is picked.

### `iOriginalDirection` @type(Integer) @default(0)

- The original direction which is selected from maximum principal stress, minimum principal stress, X-axis, Y-axis, and Z-axis.

### `dAngle` @type(Double) @default(0.0)

- The value of rotation angle.

### `dVectorSize` @type(Double) @default(1.0)

- The vector size.

### `dAmendFactor` @type(Double) @default(1.0)

- The coefficient for correction that is used for strain analysis results.

### `strGaugeName` @type(String) @default("")

- Gauge name.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {26-27}
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
                postDataOp=PostDataOp(iResultLocation=1,
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

# StrainGauge > TangentProjection
Calculation.StrainGauge.TangentProjection(ilNodeIDs=[110], dWidth=0.005, dLength=0.01,
                                        iOriginalDirection=2, dAmendFactor=2.0)
```
