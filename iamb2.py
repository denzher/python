import random
dictionary='iamb_dictionary.txt'
words_with_info=[]
scheme=['гл','мест','прил','сущ']
line_1=[]
ksyll=0



DBG = False
def print_dbg(*args):
    """При заданном ключе DBG выводит отладочные сообщения"""
    if DBG:
        print(*args)

def syllables_accentuation(dictionary):
    '''
    заносит в список слова из файла,количества слогов и номер ударного слога\n
    dictionary - файл с набором слов \n
    \t Автор Жеребцов Д.Д. \n 
    '''  
    syllables=0
    vowels=['у','е','ё','ы','а','о','э','я','и','ю']
    accentuation_syllable=0
    word=''
    part_of_speach=''
    f=open(dictionary) 

    for line in f:
        line = line.rstrip()
       
        
        length_of_string=len(line)

        for i in range(length_of_string):
            if line[i]!=' ':
                
                word+=line[i]
            else:
                index_space=i
                break
        
        print_dbg(index_space)

        for i in range(index_space+1,length_of_string):
            part_of_speach+=line[i]
        
        print_dbg(part_of_speach)
        print_dbg(word)

        length_of_word=len(word)
        
        for i in range(length_of_word):
            if word[i] in vowels:
                syllables+=1
            elif word[i] == '`':
                accentuation_syllable=syllables+1
        print_dbg ("syllables: ",syllables)
        print_dbg ("accentuation_syllable: ",accentuation_syllable)
        #записываем данные в список
        words_with_info.append([word])
        index=words_with_info.index([word])
        words_with_info[index].append(syllables)
        words_with_info[index].append(accentuation_syllable)
        words_with_info[index].append(part_of_speach)
        #обнуляем перед переходом к следующей строке
        word=''
        syllables=0
        accentuation_syllable=0
        part_of_speach=''
        
    f.close 
    return(words_with_info)  
    
    
def create_1_line(words_with_info):
       
    # переменная для "переноса" слога от одного слова к другому
    extra=0
    #переменная должна быть равна 2 для соблюдения размера
    iamb_ac=0
    #создание первой строки согласно схеме
    for i in range(len(scheme)):
        for j in range(len(words_with_info)):
            if scheme[i] == words_with_info[j][3]:
                #проверяем размер
                if extra!=0:
                    iamb_ac = words_with_info[j][2]+extra
                    extra = 0
                else:
                    iamb_ac = words_with_info[j][2]
                if words_with_info[j][1] > 2:
                    extra+=1
                if iamb_ac==2:    
                    break
        line_1+=[words_with_info[j][0]]
        #количество слогов
        ksyll+=[words_with_info[j][1]
        
    return(line_1,ksyll)        
        
        
if __name__ == '__main__':
    words_with_info=syllables_accentuation(dictionary)
    random.shuffle(words_with_info)
    print(words_with_info)
    
    
    line_1,ksyll=create_1_line(words_with_info)
        
    #вывод первой строки
    for i in range(len(line_1)):
        if i == 2:
            print('-',end=' ')
        print(line_1[i],end=' '),
    print(ksyll)    
    pass
            



