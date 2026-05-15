---
title: "ACModeling.Create.Convex()"
description: "Create Convex In Boundary"
version _introduced: "5.0.1"
available _versions: "all"
ribbon: "ACModeling > Create > Convex"
---

## Description

Create Convex In Boundary

## Syntax

```psj
ACModeling.Create.Convex(...)
```

## Inputs

<!-- @since:5.0.1 @optional -->
### crlParts

- Specify the part.
- The default value is \[].

<!-- @since:5.0.1 @optional -->
### dMeshSize

- Specify the mesh size.
- The default value is 0.005.

<!-- @since:5.0.1 @optional -->
### dOffset

- Specify the offset.
- The default value is 0.02.

<!-- @since:5.0.1 @optional -->
### dRadius

- Specify the radius.
- The default value is 0.02.

<!-- @since:5.0.1 @optional -->
### iDAxisGround

- Specify the axis ground.
- The default value is 0.

<!-- @since:5.0.1 @optional -->
### dScale

- Specify the scale.
- The default value is 0.001.

## Return Code

A String of 1 if success, or 0 if fail.

## Sample Code

```psj
ACModeling.Create.Convex(crlParts=[], dMeshSize=0.005, dOffset=0.02, dRadius=0.02, iDAxisGround=0, dScale=0.001)
```
