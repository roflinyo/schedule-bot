from wr_to_file import Filehelper
from datetime import datetime
class Helper():
    		
    def monday():
        return 'Понедельник\n🔥10:10-11:40🔥\nАнглийский язык\n🔥14:00-15:30🔥'
    def tuesday():
        return 'Вторник\n🔥8:00-9:30🔥\nФизическая культура\n🔥10:10-11:40🔥\nАнглийский язык'
    def wednesday():
        return 'Среда\n🔥8:30-10:00🔥\nДискретная математика\n🔥10:10-11:40🔥\nАлгебра и Геометрия(лекция)\n🔥11:50-13:20🔥\nИнформатика и программирование\n🔥14:00-15:30🔥\nИнформатика и программирование(лекция)'
    def thursday():
        return 'Четверг\n🔥8:30-10:00🔥\nИстория\n🔥10:10-11:40🔥\nИнформатика и программирование\n🔥11:50-13:20🔥\nАнглийский язык\n🔥14:00-15:30🔥\nАлгебра и Геометрия'
    def friday():
        return 'Пятница\n🔥8:00-9:30🔥\nФизическая культура\n🔥10:10-11:40🔥\nМатематический анализ\n🔥11:50-13:20🔥\nПсихология\n🔥14:00-15:30🔥\nИстория\n🔥15:40-17:10🔥\nДискретная математика'
    def exams():
        return '👊23.12.20 - Дискретная математика(14:00 в 1307)\n👊24.12.20 - Английский язык(проф)(в 11.50)\n👊25.12.20 - История(14:00 в 1305)\n👊25.12.20 - Психология(11.50 в 1305)\n👊28.12.20 - Английский язык(в 10.10)\n👊29.12.20 - История\n👊29.12.20 - Дискретная математика\n👊29.12.20 - Физ.культура(8:00-9.30 d УНИКСе)\n👊30.12.20 - Дискретная математика(14:00 в 1409)'
    def kr_deadlines():
        data = Filehelper.file_get('deadlines_kr.txt')
        lst = ''
        for i in data:
            for ii in i:
                if ii != 1 and ii != 2 and ii != 3:                   
                    lst += '{0}'.format(i[ii]) + '\n'
        return lst

    def homework_prepair():
        data = Filehelper.file_get('./homework.txt')
        redy_str = ''
        #print(type(data[0]))
        for i in range(len(data)):
            if i == 0:
                redy_str = redy_str + 'Матан: ' + '{0}'.format(data[i]) + '\n'
            if i == 1:
                redy_str = redy_str + 'Алгем: ' + '{0}'.format(data[i]) + '\n'
            if i == 2:
                redy_str = redy_str + 'Дискретка: ' + '{0}'.format(data[i]) + '\n'
            if i == 3:
                redy_str = redy_str + 'История: ' + '{0}'.format(data[i]) + '\n'
        return redy_str
        

