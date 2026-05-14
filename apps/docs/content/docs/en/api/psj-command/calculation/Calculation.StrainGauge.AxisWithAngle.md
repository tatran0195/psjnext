---
title: "Calculation.StrainGauge.AxisWithAngle()"
description: "Display stress/strain data for an input rotation angle from the first defined axis on a plane consisting of two axes"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Calculation > StrainGauge > AxisWithAngle"
macro _link: "[CmdAddStrainGaugeAxisAngle](../../macro/calculation/CmdAddStrainGaugeAxisAngle)"
---

## Description

Display stress/strain data for an input rotation angle from the first defined axis on a plane consisting of two axes.

## Syntax

```psj
Calculation.StrainGauge.AxisWithAngle(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[Integer] @optional @default:[] -->
### `ilNodeIDs`

- The IDs of the selected nodes.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iAxis1`

- The first axis from maximum principal stress, minimum principal stress, and middle principal stress.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iAxis2`

- The second axis from the minimum principal stress and the middle principal stress.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dAngle`

- The value of rotation angle.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dWidth`

- The width of the selection when the node is picked.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dLength`

- The length of the selection when the node is picked.

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

```psj {27}
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
