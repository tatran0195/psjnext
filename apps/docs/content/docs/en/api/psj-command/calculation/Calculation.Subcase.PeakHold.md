---
title: "Calculation.Subcase.PeakHold()"
description: "Create a subcase with the maximizes stress, MISES stress, beam MAX, MIN, and AXILAL from two or more selected subcases"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Calculation > Subcase > PeakHoldEX"
macro _link: "[PostToolsSubcasePeakHoldEx](../../macro/calculation/PostToolsSubcasePeakHoldEx)"
---

## Description

Create a subcase with the maximizes stress, MISES stress, beam MAX, MIN, and AXILAL from two or more selected subcases.

## Syntax

```psj
Calculation.Subcase.PeakHold(...)
```

## Inputs

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iAnalysisType`

- The analysis type.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bFatigue`

- Whether to use the fatigue calculation.

<!-- @since:5.1.0 @type:Double @optional @default:270.0 -->
### `dQb`

- The tension strength of the materia

<!-- @since:5.1.0 @type:Double @optional @default:130.0 -->
### `dQw`

- The material fatigue limit.

<!-- @since:5.1.0 @type:Double @optional @default:165.0 -->
### `dQy`

- The yield stress of the material.

<!-- @since:5.1.0 @type:String @optional @default:"Subcase1PeakHold" -->
### `strSubcaseName`

- The name of new subcase to be created.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iSubcaseID`

- The ID of new subcase to be created.

<!-- @since:5.1.0 @type:Map of PEAKHOLD _SUBCASE _MAP @optional @default:PEAKHOLD _SUBCASE _MAP() -->
### `mapPeakHoldSubcases`

- The selected subcases to create peakhold results.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {6-10}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\PSJ\\PSJ-Utility\\PostSample\\103 _solid.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)

# Subcase.RelativeOffset
peakHold = Calculation.Subcase.PeakHold(iAnalysisType=2, 
                                        strSubcaseName="Subcase 11 Peak Hold",
                                        iSubcaseID=11, 
                                        mapPeakHoldSubcases=[PEAKHOLD _SUBCASE _MAP(
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
