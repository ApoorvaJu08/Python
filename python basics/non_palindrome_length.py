
def reverse(s):
    return s[::-1]

def isNotPalindrome(s):
    r = reverse(s)
    if s != r:
        return True
    return False

s = input()
n = len(s)
l = [s[i:j+1] for i in range(n) for j in range(i, n)]
np, max_list = [], []
for i in range(len(l)):
    ans = isNotPalindrome(l[i])
    if ans == 1:
        np.append(l[i])
max_list = [len(np[i]) for i in range(len(np))]
print(max(max_list))