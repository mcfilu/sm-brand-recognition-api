import json
import os
import csv
import random

def extract_data_from_json_folder(json_folder_path, output_file_path, key_name):
    with open(output_file_path, "w") as output_file:
        writer = csv.writer(output_file)
        count = 0
        for file_name in os.listdir(json_folder_path):
            print("gone")
            if file_name.endswith(".json"):
                with open(os.path.join(json_folder_path, file_name)) as json_file:
                    json_data = json.load(json_file)
                    try:
                        value = json_data.get("edge_media_to_caption").get('edges')[0].get("node").get("text")
                    except:
                        value = None
                    if value is not None:
                        writer.writerow([file_name, value])
                    count += 1

        print(count)

json_folder_path = "/Users/filipolszewski/Downloads/json2"
output_file_path = "cleaned_comms2.csv"
key_name = "my_key"

# extract_data_from_json_folder(json_folder_path, output_file_path, key_name)


def combine_data(output_file_path, cleaned_comms):
    with open(output_file_path, "w") as output_file:
        writer = csv.writer(output_file)
        with open('output.csv', 'r') as comms_list_file:
            comms_list = csv.reader(comms_list_file)
            with open('output.csv', 'r') as cleaned_comms_file:
                cleaned_comms = csv.reader(cleaned_comms_file)
                for comm in comms_list:
                    pass

        for file_name in os.listdir():
            print("gone")
            if file_name.endswith(".json"):
                with open(os.path.join(json_folder_path, file_name)) as json_file:
                    json_data = json.load(json_file)
                    try:
                        value = json_data.get("edge_media_to_caption").get('edges')[0].get("node").get("text")
                    except:
                        value = None
                    if value is not None:
                        writer.writerow([file_name, value])

def combine_into_one_file():
    # Open the first file and read its contents into a dictionary
    file_1_data = {}
    with open('/Users/filipolszewski/Downloads/post_info.txt', 'r') as file_1:
        for line in file_1:
            values = line.strip().split()
            filename = values[3]
            value = values[2]
            file_1_data[filename] = value


    # # Open the second file and read its contents into a dictionary
    file_2_data = {}
    with open('cleaned_comms2.csv', 'r') as file_2:
        file_2_reader = csv.reader(file_2)
        for line in file_2_reader:
            filename, comment = line
            file_2_data[filename] = comment

    # Open a new file for writing
    with open('final_comments.csv', 'w') as output_file:
        # Iterate over the keys in the first dictionary (since they should be the same as in the second)
        writer = csv.writer(output_file)
        for filename in file_1_data.keys():
            # Write the filename, 0/1 value, and comment value to the output file
            try:
                line=[filename, file_1_data[filename], file_2_data[filename]]
                writer.writerow(line)
            except:
                pass
            # output_file.write(filename + ' ' + file_1_data[filename] + ' ' + file_2_data[filename] + '\n')

# combine_into_one_file()

def only_ads():
    with open("ad_only.csv", "w") as ad_comms:
        writer = csv.writer(ad_comms)
        with open("final_comments.csv", 'r') as final_comemts:
            reader = csv.reader(final_comemts)
            for line in reader:
                print(line)
                print(line[1])
                print(line[2])
                if line[1] == "1":
                    new_line = [line[1], line[2]]
                    writer.writerow(new_line)
# only_ads()

def select_random_rows(input_file, output_file):
    with open(input_file, 'r') as f:
        reader = csv.reader(f)
        # print(len(list(reader)))
        data = list(reader)

    # Select 20,000 random rows
    selected_rows = random.sample(data, 20000)

    # Write selected rows to output file
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(selected_rows)

# select_random_rows('ad_only.csv', 'final_data.csv')

def concatinate_data():
    with open("ad_only.csv", "a", newline="") as ad_comms:
        writer = csv.writer(ad_comms)
        with open("/Users/filipolszewski/Downloads/captions_csv.csv", "r") as non_ads:
            reader = csv.reader(non_ads)
            print("here")
            for line in reader:
                print("line")
                new_line = [0, line[2]]
                writer.writerow(new_line)

# concatinate_data()

def clean_non_advertisement():
    count = 0
    with open("cleaned_non_ads.csv", "w") as cleaned_non_ads:
        writer = csv.writer(cleaned_non_ads)
        with open("/Users/filipolszewski/Downloads/captions_csv.csv", "r") as non_ads:
            reader = csv.reader(non_ads)
            for line in reader:
                if len(line[2]) > 0:
                    new_line = [0, line[2]]
                    writer.writerow(new_line)
                    count += 1

    print(count)

# clean_non_advertisement()

def shuffle_rows(input_file1, input_file2, output_file):
    data = []
    # Read data from first input file
    with open(input_file1, 'r') as f:
        reader = csv.reader(f)
        data.extend(list(reader))

    # Read data from second input file
    with open(input_file2, 'r') as f:
        reader = csv.reader(f)
        data.extend(list(reader))

    # Shuffle rows
    random.shuffle(data)

    # Write shuffled rows to output file
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

# shuffle_rows('cleaned_non_ads.csv', 'final_data.csv', 'final_comms_data.csv')


def remove_ad_tags():
    with open('final_comms_data.csv', 'r') as data:
        reader = csv.reader(data)
        with open('final_cleaned_comms_data.csv', 'w') as cleaned:
            writer = csv.writer(cleaned)
            for line in reader:
                label = line[0]
                text = line[1]
                text = text.replace('ad', ' ').replace('advertisement', ' ').replace('#ad', ' ').replace('#advertisement', ' ').replace('sponsored', ' ').replace('#sponsored', ' ')
                writer.writerow([label, text])

# remove_ad_tags()

def remove_tags():
    with open('final_cleaned_comms_data.csv', 'r') as data:
        reader = csv.reader(data)
        with open('final_data_without_tags.csv', 'w') as cleaned:
            writer = csv.writer(cleaned)
            for line in reader:
                label = line[0]
                text = line[1]
                text = text.replace('#', ' ').replace('hashtag', ' ')
                writer.writerow([label, text])

# remove_tags()


def process_string():

    with open('final_data_without_tags.csv', 'r') as data:
        reader = csv.reader(data)
        with open('final_data_fully_cleaned.csv', 'w') as cleaned:
            writer = csv.writer(cleaned)
            for line in reader:
                label = line[0]
                text = line[1]
                text = text.replace('.', '').replace(',', '').replace('•', '').replace('-', '').replace('_', '').replace('"', '').replace("'", "")

                # Split the text into lines
                lines = text.split('\n')

                # Remove empty lines
                lines = [line for line in lines if line.strip() != '']

                # Join the non-empty lines back into a single string
                text = ' '.join(lines)

                # Remove dots, commas, and the character •

                writer.writerow([label, text])

# process_string()


def concatinate_finals():
    with open('final_data_fully_cleaned.csv', 'a') as final:
        writer = csv.writer(final)
        with open('no_ad_mention.csv', 'r') as no_ad:
            reader = csv.reader(no_ad)
            for line in reader:
                label = 0
                text = line[0]
                writer.writerow([label, text])

# concatinate_finals()