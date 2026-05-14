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

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bRangeMax`

- Whether to display only the notes that are less or equal to the specified value.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bRangeMin`

- Whether to display only the notes that are greater or equal to the specified value.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bFlagVisibleGroupOnly`

- Whether to display only peaks on the currently visible part.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bFlagVisibleAreaOnly`

- Whether to display only peaks within the visible region shown in the result window. Peaks outside the region or on the reverse side are hidden.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bFlagMaxPrincipalStress`

- Whether to display the maximum principal stress value on the notes.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bFlagMinPrincipalStress`

- Whether to display the minimum principal stress value on the notes.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bVectorMaxPrincipalStress`

- Whether to display the maximum principal stress vector.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bVectorMinPrincipalStress`

- Whether to display the minimum principal stress vector.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bDisplayPeakNum`

- Whether to display the number of peaks.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bDisplaySearchOptions`

- Whether to display the parameters used.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bFlagColor`

- Whether to change the note color base on the condition.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bRefreshFlag`

- Whether to refresh the notes.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dRangeMax`

- The maximum range value.

<!-- @since:5.1.0 @type:Double @optional @default:0.0 -->
### `dRangeMin`

- The minimum range value.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iColorType`

- The method to display the note color.
  - 0: Singular Points
  - 1: Principal Stress
  - 2: User Input

<!-- @since:5.1.0 @type:Class of COLOR _SINGULAR @optional @default:COLOR _SINGULAR -->
### `colSingular`

- The color for each load point, constraint point, rigid element connection point, and material boundary point.

<!-- @since:5.1.0 @type:Class of COLOR _PRINCIPAL @optional @default:COLOR _PRINCIPAL -->
### `colPrincipal`

- The note color based on the maximum/minimum principal stress relationship.

<!-- @since:5.1.0 @type:Class of COLOR _USER @optional @default:COLOR _USER -->
### `colUser`

- The user input color.

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
