directory = "path/here"
keywords = ["key", "word"]
for filename in os.listdir(directory):
    with open(os.path.join(directory, filename)) as file:
        keyword_list = []
        for line_number, line in enumerate(file):
            for keyword in keywords:
                if keyword in line:
                    keyword_list.append(keyword)
        if keyword_list:
            print(f"Keywords found in {filename}: {keyword_list}")
        else:
            print(f"None of the keywords were found in {filename}")
# END
