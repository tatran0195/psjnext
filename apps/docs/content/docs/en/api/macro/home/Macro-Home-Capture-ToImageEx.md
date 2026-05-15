---
title: "Capture _ToImageEx()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

Capture to Image File.

## Syntax

```psj
Capture _ToImageEx(string strNamePath, bool WhiteBG, bool TransparentBG,
    bool FixedSize, int exportWidth, int exportHeight)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

Import file path

<!-- @since:5.0.1 -->
### 2. Bool

White background bool flag true = 1, false = 0

<!-- @since:5.0.1 -->
### 3. Bool

Transparent background flag true = 1, false = 0

<!-- @since:5.0.1 -->
### 4. Bool

Fixed Size flag true = 1, false = 0

<!-- @since:5.0.1 -->
### 5. Int

Export Width

<!-- @since:5.0.1 -->
### 6. Int

Export Height

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Capture _ToImageEx("D:/Test.jpg", 0, 0, 0, 1200, 900)
```
