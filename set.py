class Set:
    def __init__(self) -> None:
        
        self._elemets=[]
    
    def __len__(self):

        return len(self._elemets)
    
    def __contains__(self, element):

        return element in self._elemets
    


    def add(self,element):
        if element in self:
            return
        self._elemets.append(element)
    
    def remove(self,element):
        assert element in self, 'This value doesnot exist in the set'
        self._elemets.remove(element)

    def isSubsetOf(self, setB):
        for element in self:
            if element not in setB:
                return False
        return True
    
    def __eq__(self,setB):
        if len(self)!=len(setB):
            return False
        return self.isSubsetOf(setB)
    
    def union(self, setB):
        newset=Set()
        newset._elemets.extend(self._elemets)
        for element in setB:
            newset.add(element)
        return newset
    
    def intersection(self, setB):
        newset=Set()
        for element in self:
            if element in setB:
                newset.add(element)
        return newset
    
    def difference(self, setB):
        newset=Set()
        newset._elemets.extend(self._elemets)
        common_emement=self.intersection(setB)
        for element in common_emement:
            newset.remove(element)
        return newset
    
    def __iter__(self):

        return iter(self._elemets)

    def __str__(self):

        return str(self._elemets)

if __name__=='__main__':
    A=Set()
    B=Set()
    A.add('english')
    A.add('math')
    A.add('physics')
    A.add('chemistry')
    A.add('biology')

    B.add('english')
    B.add('math')
    B.add('History')
    B.add('Arts')
    B.add('Psychology')

    C=A.union(B)
    D=A.intersection(B)
    DD=B.intersection(A)
    print(A==B)
    print(D==DD)
    E=B.difference(A)
    print(A)
    print(B)
    print(C)
    print(D)
    print(E)