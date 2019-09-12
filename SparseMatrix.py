class SparseMatrix:
    # Create a sparse matrix of size numRows x numCols initialized to 0.

    def __init__(self, numRows, numCols):
        self._numRows = numRows
        self._numCols = numCols
        self._elementList = list()

    def numRows(self):
        return self._numRows

    def numCols(self):
        return self._numCols

    def __setitem__(self, ndxTuple, scalar):
        ndx = self._findPosition( ndxTuple[0], ndxTuple[1])
        if ndx is not None:  # if the element is found in the list.
            if scalar != 0.0:
                self._elementList[ndx].value = scalar
            else:
                self._elementList.pop(ndx)
        else:  # if the element is zero and not in the list.
            if scalar != 0.0:
                element = _MatrixElement(ndxTuple[0], ndxTuple[1], scalar)
                self._elementList.append(element)

    def __getitem__(self, ndxTuple):
        ndx = self._findElement(ndxTuple[0], ndxTuple[1])
        if ndx is not None:
            return self._elementList.value
        return None

    def _findPosition(self, row, col):
        n = len(self._elementList)
        for i in range(n):
            if row == self._elementList[i].row and col == self._elementList[i].col:
                return i  # return the index of the element if found.
        return None

    def getvalue(self, row, col):
        n = len(self._elementList)
        for i in range(n):
            if row == self._elementList[i].row and col == self._elementList[i].col:
                return self._elementList[i].value  # return the index of the element if found.
        return None

class _MatrixElement:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value


if __name__ == '__main__':
    spm = SparseMatrix(3, 3)
    tp = (0,3)
    spm.__setitem__(tp, 3)
    print(spm.numCols())
    print(spm.numRows())
    print(spm._findPosition(0,3))
    print(spm.getvalue(0, 3))


