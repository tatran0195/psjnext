---
title: "Calculation.StrainGauge.ExistingResult()"
description: "Obtain the strain in the vector direction of the existing result"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Calculation > StrainGauge > ExistingResult"
macro _link: "[CmdAddStrainGaugeExistingResult](../../macro/calculation/CmdAddStrainGaugeExistingResult)"
---

## Description

Obtain the strain in the vector direction of the existing result.

## Syntax

```psj
Calculation.StrainGauge.ExistingResult(...)
```

## Inputs

<!-- @since:5.1.0 @type:List[Integer] @optional @default:[] -->
### `ilNodeIDs`

- The IDs of the selected nodes.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iAnalysisType`

- The analysis type.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iResultSet`

- The result set.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iTimeStep`

- The time step.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iResultType`

- The result type.

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
                strResultName="Stress", 
                strResultCompName="XY", 
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
                    strResultName="Stress", 
                    strResultCompName="XY"))

# StrainGauge > ExistingResult
Calculation.StrainGauge.ExistingResult(ilNodeIDs=[109], iAnalysisType=2, iResultType=6, dWidth=0.005, dLength=0.01)
```
