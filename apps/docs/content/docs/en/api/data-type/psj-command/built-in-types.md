---
title: Built-in Types
id: built-in-types
---

An enumeration used in all PSJ-Commands functions.

| Jupiter Macro/API data type | Abbreviation       | Prefix + VariableName | Description                                                                                                                                                                      |
| --------------------------- | ------------------ | :-------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Integer                     | `int`              | **i**VariableName     | Represents a positive or negative value with no decimal point.<br />2147483647 is the default value of `(blank=no input)` in the integer value field                             |
| Boolean                     | `bool`             | **b**VariableName     | Represents the boolean values `False(0)` and `True(1)`                                                                                                                           |
| Double                      | `double`           | **d**VariableName     | Represents a computer level double precision floating point number.<br />1.79769e+308 is the default value of `(Blank=no input)` in the real number field                        |
| String                      | `str`              | **str**VariableName   | Represents a string. Enclose with double quote `""`                                                                                                                              |
| Cursor                      | `cursor`           | **cr**VariableName    | **TypeID:** Represents an entity in the form of ID.<br />**Example:**<br />`3:1` <br />Except for CAD part, which takes 2 parameters: ID and Key.<br />**Example:**<br />`3:1-1` |
| Position                    | `position`         | **pos**VariableName   | n/a                                                                                                                                                                              |
| Vector                      | `vector`           | **vec**VariableName   | n/a                                                                                                                                                                              |
| List of Integer             | `int list`         | **il**VariableName    | n/a                                                                                                                                                                              |
| List of Double              | `double list`      | **dl**VariableName    | n/a                                                                                                                                                                              |
| List of String              | `string list`      | **strl**VariableName  | n/a                                                                                                                                                                              |
| List of Cursor              | `List of Cursor`   | **crl**VariableName   | **TypeID:** Represents a list of cursors.<br />**Example:**<br />`[3:1,3:2]` <br />                                                                                              |
| List of Position            | `position list`    | **posl**VariableName  | n/a                                                                                                                                                                              |
| List of Vector              | `vector list`      | **vecl**VariableName  | n/a                                                                                                                                                                              |
| List of Boolean             | `bool list`        | **bl**VariableName    | n/a                                                                                                                                                                              |
| Pair of Cursor              | `cursor pair`      | **crp**VariableName   | n/a                                                                                                                                                                              |
| List of Cursor Pair         | `cursor pair list` | **crpl**VariableName  | n/a                                                                                                                                                                              |
| TSheetd                     | `TSheetd`          | **tsh**VariableName   | n/a                                                                                                                                                                              |
| CursorStr                   | n/a                | **cr**VariableName    | Represents a single cursor or multiple cursors separated by commas. It can be used as instead of Cursor, or a content of List of Cursor.                                         |
