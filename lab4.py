#вариант 3 YAML - JSON Monday
lastbr = '' # очередь открытых скобок
def is_integer(n): # проверяем, можно ли объект n привести к целому числу без потерь
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()
with open('time.yml', 'r', encoding='utf-8') as r: 
    tt = r.readlines() # считываем YAML
def writeline(line, l, out): 
    global tt # доступ к будущим строкам файла для закрытия скобок
    global lastbr #информация об открытых скобках
    bracket = False # нужно ли открыть скобку
    bracketclose = 0 # кол-во скобок, которые нужно закрыть 
    spaces = tt[l].count('  ') # считаем новое кол-во пробелов
    if len(line.split())==1:
        if ':' in line:
            line = '"' + line.split()[0][:-1] + '":' + '\n' # если строка открывает вложенность, мы ее сохраняем
    else:
        if ':' in line:
            if len(line.split())==2 and is_integer(line.split()[1]):
                line = '"' + line.split()[0][:-1] + '": '  + ' '.join(line.split()[1:]) + ',' + '\n'
            else:
                line = '"' + line.split()[0][:-1] + '": "' + ' '.join(line.split()[1:]) +'",' + '\n'
    '''Если же строка не влияет на вложенность, мы определяем,
    нужно ли ставить кавычки к значению ключа в зависимости от того,
    является ли он числом'''
    try:
        if tt[1+1].count('  ')>spaces:
            bracket = True
            lastbr += '{'
            '''Если следующая строчка имеет больший отступ -
            открываем новую скобку'''
        elif tt[l+1].count('  ')<spaces:
            bracketclose = spaces - tt[l+1].count('  ') 
            '''Если меньший - закрываем столько скобок, на
            сколько уровней сократился отступ'''
    except IndexError:
        bracketclose = spaces
        '''Если же строка последняя, мы получим ошибку при обращении к следующей
        и закроем все скобки'''
    if bracket:
        line=line +'{'+ '\n'
        out.write(line) # Если нужно открыть скобку - сначала открываем, затем записываем строку
    elif bracketclose: # Если нужно закрыть скобки - закрываем их с переносом строки
        out.write(line[:-2] + '\n') #убираем запятую
        for i in range(bracketclose):
            out.write('}')
            if i != bracketclose-1:
                out.write('\n')
            lastbr = lastbr[:len(lastbr)-1]
        if spaces-bracketclose>0:
            out.write(',' + '\n')
            ''' Если отступ не станет нулевым после закрытия скобок - значит
            нужно поставить запятую, т.к. мы все еще находимся на каком-то
            уровне вложенности'''
    else:
        out.write(line) # Если скобок ставить не нужно - мы сохраняем вложенность и ставим запятую
def main():
    out = open('out.json', 'w', encoding='utf-8')
    out.write('{' + '\n') # скобка в начале файла
    for i in range(len(tt)):
        writeline(tt[i], i, out) #применяем метод построчного перевода файла
    out.write('\n'+'}' ) #закрываем скобку, открытую в начале файла
    
main()
print(open('out.json', encoding='utf-8').read())
