class TestMethod:
    def __init__(self) -> None:
        self.a = 0        

    def _set_values(self, a: int) -> None:
        self.a = a
    
    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b
    
    def sub(self, a: int, b: int) -> int:
        return a - b


if __name__ == "__main__":
    tm = TestMethod()
    print(f"tm.add         : {tm.add(1, 2)}")
    print(f"tm.sub         : {tm.sub(1, 2)}")

    print(f"TestMethod.add : {TestMethod.add(1, 2)}")
    # print(f"TestMethod.sub : {TestMethod.sub(1, 2)}")  # Error
