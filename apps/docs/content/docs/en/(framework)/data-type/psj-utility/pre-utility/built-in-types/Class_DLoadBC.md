---
title: DLoadBC
id: DLoadBC
---

## Description

This is an instance of a DLoadBC class, represents LBC item inside Jupiter.

## Properties

| Attribute       | Description                                                                                                                                                   |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| isValid         | Determine the validation of the LBC.<br /> The return value is `True` if the LBC is valid, `False` if not (invalid).                                          |
| type            | Type name of the LBC.<br />The return value is Type (string).                                                                                                 |
| typeID          | Type ID of the LBC.<br />The return value is an [`Int notation of DItem Types`](../../../psj-command/DItem-types) (int).                                      |
| tableID         | Table ID of the LBC.<br />The return value is an [`Int notation of DTable Types`](../enumeration-types/dtable-types) (int).                                   |
| id              | External ID of the LBC.<br/>It can be duplicated, but not recommended.<br/>ID can be changed using the renumbering function.<br/>The return value is ID (int) |
| targets         | Hold the contents of the LBC.<br />The return value is a list of [`DItem`](DItem).                                                                            |
| masters         | Master face/edge/node of the LBC.<br />The return value is a list of [`DItem`](DItem).                                                                        |
| slaves          | Slave face/edge/node of the LBC.<br />The return value is a list of [`DItem`](DItem).                                                                         |
| parent          | A sub-assembly that is the parent of LBC in the assembly tree.<br />The return value is a list of [`DItem`](DItem).                                           |
| isHidden        | Determine display state of the LBC.<br />The return value is `True` if the LBC is hidden, `False` if the LBC is displayed.                                    |
| name            | Name of the LBC.                                                                                                                                              |
| lbcAnalysisType | Type of the analysis solver of LBC.<br />The return value is [lbcAnalysisType](#lbcanalysistype) (string).                                                    |
| lbcCoord        | Reference Coordinate System of LBC. <br/>The return value is [DCoord](DCoord) (object).                                                                       |
| color\* [^(1)]  | LBC color information.<br />This value can be adjusted.<br />The return value is a RGB color.                                                                 |

## Attribute

### lbcAnalysisType

| Name        | Description                          |
| ----------- | ------------------------------------ |
| FOR_BOTH    | Both Structure and Thermal Analyses. |
| FOR_STRUCT  | Structure Analysis.                  |
| FOR_THERMAL | Thermal Analysis.                    |

### Notice

[^(1)]:
    An asterisk symbol \* in attribute name means that attribute can be changed/assigned from the current to the new
    value.
