import ast,os,datetime

input_file = "./dic/wordSaved/list2.txt"
output_dir = "./dic/wordSaved"
output_base = "wordlist"
output_file = "./dic/wordSaved/wordlist1.txt" 

#get when updated
update = datetime.datetime.now().date()

# read input file
with open(input_file, "r") as f:
    data = f.read().strip()

# convert input data to list of words
word_list = ast.literal_eval(data)

# create output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# generate output filename
if not os.path.exists(output_file):
    output_file = os.path.join(output_dir, output_base + "1.txt")
else:
    # 更新新查的词语
    with open(output_file,"r") as f:
        f_check = f.read().split('\n')
    with open(output_file, "a") as f:
        f.write("\n"+f'***updated when {update}***'+"\n")
        for word in word_list:
            if word not in f_check:
                f.write(word + "\n")
                f_check.append(word)


print('done')

# write word list to output file

