---
title: "Calculation.StrainGauge.TwoPoints()"
description: "Display stress and strain in the direction connecting two points"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Calculation > StrainGauge > TwoPoints"
macro _link: "[CmdAddStrainGauge2Nodes](../../macro/calculation/CmdAddStrainGauge2Nodes)"
---

## Description

Display stress and strain in the direction connecting two points.

## Syntax

```psj
Calculation.StrainGauge.TwoPoints(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### iNodeID

- Specify the ID of the 1st selected node. This argument can be used for both 2Nodes or Node-Point selection methods.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iNodeID2

- Specify the ID of the 2nd selected node. This argument was used incase of the selection method is 2Nodes.
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### dlPosition

- Specify the coordinate of the selected Point. This argument was used incase of the selection method is Node-Point.
- The default value is \[0.0,0.0,0.0].

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

# StrainGauge > TwoPoints
Calculation.StrainGauge.TwoPoints(iNodeID=110, iNodeID2=111, dWidth=0.005, dLength=0.01)
```
