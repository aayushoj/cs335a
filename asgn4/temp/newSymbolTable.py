class SystemTable:

    def __init__(self):
        self.SystemTable = {
                'main' : {
                    'name' : 'main',
                    'identifiers' : {},
                    'type' : 'main',
                    'parent' : None,
                    }
                }
        self.currScope = 'main'
        self.tNo = -1
        self.scopeNo = -1

    def newScope(self):
        scope = self.newScopeName()
        self.SystemTable[scope] = {
                'name' : scope,
                'identifiers' : {},
                'type' : 'scope',
                'parent' : self.currScope,
                }
        self.currScope = scope

    def endScope(self):
        self.currScope = self.SystemTable[self.currScope]['parent']

    def variableAdd(self, idVal, place, idType, idSize = 4):
        if idSize == 0:
            idSize = self.getSize(idType)
        scope = self.getScope(idVal)
        if scope == None:
            sc = str(self.currScope)+'_'+place
            self.SystemTable[self.currScope]['identifiers'][idVal] = {
                    'place' : sc,
                    'type' : idType,
                    'size' : idSize
                    }
        # print(self.SystemTable[self.currScope]['identifiers'])

    def variableSearch(self, idVal):
        scope = self.getScope(idVal)
        # print(scope)
        if(scope == None):
            return False
        else:
            return scope

    def getAttr(self, idVal, attrName):
        scope = self.getScope(idVal)
        if scope != None:
            return  self.SystemTable[scope]['identifiers'][idVal].get(attrName)
        else:
            return None

    def addAttr(self, idVal, attrName, attrVal):
        scope = self.getScope(idVal)
        if scope != None:
            self.SystemTable[self.getScope(idVal)]['identifiers'][idVal][attrName] = attrVal
            return True
            # print("Success")
        else:
            #print("Fail")
            return False

    def getSize(self, typeExpr):
        if typeExpr in ['INT', 'BOOL', 'FLOAT', 'CHAR', 'VOID' ]:
            return 4

    def getScope(self, idVal):
        scope = self.currScope
        while self.SystemTable[scope]['type'] not in ['main']:
            if idVal in self.SystemTable[scope]['identifiers']:
                return scope
            scope = self.SystemTable[scope]['parent']

        if idVal in self.SystemTable[scope]['identifiers']:
            return scope
        return None

    def getTemp(self):
        self.tNo += 1
        newTemp = "t"+str(self.tNo) 
        return newTemp

    def newScopeName(self):
        self.scopeNo += 1
        newScope = "s"+str(self.scopeNo) 
        return newScope


