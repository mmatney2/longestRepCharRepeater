
    #update output 
    #determine longest possible repeater based on k
    #if 2 indeces are k or less apart, replace those
    #if 2 indeces are 0 apart, add to window 
    #if there's a lot of single letter that are k or less aparrt and that could equal a big string, need those indeces...so need to get all indeces...hashmap? 
def charReplacement(s, k):
    count = {}
    res = 0

    l=0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        while (r - l + 1) - max(count.values()) > k: #MAKE sure current window is valid (length) subtracted by the count of the most frequent char = to the number of replacements we have to do and if it's greater than k (the number of replacements allowed), we shift left pointer. But before we do, take the count of the char at the left position and decriment it by 1
            count[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)
    return res
print(charReplacement('ABRVCD', 2))

#so in this on, we're going to get the longest chain of letters that are the same and replace k letters. so that means, setting up a window, and decrement left pointer if window is too big to replace k letters and increase the window if you get a 'same' letter to expand the window and get 