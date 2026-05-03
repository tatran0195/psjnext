---
title: "Calculation.Subcase.PeakHold()"
description: "Create a subcase with the maximizes stress, MISES stress, beam MAX, MIN, and AXILAL from two or more selected subcases"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Calculation > Subcase > PeakHoldEX"
macro_link: "[PostToolsSubcasePeakHoldEx](../../macro/calculation/PostToolsSubcasePeakHoldEx)"
---

## Description

Create a subcase with the maximizes stress, MISES stress, beam MAX, MIN, and AXILAL from two or more selected subcases.

## Syntax

```psj
Calculation.Subcase.PeakHold(...)
```

## Inputs

### `iAnalysisType` @type(Integer) @default(1)

- The analysis type.

### `bFatigue` @type(Boolean) @default(False)

- Whether to use the fatigue calculation.

### `dQb` @type(Double) @default(270.0)

- The tension strength of the materia

### `dQw` @type(Double) @default(130.0)

- The material fatigue limit.

### `dQy` @type(Double) @default(165.0)

- The yield stress of the material.

### `strSubcaseName` @type(String) @default("Subcase1PeakHold")

- The name of new subcase to be created.

### `iSubcaseID` @type(Integer) @default(1)

- The ID of new subcase to be created.

### `mapPeakHoldSubcases` @type(Map of PEAKHOLD\_SUBCASE\_MAP) @default(PEAKHOLD\_SUBCASE\_MAP())

- The selected subcases to create peakhold results.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {6-10}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103_solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# Subcase.RelativeOffset
peakHold = Calculation.Subcase.PeakHold(iAnalysisType=2, 
                                        strSubcaseName="Subcase 11 Peak Hold",
                                        iSubcaseID=11, 
                                        mapPeakHoldSubcases=[PEAKHOLD_SUBCASE_MAP(
                                        iResultSet=1, 
                                        listSubcaseIDs=[1, 2, 3, 4, 5])])
JPT.Debugger(peakHold)
Post.ShowContour(crPostJob=TSVPostJob(1), 
                lContourSettings=[PostContourSetting(postResultKey=PostResultKey(
                iAnalysisType=2,
                iAnalysisID=1, 
                iResultSet=11, 
                iTimeStep=11, 
                strResultName="Displacement",
                strResultCompName="Translational", 
                iResultPos=1), 
                postDataOp=PostDataOp(iResultLocation=1, iOptionCoord=1))])
Post.EnableMiddleNodes()
Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                    postResultKey=PostResultKey(
                    iAnalysisType=2, 
                    iAnalysisID=1, 
                    iResultSet=11, 
                    iTimeStep=11, 
                    strResultName="Displacement", 
                    strResultCompName="Translational"))
```
