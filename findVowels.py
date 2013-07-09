#find the word with 'aeiou' in order
#-*-coding:UTF-8-*-
#导入dictionary字典文件
filedate=open('c:\doc.txt','r')

#定义文件格式整理函数
def cleanWord(word):
    return word.strip().lower()

#定义单词元音字母提取函数 
def getVowelsInWord(word):
    VowelStr='aeiou'
    VowelInWord=''
    for i in word:
        if i in VowelStr:
            VowelInWord+=i
    return VowelInWord

#主程序内容,调用函数处理文件
print "Find words contains vowels 'aeiou' in order:"
for word in filedate:
    word=cleanWord(word)
    if len(word)<=6:
        continue
    vowelstr = getVowelsInWord(word)
    if vowelstr =='aeiou':
        print word
