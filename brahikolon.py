import random
dictionary='brahikolon.txt'

DBG = False
def print_dbg(*args):
    """При заданном ключе DBG выводит отладочные сообщения"""
    if DBG:
        print(*args)

def create_list_of_rhymes_from_dictionary(dictionary): 
    """
    создает список списков рифмованных слов (по двум последним буквам,\n
    не включая ь), взятых из файла \n
    dictionary - файл с набором слов
    \t Автор Жеребцов Д.Д. \n
    """ 
    suffixes=[]
    f=open(dictionary)
    for line in f:
        
      
        line = line.rstrip()
        l=len(line)
        print_dbg(l)
        if line[l-1]=='ь':
            current_suffix=line[l-3]+line[l-2]    
        else:
            current_suffix=line[l-2]+line[l-1]
    
        if current_suffix not in suffixes:
            suffixes.append(current_suffix)
            suffixes.append([line])
        else:    
            index=suffixes.index(current_suffix)
            suffixes[index+1].append(line)
         
    # Правильно и аккуратно делать через менеджеры контекста
    # https://docs.python.org/3/reference/compound_stmts.html#the-with-statement     
    print_dbg(suffixes)
    f.close      
    return suffixes

def create_list_of_words_without_rhymes(suffixes):
    """
    создаем список слов без пары-рифмы
    """
    first_word=[]
    for i in range(1,len(suffixes),2): 
        print_dbg(suffixes[i])
        if len(suffixes[i]) == 1:
            first_word+=suffixes[i]
    random.shuffle(first_word)
    print_dbg(first_word)
    return first_word
        
def create_list_of_words_with_rhymes(suffixes):
    '''
    создаем список слов с парой-рифмой
    '''   
    rhyme_word=[]
    for i in range(1,len(suffixes),2): 
        if len(suffixes[i])>1:
            rhyme_word+=[suffixes[i]] 
    print_dbg(rhyme_word)
    random.shuffle(rhyme_word)
    rhyme_word=sum(rhyme_word, [])
    return rhyme_word




# исполняемый файл должен содержать:
if __name__ == '__main__':

    suffixes=create_list_of_rhymes_from_dictionary(dictionary)
    first_word=create_list_of_words_without_rhymes(suffixes)
    rhyme_word=create_list_of_words_with_rhymes(suffixes)
    for i in range(len(first_word)):
        print(first_word[i],"-",rhyme_word[i])
    pass

# с этим разобрались, теперь пишем набираем используя несколько словарей для генерируем строку в нужном нам стиле.
# за одно читаем про tkinter. Делать без GUI нынче не модно
# Исправляй все замечания, структурируй код и завтра вечером присылай 