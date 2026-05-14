---
title: DMaterialLib
id: DMaterialLib
---

## Description

This is an instance of a DMaterialLib class, represents library material item inside Jupiter.

## Properties

| Attribute      | Description                                                                                                                                              |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name           | Name of the material.<br />The return value is a string name (str).                                                                                      |
| description    | Description of the material.<br />The return value is a string description (str).                                                                        |
| isComposite    | Determine whether is is a composite material.                                                                                                            |
| id             | External ID of the material.<br />ID cannot be duplicated.<br />ID can be changed using the renumbering function.<br />The return value is ID (int).     |
| color\* [^(1)] | Material color information.<br />This value can be adjusted.<br />The return value is a RGB color.                                                       |
| matStandard    | Determine the standard of the material.<br /> The return value is a standard of SD_JIS, SD_ISO, SD_AISI, SD_SAE, SD_BS, SD_DIN, SD_EN, SD_NF, or SD_OCT. |
| dictMatProps   | All material properties information.<br />The return value is a dictionary.                                                                              |
| GetValues      | Get and convert the material property value.<br />The return value is a list of material value (double).                                                 |
| SetValues      | Set and convert the new material property value.<br />The return value is a dictionary.                                                                  |

## Attribute

### GetValues

#### `keys`

- A _List of String_ specifying the keys of material property.
- This is a required input.

#### `unit`

- An _Enum_ specifying the _[unit of material](../../../../data-type/psj-command/material-unit-types)_ to be converted.
  - For the material property with unit, the unit should be specified.
  - For the non-unit material property, the unit should be set by None, -1, or set it empty.
- The default value is -1.

```psj {2-5} title="Sample Code"
mat0 = JPT.GetAllLibraryMaterials()[0]
dict1 = mat0.dictMatProps
list_keys=['Density', 'density', 'DENSITY']
unit=JPT.DensityUnit.Density_kg_m3
pprint(mat0.GetValues(keys=list_keys, unit=unit))
```

### Notice

[^(1)]: The attribute can be changed/assigned from the current to the new value.
