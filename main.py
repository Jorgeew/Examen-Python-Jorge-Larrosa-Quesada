import functions

dictWine = functions.read_data()
dictWhite, dictRed = functions.split(dictWine)
list = functions.reduce(dictWhite, 'PH')
