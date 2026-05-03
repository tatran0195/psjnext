---
title: "Calculation.PeakSearchUpdateViewSetting()"
description: "Update the view setting of peak search"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Calculation > PeakSearchUpdateViewSetting"
macro_link: ""
---

## Description

Update the view setting of peak search.

## Syntax

```psj
Calculation.PeakSearchUpdateViewSetting(...)
```

## Inputs

### `bRangeMax` @type(Boolean) @default(False)

- Whether to display only the notes that are less or equal to the specified value.

### `bRangeMin` @type(Boolean) @default(False)

- Whether to display only the notes that are greater or equal to the specified value.

### `bFlagVisibleGroupOnly` @type(Boolean) @default(False)

- Whether to display only peaks on the currently visible part.

### `bFlagVisibleAreaOnly` @type(Boolean) @default(False)

- Whether to display only peaks within the visible region shown in the result window. Peaks outside the region or on the reverse side are hidden.

### `bFlagMaxPrincipalStress` @type(Boolean) @default(False)

- Whether to display the maximum principal stress value on the notes.

### `bFlagMinPrincipalStress` @type(Boolean) @default(False)

- Whether to display the minimum principal stress value on the notes.

### `bVectorMaxPrincipalStress` @type(Boolean) @default(False)

- Whether to display the maximum principal stress vector.

### `bVectorMinPrincipalStress` @type(Boolean) @default(False)

- Whether to display the minimum principal stress vector.

### `bDisplayPeakNum` @type(Boolean) @default(False)

- Whether to display the number of peaks.

### `bDisplaySearchOptions` @type(Boolean) @default(False)

- Whether to display the parameters used.

### `bFlagColor` @type(Boolean) @default(False)

- Whether to change the note color base on the condition.

### `bRefreshFlag` @type(Boolean) @default(False)

- Whether to refresh the notes.

### `dRangeMax` @type(Double) @default(0.0)

- The maximum range value.

### `dRangeMin` @type(Double) @default(0.0)

- The minimum range value.

### `iColorType` @type(Integer) @default(0)

- The method to display the note color.
  - 0: Singular Points
  - 1: Principal Stress
  - 2: User Input

### `colSingular` @type(Class of COLOR\_SINGULAR) @default(COLOR\_SINGULAR)

- The color for each load point, constraint point, rigid element connection point, and material boundary point.

### `colPrincipal` @type(Class of COLOR\_PRINCIPAL) @default(COLOR\_PRINCIPAL)

- Note color based on the maximum/minimum principal stress relationship.

### `colUser` @type(Class of COLOR\_USER) @default(COLOR\_USER)

- The user input color.

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {30-33}
# Prepare result model
samplePath = JPT.GetProgramPath() + "SampleData\\Post\\Static_Renkon.op2"
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
view_setting = Calculation.PeakSearchUpdateViewSetting(
  bFlagVisibleAreaOnly=True, 
  bVectorMaxPrincipalStress=True, 
  bFlagColor=True)
print(view_setting)
```
