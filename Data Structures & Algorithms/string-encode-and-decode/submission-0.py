class Solution:
    # Trick, what is the way to encode so that you dont over encode etc, as any ascii character can appear
    def encode(self, strs: List[str]) -> str:
        # We can guarantee the first number be our number, thus we can say how long the next word is, and then the first after that is ours again etc
        encoded = ""
        for string in strs:
            n = str(len(string))
            encoded += n+"#"+string
        return encoded

    def decode(self, s: str) -> List[str]:
        # First is the length of the first element in the list etc
        left,right = 0,0

        res = []
        while left < len(s):
            if s[right] == "#": # Found the length
                str_len = int(s[left:right])
                start_str = right+1
                end_str = right+1+str_len

                string_to_add = s[start_str: end_str]
                res.append(string_to_add)

                left = end_str
                right = end_str
            else:
                right += 1
            
        return res