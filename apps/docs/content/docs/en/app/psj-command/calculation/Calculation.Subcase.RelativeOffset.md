---
title: "Calculation.Subcase.RelativeOffset()"
description: "Create a subcase of relative displacement with zero displacement for any selected nodal ID"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Calculation > Subcase > RelativeOffset"
macro_link: "[PostToolsSubcaseRelativeOffset](../../macro/calculation/PostToolsSubcaseRelativeOffset)"
---

## Description

Create a subcase of relative displacement with zero displacement for any selected nodal ID.

## Syntax

```psj
Calculation.Subcase.RelativeOffset(...)
```

## Inputs

### `iAnalysisType` @type(Integer) @default(1)

- The analysis type.

### `iResultSet` @type(Integer) @default(1)

- The result set.

### `iTimeStep` @type(Integer) @default(0)

- The time step.

### `iNodeID` @type(Integer) @default(0)

- The ID of the selected node.

### `iSubcaseID` @type(Integer) @default(0)

- The ID of the subcase to be created.

### `strSubcaseName` @type(String) @default("Subcase1PeakHold")

- The name of subcase to be created.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {6-7}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
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
