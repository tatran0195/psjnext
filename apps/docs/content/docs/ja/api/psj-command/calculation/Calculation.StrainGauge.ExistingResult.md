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

<!-- @since:5.1.0 @optional -->
### ilNodeIDs

- Specify the IDs of the selected nodes.
- The default value is \[].

<!-- @since:5.1.0 @optional -->
### iAnalysisType

- Specify the analysis type.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iResultSet

- Specify the result set.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### iTimeStep

- Specify the time step.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### iResultType

- Specify the result type.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### dWidth

- Specify the width of the selection when the node is picked.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### dLength

- Specify the length of the selection when the node is picked.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### dAmendFactor

- Specify the coefficient for correction that is used for strain analysis results.
- The default value is 1.0.

<!-- @since:5.1.0 @optional -->
### strGaugeName

- Specify the gauge name.
- The default value is "".

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
