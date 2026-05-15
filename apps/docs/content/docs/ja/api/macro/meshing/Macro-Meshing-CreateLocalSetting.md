---
title: "CreateLocalSetting()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create Local Settings

## Syntax

```psj
CreateLocalSetting(string name, MeshLocalParam param, cursor[] target, int[] hard _point _id,
    point[] hard _Point _xyz, cursor[] hard _point _target, cursor edit _target)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

Node List

<!-- @since:5.0.1 -->
### 2. MeshLocalParam::int

Entity Type 0=NONE,1=BODY,2=FACE,3=EDGE,8=FACE\_POINT,9=EDGE\_POINT

<!-- @since:5.0.1 -->
### 3. MeshLocalParam::bool

Enable Size Param 0=No 1=Yes

<!-- @since:5.0.1 -->
### 4. MeshLocalParam::double

Avg\_Element\_Size

<!-- @since:5.0.1 -->
### 5. MeshLocalParam::double

Max\_Element\_Size

<!-- @since:5.0.1 -->
### 6. MeshLocalParam::double

Min\_Element\_Size

<!-- @since:5.0.1 -->
### 7. MeshLocalParam::bool

Enable Trim Angle 0=No 1=Yes

<!-- @since:5.0.1 -->
### 8. MeshLocalParam::double

Trim Angle

<!-- @since:5.0.1 -->
### 9. MeshLocalParam::bool

Enable Mesh Count 0=No 1=Yes

<!-- @since:5.0.1 -->
### 10. MeshLocalParam::int

Node Count

<!-- @since:5.0.1 -->
### 11. MeshLocalParam::int

Bias Node Id

<!-- @since:5.0.1 -->
### 12. MeshLocalParam::double

Bias Factor

<!-- @since:5.0.1 -->
### 13. MeshLocalParam::int

Bias Method 0=LINEAR,1=BIAS,2=BIAS\_CENTER,3=BIAS\_SIDE

<!-- @since:5.0.1 -->
### 14. MeshLocalParam::int

Bias Progression 0=GEOMETRY,1=ARITHMETIC

<!-- @since:5.0.1 -->
### 15. MeshLocalParam::bool

Enable Mesh Pattern 0=No 1=Yes

<!-- @since:5.0.1 -->
### 16. MeshLocalParam::int

Mesh Pattern Type 0=UNSTRUCTURED,1=STRUCTURED\_ISO,2=IMPRINTING\_ISO

<!-- @since:5.0.1 -->
### 17. MeshLocalParam::bool

Enable Keep Entity 0=No 1=Yes

<!-- @since:5.0.1 -->
### 18. MeshLocalParam::double

Hard Point X

<!-- @since:5.0.1 -->
### 19. MeshLocalParam::double

Hard Point Y

<!-- @since:5.0.1 -->
### 20. MeshLocalParam::double

Hard Point Z

<!-- @since:5.0.1 -->
### 21. MeshLocalParam::int

Hard Point Id

<!-- @since:5.0.1 -->
### 22. MeshLocalParam::bool

Enable Freeze Mesh 0=No 1=Yes

<!-- @since:5.0.1 -->
### 23. Cursor\[]

Target List(Body/Face/Edge)

<!-- @since:5.0.1 -->
### 24. int\[]

Hard Point Id list

<!-- @since:5.0.1 -->
### 25. Point\[]

Hard Point XYZ list

<!-- @since:5.0.1 -->
### 26. Cursor\[]

Hard Point Target list

<!-- @since:5.0.1 -->
### 27. Cursor

Edit Target

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
CreateLocalSetting("MeshParam _1", {2, 1, 0.005, 0.01, 0.001, 0, 0, 0, 0, 0,
    0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0}, [6:8], [], [], [], 0:0)
```
