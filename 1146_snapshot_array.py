import bisect
class SnapshotArray:
    def __init__(self, length: int):
        self.snap_id = 0
        self.array = [[[0, 0]] for _ in range(length)]
        
    def set(self, index: int, val: int) -> None:
        if self.array[index][-1][0] == self.snap_id:
            self.array[index][-1][1] = val
        else:
            self.array[index].append([self.snap_id, val])

    def snap(self) -> int:
        curr = self.snap_id
        self.snap_id += 1
        return curr

    def get(self, index: int, snap_id: int) -> int:
        history = self.array[index]
        ind = bisect.bisect_right(history, snap_id, key=lambda x: x[0]) - 1
        return self.array[index][ind][1]
        

snapshotArr = SnapshotArray(3) # set the length to be 3
snapshotArr.set(0,5) # Set array[0] = 5
snapshotArr.snap() # Take a snapshot, return snap_id = 0
snapshotArr.set(0,6);
print(snapshotArr.get(0,0)) # Get the value of array[0] with snap_id = 0, return 5

snapshotArr = SnapshotArray(4) # set the length to be 4
snapshotArr.snap() # Take a snapshot, return snap_id = 0
snapshotArr.snap() # Take a snapshot, return snap_id = 0
snapshotArr.get(3,1) # Set array[0] = 5
snapshotArr.set(2,4);
print(snapshotArr.get(1,4)) # Get the value of array[0] with snap_id = 0, return 5

snapshotArr = SnapshotArray(3) # set the length to be 4
snapshotArr.set(1,6)
snapshotArr.snap() # Take a snapshot, return snap_id = 0
snapshotArr.snap() # Take a snapshot, return snap_id = 0
snapshotArr.get(1,19) # Set array[0] = 5
snapshotArr.set(0,4)
print(snapshotArr.get(2,1)) # Get the value of array[0] with snap_id = 0, return 5
print(snapshotArr.get(2,0)) # Get the value of array[0] with snap_id = 0, return 5
print(snapshotArr.get(0,1)) # Get the value of array[0] with snap_id = 0, return 5