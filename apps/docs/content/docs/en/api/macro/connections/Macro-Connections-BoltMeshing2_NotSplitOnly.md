---
title: "BoltMeshing2 _NotSplitOnly()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

For CAD bolts, divide the bolt into upper and lower parts, generate the mesh, and apply load and boundary conditions for ADVC.

## Syntax

```psj
BoltMeshing2 _NotSplitOnly(string strName, int method , double offset, int shared _face, int separate _face, int split _only, int make _section _face, cursor local _c, meshParam param, int lbc _direction, double value, bool bolt _fix _length, cursor pretension _table, cursor pretension _coord, int unit, cursor[] targets, pos[] cut _positions)'
```

## Inputs

<!-- @since:5.1.0 -->
### 1. String

The name of newly created LBCs.

<!-- @since:5.1.0 -->
### 2. int

Selet cutting section coordinate 0 = X-Z, coordinate 1 = Y-Z, coordinate 2 = Z-X or 3 Points.

<!-- @since:5.1.0 -->
### 3. double

Offset value.

<!-- @since:5.1.0 -->
### 4. int

Shared face option.

<!-- @since:5.1.0 -->
### 5. int

Separate Face option.

<!-- @since:5.1.0 -->
### 6. int

Split only option.

<!-- @since:5.1.0 -->
### 7. int

Make section face option.

<!-- @since:5.1.0 -->
### 8. cusror

Local Coordinate to refer.

<!-- @since:5.1.0 -->
### 9. MeshSizeParameters::double

Avg\_Element\_Size

<!-- @since:5.1.0 -->
### 10. MeshSizeParameters::double

Max\_Element\_Size

<!-- @since:5.1.0 -->
### 11. MeshSizeParameters::double

Min\_Element\_Size

<!-- @since:5.1.0 -->
### 12. MeshSizeParameters::double

Reduction Factor, default=1

<!-- @since:5.1.0 -->
### 13. MeshSizeParameters::double

Geometry Angle, default=pi/4 radian

<!-- @since:5.1.0 -->
### 14. MeshSizeParameters::double

Geometry Min Size, default=0.001

<!-- @since:5.1.0 -->
### 15. MeshSizeParameters::double

Grading Factor, default=1.25

<!-- @since:5.1.0 -->
### 16. MeshSizeParameters::double

Min Stretch Value, default=0.1

<!-- @since:5.1.0 -->
### 17. MeshSizeParameters::double

Geometry Edge Deviation, default=0.1

<!-- @since:5.1.0 -->
### 18. MeshSizeParameters::double

Geometry Quality Ratio, default=0.7

<!-- @since:5.1.0 -->
### 19. MeshSizeParameters::double

Geometry Count Ratio, default=0.5

<!-- @since:5.1.0 -->
### 20. MeshSizeParameters::int

Performance Mode 0 = Fastest, 1 = Good Quality, 2 = Best Quality

<!-- @since:5.1.0 -->
### 21. MeshSizeParameters::int

Optimization Level 0 = Disable, 1 = Level1, 2 = Level2, 3= Level3, 4 = Level4, 5 = Level5

<!-- @since:5.1.0 -->
### 22. MeshSizeParameters::bool

Auto Merge Edges flag true = 1, false = 0

<!-- @since:5.1.0 -->
### 23. MeshSizeParameters::bool

Auto Merge Faces flag true = 1, false = 0

<!-- @since:5.1.0 -->
### 24. MeshSizeParameters::double

Auto mesh pattern minimum elem angle.

<!-- @since:5.1.0 -->
### 25. MeshSizeParameters::double

Auto merge tiny faces angle.

<!-- @since:5.1.0 -->
### 26. MeshSizeParameters::bool

Output Quad Mesh flag true = 1, false = 0

<!-- @since:5.1.0 -->
### 27. MeshSizeParameters::bool

Pure Quad Mesh flag true = 1, false = 0

<!-- @since:5.1.0 -->
### 28. MeshSizeParameters::bool

Bad Input Model flag true = 1, false = 0

<!-- @since:5.1.0 -->
### 29. MeshSizeParameters::bool

Close Gaps flag true = 1, false = 0

<!-- @since:5.1.0 -->
### 30. MeshSizeParameters::bool

Local Remesh flag true = 1, false = 0

<!-- @since:5.1.0 -->
### 31. MeshSizeParameters::bool

Geometry Approximation flag true = 1, false = 0

<!-- @since:5.1.0 -->
### 32. MeshSizeParameters::bool

Curvature Control flag true = 1, false = 0

<!-- @since:5.1.0 -->
### 33. MeshSizeParameters::bool

Delete Circle Chamfer flag true = 1, false = 0

<!-- @since:5.1.0 -->
### 34. MeshSizeParameters::bool

Tiny Cylinder Mesh option flag true = 1, false = 0

<!-- @since:5.1.0 -->
### 35. MeshSizeParameters::int

Next Entity Offset ID

<!-- @since:5.1.0 -->
### 36. MeshSizeParameters::int

Next Elem Offset ID

<!-- @since:5.1.0 -->
### 37. MeshSizeParameters::int

Next Node Offset ID

<!-- @since:5.1.0 -->
### 38. bool

Bolt Fix Lengh flag true = 1, false = 0

<!-- @since:5.1.0 -->
### 39. Cursor

Cursor of Abaqus pretension.

<!-- @since:5.1.0 -->
### 33. double

Pretension value.

<!-- @since:5.1.0 -->
### 34. int

Local unit of Abaqus pretension.

<!-- @since:5.1.0 -->
### 35. String

Pretention direction.

<!-- @since:5.1.0 -->
### 36. point

Control node \[X,Y,Z] coordinate of Abaqus pretension.

<!-- @since:5.1.0 -->
### 37. Cursor\[]

List of target parts.

<!-- @since:5.1.0 -->
### 38. point\[]

List of cut positions.

## Return Code

- "1": The function can be executed.
- "0": The function cannot be executed.

## Sample Code

```psj
BoltMeshing2 _NotSplitOnly("BoltMeshing _1", 1, 0.005, 0, 0, 0, 1, 0:0, {0.005, 0.01, 0.001, 1, 0.7853981634, 0.001, 1.25, 0.1, 0.1, 0.7, 0.5, 1, 3, 0, 0, 0, 0.5235987902, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10000000, 0, 0}, 0, 100, 1, 0:0, 0:0, 0, [3:1], [[0.003420201433256688, 0.03333333333333333, 0.009396926207859084]])
```
