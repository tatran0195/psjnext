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

<!-- @since:5.1.0 @type:List[Integer] @optional @default:[] -->
### `ilNodeIDs`

- The IDs of the selected nodes.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dWidth`

- The width of the selection when the node is picked.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dLength`

- The length of the selection when the node is picked.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iOriginalDirection`

- The original direction which is selected from maximum principal stress, minimum principal stress, X-axis, Y-axis, and Z-axis.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dAngle`

- The value of rotation angle.

<!-- @since:5.1.0 @type:Double @optional @default:1.0 -->
### `dVectorSize`

- The vector size.

<!-- @since:5.1.0 @type:Double @optional @default:1.0 -->
### `dAmendFactor`

- The coefficient for correction that is used for strain analysis results.

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strGaugeName`

- The gauge name.

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
