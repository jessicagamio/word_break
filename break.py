
class Node(object):
    """Create Node"""
    def __init__(self, data, children = None):
        """Initializes instance"""
        self.data = data
        self.children = children or []

class Tree(object):
    """Creat Tree"""
    def __init__(self, root = None):
        if self.root == None:
            self.root = self
            



def createTreeNodes(phrase, vocab, idx=0):
    phrase_list = [char for char in phrase]
    phrase_set = set(phrase_list)

    # create a dictionary of the vocab words
    vocab_dictionary = {}

    for char in phrase_set:
        for word in vocab:
            if word.startswith(char):
                if  vocab_dictionary.get(char):
                    vocab_dictionary[char].append(word)     
                else:
                    vocab_dictionary[char] = [word]
                

    # creat node
    node = Node(phrase[idx])

    key = node.data

    words = vocab_dictionary.get(key)

    if words:
        print('words------->',words)
        # check to see if current phrase starts with words from dictionary
        for word in words:
            if phrase[idx:].startswith(word):
                node.children.append(word)
                print('child------------>', word)

        # Use len of each child and add on to index to analyze next phrase
        for child in node.children:
            new_idx = idx + len(child)
            createTreeNodes(phrase[new_idx:], vocab, idx = new_idx)





def parse(phrase, vocab, index=0):
    """return a set of all possible phrases using vocabulary words"""

    sentences = Tree(createTreeNodes(phrase, vocab))


    # Traverse tree depth first to find all possible sentences

    
vocab = {'i', 'a', 'ten', 'oodles', 'ford', 'inner', 'to', 'night', 'ate', 'noodles', 'for', 'dinner', 'tonight'}
createTreeNodes('iatenoodlesfordinnertonight', vocab)












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