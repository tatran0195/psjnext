---
title: "AttachTemplateAnimation()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Attach animation setting to specified template.

## Syntax

```psj
AttachTemplateAnimation(string templateName, int Mode, int FPS, int DivideNum, int DivideType, int LoopType, int AnimationResType, bool ApplyDeform, bool Locus, bool PhaseAngleAni, bool AcousticCombineAni, string[] SubcaseIds, bool MultiAnalysis, bool MemCache, bool FixContour, bool SectionMode, bool SetTime, float StartTime, float EndTime))
```

## Inputs

<!-- @since:5.0.1 -->
### 1. string

Template name.

<!-- @since:5.0.1 -->
### 2. int

Animation mode

<!-- @since:5.0.1 -->
### 3. int

Animation speed (FPS)

<!-- @since:5.0.1 -->
### 4. int

No. of Frame

<!-- @since:5.0.1 -->
### 5. int

Dividing Method

<!-- @since:5.0.1 -->
### 6. int

Looping Type

<!-- @since:5.0.1 -->
### 7. bool

Animation Res Type

<!-- @since:5.0.1 -->
### 8. bool

Apply Deform

<!-- @since:5.0.1 -->
### 9. bool

Locus

<!-- @since:5.0.1 -->
### 10. bool

Animation setting for Phase Angle Ani

<!-- @since:5.0.1 -->
### 11. bool

Animation setting for Acoustic Combine Ani

<!-- @since:5.0.1 -->
### 12. string \[]

Subcase IDs

<!-- @since:5.0.1 -->
### 13. bool

MultiAnalysis flag

<!-- @since:5.0.1 -->
### 14. bool

Mem Cache flag

<!-- @since:5.0.1 -->
### 15. bool

Fix Contour flag

<!-- @since:5.0.1 -->
### 16. bool

Section display method,

<!-- @since:5.0.1 -->
### 17. bool

Set Time flag

<!-- @since:5.0.1 -->
### 18. float

Start Time

<!-- @since:5.0.1 -->
### 19. float

End Time

## Return Code

- "1": Succeeded.
- "0": Failed.

## Sample Code

```psj
AttachTemplateAnimation("My Template", 0, 8, 8, 1, 1, 0, 1, 0, 0, 0, [], 0, 1, 0, 0, 0, 0.01, 1)
```
