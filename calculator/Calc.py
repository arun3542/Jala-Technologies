from abc import ABC,abstractmethod


class Calc(ABC):

    @abstractmethod
    def doCalculation(self):
        pass

    @abstractmethod
    def getResult(self):
        pass