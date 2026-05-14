---
title: "Calculation.AcousticAnalysis.ACCombinedAnimation()"
description: "Perform the animation with physical quantities that select deformation, contour color, and vector separately"
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Calculation > AcousticAnalysis > ACCombinedAnimation"
macro _link: "[ACCombinedAnimation](../../macro/calculation/ACCombinedAnimation)"
---

## Description

Perform the animation with physical quantities that select deformation, contour color, and vector separately.

## Syntax

```psj
Calculation.AcousticAnalysis.ACCombinedAnimation(...)
```

## Inputs

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iTimeStep`

- The time step.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iAnalysisType`

- The analysis type.

<!-- @since:5.1.0 @type:String @optional @default:"FluidPressure" -->
### `strName`

- The subcase name.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bDeformation`

- Whether to use the deformation result.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bContour`

- Whether to display the contour.

<!-- @since:5.1.0 @type:Boolean @optional @default:True -->
### `bVector`

- Whether to display the vector.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iContour`

- The contour option.
  - 0: Fluid Pressure
  - 1: Acoustic Intensity Normal

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iVector`

- The vector option.
  - 0: Fluid Velocity
  - 1: Instantaneous Intensity

## Return Code

- A _Boolean_ specifying whether the process is executed successfully or not:
  - _True_: The process is executed successfully.
  - _False_: Cannot execute the function.

## Sample Code

```psj {8}
# Please set path to your sample Nastran Vibro-Acoustic file.
filePath="C:/Temp/Sample.op2"

# Prepare result model
Home.ImportResults.Nastran(strPath=filePath, dFaceAngle=60.16, dEdgeAngle=60.16, bIsVibro=True)

# AcousticAnalysis.ACCombinedAnimation
Calculation.AcousticAnalysis.ACCombinedAnimation(iTimeStep=2, iAnalysisType=4, strName="Subcase 201")
Post.ShowContour(crPostJob=TSVPostJob(1), 
                lContourSettings=[PostContourSetting(postResultKey=PostResultKey(
                iAnalysisType=4, 
                iResultSet=201, 
                iTimeStep=2, 
                strResultName="Fluid Pressure", 
                strResultCompName="P", 
                iResultPos=1), 
                postDataOp=PostDataOp(
                iResultLocation=1, 
                iOptionCoord=1, 
                iOptionComplex=16))])
Post.ShowDeformation(crPostJob=TSVPostJob(1), 
                    postResultKey=PostResultKey(
                    iAnalysisType=4, 
                    iResultSet=201, 
                    iTimeStep=2, 
                    strResultName="Fluid Pressure", 
                    strResultCompName="P"), 
                    postDataOption=PostDataOp(iOptionComplex=16))
```
