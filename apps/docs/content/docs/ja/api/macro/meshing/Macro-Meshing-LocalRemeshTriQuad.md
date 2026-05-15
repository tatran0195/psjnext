---
title: "LocalRemeshTriQuad()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Meshing specified surfaces.

## Syntax

```psj
LocalRemeshTriQuad(cursor[] target _items, meshSizeParameters param, bool meshSetting,
    bool use _setting, bool grading, bool fmesher, bool override _type, bool keepConnection, bool projectCAD, bool id _check, bool tinyFacMerge, double minWidth, double maxWidth, bool keep _remesh _edge, int grading _elem)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. Cursor\[]

Target Item Cursor(\[\*:\*\*],\*=Items Type 3=Parts 6=Faces 5=Edges ,\*\*=Items ID)

<!-- @since:5.0.1 -->
### 2. MeshSizeParameters::double

Avg\_Element\_Size

<!-- @since:5.0.1 -->
### 3. MeshSizeParameters::double

Max\_Element\_Size

<!-- @since:5.0.1 -->
### 4. MeshSizeParameters::double

Min\_Element\_Size

<!-- @since:5.0.1 -->
### 5. MeshSizeParameters::double

Reduction Factor, default=1

<!-- @since:5.0.1 -->
### 6. MeshSizeParameters::double

Geometry Angle, default=pi/4 radian

<!-- @since:5.0.1 -->
### 7. MeshSizeParameters::double

Geometry Min Size, default=0.001

<!-- @since:5.0.1 -->
### 8. MeshSizeParameters::double

Grading Factor, default=1.25

<!-- @since:5.0.1 -->
### 9. MeshSizeParameters::double

Min Stretch Value, default=0.1

<!-- @since:5.1.0 -->
### 10. MeshSizeParameters::double

Geometry Edge Deviation, default=0.1

<!-- @since:5.0.1 -->
### 11. MeshSizeParameters::double

Geometry Quality Ratio, default=0.7

<!-- @since:5.0.1 -->
### 12. MeshSizeParameters::double

Geometry Count Ratio, default=0.5

<!-- @since:5.0.1 -->
### 13. MeshSizeParameters::int

Performance Mode 0 = Fastest, 1 = Good Quality, 2 = Best Quality

<!-- @since:5.0.1 -->
### 14. MeshSizeParameters::int

Optimization Level 0 = Disable, 1 = Level1, 2 = Level2, 3= Level3, 4 = Level4, 5 = Level5

<!-- @since:5.0.1 -->
### 15. MeshSizeParameters::bool

Auto Merge Edges flag true = 1, false = 0

<!-- @since:5.0.1 -->
### 16. MeshSizeParameters::bool

Auto Merge Faces flag true = 1, false = 0

<!-- @since:5.1.0 -->
### 17. MeshSizeParameters::double

Auto mesh pattern minimum elem angle.

<!-- @since:5.1.0 -->
### 18. MeshSizeParameters::double

Auto merge tiny faces angle.

<!-- @since:5.0.1 -->
### 19. MeshSizeParameters::bool

Output Quad Mesh flag true = 1, false = 0

<!-- @since:5.0.1 -->
### 20. MeshSizeParameters::bool

Pure Quad Mesh flag true = 1, false = 0

<!-- @since:5.0.1 -->
### 21. MeshSizeParameters::bool

Bad Input Model flag true = 1, false = 0

<!-- @since:5.0.1 -->
### 22. MeshSizeParameters::bool

Close Gaps flag true = 1, false = 0

<!-- @since:5.0.1 -->
### 23. MeshSizeParameters::bool

Local Remesh flag true = 1, false = 0

<!-- @since:5.0.1 -->
### 24. MeshSizeParameters::bool

Geometry Approximation flag true = 1, false = 0

<!-- @since:5.1.0 -->
### 25. MeshSizeParameters::bool

Curvature Control flag true = 1, false = 0

<!-- @since:5.1.0 -->
### 26. MeshSizeParameters::bool

Delete Circle Chamfer flag true = 1, false = 0

<!-- @since:5.1.0 -->
### 27. MeshSizeParameters::bool

Tiny Cylinder Mesh option flag true = 1, false = 0

<!-- @since:5.1.0 -->
### 28. MeshSizeParameters::int

Next Entity Offset ID

<!-- @since:5.1.0 -->
### 29. MeshSizeParameters::int

Next Elem Offset ID

<!-- @since:5.1.0 -->
### 30. MeshSizeParameters::int

Next Node Offset ID

<!-- @since:5.0.1 -->
### 31. bool

Use Local Mesh Setting flag true = 1, false = 0

<!-- @since:5.0.1 -->
### 32. bool

Grading flag true = 1, false = 0

<!-- @since:5.1.0 -->
### 33. bool

Use FMesher 0=No 1=Yes

<!-- @since:5.1.0 -->
### 34. bool

Override Type 0=IsoMesh 1=FreeMesh

<!-- @since:5.1.0 -->
### 35. bool

Project CAD flag true = 1, false = 0

<!-- @since:5.1.0 -->
### 36. bool

Keep connection flag true = 1, false = 0

<!-- @since:5.1.0 -->
### 37. bool

Tiny Face Merge true = 1, false = 0

<!-- @since:5.1.0 -->
### 38. float

Min Face Width

<!-- @since:5.1.0 -->
### 39. float

Max Face Width

<!-- @since:5.1.0 -->
### 40. bool

ID Check true = 1, false = 0

<!-- @since:5.1.0 -->
### 41. bool

Keep Remesh Edge true = 1, false = 0

<!-- @since:5.1.0 -->
### 42. int

The number of adjacent layers to be locally remeshed.

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 17. MeshSizeParameters::bool

Output Quad Mesh flag true = 1, false = 0

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 18. MeshSizeParameters::bool

Pure Quad Mesh flag true = 1, false = 0

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 25. MeshSizeParameters::int

Next Entity Offset ID

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 26. MeshSizeParameters::int

Next Elem Offset ID

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 27. MeshSizeParameters::int

Next Node Offset ID

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 28. bool

Mesh Setting flag true = 1, false = 0

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 29. bool

Grading flag true = 1, false = 0

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 30. bool

Keep connection flag true = 1, false = 0

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 33. double

Min Face Width

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 34. double

Max Face Width

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
LocalRemeshTriQuad([6:26], {0.01, 0.02, 0.001, 1, 0.7853981853, 0.001, 1.25, 0.1, 0.1, 0.7, 0.5, 1, 3, 0, 0, 0, 0.5235987902, 0, 0, 0, 0, 1, 0, 0, 0, 0, 27, 1233, 513}, 1, 1, 0, 0, 1, 1, 0, 0, 0.001, 0, 0, 1)
```
