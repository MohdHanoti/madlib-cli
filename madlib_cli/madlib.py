import re

def read_template(path):
    '''
    this function read what inside the path
    '''
    if path == 'assets/dark_and_stormy_night_template.txt' or path == 'assets/make_me_a_video_game_output.txt':
        with open(path) as file:
            story=file.read()
            return story
    else:
        raise FileNotFoundError        


def parse_template(str):
    '''this function parse the content'''
    stripped = re.sub(r'[^{}]+(?=})', '', str)
    parts = re.findall(r'[^{}]+(?=})', str)
    return stripped, tuple(parts)

def merge(str,list):
    '''this function merge the function'''
    new_str=str.format(*list)
    return new_str

if __name__ == "__main__":
    print (
        """
        ** Welcome to the Madlib game ******************
        ** Mad libs are a word replacement game ******** 
        ** all you have to do is entering some worlds **
        ** it will replaced in a paragraph *************
        ** it will be fuunny and you will lough ********
        ** just answer the questions and hit enter..****
        """)
    def madlib():
        '''this function takes the input from the user and put it in the right space'''
        path="assets/make_me_a_video_game_output.txt"
       
        content=read_template(path)
        stripped, parts = parse_template(content)
        inputs=[]
        for part in parts:
            user_input=input(f"please enter a {part} : ")
            inputs.append(user_input)
        final_story=merge(stripped,inputs)    
        print(final_story)
        return final_story

    def new_file(story):
        '''this function saves the content as file'''
        with open("assets/response.txt",'w') as file:
            file.write(story)
            print ("SAVED")

    new_file(madlib())            

