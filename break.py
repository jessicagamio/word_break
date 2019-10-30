
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
    print('list--->',phrase_list)
    phrase_set = set(phrase_list)
    print('set--->', phrase_set)

    # create a dictionary of the vocab words
    vocab_dictionary = {}

    for char in phrase_set:
        for word in vocab:
            # print('vocab-------.', vocab)
            print('char -->',char, '| word --->', word)
            if word.startswith(char):
                print(word, ' start with ', char)
                if  vocab_dictionary[char]!=[]:
                    vocab_dictionary[char] = vocab_dictionary[char].append(word)
                    print('dictionary--->', vocab_dictionary[char])
                vocab_dictionary[char] = [word]




    # creat node
    node = Node(phrase[idx])

    key = node.data

    for data in vocab_dictionary[key]:
        if phrase[idx:].startswith(data):
            node.children.append(data)
            print('char------------>', data)

    for child in node.children:
        new_idx = idx + len(child)
        createTreeNodes(phrase[new_idx:], vocab, idx = new_idx)





# def parse(phrase, vocab, index=0):
#     """return a set of all possible phrases using vocabulary words"""

#     return sentences = Tree(createTreeNodes(phrase, vocab))


    # Traverse tree
    
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