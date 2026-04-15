class Solution:
    
    def plusOne(self, digits: List[int]) -> List[int]:
        # Step 1: Combine list of ints into a single string
        string = ""
        for i in range(len(digits)):
            string = string + str(digits[i])
            
        # Step 2: Convert to int and increment
        number = int(string)
        number = number + 1
        
        # Step 3: Convert back to string to separate digits
        string2 = str(number)
        
        # Step 4: Convert each char back to an int in a new list
        list2 = []
        for char in string2:
            list2.append(int(char))
            
        return list2