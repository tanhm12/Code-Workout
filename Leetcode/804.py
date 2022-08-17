from typing import List

def uniqueMorseRepresentations(words: List[str]):
    all_representations = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    offset = ord('a')
    get_representation = lambda x: ''.join([all_representations[ord(c) - offset] for c in x])
    return len(set([get_representation(word) for word in words]))

words = ["gin","zen","gig","msg"]

print(uniqueMorseRepresentations(words))
    
    