# psj-editor

**PSJ documentation & Python code generator** — full TypeScript rewrite.

Generates the `jupiterutils` Python package and IDE calltip data files from:

- A macro Python source tree (PSJ command signatures)
- A documentation website (Markdown files for utilities, dialogs, commands)
- Enum definition files (`input/*.txt`)

---

## What it generates

| Output file                     | Description                                                             |
| ------------------------------- | ----------------------------------------------------------------------- |
| `output/PSJ_Classes.py`         | Python class hierarchy mirroring the PSJ command namespace              |
| `output/Utility.py`             | `JPT` class with entity-type enums, D-entity factories, utility methods |
| `output/pyjdg.py`               | `JDGCreator` dialog class with all GUI method stubs                     |
| `output/__init__.py`            | Package init re-exporting all top-level classes                         |
| `output/PSJCommandCalltips.dat` | IDE autocomplete data for PSJ commands                                  |
| `output/PSJUtilityCalltips.dat` | IDE autocomplete data for JPT utilities                                 |
| `output/PSJGuiTooltip.dat`      | IDE autocomplete data for dialog functions                              |
| `IDEData.zip`                   | Zip of all three `.dat` files for IDE distribution                      |

Intermediate list files are also written to `output/` for debugging:
`PSJCmdFull.py`, `UtilityFull.py`, `DlgFull.py`.

---

## Requirements

- **Node.js** ≥ 18
- **npm** ≥ 9

---

## Setup

```bash
npm install
cp .env.example .env
# Edit .env with your WEB_ROOT and MACRO_ROOT paths
```

**.env variables:**

| Variable     | Description                                                                                         |
| ------------ | --------------------------------------------------------------------------------------------------- |
| `WEB_ROOT`   | Root of the documentation website (contains `docs/psj-command`, `docs/psj-utility`, `docs/psj-gui`) |
| `MACRO_ROOT` | Root of the Jupiter macro Python source tree                                                        |

---

## Usage

### Development (run with `tsx`, no build step)

```bash
npm run dev
# or
npm run generate
```

### Production (compile then run)

```bash
npm run build
npm start
```

---

## Pipeline

```
1. Load .env config
2. COLLECT
   ├─ Walk MACRO_ROOT/**/*.py  → PSJ command signatures
   ├─ Walk WEB_ROOT/docs/psj-utility/*.md  → utility function params
   ├─ Walk WEB_ROOT/docs/psj-gui/*.md  → dialog function params
   └─ Read input/*.txt  → entity-type enum values
3. Write intermediate list files  (output/PSJCmdFull.py, UtilityFull.py, DlgFull.py)
4. Generate Python source files  (PSJ_Classes.py, Utility.py, pyjdg.py, __init__.py)
5. Generate IDE calltip .dat files
6. Copy Python files  → jupiter_utils/jupiterutils/
7. Copy .dat files    → IDEData/
8. Create IDEData.zip
```

---

## Project structure

```
psj-editor/
├── src/
│   ├── index.ts                        # Entry point / pipeline orchestrator
│   ├── config.ts                       # .env loader & Config type
│   ├── logger.ts                       # Structured console logger
│   ├── utils.ts                        # Shared: file I/O, param parsing, cursor expansion
│   ├── types/
│   │   └── index.ts                    # All domain types (Param, PsjCommand, ClassTree, …)
│   ├── collectors/
│   │   ├── psjCommandCollector.ts      # Walk macro sources → PsjCommand[]
│   │   ├── utilFunctionCollector.ts    # Walk markdown docs → UtilFunction[]
│   │   ├── docReader.ts                # Read ## Description sections from .md files
│   │   └── entityTypeCollector.ts      # Parse input/*.txt enum files
│   ├── generators/
│   │   ├── classTreeBuilder.ts         # Flat PsjCommand[] → nested ClassTree
│   │   ├── psjClassesGenerator.ts      # ClassTree → PSJ_Classes.py
│   │   ├── utilityGenerator.ts         # Entities + utils → Utility.py
│   │   ├── pyjdgGenerator.ts           # Dialog functions → pyjdg.py
│   │   ├── initGenerator.ts            # ClassTree → __init__.py
│   │   └── calltipsGenerator.ts        # Commands/utils/dialogs → .dat files
│   └── writers/
│       ├── fileWriter.ts               # Atomic file writer
│       └── zipWriter.ts                # IDEData.zip creator (archiver)
├── input/                              # Entity type .txt files + calltips base
├── output/                             # Generated files (git-ignored)
├── IDEData/                            # .dat files for IDE (git-ignored)
├── .env.example
├── package.json
└── tsconfig.json
```

---

## Key design decisions vs. original

| Aspect            | Original                                    | Rewrite                                  |
| ----------------- | ------------------------------------------- | ---------------------------------------- |
| Directory walking | Rust binary (`psj-editor.exe`)              | Native `fs/promises` `readdir` recursion |
| CSV parsing       | `papaparse` (wrong tool — files aren't CSV) | Native line splitting                    |
| File writes       | Sequential `appendFile` chains              | Parallel `writeMany` with atomic rename  |
| Type safety       | Untyped `any` throughout                    | Strict TypeScript, zero `any`            |
| Module system     | CommonJS `require()`                        | ESM `import`                             |
| Async             | `promisify(fs.X)`                           | Native `fs/promises`                     |
| Zip               | `7z.exe` subprocess                         | `archiver` npm package                   |
| Structure         | Single 800-line file                        | 17 focused modules                       |
