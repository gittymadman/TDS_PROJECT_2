# /// script
# requires-python = ">=3.12"
# dependencies = [
# "ipykernel>=6.29.5",
#     "matplotlib>=3.9.3",
#     "numpy>=2.2.0",
#     "openai>=1.57.1",
#     "pandas>=2.2.3",
#     "python-dotenv>=1.0.1",
#     "requests>=2.32.3",
#     "seaborn>=0.13.2",
# ]
# [project.optional-dependencies]
# pandas-dependencies = [
#     "pandas>=2.2.3",
# ]
# ///


import os
import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import requests
import re
import subprocess
import base64
from PIL import Image

load_dotenv()
api_key = os.environ.get("AIPROXY_TOKEN")


client = OpenAI(
    api_key=api_key
)
url = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
headers = {
    "Content-Type":"application/json",
    "Authorization":f"Bearer{api_key}"
}

def create_folder():
    base_path = os.getcwd()
    x = sys.argv[1]
    folder_name,ext = os.path.splitext(os.path.basename(x))
    print(folder_name)
    folder_path = os.path.join(base_path,f'{folder_name}')

    os.makedirs(folder_path,exist_ok=True) # if exist_ok = True, function will not raise an error if we are trying to create a direct. which already exist
    print(f'Folder Created:{folder_path}')
    return folder_path

def load_and_explore(file_name):
    df = pd.read_csv(f"{file_name}",encoding='latin-1')
    
    summary = {
        'file_name':file_name,
        'shape':df.shape,
        'columns':df.columns.tolist(),
        'data_types':df.dtypes.to_dict(),
        'missing_values':df.isna().sum().to_dict(),
        'sample_rows':df.head().to_dict(orient='records')
    }
    return df,summary

def extract_column_info(file_path):
    df = pd.read_csv(file_path)
    column_info = {col:str(dtype) for col,dtype in zip(df.columns,df.dtypes)}
    return column_info



def analyze_data(df):
    analysis={}
    analysis['summary_stats']=df.describe().to_dict()
    # analysis['correlation_matrix']=df.corr().to_dict()
    analysis['null_counts'] = df.isna().sum().to_dict()
    return analysis

def visualize_df(df,folder_path):
    name = 'correlation_matrix.png'
    file_path = os.path.join(folder_path,name)
    plt.figure(figsize=(10,8))
    numeric_df = df.select_dtypes(include=['number'])
    sns.heatmap(numeric_df.corr(),annot=True,cmap='coolwarm',fmt=".2f")
    plt.savefig(file_path)

    return 

def get_narrative(summary, analysis):
    prompt = f"""
    We analyzed a dataset with the following structure: {summary}.
    Our analysis revealed the following key statistics: {analysis}.
    Please write a report as a story, emphasizing key findings, insights, and future implications.
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        prompt=prompt,
        max_tokens=1500
    )
    return response['choices'][0]['text']

def save_readme(narrative,folder_path):
    name = 'README.md'
    file_path = os.path.join(folder_path,name)
    with open(file_path,'w') as file:
        file.write(' # ANALYSIS REPORT:\n\n')
        file.write(narrative)
        file.write('\n\nIMAGES:\n\n')
        file.write(f"[Correlation matrix]({folder_path}_correlation_matrix.png)\n") # correlation_matrix.png acts as a link !!
        file.close()
    
    return 
# def get_function_desc(function_name,description,):
#     function_description = [
#         {
#             "name":function_name,
#             "description":description,
#             "parameters":{
#                 "type":"object",
#                 "properties":{

#                 }
#             }
#         }
#     ]

def ask_question_to_open_ai(summary,analysis,folder_path,csv_file_path):
    data = {
        "model":"gpt-4o-mini",
        "messages":[
            {
                "role":"system",
                "content":'''You are an assistant for data analysis. Provide insights, suggest visualizations, infer patterns, and summarize data based on given column names and details. List meaningful plots that can be created, and generate Python code to extract key findings and plot these visualizations. Give code for plotting only top 3 visualizations. Ensure plots have clear file names. Use pandas and matplotlib only.One visualization should have one chart only. For file reading, use the column structure provided by the user. Avoid unnecessary tokens and no need for correlation matrix plot.Properly label each chart you are generating and do not generate any null charts. Try to remove datapoints which form small part of whole graph'''
            },
            {
                "role":"user",
                "content":f'''We analyzed a dataset with the following structure: {summary}.
                            Our analysis revealed the following key statistics: {analysis}.
                            Use latin-1 encoding for reading the csv file.
                            Path for saving generated images: {folder_path}
                            Path for reading csv file: {csv_file_path}
                            Change the folder path accordingly to save files.
                            Include the statistics and analysis provided in the README file also.
                            Please write a report as a story, emphasizing key findings, insights
                            and future implications.
                            '''

            },
        ]
    }
    response = requests.post(url,headers=headers,json=data)

    if response.status_code == 200:
        result = response.json()
        # print(result) 
        # print(result['choices'][0]['message']['content'])
        output = result['choices'][0]['message']['content']
    else:
        print(f"Error:{response.status_code},{response.text}")

    return output

def convert_to_base_64(url_image):
    with open(url_image,'rb') as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def llm_vision_image_to_text(url_image):
    print(f"Entering vision with url:{url_image}")
    image = Image.open(url_image)
    resized_image = image.resize((512,512))
    resized_image.save(url_image)
    base64_image = convert_to_base_64(url_image)
    data = {
        "model":"gpt-4o-mini",
        'messages':[
            {
                "role":"system",
                "content":'''You will be given charts,graphs,etc...infer those and return the inferences. Keep it precise and neat. Give heading for what type of chart you are infering and inferences in 3-4 bullet points only.'''
            },
            {
                "role":"user",
                
                "content":f"data:image/jpeg;base64,{base64_image}"
            },
        ],
    
    }
    response = requests.post(url,headers=headers,json=data)

    
    result = response.json()
    # print(result)
    output = result['choices'][0]['message']['content']
    
    return output


def extract_code_from_text(narrative):
    code_block = re.findall(r'```python(.*?)```',narrative,re.DOTALL) # re.DOTALL will help in matching newline cahracters also
    # Refer to this link https://interactivechaos.com/en/python/function/redotall
    if not code_block:
        print("Python code not found in this text.")
        return None
    final_code_block = '\n'.join(code_block)
    return final_code_block

def save_python_code(final_code_block,folder_path):
    file_name = 'extracted_code.py'
    file_path = os.path.join(folder_path,file_name)
    with open(file_path,'w') as file:
        file.write(final_code_block)
    print("Extracted code saved in file...")
    file.close()

def run_python_code(main_directory_path,folder_path,file_path='extracted_code.py',out_file='log.txt'):
    out_file_path = os.path.join(folder_path,out_file)
    code_file_path = os.path.join(folder_path,file_path)
    env = 'D:/IITM-BSC/TDS/TDS_PROJECT_2/.venv/Lib/site-packages'
    with open(out_file_path,'w') as file:
        subprocess.run(['python',code_file_path],stdout=file,stderr=file,check=True,cwd='D:/IITM-BSC/TDS/TDS_PROJECT_2') # check=True stops execution if there is any error in executing generated python file.
    print(f"O/P saved in {out_file} ")
    return


def send_image_paths_to_api(folder_path):
    x=0
    for file_name in os.listdir(folder_path):
        if file_name.lower().endswith(('.png','.jpg')) and x<2:
            x += 1
            file_path = os.path.join(folder_path,file_name)
            output = llm_vision_image_to_text(file_path)
            readme_file_path = os.path.join(folder_path,'README.md')
            with open(readme_file_path,'a') as file: # opening file in append mode as it already exists....
                file.write(f"![Image_path]({file_path})")
                file.write(output)
            file.close()


def main():
    print("Hello from tds-project-2!")
    
    main_directory_path = os.getcwd()
    csv_file_path = os.path.join(main_directory_path,sys.argv[1])
    folder_path = create_folder()
    if len(sys.argv) != 2:
        print("The correct usage is: uv run aytolysis.py <dataset_name>")
        sys.exit(1)
    csv_file = sys.argv[1]
    df,summary = load_and_explore(csv_file)
    analysis = analyze_data(df)
    visualize_df(df,folder_path)
    # narrative = get_narrative(summary,analysis)
    
    narrative = ask_question_to_open_ai(summary,analysis,folder_path,csv_file_path)
    save_readme(narrative,folder_path) # This readme file will be used for creating more visualization plots using python subprocess...
    final_code_block = extract_code_from_text(narrative)
    save_python_code(final_code_block,folder_path)
    run_python_code(main_directory_path,folder_path)
    send_image_paths_to_api(folder_path)


if __name__ == "__main__":
    main()
