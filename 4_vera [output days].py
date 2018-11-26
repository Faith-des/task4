import datetime

with open('4_vera.tsv') as f:
    for line_number, line_data in enumerate(f):
        
        if line_number == 0:
            continue
        student_id, account_created, last_active, balance, language_id = line_data.rstrip('\n').split('\t')
        if language_id == 'ru':
            
            #print(student_id, account_created, last_active, balance, language_id)
            python_date_start = datetime.datetime.strptime(account_created, '%Y-%m-%d')
            python_date_end = datetime.datetime.strptime(last_active, '%Y-%m-%d')
            active_day = python_date_end - python_date_start
            
            days_kol = int(active_day.days) 
            a = [student_id, account_created, last_active, days_kol, balance, language_id]
            print(a[3])
            
        #if line_number == 10:
        #    break