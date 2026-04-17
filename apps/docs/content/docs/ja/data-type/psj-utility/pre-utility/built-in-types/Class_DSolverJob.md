---
title: DSolverJob
id: DSolverJob
---

## Description

This is an instance of a DSolverJob class, represents a Job inside Jupiter.

## Properties

| Attribute      | Description                                                                                                                                                      |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| isValid        | Determine the validation of the Job.<br /> The return value is `True` if the Job is valid, `False` if not (invalid).                                             |
| type           | Type name of the Job.<br />The return value is Type (string).                                                                                                    |
| typeID         | Type ID of the Job.<br />The return value is an [`Int notation of DItem Types`](../../../psj-command/DItem-types) (int).                                         |
| tableID        | Table ID of the Job.<br />The return value is an [`Int notation of DTable Types`](../enumeration-types/dtable-types) (int).                                      |
| id             | External ID of the Job.<br />It can be duplicated, but not recommended.<br />ID can be changed using the renumbering function.<br />The return value is ID (int) |
| targets        | Hold the contents of the Job.<br />The return value is a list of [`DItem`](DItem).                                                                               |
| masters        | Master face/edge/node of the Job.<br />The return value is a list of [`DItem`](DItem).                                                                           |
| slaves         | Slave face/edge/node of the Job.<br />The return value is a list of [`DItem`](DItem).                                                                            |
| parent         | A sub-assembly that is the parent of Job in the assembly tree.<br />The return value is a list of [`DItem`](DItem).                                              |
| isHidden       | Determine display state of the Job.<br />The return value is `True` if the Job is hidden, `False` if the Job is displayed.                                       |
| name           | Name of the Job.<br />The return value is Name (string).                                                                                                         |
| jobSteps       | Time step of the Job.<br />It is used for ADVC and Abaqus Job.<br />The return value is a list of DItem.                                                         |
| jobDescription | Description of the Job.<br />The return value is description text (string).                                                                                      |
