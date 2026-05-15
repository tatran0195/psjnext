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

<!-- @since:5.1.0 @optional -->
### iTimeStep

- Specify the time step.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### iAnalysisType

- Specify the analysis type.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### strName

- Specify the subcase name.
- The default value is "FluidPressure".

<!-- @since:5.1.0 @optional -->
### bDeformation

- Specify whether to use the deformation result.
- The default value is _True_.

<!-- @since:5.1.0 @optional -->
### bContour

- Specify whether to display the contour.
- The default value is _True_.

<!-- @since:5.1.0 @optional -->
### bVector

- Specify whether to display the vector.
- The default value is _True_.

<!-- @since:5.1.0 @optional -->
### iContour

- Specify the contour option.
  - 0: Fluid Pressure
  - 1: Acoustic Intensity Normal
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### iVector

- Specify the vector option.
  - 0: Fluid Velocity
  - 1: Instantaneous Intensity
- The default value is 0.

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
