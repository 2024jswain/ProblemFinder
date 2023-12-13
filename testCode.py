from GPTanalysis import GPTanalysis
from reviewCollector import reviewCollector


def GPTKeyTest():

    goodKey = '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'
    badKey = "iamabadapikeymwhahahahah"


    testGTPgoodkey = GPTanalysis(goodKey)
    testGTPbadkey = GPTanalysis(badKey)

    return testGTPgoodkey.testKey() and not testGTPbadkey.testKey()



def ASINKeyTest():

    goodKey = 'C5C4760E665B4FDEB257AEB14D5073D1'
    badKey = "iamabadapikeymwhahahahah"


    testASINkgoodkey = reviewCollector(goodKey)
    testASINbadkey = reviewCollector(badKey)


    return testASINkgoodkey.testKey() and not testASINbadkey.testKey()


