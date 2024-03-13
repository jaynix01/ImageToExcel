import easyocr
import os
import re
import xlsxwriter


def text_detect(file_path):
    reader = easyocr.Reader(['en'])
    detected_text = reader.readtext(file_path, detail=0, paragraph=True)

    item_detect(detected_text)


def item_detect(detect_text):
    pattern_number = r'\b\d{2,4}\b'
    number_list = re.findall(pattern_number, detect_text[0])
    if number_list:
        number = ''.join(number_list)
    else:
        number = ''

    vehicle = detect_text[4]
    if vehicle:
        vehicle = detect_text[4]
    else:
        vehicle = ''

    pattern_client = r'(.+) \+ (\d{3} \d{3} \d{3} \d{3})'
    matches_client = re.match(pattern_client, detect_text[5])
    if matches_client:
        client_name = matches_client.group(1)
        client_phone_number = matches_client.group(2)
    else:
        client_name = ''
        client_phone_number = ''

    tires = detect_text[6]
    if "Predmetem dohody je uschova" in tires:
        tires = re.sub(r'^Predmetem dohody je uschova\s*', '', tires)
    else:
        tires = ''

    pattern_datetime = r"\b\d{2}\.\d{2}\.\d{4}\b"
    datetime_list = re.findall(pattern_datetime, detect_text[9])
    if datetime_list:
        datetime = ''.join(datetime_list)
    else:
        datetime = ''

    result_list = [[number,vehicle,client_name,
                   client_phone_number,tires,datetime]]
    
    save_in_excel(result_list)


def save_in_excel(result_list, result_file='result.xlsx'):
    current_row = 0

    workbook = xlsxwriter.Workbook(result_file)
    worksheet = workbook.add_worksheet()

    for row in result_list:
        for col_index, cell_value in enumerate(row):
            worksheet.write(current_row, col_index, cell_value)
        current_row += 1 

    workbook.close()

    print('Done')


def process_files_in_folder(folder_path):
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.jpg') or file_name.endswith('.png'):
            full_file_path = os.path.join(folder_path, file_name)
            print(f'Processing file: {full_file_path}')
            text_detect(full_file_path)


def main():
    folder_path = input('Enter path to folder: ')
    process_files_in_folder(folder_path)


if __name__ == '__main__':
    main()
