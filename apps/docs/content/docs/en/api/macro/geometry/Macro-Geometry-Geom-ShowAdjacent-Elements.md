---
title: "Geom _ShowAdjacent _Elements()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Select element(s) then it results in the Adjacent elements with the given constraints

## Syntax

```psj
Geom _ShowAdjacent _Elements(double stopAngle,bool IncludeStopFace,int Layer,bool IsPreview,
    Cursor[] startFaceCursor,Cursor[] stopFaceCursor)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Double

```
Stop Angle value
```

<!-- @since:5.0.1 -->
### 2. Bool

```
Value of whether stop elem has to be included or not
```

<!-- @since:5.0.1 -->
### 3. Int

```
number of Layers
```

<!-- @since:5.0.1 -->
### 4. Bool

```
Whether the result is preview or Run
```

<!-- @since:5.0.1 -->
### 5. Cursor\[]

```
List of Start elements cursor([11:Elem ID])
```

<!-- @since:5.0.1 -->
### 6. Cursor\[]

```
List of Stop elements cursor([11:Elem ID])
```

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code
