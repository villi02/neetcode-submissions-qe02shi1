class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            n = str(len(string))
            encoded += n+"#"+string
        return encoded

    def decode(self, s: str) -> List[str]:
        left,right = 0,0

        res = []
        while left < len(s):
            if s[right] == "#":
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