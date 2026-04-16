# Title:   Assembly.RightClick.TransferDocumentData()
# Desc:    Transfer data information of entity between documents
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/assembly/Assembly.RightClick.TransferDocumentData
# ---
# Create a Cube in document 1: Jupiter1
Geometry.Part.Cube()

# Copy/Transfer Cube into document 2: Jupiter2
result = Assembly.RightClick.TransferDocumentData(strSourceDocTitle="Jupiter1", strDestDocTitle="Jupiter2",  # [hl:start]
    crlParts=[Part(1)], strlNewPartName=[])  # [hl:end]

JPT.Debugger(result)
