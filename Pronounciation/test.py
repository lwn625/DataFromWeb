import requests



# Define the webpage
# Mind that the webpage is changed for individual english word
web_url_1="http://dict.youdao.com/dictvoice?audio="
web_url_3="&type=2"

# Set up an identifier for the output file name
i=1

# Open the file containing a column of english words
# Mind the encoding argument
with open('dict_list.txt','r',encoding='utf-16') as file_dict:
    # Use readlines to read all content of the file
    words=file_dict.readlines()

    for line in words:
        # Delete the special character '\n' in each line
        web_url_2=line.rstrip('\n')
        print(web_url_2)

        # Form the webpage that contains the pronounciation of the current english word
        web_url=web_url_1+web_url_2+web_url_3

        # Define the output name: e.g. 001_think.mp3
        mp3_filename=str(i).zfill(3)+'_'+web_url_2+'.mp3'
        i=i+1
        #Use request.get to obtain the content
        r = requests.get(web_url)

        # Write the content into the defined file
        # Mind the arguments wb, w means write mode, b means overwrite
        with open(mp3_filename,'wb') as f:
            f.write(r.content)
# close the files
f.close()
file_dict.close()

