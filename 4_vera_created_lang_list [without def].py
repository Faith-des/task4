
# Tty to creat a list of languages!            
languages = []


with open('4_vera.tsv') as f:
    for line_number, line_data in enumerate(f):
        
        if line_number == 0:
            continue
        student_id, account_created, last_active, balance, language_id = line_data.rstrip('\n').split('\t')
        
        '''if language_id in languages:
            continue
        else:
            languages.append(language_id)'''
        new_lang = True
        for lang in languages:
            if lang == language_id:
                new_lang = False
            

        if new_lang == True:
            languages.append(language_id)
        
print(languages)

languages.sort()
languages.reverse()
print(languages)

