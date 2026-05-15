---
title: "Calculation.PeakSearchUpdateViewSetting()"
description: "Update the view setting of peak search"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Calculation > PeakSearchUpdateViewSetting"
macro _link: ""
---

## Description

Update the view setting of peak search.

## Syntax

```psj
Calculation.PeakSearchUpdateViewSetting(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### bRangeMax

- Specify whether to display only the notes that are less or equal to the specified value.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### bRangeMin

- Specify whether to display only the notes that are greater or equal to the specified value.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### bFlagVisibleGroupOnly

- Specify whether to display only peaks on the currently visible part.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### bFlagVisibleAreaOnly

- Specify whether to display only peaks within the visible region shown in the result window. Peaks outside the region or on the reverse side are hidden.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### bFlagMaxPrincipalStress

- Specify whether to display the maximum principal stress value on the notes.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### bFlagMinPrincipalStress

- Specify whether to display the minimum principal stress value on the notes.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### bVectorMaxPrincipalStress

- Specify whether to display the maximum principal stress vector.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### bVectorMinPrincipalStress

- Specify whether to display the minimum principal stress vector.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### bDisplayPeakNum

- Specify whether to display the number of peaks.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### bDisplaySearchOptions

- Specify whether to display the parameters used.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### bFlagColor

- Specify whether to change the note color base on the condition.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### bRefreshFlag

- Specify whether to refresh the notes.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### dRangeMax

- Specify the maximum range value.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### dRangeMin

- Specify the minimum range value.
- The default value is 0.0.

<!-- @since:5.1.0 @optional -->
### iColorType

- Specify the method to display the note color.
  - 0: Singular Points
  - 1: Principal Stress
  - 2: User Input
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### colSingular

- Specify the color for each load point, constraint point, rigid element connection point, and material boundary point.
- The default value is _COLOR\_SINGULAR_.

<!-- @since:5.1.0 @optional -->
### colPrincipal

- Specify note color based on the maximum/minimum principal stress relationship.
- The default value is _COLOR\_PRINCIPAL_.

<!-- @since:5.1.0 @optional -->
### colUser

- Specify the user input color.
- The default value is _COLOR\_USER_.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {30-33}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\Post\\Static _Renkon.op2"
Home.ImportResults.Nastran(strPath = samplePath, dFaceAngle=60.16, dEdgeAngle=60.16)
# Plot the result
Post.ShowContour(
  crPostJob=TSVPostJob(1),
   lContourSettings=[PostContourSetting(postResultKey=PostResultKey(
    iAnalysisType=1, 
    iResultSet=1, 
    iTimeStep=1, 
    strResultName="Stress", 
    strResultCompName="Max Principal Stress", 
    iResultPos=4), 
   postDataOp=PostDataOp(
    iResultLocation=1, 
    iOptionCoord=1, 
    iOptionConversion=1, 
    iOptionContinuous=8))])
Post.ShowDeformation(
  crPostJob=TSVPostJob(1), 
  postResultKey=PostResultKey(
    iAnalysisType=1, 
    iResultSet=1, 
    iTimeStep=1, 
    strResultName="Stress", 
    strResultCompName="Max Principal Stress"))

# Peak search and update view settings
Calculation.PeakSearch(bStep=False, crlTargets=[Part(1)])
view _setting = Calculation.PeakSearchUpdateViewSetting(
  bFlagVisibleAreaOnly=True, 
  bVectorMaxPrincipalStress=True, 
  bFlagColor=True)
print(view _setting)
```
