---
title: "Post.Animation.Movie()"
description: "Export animation as a movie file."
version _introduced: "5.1.0"
available _versions: "all"
ribbon: "Post > Animation > Movie"
macro _link: "[CmdPostAnimationExportMovieToFile](../../macro/post/CmdPostAnimationExportMovieToFile)"
---

## Description

Export animation as a movie file.

## Syntax

```psj
Post.Animation.Movie(...)
```

## Inputs

<!-- @since:5.1.0 @optional -->
### strFilePath

- Specify path of movie file including extension indicates file format.
- The default value is ''.

<!-- @since:5.1.0 @optional -->
### strEncoder

- Specify encoder. This option can use if movie type is mpeg4.
- The default value is 'h264'.

<!-- @since:5.1.0 @optional -->
### iFPS

- Specify FPS.
- The default value is 8.

<!-- @since:5.1.0 @optional -->
### iRepeat

- Specify repeat number.
- The default value is 1.

<!-- @since:5.1.0 @optional -->
### bMakeImage

- Specify whether or not export every frames of the movie to image files.
- The default value is _False_.

<!-- @since:5.1.0 @optional -->
### iWidth

- Specify width of export movie.
- The default value is 1920.

<!-- @since:5.1.0 @optional -->
### iHeight

- Specify height of export movie.
- The default value is 1080.

<!-- @since:5.1.0 @optional -->
### iBackGroundColor

- Specify background color.
  - 0: Use current background color.
  - 1: Set background color to White.
  - 2: Set backgroun color to transparent (only if .gif movie).
- The default value is 0.

<!-- @since:5.1.0 @optional -->
### bOptimized

- Specify whether or not using Optimization Toolkit.
- The default value is _False_.

## Return Code

A _Boolean_ specifying succeeded or failed.

## Sample Code

```pj {25-31}
import os

samplePath = os.path.join(JPT.GetProgramPath(),r"SampleData\PSJ\PSJ-Utility\PostSample\101 _solid.op2")
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

temp _folder=JPT.GetAppPathInfo(JPT.PathType.TEMP _PATH)
outputPath = os.path.join(temp _folder,"101 _solid _movie.mp4")

Post.Animation.Movie(
    strFilePath=outputPath, 
    strEncoder="h264", 
    iFPS=8, 
    iRepeat=1, 
    iWidth=882, 
    iHeight=441)
```
