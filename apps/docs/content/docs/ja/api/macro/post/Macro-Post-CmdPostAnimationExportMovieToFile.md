---
title: "CmdPostAnimationExportMovieToFile()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

Export animation

## Syntax

```psj
CmdPostAnimationExportMovieToFile(string pathName, string encoder, int fps, int repeat, bool makeImage, int width, int height, int bgcolor)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. string

The full path to the exporting animation.

<!-- @since:5.1.0 -->
### 2. string

Encoder. This option can use if movie type is mpeg4.

<!-- @since:5.1.0 -->
### 3. int

Frame Per Second.

<!-- @since:5.1.0 -->
### 4. int

Repeat.

<!-- @since:5.1.0 -->
### 5. bool

Make Image option. 0: No, 1: Yes.

<!-- @since:5.1.0 -->
### 6. int

Screen width.

<!-- @since:5.1.0 -->
### 7. int

Screen height.

<!-- @since:5.1.0 -->
### 9. int

Background color. 0: Use current background color, 1: Set background color to White, 2: Set backgroun color to transparent (only if .gif movie).

## Return Code

True: succeeded, False: failed.

## Sample Code

```psj
CmdPostAnimationExportMovieToFile("C:/Temp/animation.gif", "h264", 8, 1, 0, 1378, 708, 0)
```
