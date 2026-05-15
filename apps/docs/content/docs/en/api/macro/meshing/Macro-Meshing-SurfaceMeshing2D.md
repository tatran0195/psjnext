---
title: "SurfaceMeshing2D()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Surface Meshing 2D

## Syntax

```psj
SurfaceMeshing2D(cursor[] body, meshParam param, bool use _local _setting, bool use _FMesher,
    int thread _num, bool keep _ref _data, bool mesh _color, COLOR color, bool reserved)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

body List

<!-- @since:5.0.1 -->
### 2. MeshParam::double

Avg\_Element\_Size

<!-- @since:5.0.1 -->
### 3. MeshParam::double

Max\_Element\_Size

<!-- @since:5.0.1 -->
### 4. MeshParam::double

Min\_Element\_Size

<!-- @since:5.0.1 -->
### 5. MeshParam::double

Reduction\_Factor

<!-- @since:5.0.1 -->
### 6. MeshParam::double

Geom\_Angle

<!-- @since:5.0.1 -->
### 7. MeshParam::double

Geom\_MinSize

<!-- @since:5.0.1 -->
### 8. MeshParam::double

Grading\_Factor

<!-- @since:5.0.1 -->
### 9. MeshParam::double

Min\_Stretch\_Val

<!-- @since:5.0.1 -->
### 10. MeshParam::double

Geom\_Edge\_Deviation

<!-- @since:5.0.1 -->
### 11. MeshParam::double

Geom\_Quality\_Ratio

<!-- @since:5.0.1 -->
### 12. MeshParam::double

Geom\_Count\_Ratio

<!-- @since:5.0.1 -->
### 13. MeshParam::int

Performance\_Mode 0=Fastest,1=Good Quality,2=Best Quality

<!-- @since:5.0.1 -->
### 14. MeshParam::int

Optimization\_Level 0=Disable,1=Level1,2=Level2,3=Level3,4=Level4,5=Level5

<!-- @since:5.0.1 -->
### 15. MeshParam::bool

Auto\_Merge\_Edges 0=No 1=Yes

<!-- @since:5.0.1 -->
### 16. MeshParam::bool

Auto\_Merge\_Faces 0=No 1=Yes

<!-- @since:5.0.1 -->
### 17. MeshParam::double

Auto\_MeshPattern\_MinElemAngle

<!-- @since:5.0.1 -->
### 18. MeshParam::double

Auto\_MergeTinyFaces\_Angle

<!-- @since:5.0.1 -->
### 19. MeshParam::bool

Output\_Quad\_Mesh 0=No 1=Yes

<!-- @since:5.0.1 -->
### 20. MeshParam::bool

Pure\_Quad\_Mesh 0=No 1=Yes

<!-- @since:5.0.1 -->
### 21. MeshParam::bool

Bad\_Input\_Model 0=No 1=Yes

<!-- @since:5.0.1 -->
### 22. MeshParam::bool

Close\_Gaps 0=No 1=Yes

<!-- @since:5.0.1 -->
### 23. MeshParam::bool

Local\_Remesh 0=No 1=Yes

<!-- @since:5.0.1 -->
### 24. MeshParam::bool

Geom\_Approximation 0=No 1=Yes

<!-- @since:5.0.1 -->
### 25. MeshParam::bool

Curvature\_Control 0=No 1=Yes

<!-- @since:5.0.1 -->
### 26. MeshParam::bool

Delete\_CircChamfer 0=No 1=Yes

<!-- @since:5.1.0 -->
### 27. MeshParam::bool

Tiny\_Cylinder\_Meshing 0=No 1=Yes

<!-- @since:5.0.1 -->
### 28. MeshParam::int

Next\_Entity\_Offset\_Id

<!-- @since:5.0.1 -->
### 29. MeshParam::int

Next\_Elem\_Offset\_Id

<!-- @since:5.1.0 -->
### 30. MeshParam::int

Next\_Node\_Offset\_Id

<!-- @since:5.0.1 -->
### 31. bool

Use Local Settings 0=No 1=Yes

<!-- @since:5.1.0 -->
### 32. bool

Use FMesher 0=No 1=Yes

<!-- @since:5.1.0 -->
### 33. int

Thread Number

<!-- @since:5.0.1 -->
### 34. bool

Keep Reference Data 0=No 1=Yes

<!-- @since:5.1.0 -->
### 35. bool

Use mesh color 0=No 1=Yes

<!-- @since:5.1.0 -->
### 36. COLOR

Mesh Color

<!-- @since:5.1.0 -->
### 37. bool

Reserved.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 27. MeshParam::int

Next\_Entity\_Offset\_Id

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 30. bool

Use Local Settings 0=No 1=Yes

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 32. int

Thread Number

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 33. bool

Keep Reference Data 0=No 1=Yes

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 35. COLOR

Mesh Color

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
SurfaceMeshing2D([3:1], {0.005, 0.01, 0.0001, 1, 0.7853981634, 0.0001, 1.25, 0.1, 0.1, 0.7, 0.5, 1, 3, 0, 0, 0, 0.5235987756, 0, 0, 0, 0, 0, 1, 0, 0, 0, 10000000, 0, 0}, 1, 0, 16, 1, 0, 65280, 0)
```
