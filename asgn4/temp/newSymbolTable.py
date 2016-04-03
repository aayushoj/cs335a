class SymbolTable:

    def __init__(self):
        self.symbolTable = {
                'main' : {
                    'name' : 'main',
                    'type' : 'main',
                    'parent' : None,
                    'identifiers' : {},
                    }
                }
        self.currentScope = 'main'
        self.tstart = "t"
        self.tNo = -1
        self.blockBase = "b"
        self.blockNo = -1
        self.wordSize = 4
        self.addressSize = 4

    def addBlock(self):
        bName = self.createBlockName()
        self.symbolTable[bName] = {
                'name' : bName,
                'type' : 'block',
                'parent' : self.currentScope,
                'identifiers' : {},
                }
        self.currentScope = bName

    def endBlock(self):
        self.currentScope = self.symbolTable[self.currentScope]['parent']

    def addIdentifier(self, idenName, place, idenType = 'unknown', idenSize = 0):
        if idenSize == 0:
            idenSize = self.getSize(idenType)
        scope = self.lookUpScope(idenName)
        if scope == None:
            self.symbolTable[self.currentScope]['identifiers'][idenName] = {
                    'place' : place,
                    'type' : idenType,
                    'size' : idenSize
                    }
        # print(self.symbolTable[self.currentScope]['identifiers'])

    def lookupIdentifier(self, idenName):
        scope = self.lookUpScope(idenName)
        # print(scope)
        if(scope == None):
            return False
        else:
            return scope

    def getIdentifierAttributes(self, idenName):
        idenScope = self.lookUpScope(idenName)
        if idenScope == None:
            return None
        else:
            return self.symbolTable[idenScope]['identifiers'].get(idenName)

    def getAttribute(self, idenName, attrName):
        idenScope = self.lookUpScope(idenName)
        if idenScope != None:
            return  self.symbolTable[idenScope]['identifiers'][idenName].get(attrName)
        else:
            return None

    def addAttribute(self, idenName, attrName, attrVal):
        idenScope = self.lookUpScope(idenName)
        if idenScope != None:
            self.symbolTable[self.lookUpScope(idenName)]['identifiers'][idenName][attrName] = attrVal
            return 1
        else:
            return 0

    def getSize(self, typeExpr):
        if typeExpr in ['INT', 'BOOL', 'FLOAT', 'CHAR', 'VOID' ]:
            return self.wordSize
        elif typeExpr[0] == 'STRING':
            return self.addressSize
        elif typeExpr[0] == 'ARRAY':
            return self.addressSize
        else:
            assert(False)


    def createTemp(self):
        self.tNo += 1
        return self.tstart + str(self.tNo)

    def createBlockName(self):
        self.blockNo += 1
        return self.blockBase + str(self.blockNo)

    def lookUpScope(self, idenName):
        scope = self.currentScope
        while self.symbolTable[scope]['type'] not in ['main']:
            if idenName in self.symbolTable[scope]['identifiers']:
                return scope
            scope = self.symbolTable[scope]['parent']

        if idenName in self.symbolTable[scope]['identifiers']:
            return scope

        return None

