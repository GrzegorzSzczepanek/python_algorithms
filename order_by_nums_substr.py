def order(sentence):
    nums = list("123456789")
    answer = ["","","","","","","","",""]
    for word in sentence.split(" "):
        for char in word:
            if char in nums:
                answer[int(char) - 1] = word
                
    
    return " ".join(list(filter( lambda x: x!="" ,answer)))
