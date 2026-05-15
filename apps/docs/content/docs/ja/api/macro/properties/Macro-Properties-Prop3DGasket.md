---
title: "Prop3DGasket()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Create property 3d gasket

## Syntax

```psj
Prop3DGasket(string strName, color propertyColor, cursor crMaterial, double dThickX, double dThickY,
    double dThickZ, cursor taTarget, cursor crEdit, bool bUniAxial, int FLG)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

Prop3DGasket name

<!-- @since:5.1.0 -->
### 2. Color

Color of the property.

<!-- @since:5.1.0 -->
### 3. Cursor

Material cursor(22:Material ID)

<!-- @since:5.0.1 -->
### 4. Double

Thickness direction X

<!-- @since:5.0.1 -->
### 5. Double

Thickness direction Y

<!-- @since:5.1.0 -->
### 6. Double

Thickness direction Z

<!-- @since:5.0.1 -->
### 7. Cursor

Target entities cursor

<!-- @since:5.1.0 -->
### 8. Cursor

Edit cursor

<!-- @since:5.1.0 -->
### 9. Bool

UniAxial bool flag True = 1, False = 0

<!-- @since:5.1.0 -->
### 10. Int

FLG

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 2. Cursor

Material cursor(22:Material ID)

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 3. Double

Thickness direction X

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 6. Cursor

Target entities cursor

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 8. Bool

UniAxial bool flag True = 1, False = 0

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 9. Int

FLG

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Prop3DGasket("Gasket Property 1", 13642735, 22:6, 1, 2, 3, [3:1], 0:0, 1, 1)
```
