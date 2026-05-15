---
title: "ALIGNMENTBYOOBB()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.1.0"
available _versions: "all"
---

## Description

A bounding box is defined for each part in such a way that it minimizes empty space, and part movement is performed by aligning these bounding boxes with each other.

## Syntax

```psj
ALIGNMENTBYOOBB(cursor referencePart, cursor movingPart, int positionType, 3:1, 0, [0, 0, 0], [0, 0, 0])
```

## Inputs

<!-- @since:5.1.0 -->
### 1. Cursor

A _Cursor_ specifying the target part to which alignment will be made.

<!-- @since:5.1.0 -->
### 2. Cursor

A _Cursor_ specifying the part to be moved.

<!-- @since:5.1.0 -->
### 3. Int

An _Integer_ specifying the type of alignment.

- 0: Center of Part
- 1: Center of Plane1
- 2: Center of Plane2
- 3: Center of Plane3
- 4: Center of Plane4
- 5: Center of Plane5
- 6: Center of Plane6
- 7: Center of Point 1 and 2
- 8: Center of Point 2 and 3
- 9: Center of Point 3 and 4
- 10: Center of Point 4 and 1
- 11: Center of Point 1 and 5
- 12: Center of Point 2 and 6
- 13: Center of Point 3 and 7
- 14: Center of Point 4 and 8
- 15: Center of Point 5 and 6
- 16: Center of Point 6 and 7
- 17: Center of Point 7 and 8
- 18: Center of Point 8 and 5
- 19: Point 1
- 20: Point 2
- 21: Point 3
- 22: Point 4
- 23: Point 5
- 24: Point 6
- 25: Point 7
- 26: Point 8

<!-- @since:5.1.0 -->
### 4. Double\[]

A _List of Double_ specifying trantlation values for adjustment from the moved

<!-- @since:5.1.0 -->
### 5. Double\[]

A _List of Double_ specifying rotation values for adjustment from the moved position.

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ALIGNMENTBYOOBB(3:2, 3:1, 0, [0, 0, 0], [0, 0, 0])
```
