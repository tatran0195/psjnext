---
title: "Calculation.Subcase.RelativeOffset()"
description: "Create a subcase of relative displacement with zero displacement for any selected nodal ID"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Calculation > Subcase > RelativeOffset"
macro _link: "[PostToolsSubcaseRelativeOffset](../../macro/calculation/PostToolsSubcaseRelativeOffset)"
---

## Description

Create a subcase of relative displacement with zero displacement for any selected nodal ID.

## Syntax

```psj
Calculation.Subcase.RelativeOffset(...)
```

## Inputs

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iAnalysisType`

- The analysis type.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iResultSet`

- The result set.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iTimeStep`

- The time step.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iNodeID`

- The ID of the selected node.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iSubcaseID`

- The ID of the subcase to be created.

<!-- @since:5.1.0 @type:String @optional @default:"Subcase1PeakHold" -->
### `strSubcaseName`

- The name of subcase to be created.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {6-7}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103 _solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# Subcase.RelativeOffset
relativeOffset = Calculation.Subcase.RelativeOffset(iAnalysisType=2, iTimeStep=1, iNodeID=133, iSubcaseID=11, \
                                                    strSubcaseName="Relative Offset 11  Subcase 1")
JPT.Debugger(relativeOffset)
Post.ShowContour(crPostJob=TSVPostJob(1), 
                lContourSettings=[PostContourSetting(postResultKey=PostResultKey(iAnalysisType=2, \
                iResultSet=1, iTimeStep=11, strResultName="Displacement", strResultCompName="Translational", \
                iResultPos=1), postDataOp=PostDataOp(iResultLocation=1, iOptionCoord=1))])
```
