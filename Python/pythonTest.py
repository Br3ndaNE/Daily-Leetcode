
class Rectangle:
    x = 0
    y = 0
    z = 0

    def __init__(self, value1, value2, value3):
        self.x = value1
        self.y = value2
        self.z = value3
    
    def Getter(self):
        print(self.x)
        print(self.y)
        print(self.z)

    def Setter(self, value1, value2, value3):
        self.x = value1
        self.y = value2
        self.z = value3

# objRect = Rectangle(1,2,3)
# objRect.Getter()
# objRect.Setter(110,151,3)
# objRect.Getter()


lst = [1,6,43,2,10,123]

def sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-1):
            if(lst[j+1] > lst[j]):
                lst[j], lst[j+1] = lst[j+1], lst[j]
                print(lst)
            
    return(lst)

lst2 = ["kommetje", "komkommer", "komhier"]

def prefix(lst):
    mostCommonPrefix = lst[0]
    for i in range(1, len(lst)):
        # Compare the prefix with the current string up to the length of the prefix
        for j in range(len(mostCommonPrefix)):
            # If characters don't match or we've reached the end of the current string
            if j == len(lst[i]) or lst[i][j] != mostCommonPrefix[j]:
                mostCommonPrefix = mostCommonPrefix[:j]  # Trim the prefix
                break  # No need to check further with the current string
        # If the prefix is reduced to an empty string, no need to continue
        if not mostCommonPrefix:
            return ""

    return mostCommonPrefix

print(prefix(lst2))