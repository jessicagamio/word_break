
def parse(phrase, vocab):
    """return a set of all possible phrases using vocabulary words"""



    # Break the 



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