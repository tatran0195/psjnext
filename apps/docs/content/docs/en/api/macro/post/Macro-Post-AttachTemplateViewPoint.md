---
title: "AttachTemplateViewPoint()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Attach viewpoint setting to specified template.

## Syntax

```psj
AttachTemplateViewPoint(string templateName, float trans[0], float trans[1], float trans[2], float trans[3], float trans[4], float trans[5], float trans[6], float trans[7], float trans[8], float trans[9], float trans[10], float trans[11], float trans[12], float trans[13], float trans[14], float trans[15], float Cent[0], float Cent[1], float Cent[2], float PanOffsetX, float PanOffsetY, float ScaleFactor, bool Rotate, bool Pan, bool Scale)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. string

Template name.

<!-- @since:5.0.1 -->
### 2. float

00 of 4x4 transform matrix (00 - 33).

<!-- @since:5.0.1 -->
### 3. float

01 of 4x4 transform matrix.

<!-- @since:5.0.1 -->
### 4. float

02 of 4x4 transform matrix.

<!-- @since:5.0.1 -->
### 5. float

03 of 4x4 transform matrix.

<!-- @since:5.0.1 -->
### 6. float

10 of 4x4 transform matrix.

<!-- @since:5.0.1 -->
### 7. float

11 of 4x4 transform matrix.

<!-- @since:5.0.1 -->
### 8. float

12 of 4x4 transform matrix.

<!-- @since:5.0.1 -->
### 9. float

13 of 4x4 transform matrix.

<!-- @since:5.0.1 -->
### 10. float

20 of 4x4 transform matrix.

<!-- @since:5.0.1 -->
### 11. float

21 of 4x4 transform matrix.

<!-- @since:5.0.1 -->
### 12. float

22 of 4x4 transform matrix.

<!-- @since:5.0.1 -->
### 13. float

23 of 4x4 transform matrix.

<!-- @since:5.0.1 -->
### 14. float

30 of 4x4 transform matrix.

<!-- @since:5.0.1 -->
### 15. float

31 of 4x4 transform matrix.

<!-- @since:5.0.1 -->
### 16. float

32 of 4x4 transform matrix.

<!-- @since:5.0.1 -->
### 17. float

33 of 4x4 transform matrix.

<!-- @since:5.0.1 -->
### 18. float

Rotation center x.

<!-- @since:5.0.1 -->
### 19. float

Rotation center y.

<!-- @since:5.0.1 -->
### 20. float

Rotation center z.

<!-- @since:5.0.1 -->
### 21. float

Offset x.

<!-- @since:5.0.1 -->
### 22. float

Offset y.

<!-- @since:5.0.1 -->
### 23. float

Scale Factor.

<!-- @since:5.0.1 -->
### 24. bool

Rotate flag.

<!-- @since:5.0.1 -->
### 25. bool

Pan flag.

<!-- @since:5.0.1 -->
### 26. bool

Scale flag.

## Return Code

- "1": Succeeded.
- "0": Failed.

## Sample Code

```psj
AttachTemplateViewPoint("My Template", -0.707107, -0.5, 0.5, 0, 0.707107, -0.5, 0.5, 0, 0, 0.707107, 0.707107, 0, 0, 0, 0, 1, 0.005, 0.005, 0.005, 0, 0, 0.0136569, 1, 1, 1)
```
