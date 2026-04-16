# Title:   JPT.GetDocumentByID()
# Desc:    Get information of an indicated document by using its ID
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-utility/PSJ-Utility_GetDocumentByID
# ---
doc = JPT.CreateNewDocument()
docInfor = JPT.GetDocumentByID(doc.docID)  # [hl]
JPT.Debugger(docInfor)
