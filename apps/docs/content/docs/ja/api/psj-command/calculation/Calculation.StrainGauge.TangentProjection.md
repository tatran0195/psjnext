---
title: "Calculation.StrainGauge.TangentProjection()"
description: "Display the tangential strain at each node"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Calculation > StrainGauge > TangentProjection"
macro _link: "[CmdAddStrainGaugeTangentProject](../../macro/calculation/CmdAddStrainGaugeTangentProject)"
---

## Description

Display the tangential strain at each node.

## Syntax

```psj
Calculation.StrainGauge.TangentProjection(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### ilNodeIDs

- Specify the IDs of the selected nodes.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### dWidth

- Specify the width of the selection when the node is picked.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### dLength

- Specify the length of the selection when the node is picked.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### iOriginalDirection

- Specify the original direction which is selected from maximum principal stress, minimum principal stress, X-axis, Y-axis, and Z-axis.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### dAngle

- Specify the value of rotation angle.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### dVectorSize

- Specify the vector size.
- The default value is 1.0.

<!-- @since:5.1.0 @optional -->
### dAmendFactor

- Specify the coefficient for correction that is used for strain analysis results.
- The default value is 1.0.

<!-- @since:5.1.0 @optional -->
### strGaugeName

- Specify gauge name.
- The default value is "".

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {26-27}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103 _solid.op2"
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
