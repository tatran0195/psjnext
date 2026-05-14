---
title: "Calculation.StrainGauge.MaxMinPrincipal()"
description: "Display stress or strain in the direction of the maximum or minimum principle stress"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Calculation > StrainGauge > MaxMinPrincipal"
macro _link: "[CmdAddStrainGaugeMaxPrincipal](../../macro/calculation/CmdAddStrainGaugeMaxPrincipal)"
---

## Description

Display stress or strain in the direction of the maximum or minimum principle stress

## Syntax

```psj
Calculation.StrainGauge.MaxMinPrincipal(...)
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

<!-- @since:5.1.0 @type:Double @optional @default:1.0 -->
### `dAmendFactor`

- The coefficient for correction that is used for strain analysis results.

<!-- @since:5.1.0 @type:String @optional @default:"" -->
### `strGaugeName`

- The gauge name.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bMaxMin`

- Whether to use of maximum or minimum direction.

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

# StrainGauge > MaxMinPrincipal
Calculation.StrainGauge.MaxMinPrincipal(ilNodeIDs=[129,110], dWidth=0.005, dLength=0.01, bMaxMin=True)
```
