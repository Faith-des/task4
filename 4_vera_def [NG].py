import datetime



def active_stud(lang):
    min_days = float('inf')
    with open('4_vera.tsv') as f:
        for line_number, line_data in enumerate(f):
            if line_number == 0:
                continue
            student_id, account_created, last_active, balance, language_id = line_data.rstrip('\n').split('\t')
            python_date_start = datetime.datetime.strptime(account_created, '%Y-%m-%d')
            python_date_end = datetime.datetime.strptime(last_active, '%Y-%m-%d')
            active_day = python_date_end - python_date_start
            days_kol = int(active_day.days)

            for l in lang:
               
                if language_id == l:
                    a = [student_id, account_created, last_active, days_kol, balance, language_id]
                        
                if a[3] < min_days:
                    min_days = a[3]
                    a_result = a
        print(a_result)
                            #return a_result
languages = ['ru','jp']
active_stud(languages)
            #if line_number == 10:
            #    break
