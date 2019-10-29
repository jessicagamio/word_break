
def parse(phrase, vocab):
    """return a set of all possible phrases using vocabulary words"""



    # Break the given phrase into vocab words

        # iterate through phrase
            # add char into a temp_word container 
            # check to see if temp_word in vocabulary set
            # if temp_sentence in vocabulary set
                # Add a space to temp_sentence

            # if temp word NOT in vocabulary
                # continue adding char to temp_sentence 

        # Add phrase into sentence set


    # Run through phrase from left to right

        # temp_sentence is an empty string
        # iterate throught sentence
            # if temp_sentence in vocab set
                # add space t0 temp sentence
            # if temp_sentence not in vocab set
                # add character to temp sentence


    # Run through phrase from right to left
        # temp sentence is empty
        # split sentence into sentence list by spacs
        # reverse sentence list
        # Join rev_senetency by spaces

        # temp_sentence is an empty string
        # iterate throught rev_sentence
            # if temp_sentence in vocab set
                # add space t0 temp sentence
            # if temp_sentence not in vocab set
                # add character to temp sentence





class TestFunction(unittest.TestCase):
    def test(self):
        vocab = {'i', 'a', 'ten', 'oodles', 'ford', 'inner', 'to', 'night', 'ate', 'noodles', 'for', 'dinner', 'tonight'}
        self.assertEqual(parse('iatenoodlesfordinnertonight', vocab), 
            {
                    "i a ten oodles for dinner to night",
                    "i a ten oodles for dinner tonight",
                    "i a ten oodles ford inner to night",
                    "i a ten oodles ford inner tonight",
                    "i ate noodles for dinner to night",
                    "i ate noodles for dinner tonight",
                    "i ate noodles ford inner to night",
                    "i ate noodles ford inner tonight"
                }
                )


if __name__=="__main__":
    unittest.main()