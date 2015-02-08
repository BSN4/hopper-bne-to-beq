def writeByteAndPreserveProc(seg,instr_adr,adr,b):
	proc = seg.getProcedureAtAddress(instr_adr)
	entry = proc.getEntryPoint() if proc != None else Segment.BAD_ADDRESS
	seg.writeByte(adr, b)
	seg.markAsCode(instr_adr)
	if entry != Segment.BAD_ADDRESS:
		seg.markAsProcedure(entry)
	
doc = Document.getCurrentDocument()
seg = doc.getCurrentSegment()
adr = doc.getCurrentAddress()
b = seg.readByte(adr + 1)
print(b)

writeByteAndPreserveProc(seg, adr, adr + 1, b ^ 1)
