---
title: "ElemRelatedInfo _Beam()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Set Bar/Beam Parameter

## Syntax

```psj
ElemRelatedInfo _Beam(list[] eribeam _data)
```

## Inputs

<!-- @since:5.1.0 -->
### 1. list\[]

list of eribeam data

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 1. Int\[]

end node ids parameter

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 2. Int\[]

orientation vectors parameter

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 3. Int\[]

orientation vectors by Node parameter

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 4. Int\[]

offset A vectors parameter

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 5. Int\[]

offset B vectors parameter

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 6. Int\[]

pinA flags parameter

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 7. Int\[]

pinB flags parameter

<!-- @since:5.0.1 @removed:5.1.0 @deprecated -->
### 8. Int\[]

warping flags parameter

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
ElemRelatedInfo _Beam([[1196, 4, 493, 585, [0, 0, 1], 2147483647, [1.79769e+308, 1.79769e+308, 1.79769e+308], [1.79769e+308, 1.79769e+308, 1.79769e+308], 2147483647, 2147483647]])
```
