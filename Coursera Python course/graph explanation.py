samplePassage = "Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."

def freqAll(samplePassage):
    wordlist = samplePassage.split(' ')

    freqMap = {}
    for word in wordlist: 
        freqMap[word] = wordlist.count(word) #masukkin  value di iteration ke dictionary freqMap
    print(freqMap)
    return freqMap #biar misalnya functionnya dipanggil dan di print ngasih liat value variable yg dipakein function ini


wordMap = freqAll(samplePassage)

print(wordMap)
