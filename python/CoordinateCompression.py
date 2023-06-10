class CoordinateCompression:
    def __init__(self) -> None:
        self.coordinate = set()
        self.compression = dict()

    def add(self, x):
        self.coordinate.add(x)
        return self

    def produce(self):
        sorted(self.coordinate)
        self.compression = {j: i for i, j in enumerate(self.coordinate)}
        return self

    def __getitem__(self, x) -> int:
        if not self.compression:
            # call self.produce before getitem
            raise Exception
        return self.compression[x]

    def __len__(self) -> int:
        return len(self.compression)
