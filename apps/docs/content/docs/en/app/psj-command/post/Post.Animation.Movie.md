---
title: "Post.Animation.Movie()"
description: "Export animation as a movie file."
version_introduced: "5.1.0"
available_versions: "all"
ribbon: "Post > Animation > Movie"
macro_link: "[CmdPostAnimationExportMovieToFile](../../macro/post/CmdPostAnimationExportMovieToFile)"
---

## Description

Export animation as a movie file.

## Syntax

```psj
Post.Animation.Movie(...)
```

## Inputs

### `strFilePath` @type(String) @default('')

- Path of movie file including extension indicates file format.

### `strEncoder` @type(String) @default('h264')

- Encoder. This option can use if movie type is mpeg4.

### `iFPS` @type(Integer) @default(8)

- FPS.

### `iRepeat` @type(Integer) @default(1)

- Repeat number.

### `bMakeImage` @type(Boolean) @default(False)

- Whether or not export every frames of the movie to image files.

### `iWidth` @type(Integer) @default(1920)

- Width of export movie.

### `iHeight` @type(Integer) @default(1080)

- Height of export movie.

### `iBackGroundColor` @type(Integer) @default(0)

- Background color.
  - 0: Use current background color.
  - 1: Set background color to White.
  - 2: Set backgroun color to transparent (only if .gif movie).

### `bOptimized` @type(Boolean) @default(False)

- Whether or not using Optimization Toolkit.

## Return Code

A _Boolean_ specifying succeeded or failed.

## Sample Code

```psj{25-31}
import os

samplePath = os.path.join(JPT.GetProgramPath(),r"SampleData\PSJ\PSJ-Utility\PostSample\101_solid.op2")
Home.ImportResults.Nastran(strPath=samplePath)

# Show contour
Post.ShowContour(
    crPostJob=TSVPostJob(1), 
    lContourSettings=[
        PostContourSetting(
            postResultKey=PostResultKey(
                iAnalysisType=1, iResultSet=1, iTimeStep=1, strResultName="Displacement", 
                strResultCompName="Translational", iResultPos=1), 
                postDataOp=PostDataOp(iResultLocation=1, iOptionCoord=1))])

Post.ShowDeformation(
    crPostJob=TSVPostJob(1), 
    postResultKey=PostResultKey(
        iAnalysisType=1, iResultSet=1, iTimeStep=1, strResultName="Displacement", strResultCompName="Translational"))
Post.EnableMiddleNodes()

temp_folder=JPT.GetAppPathInfo(JPT.PathType.TEMP_PATH)
outputPath = os.path.join(temp_folder,"101_solid_movie.mp4")

Post.Animation.Movie(
    strFilePath=outputPath, 
    strEncoder="h264", 
    iFPS=8, 
    iRepeat=1, 
    iWidth=882, 
    iHeight=441)
```
