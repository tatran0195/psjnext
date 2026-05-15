---
title: "Property1DSection()"
description: "TODO: Add description. (auto-generated placeholder — review required)"
version _introduced: "5.0.1"
available _versions: "all"
---

## Description

1D section property

## Syntax

```psj
Property1DSection(string Name, int SectionType, int SectionGenerateType, double SizeA,
    double SizeB, double SizeH, double SizeT1, double SizeT2, double SizeT3, bool Tapered,
    double A _tap, double B _tap, double H _tap, double T1 _tap, double T2 _tap, double T3 _tap)
```

## Inputs

<!-- @since:5.0.1 -->
### 1. String

Name Section

<!-- @since:5.0.1 -->
### 2. Int

Section Type \[General Section = 0, Library Section = 1]

<!-- @since:5.0.1 -->
### 3. Int

Section Generate Type \[PROP\_SECTION\_GEN\_RECT = 0, PROP\_SECTION\_GEN\_RECT\_TUBE = 1, PROP\_SECTION\_GEN\_CIRCLE = 2, PROP\_SECTION\_GEN\_CIRCLE\_TUBE = 3, PROP\_SECTION\_GEN\_C = 4, PROP\_SECTION\_GEN\_IH = 5, PROP\_SECTION\_GEN\_L = 6, PROP\_SECTION\_GEN\_T =7]

<!-- @since:5.0.1 -->
### 4. Double

Section size A

<!-- @since:5.0.1 -->
### 5. Double

Section size B

<!-- @since:5.0.1 -->
### 6. Double

Section size H

<!-- @since:5.0.1 -->
### 7. Double

Section size T1

<!-- @since:5.0.1 -->
### 8. Double

Section size T2

<!-- @since:5.0.1 -->
### 9. Double

Section size T3

<!-- @since:5.0.1 -->
### 10. Bool

Tapered flag true = 1,false = 0

<!-- @since:5.0.1 -->
### 11. Double

Tap size A

<!-- @since:5.0.1 -->
### 12. Double

Tap size B

<!-- @since:5.0.1 -->
### 13. Double

Tap size H

<!-- @since:5.0.1 -->
### 14. Double

Tap size T1

<!-- @since:5.0.1 -->
### 15. Double

Tap size T2

<!-- @since:5.0.1 -->
### 16. Double

Tap size T3

## Return Code

- "1": The function can be executed
- "0": The function cannot be executed

## Sample Code

```psj
Property1DSection("T", 0, 7, 0, 0.0005, 0.0005, 0.0001, 0.0001, 0, 0, 0, 0, 0, 0, 0, 0)
```
