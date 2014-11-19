# singleton
def singleton(cls, *args, **kw):  
    instances = {}  
    def _singleton():  
        if cls not in instances:  
            instances[cls] = cls(*args, **kw)  
        return instances[cls]  
    return _singleton  

# abstract factory     
class AbstractRichie(object):
    def TestCPU(self): pass
    def TestMMU(self): pass
    def TestMotherboard(self): pass
    def GetConcreteRichie(type):
        if type == "RICHIE": return Richie()
        if type == "ADVANCEDRICHIE": return AdvancedRichie()
        if type == "SUPERRICHIE": return SuperRichie()
        if type == "ULTRARICHIE": return UltraRichie()
        assert 0, "Bad creation: " + type
    GetConcreteRichie = staticmethod(GetConcreteRichie)

# concrete factory
@singleton 
class Richie(AbstractRichie):
    def __init__(self):
        super(AbstractRichie, self).__init__()
        self.CPU = CPUOfRichie()
        self.MMU = MMUOfRichie()
        self.Motherboard = MotherboardOfRichie()
    def TestCPU(self): self.CPU.test()
    def TestMMU(self): self.MMU.test()
    def TestMotherboard(self): self.Motherboard.test()
    
@singleton 
class AdvancedRichie(AbstractRichie):
    def __init__(self):
        super(AbstractRichie, self).__init__()
        self.CPU = CPUOfAdvancedRichie()
        self.MMU = MMUOfAdvancedRichie()
        self.Motherboard = MotherboardOfAdvancedRichie()
    def TestCPU(self): self.CPU.test()
    def TestMMU(self): self.MMU.test()
    def TestMotherboard(self): self.Motherboard.test()

@singleton 
class SuperRichie(AbstractRichie):
    def __init__(self):
        super(AbstractRichie, self).__init__()
        self.CPU = CPUOfSuperRichie()
        self.MMU = MMUOfSuperRichie()
        self.Motherboard = MotherboardOfSuperRichie()
    def TestCPU(self): self.CPU.test()
    def TestMMU(self): self.MMU.test()
    def TestMotherboard(self): self.Motherboard.test()

@singleton 
class UltraRichie(AbstractRichie):
    def __init__(self):
        super(AbstractRichie, self).__init__()
        self.CPU = CPUOfUltraRichie()
        self.MMU = MMUOfUltraRichie()
        self.Motherboard = MotherboardOfUltraRichie()
    def TestCPU(self): self.CPU.test()
    def TestMMU(self): self.MMU.test()
    def TestMotherboard(self): self.Motherboard.test()

# abstract product
class CPU(object):
    def test(self): pass
class MMU(object):
    def test(self): pass
class Motherboard(object):
    def test(self): pass

# concrete product
class CPUOfRichie(CPU):
    def __init__(self): super(CPU, self).__init__()
    def test(self): print("Test on Richie's CPU")
class CPUOfAdvancedRichie(CPU):
    def __init__(self): super(CPU, self).__init__()
    def test(self): print("Test on Advanced Richie's CPU")
class CPUOfSuperRichie(CPU):
    def __init__(self): super(CPU, self).__init__()
    def test(self): print("Test on Super Richie's CPU")
class CPUOfUltraRichie(CPU):
    def __init__(self): super(CPU, self).__init__()
    def test(self): print("Test on Ultra Richie's CPU")

class MMUOfRichie(MMU):
    def __init__(self): super(MMU, self).__init__()
    def test(self): print("Test on Richie's MMU")
class MMUOfAdvancedRichie(MMU):
    def __init__(self): super(MMU, self).__init__()
    def test(self): print("Test on Advanced Richie's MMU")
class MMUOfSuperRichie(MMU):
    def __init__(self): super(MMU, self).__init__()
    def test(self): print("Test on Super Richie's MMU")
class MMUOfUltraRichie(MMU):
    def __init__(self): super(MMU, self).__init__()
    def test(self): print("Test on Ultra Richie's MMU")

class MotherboardOfRichie(Motherboard):
    def __init__(self): super(Motherboard, self).__init__()
    def test(self): print("Test on Richie's Motherboard")
class MotherboardOfAdvancedRichie(Motherboard):
    def __init__(self): super(Motherboard, self).__init__()    
    def test(self): print("Test on Advanced Richie's Motherboard")
class MotherboardOfSuperRichie(Motherboard):
    def __init__(self): super(Motherboard, self).__init__()    
    def test(self): print("Test on Super Richie's Motherboard")
class MotherboardOfUltraRichie(Motherboard):
    def __init__(self): super(Motherboard, self).__init__()
    def test(self): print("Test on Ultra Richie's Motherboard")



if __name__ == '__main__':
    print("---Start Diagnostics on Different Architectures---")
    ConcreteRichie = AbstractRichie.GetConcreteRichie("RICHIE")
    ConcreteRichie.TestCPU()
    ConcreteRichie.TestMMU()
    ConcreteRichie.TestMotherboard()

    ConcreteRichie = AbstractRichie.GetConcreteRichie("ADVANCEDRICHIE")
    ConcreteRichie.TestCPU()
    ConcreteRichie.TestMMU()
    ConcreteRichie.TestMotherboard()

    ConcreteRichie = AbstractRichie.GetConcreteRichie("SUPERRICHIE")
    ConcreteRichie.TestCPU()
    ConcreteRichie.TestMMU()
    ConcreteRichie.TestMotherboard()

    ConcreteRichie = AbstractRichie.GetConcreteRichie("ULTRARICHIE")
    ConcreteRichie.TestCPU()
    ConcreteRichie.TestMMU()
    ConcreteRichie.TestMotherboard()

    print("\n---Test Singleton---\n"
          +"Compare two ConcreteRichies instances created consecutively with same parameter, \"True\" means these two ConcreteRichies are the same one.")
    one = AbstractRichie.GetConcreteRichie("RICHIE")
    two = AbstractRichie.GetConcreteRichie("RICHIE")
    print "Test Singleton Result: ", one == two 
