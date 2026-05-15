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

<!-- @since:5.1.0 @optional -->
### iAnalysisType

- Specify the analysis type.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### bFatigue

- Specify whether to use the fatigue calculation.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### dQb

- Specify the tension strength of the materia
- The default value is 270.0.

<!-- @since:5.1.0 @optional -->
### dQw

- Specify the material fatigue limit.
- The default value is 130.0.

<!-- @since:5.1.0 @optional -->
### dQy

- Specify the yield stress of the material.
- The default value is 165.0.

<!-- @since:5.1.0 @optional -->
### strSubcaseName

- Specify the name of new subcase to be created.
- The default value is "Subcase1PeakHold".

<!-- @since:5.1.0 @optional -->
### iSubcaseID

- Specify the ID of new subcase to be created.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### mapPeakHoldSubcases

- Specify the selected subcases to create peakhold results.
- The default value is PEAKHOLD\_SUBCASE\_MAP().

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
