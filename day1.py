# 1. Combine several Lists =========================================
first = ['Behind', 'every', 'great', 'man']
second = ['is', 'a', 'woman']
third = ['rolling', 'her', 'eyes']

data = first + second + third

def listToString(s):   
    str1 = " "  
    # return string   
    return (str1.join(s))       


print(listToString(data))  


#3. Char Counter =========================================
def check_freq(x):
    freq = {}
    for c in x:
       freq[c] = x.count(c)
    return freq
print(check_freq("mammals"))

# 4. Bubble Sort =========================================
def tukar(lists,i,j):
    lists[i],lists[j]=lists[j], lists[i]
    
def bubbleTugas(listku):
    perubahan = True
    sesi = len(listku) #banyaknya sesi yang digunakan untuk mengecek data dari awal
    while sesi > 1 and perubahan:
        perubahan = False
        j = 1
        while j < sesi:
            if listku[j]<listku[j-1]:
                perubahan = True
                tukar(listku,j,j-1) 
            j+=1
            
        print(listku)
        #Jika penanda 'perubahan' tidak terjadi maka perulangan berhenti dan artinya data sudah terurut tanpa melakukan perulangan lagi.
        if not perubahan:
            print("hasil akhir = %s" %str(listku))
        sesi-=1
mylist= [12,3,5,4,8,9]
bubbleTugas(mylist)

# 6. Missing Letter =========================================
def missing_elements(L):
    start, end = L[0], L[-1]
    return sorted(set(range(start, end + 1)).difference(L))

def find_missing_letter(chars):
    numbers = list(map(ord, chars))
    n = missing_elements(numbers)
    return chr(n[0])

list_letters_first = ["c","d","e","g","h"]
list_letters_second = ["X","Z"]

print("find_missing_letter : ", find_missing_letter(list_letters_first))
print("list_letters_second : ", find_missing_letter(list_letters_second))

# 5. Masking =========================================
def censor(text, word):
    wordlist = text.split()
    new_words_list = []
    for item in wordlist:
        if item.find(word) > -1:
            new_words_list.append( '*' * len(word))
        else:
            new_words_list.append(item)
    return " ".join(new_words_list)

print(censor("You dirty guy and dirty boy dirty.", "dirty"))



# 7 Sorting Odd Numbers =========================================

numbers = [9,4,2,4,1,5,3,0]
# sort the vowels
numbers.sort()
# print vowels
print(numbers)