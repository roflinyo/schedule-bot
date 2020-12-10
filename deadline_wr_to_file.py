from datetime import datetime, timedelta
from wr_to_file import Filehelper


class DeadlineWriter:
    
    def wrk_with_text_deadline_kr(text):
        now = datetime.now()
        a = 'сл'
        b = 'нед'
        aa = 'удал'
        bb = 'кр'
        if a in text and b in text:
            
            if 'мат' in text and 'ан' in text:
                now2 = now + timedelta(days = 4)
                now3 = now + timedelta(days = 7)
                data = Filehelper.file_get('./deadlines_kr.txt')
                data[0] = ({now2:'Матан: {0}.{1}'.format(now3.day,now3.month)})
                Filehelper.file_wr(data,'./deadlines_kr.txt')
                
            if 'ал' in text and 'гем' in text:
                now2 = now + timedelta(days = 4)
                now3 = now + timedelta(days = 7)
                data = Filehelper.file_get('./deadlines_kr.txt')
                data[1] = ({now2:'Алгем: {0}.{1} '.format(now3.day,now3.month)})
                Filehelper.file_wr(data,'./deadlines_kr.txt')
                
            if 'дискр' in text:
                now2 = now + timedelta(minutes = 1)
                now3 = now + timedelta(days = 7)
                data = Filehelper.file_get('./deadlines_kr.txt')
                data[2] = ({now2:'Дискретка: {0}.{1}'.format(now3.day,now3.month)})
                Filehelper.file_wr(data,'./deadlines_kr.txt')
                
        elif aa in text and bb in text:
            
            if 'мат' in text and 'ан' in text:
                data = Filehelper.file_get('./deadlines_kr.txt')
                data[0] = ({0:'Матан:---'})
                Filehelper.file_wr(data,'./deadlines_kr.txt')
                
            if 'ал' in text and 'гем' in text:
                data = Filehelper.file_get('./deadlines_kr.txt')
                data[1] = ({0:'Алгем:---'})
                Filehelper.file_wr(data,'./deadlines_kr.txt')
                
            if 'дискр' in text:
                data = Filehelper.file_get('./deadlines_kr.txt')
                data[2] = ({0:'Дискретка:---'})
                Filehelper.file_wr(data,'./deadlines_kr.txt')


    def wrk_with_text_deadline_hw_m(text):
        data = Filehelper.file_get('./homework.txt')
        data[0] = text[10:]
        Filehelper.file_wr(data,'./homework.txt')

    def wrk_with_text_deadline_hw_a(text):
        data = Filehelper.file_get('./homework.txt')
        data[1] = text[10:]
        Filehelper.file_wr(data,'./homework.txt')

    def wrk_with_text_deadline_hw_d(text):
        data = Filehelper.file_get('./homework.txt')
        data[2] = text[10:]
        Filehelper.file_wr(data,'./homework.txt')

    def wrk_with_text_deadline_hw_h(text):
        data = Filehelper.file_get('./homework.txt')
        data[3] = text[10:]
        Filehelper.file_wr(data,'./homework.txt')







    
    
        
            
