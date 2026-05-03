---
title: "Calculation.StrainGauge.MaxMinPrincipal()"
description: "Display stress or strain in the direction of the maximum or minimum principle stress"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Calculation > StrainGauge > MaxMinPrincipal"
macro_link: "[CmdAddStrainGaugeMaxPrincipal](../../macro/calculation/CmdAddStrainGaugeMaxPrincipal)"
---

## Description

Display stress or strain in the direction of the maximum or minimum principle stress

## Syntax

```psj
Calculation.StrainGauge.MaxMinPrincipal(...)
```

## Inputs

### `ilNodeIDs` @type(List\[Integer]) @default(\[])

- The IDs of the selected nodes.

### `dWidth` @type(Double) @default(0.0)

- The width of the selection when the node is picked.

### `dLength` @type(Double) @default(0.0)

- The length of the selection when the node is picked.

### `dAmendFactor` @type(Double) @default(1.0)

- The coefficient for correction that is used for strain analysis results.

### `strGaugeName` @type(String) @default("")

- The gauge name.

### `bMaxMin` @type(Boolean) @default(True)

- Whether to use of maximum or minimum direction.

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

# StrainGauge > MaxMinPrincipal
Calculation.StrainGauge.MaxMinPrincipal(ilNodeIDs=[129,110], dWidth=0.005, dLength=0.01, bMaxMin=True)
```
