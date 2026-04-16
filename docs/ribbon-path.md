# Ribbon Path Configuration

The `ribbon` frontmatter property is used to map a document or command to a specific location in the **Jupiter Ribbon Interface**. This allows for a seamless connection between documentation and its corresponding UI action.

## Schema Definition

| Property        | Type     | Description                                                 |
| :-------------- | :------- | :---------------------------------------------------------- |
| `tab`           | `string` | The ribbon tab name (e.g., "Geometry", "Mesh", "Analysis"). |
| `panel`         | `object` | Configuration for the panel group within the tab.           |
| `panel.label`   | `string` | The display name of the panel.                              |
| `panel.item`    | `object` | The primary ribbon item (button) configuration.             |
| `item.label`    | `string` | The display label for the button.                           |
| `item.icon`     | `string` | The Lucide icon identifier.                                 |
| `item.shortcut` | `string` | Keyboard shortcut string (e.g., "Ctrl+M").                  |
| `item.tooltip`  | `string` | A brief description shown on hover.                         |
| `item.flyout`   | `Array`  | Optional list of sub-items for a dropdown menu.             |
| `note`          | `string` | An optional informational note displayed under the path.    |

---

## Examples

### 1. Simple Mapping

Mapping a command to a specific button in a panel.

```yaml
---
title: Create Node
description: Creates a node at a given coordinate.
ribbon:
    tab: Mesh
    panel:
        label: Geometry Tools
        item:
            label: Create Node
            icon: box-select
            shortcut: 'Alt+M, N'
---
```

### 2. Button with Flyout (Dropdown)

Mapping to a button that opens a flyout menu with multiple options.

```md
---
title: Assign Shell Property
description: Assigns a shell property to selected elements.
ribbon:
    tab: Properties
    panel:
        label: 2D Properties
        item:
            label: Assign Property
            icon: layers
            flyout:
                - label: Shell
                  icon: square
                  shortcut: 'P, S'
                - label: Membrane
                  icon: layout
                - label: Composite Shell
                  icon: stack
    note: 'Select elements before assigning.'
---
```

### 3. Advanced Configuration

Using tooltips and notes for better user guidance.

```md
---
title: Run Linear Static Analysis
description: Submits a linear static solver job.
ribbon:
    tab: Analysis
    panel:
        label: Run
        item:
            label: Analyze
            icon: play-circle
            tooltip: 'Opens the solver submission dialog'
            flyout:
                - label: Linear Static
                  icon: activity
                  shortcut: 'F5'
                  tooltip: 'Sol 101 / OptiStruct Linear'
                - label: Normal Modes
                  icon: radio
                  shortcut: 'F6'
    note: 'Ensure a loadstep is defined before running.'
---
```

### 4. Inline MDX Usage

You can also use the `<RibbonPath />` component directly within your MDX documentation.

```mdx
<RibbonPath
    ribbon={{
        tab: 'Analysis',
        panel: {
            label: 'Run',
            item: {
                label: 'Analyze',
                flyout: [{ label: 'Linear Static', shortcut: 'F5' }],
            },
        },
        note: 'Ensure a loadstep is defined first.',
    }}
/>
```
