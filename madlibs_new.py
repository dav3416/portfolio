import re

text = """Giraffes have aroused
 the curiosity of __PLURAL_NOUN__
 since the earliest times. The
 animal is the tallest of all
 living __PLURAL_NOUN__, but
 scienctists are unable to
 explain how it got its long
 __PART_OF_THE_BODY__. The
 giraffes's tremendos height,
 which might reach __NUMBER__
 __PLURAL_NOUN__, comes from
 its legs and __BODYPART__.
"""



def mad_libs(mls):
    hints = re.findall("__.*?__", mls)
    if hints is not None:
        for word in hints:
            q = "Enter a {}".format(word)
            new = input(q)
            mls = mls.replace(word, new, 1)
        print('\n')
        mls = mls.replace("\n", "")
        print(mls)
    else:
        print("invalid mls")

mad_libs(text)
        
            
