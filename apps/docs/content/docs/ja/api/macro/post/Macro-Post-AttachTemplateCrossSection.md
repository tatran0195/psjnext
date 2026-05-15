---
title: "AttachTemplateCrossSection()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Attach setting of cross section to specified template.

## Syntax

```psj
AttachTemplateCrossSection(string NewTemplateName, bool Capping, bool CuttingEdge, bool SectionElem, bool Meshline, bool Show, bool Flip, bool BoxView, bool Tranparency, double PercentTranparency, color Tranparncy, float [] Matrix, vector Pos, vector PrevPos, vector RotationCenter, vector DirectAngle, float Size, float PlnSize, float BoxSize)
```

## Inputs

<!-- @since:5.0.1 -->
### 1 string

Template name

<!-- @since:5.0.1 -->
### 2 bool

Capping flag.

<!-- @since:5.0.1 -->
### 3 bool

Cutting Edge flag.

<!-- @since:5.0.1 -->
### 4 bool

Section Elemments flag.

<!-- @since:5.0.1 -->
### 5 bool

Mesh Line flag.

<!-- @since:5.0.1 -->
### 6 bool

Show flag.

<!-- @since:5.0.1 -->
### 7 bool

Flip flag.

<!-- @since:5.0.1 -->
### 8 bool

Box view flag.

<!-- @since:5.0.1 -->
### 9 bool

Tranparency flag.

<!-- @since:5.0.1 -->
### 10 double

Percent of tranparency.

<!-- @since:5.0.1 -->
### 11 color

Color of tranparncy.

<!-- @since:5.0.1 -->
### 12 float \[]

Transform matrix of cross section.

<!-- @since:5.0.1 -->
### 13 vector

Position x,y,z.

<!-- @since:5.0.1 -->
### 14 vector

Previous position x,y,z.

<!-- @since:5.0.1 -->
### 15 vector

Rotation center x,y,z.

<!-- @since:5.0.1 -->
### 16 vector

Direct angle.

<!-- @since:5.0.1 -->
### 17 float

Size.

<!-- @since:5.0.1 -->
### 18 float

Pln size.

<!-- @since:5.0.1 -->
### 19 float

Box size.

## Return Code

- "1": Succeeded.
- "0": Failed.

## Sample Code

```psj
AttachTemplateCrossSection("My Template", 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, [-1, 0, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 1], [1e-10, 1e-10, 1e-10], [0, 0, 0], [1e-10, 1e-10, 1e-10], [0, 0, 0], 0.25, 0.2, 0.025)
```
