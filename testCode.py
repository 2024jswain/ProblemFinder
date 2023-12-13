from GPTanalysis import GPTanalysis
from reviewCollector import reviewCollector


def GPTKeyTest():

    goodKey = ''
    badKey = "iamabadapikeymwhahahahah"


    testGTPgoodkey = GPTanalysis(goodKey)
    testGTPbadkey = GPTanalysis(badKey)

    return testGTPgoodkey.testKey() and not testGTPbadkey.testKey()



def ASINKeyTest():

    goodKey = ''
    badKey = "iamabadapikeymwhahahahah"


    testASINkgoodkey = reviewCollector(goodKey)
    testASINbadkey = reviewCollector(badKey)


    return testASINkgoodkey.testKey() and not testASINbadkey.testKey()


