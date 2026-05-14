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

<!-- @since:5.1.0 @type:String @optional @default:'' -->
### `strFilePath`

- The path of movie file including extension indicates file format.

<!-- @since:5.1.0 @type:String @optional @default:'h264' -->
### `strEncoder`

- The encoder. This option can use if movie type is mpeg4.

<!-- @since:5.1.0 @type:Integer @optional @default:8 -->
### `iFPS`

- The FPS.

<!-- @since:5.1.0 @type:Integer @optional @default:1 -->
### `iRepeat`

- The repeat number.

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bMakeImage`

- Whether or not export every frames of the movie to image files.

<!-- @since:5.1.0 @type:Integer @optional @default:1920 -->
### `iWidth`

- The width of export movie.

<!-- @since:5.1.0 @type:Integer @optional @default:1080 -->
### `iHeight`

- The height of export movie.

<!-- @since:5.1.0 @type:Integer @optional @default:0 -->
### `iBackGroundColor`

- The background color.
  - 0: Use current background color.
  - 1: Set background color to White.
  - 2: Set backgroun color to transparent (only if .gif movie).

<!-- @since:5.1.0 @type:Boolean @optional @default:False -->
### `bOptimized`

- Whether or not using Optimization Toolkit.

## Return Code

A _Boolean_ specifying succeeded or failed.

## Sample Code

```psj {25-31}
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
