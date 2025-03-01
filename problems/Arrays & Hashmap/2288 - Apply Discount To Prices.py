#Summary: Return upto 2 decimal places of the sentence with the discount applied to the prices.
# so $1 will become $0.50 if the discount is 50%.


def discountPrices(self, sentence, discount):
    arr = sentence.split()
    for i,word in enumerate(arr):
        if word[0] == '$' and word[1:].replace('.','').isdigit():
            discounted_price = (float(word[1:]) * discount / 100) if discount < 100 else 0
            
            arr[i] = '${:.2f}'.format(int(word[1:]) - discounted_price) if discount < 100 else '$0.00'
    return " ".join(arr)



sentence = "there are $1 $2 and 5$ candies in the shop"
discount = 50
print(discountPrices(sentence, discount)) # "there are $0.5 $1 and 5$ candies in the shop"

#Learning: how to use format - {:.2f} is used to format the float to 2 decimal places. and then the . format is used to replace the word with the formatted float.

#Time complexity: O(n) where n is the length of the sentence.
#Space complexity: O(n) where n is the length of the sentence. We are storing the sentence in an array

