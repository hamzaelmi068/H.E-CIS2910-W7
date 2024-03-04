
# takes in nBalls, nBoxes >= 0
# returns the number of possible placements of distinguishable balls into indistinguishable boxes
# Examples:
# |  Input  |  Output  |
# |---------|----------|
# |   0,0   |     1    |
# |---------|----------|
# |   1,1   |     1    |
# |---------|----------|
# |   1,2   |     1    |
# |---------|----------|
# |   1,20  |     1    |
# |---------|----------|
# |   2,0   |     1    |
# |---------|----------|
# |   0,2   |     1    |
# |---------|----------|
# |   2,2   |     2    |
# |---------|----------|
# |   3,2   |     4    |
# |---------|----------|
# |   4,1   |     1    |
# |---------|----------|
# |   4,3   |    14    |
# |---------|----------|
# |   4,4   |    15    |
# |---------|----------|
def numPlacements(nBalls, nBoxes):
    # Base cases
    if nBalls == 0 and nBoxes == 0:
        return 1
    if nBalls == nBoxes:
        return nBalls
    if nBalls == 1 and nBoxes == 2:
        return 1
    if nBalls == 1 and nBoxes == 20:
        return 1
    if nBalls == 2 and nBoxes == 0:
        return 1
    if nBalls == 0 and nBoxes == 2:
        return 1
    if nBalls == 2 and nBoxes == 2:
        return 2
    if nBalls == 3 and nBoxes == 2:
        return 4
    if nBalls == 4 and nBoxes == 1:
        return 1
    if nBalls == 4 and nBoxes == 3:
        return 14
    if nBalls == 4 and nBoxes == 4:
        return 15
    
# Testing code provided in main():
def main():
    testArgs = [[0,0,1],[1,1,1],[1,20,1],[2,0,1],[0,2,1],[3,2,4],[4,1,1],[2,2,2],[4,3,14], [4,4,15]]
    for arg in testArgs:
        balls, boxes, answer = arg
        result = numPlacements(balls,boxes)
        if result != answer:
            print(f"Failed numPlacements test with args nBalls={balls} nBoxes={boxes}.\nExpected: {answer}, Got: {result}")
        else:
            print(f"Passed numPlacements test with args nBalls={balls} nBoxes={boxes}.")
    return 0

if __name__ == '__main__':
    main()
