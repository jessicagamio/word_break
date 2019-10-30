
class Node(object):
    """Create Node"""
    def __init__(self, data):
        """Initializes instance"""
        self.data = data
        self.children = []

class Tree(object):
    """Creat Tree"""
    def __init__(self):
        self.root = None
            




def parse(phrase, vocab, index=0):
    """return a set of all possible phrases using vocabulary words"""

    # Create a dictionary of vocab words

    phrase_list = phrase.split('')
    phrase_set = set(phrase_list)

    vocab_dictionary = {}

    for char in phrase_set:
        for word in vocab:
            if word.startswith(char):
                if  vocab_dictionary[char]:
                    vocab_dictionary[char] += word
                vocab_dictionary[char] = word

    







    # # Break the given phrase into vocab words

    #     # iterate through phrase
    #         # add char into a temp_word container 
    #         # check to see if temp_word in vocabulary set
    #         # if temp_sentence in vocabulary set
    #             # Add a space to temp_sentence

    #         # if temp word NOT in vocabulary
    #             # continue adding char to temp_sentence 

    #     # Add phrase into sentence set



    # # Run through phrase from right to left
     
    # sentences=set()
    # temp_sentence = ""
    # temp_word = ""

    # for char in phrase:
    #     temp_word+= char

    #     if temp_word in vocab:
    #         temp_sentence += temp_word + " "
    #         temp_word = ""       

    # print('sentence ====>', temp_sentence)

    # sentence = temp_sentence
    # sentences.add(sentence)
    # # sentences.add(read_rightToLeft(sentence))

    
    # for sentence in sentences:

    #     print('set of sentences....',sentence)


vocab = {'i', 'a', 'ten', 'oodles', 'ford', 'inner', 'to', 'night', 'ate', 'noodles', 'for', 'dinner', 'tonight'}
parse('iatenoodlesfordinnertonight', vocab) 


# class TestFunction(unittest.TestCase):
#     def test(self):
#         vocab = {'i', 'a', 'ten', 'oodles', 'ford', 'inner', 'to', 'night', 'ate', 'noodles', 'for', 'dinner', 'tonight'}
#         self.assertEqual(parse('iatenoodlesfordinnertonight', vocab), 
#             {
#                     "i a ten oodles for dinner to night",
#                     "i a ten oodles for dinner tonight",
#                     "i a ten oodles ford inner to night",
#                     "i a ten oodles ford inner tonight",
#                     "i ate noodles for dinner to night",
#                     "i ate noodles for dinner tonight",
#                     "i ate noodles ford inner to night",
#                     "i ate noodles ford inner tonight"
#                 }
#                 )


# if __name__=="__main__":
#     unittest.main()