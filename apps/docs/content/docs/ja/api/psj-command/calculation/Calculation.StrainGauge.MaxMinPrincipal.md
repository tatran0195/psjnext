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
### dAmendFactor

- Specify the coefficient for correction that is used for strain analysis results.
- The default value is 1.0.

<!-- @since:5.1.0 @optional -->
### strGaugeName

- Specify the gauge name.
- The default value is "".

<!-- @since:5.1.0 @optional -->
### bMaxMin

- Specify whether to use of maximum or minimum direction.
- The default value is _True_.

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
