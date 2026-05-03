---
title: "Calculation.AcousticAnalysis.ACCombinedAnimation()"
description: "Perform the animation with physical quantities that select deformation, contour color, and vector separately"
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Calculation > AcousticAnalysis > ACCombinedAnimation"
macro_link: "[ACCombinedAnimation](../../macro/calculation/ACCombinedAnimation)"
---

## Description

Perform the animation with physical quantities that select deformation, contour color, and vector separately.

## Syntax

```psj
Calculation.AcousticAnalysis.ACCombinedAnimation(...)
```

## Inputs

### `iTimeStep` @type(Integer) @default(1)

- The time step.

### `iAnalysisType` @type(Integer) @default(1)

- The analysis type.

### `strName` @type(String) @default("FluidPressure")

- The subcase name.

### `bDeformation` @type(Boolean) @default(True)

- Whether to use the deformation result.

### `bContour` @type(Boolean) @default(True)

- Whether to display the contour.

### `bVector` @type(Boolean) @default(True)

- Whether to display the vector.

### `iContour` @type(Integer) @default(0)

- The contour option.
  - 0: Fluid Pressure
  - 1: Acoustic Intensity Normal

### `iVector` @type(Integer) @default(0)

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
