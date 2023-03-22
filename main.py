import functions

dictWine = functions.read_data()
dictWhite, dictRed = functions.split(dictWine)
functions.reduce(dictWhite, 'PH')
