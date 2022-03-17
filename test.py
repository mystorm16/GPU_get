def create_text(filename):
    path = '/home/zhiqiang/'
    file_path = path + filename + '.txt'
    file = open(file_path,'w')
    file.close()

create_text('hello')
print('test.py ok')
