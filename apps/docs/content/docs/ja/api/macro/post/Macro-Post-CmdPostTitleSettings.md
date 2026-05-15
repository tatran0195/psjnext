---
title: "CmdPostTitleSettings()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Title setting.

## Syntax

```psj
CmdPostTitleSettings(bool ResultName,bool Convection,bool Unit,bool Coordinate,bool TotalMaxMin,bool FileName,bool Location,bool VisibleMaxMin,bool Animation,bool DeformRatio,bool Detail,int SizeTitleTarget,int SizeDesTarget,int ResultTitle,color ResultTitle,bool ResultTitle,int ResultDescription,color ResultDescription,bool ResultDescription,bool UseBackground,color FillBackground,color BorderBackground,float Percentage)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. bool

Result Name flag.

<!-- @since:5.0.1 -->
### 2. bool

Convection flag.

<!-- @since:5.0.1 -->
### 3. bool

Unit flag.

<!-- @since:5.0.1 -->
### 4. bool

Coordinate flag.

<!-- @since:5.0.1 -->
### 5. bool

Total Max/Min flag.

<!-- @since:5.0.1 -->
### 6. bool

File Name flag.

<!-- @since:5.0.1 -->
### 7. bool

Location flag.

<!-- @since:5.0.1 -->
### 8. bool

Visible Max/Min flag.

<!-- @since:5.0.1 -->
### 9. bool

Animation flag.

<!-- @since:5.0.1 -->
### 10. bool

Deform Ratio flag.

<!-- @since:5.0.1 -->
### 11. bool

Detail flag.

<!-- @since:5.0.1 -->
### 12. int

Font Size of Result Title.

<!-- @since:5.0.1 -->
### 13. int

Font Size of Result Description.

<!-- @since:5.0.1 -->
### 14. int

Result Title,

<!-- @since:5.0.1 -->
### 15. color

Color of Result Title,

<!-- @since:5.0.1 -->
### 16. bool

Bold flag of Result Title,

<!-- @since:5.0.1 -->
### 17. int

Result Description,

<!-- @since:5.0.1 -->
### 18. color

Color of Result Description.

<!-- @since:5.0.1 -->
### 19. bool

Bold flag of Result Description,

<!-- @since:5.0.1 -->
### 20. bool

Use Background flag.

<!-- @since:5.0.1 -->
### 21. color

Background color

<!-- @since:5.0.1 -->
### 22. color

BorderBackground,

<!-- @since:5.0.1 -->
### 23. float

Transparency.

## Return Code

Nothing.

## Sample Code

```psj
CmdPostTitleSettings(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 5, 6, 16777215, 1, 5, 16777215, 0, 0, 16777215, 16777215, 0.500000)
```
