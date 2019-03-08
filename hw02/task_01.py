import re
import csv
import os
def get_data(head, output_lists):
    file_list = ['info_1.txt', 'info_2.txt', 'info_3.txt']

    for file_name in file_list:
        full_name = os.path.join('input', file_name)
        with open(full_name, encoding='cp1251') as f_n:
            for item_str in f_n:
                i = 0
                for output_list in output_lists:
                    fill_list(item_str, head[i], output_list)
                    i += 1

def write_to_csv(file_name):
    head = [r'Изготовитель ОС', r'Название ОС', r'Код продукта', r'Тип системы']
    output_lists = [[], [], [], []]
    get_data(head, output_lists)
    os_prod_list = output_lists[0]
    os_name_list = output_lists[1]
    os_code_list = output_lists[2]
    os_type_list = output_lists[3]
    main_data = [list(x) for x in zip(*output_lists)]
    print(main_data)
    with open(file_name , 'w') as f_n:
        f_n_writer = csv.writer(f_n)
        f_n_writer.writerow(head)
        f_n_writer.writerows(main_data)


def fill_list(item_str, item_name, output_list):
    if re.match(item_name, item_str):
        item_list = re.split(r'\s+', item_str, 2)
        item_value = item_list[2]
        item_value = item_value[:-1]
        output_list.append(item_value)

if __name__ == "__main__":
    file_name = 'main_data.csv'
    full_name = os.path.join('output', file_name)
    write_to_csv(full_name)