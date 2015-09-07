__author__ = 'kud'
formater = "%r %r %r %r"
print formater %(1,2,3,4)
print formater %("one", "two","three","four")
print formater %(True, False,True,False)
print formater %(
    "I had this sting",
    "And this one too",
    "Make it more difficult",
    "And you'll make a good"
)
print formater %(formater,formater,formater,formater)