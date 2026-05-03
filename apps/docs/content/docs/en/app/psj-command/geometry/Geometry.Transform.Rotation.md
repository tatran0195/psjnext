---
title: "Geometry.Transform.Rotation()"
description: "Rotate given parts by the specified angle"
version_introduced: "5.0.1"
available_versions: "all"
ribbon: "Geometry > Transform > Rotation"
macro_link: "[RotateBody](../../macro/geometry/RotateBody)"
---
<!-- REVIEW FLAGS — requires human review
   [body_divergence] Body content differs across 2 of 2 versions — using latest
-->

## Description

Rotate given parts by the specified angle.

## Syntax

```psj
Geometry.Transform.Rotation(...)
```

## Inputs

### `crlParts` @type(List\[Cursor]) @default(\[])

- The parts to be rotated.

### `posCenter` @type(List) @default(\[0,0,0])

- The center position of rotation.

### `vecAxis` @type(List) @default(\[1,0,0])

- The axis of rotation.

### `dAngle` @type(Double) @default(0)

- The rotation angle.

### `bCreateNewPart` @type(Boolean) @default(False)

- Whether to copy a new one and perform the transform operation.

### `bCopyLBC` @type(Boolean) @default(False)

- Whether to copy load boundary condition of the original part to rotation part. This argument will be ignored i&#x66;_&#x62;CreateNewPart=False_.

### `bCopyProperty` @type(Boolean) @default(False)

- The option that copy property of the original part to rotation part. This argument will be ignored i&#x66;_&#x62;CreateNewPart=False_.

### `iCopyCount` @type(Integer) @default(1)

- The number of copy parts. This argument will be ignored i&#x66;_&#x62;CreateNewPart=False_.

### `bMergeNode` @type(Boolean) @default(False)

- Whether to merge nodes between the original part and the transformed one. This argument will be ignored i&#x66;_&#x62;CreateNewPart=False_.

### `dTol` @type(Double) @default(1.0e-5)

- The merge tolerance. This argument should be specified whe&#x6E;_&#x62;MergeNode=True_.

### `bCopyReference` @type(Boolean) @default(False) @since(5.1.0)

- Whether to copy references from the existing part to the created parts or not.
-

## Return Code

A _Boolean_ specifying whether the process is executed successfully or not:

- _True_: The process is executed successfully.
- _False_: Cannot execute the function.

## Sample Code

```psj {3,4,5,6,7,8}
Geometry.Part.Cube()

rotate_status = Geometry.Transform.Rotation(crlParts=[Part(1)], 
                                            vecAxis=[0.0, 0.001, 0.0],
                                            dAngle=0.5,
                                            bCreateNewPart=True, 
                                            iCopyCount=3,
                                            dTol=1e-05)

JPT.Debugger(rotate_status)
```
