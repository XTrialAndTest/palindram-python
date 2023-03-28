returnedPalendram=[]
def palendramTester(str):
    theWholeList = open(str, "r")
   
    for i in theWholeList:
        if i.endswith('\n'):
            trimmed=i[:-1]
         

            split=list(trimmed)
            joint=''.join(split)
            split.reverse()
            rev=''.join(split).lower()
            if trimmed.lower()==rev.lower():
                returnedPalendram.append(trimmed)
        else:
            trimmed=i
            split=list(trimmed)
            joint=''.join(split)
            split.reverse()
            rev=''.join(split).lower()
            
            if trimmed.lower()==rev.lower():
                returnedPalendram.append(trimmed)
        
    return returnedPalendram
        
  
print(palendramTester(".\palindram\words_in_english_dictionary (1).txt"))