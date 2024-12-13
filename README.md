### TDS PROJECT 2 ###

Hello :)

In this interesting project, I learnt a lot of new and cool things regarding development using LLMs.

This projects was given to me as a part of the course work of TOOLS IN DATA SCIENCE COURSE from IIT Madras.

This project mainly uses..
1. UV as the Package Manager for python.
    # Command to run the python code
    # uv run aytolysis.py <dataset_name>

2. OpenAI's gpt-4o-mini as the LLM model (Using API Calling)

### What does this Project do ###

This projects automates the prelimanary work of DATA ANALYSIS.
All you need to do is run the above line of code in the terminal, and it creates a folder named with the dataset name.

Inside that folder, we would be having 3 types of files (.png,.py and README.md)

In the extracted_code.py file, you will have the code for generating visualizations for the dataset provided.
PNG files will contain the visualizations.
README.md file will contain the inferences from the dataset, inferences from the generated visaluzations, and summary and statistics of the data.

First api call will be made to gpt-4o-mini with the summary of the data. Then the model generates the result which is added in the README.md file. Along with  that, the code for creating the visualizations will also be generated.

Then, the code alone is extracted and saved in extracted_code.py file.

This file is then run using the subprocess module in python.

The visualizations generated from running that code have been saved in the same folder created previously.

For this proper paths have been passed on to the api-call to gpt-4o-mini.

Then using the VISION-API of gpt-4o-mini, I pass on the visualizations generated and ask to llm to provide inferences on the generated visualizations.

All this will be saved in the same README.md file created.
The genrated README.md fill will also contain link to the visualizations. 

So, this porject effectively uses the gpt-4o-api for getting first hand analysis on the dataset provided.

Even thought this was new and challenging, got an opportunity to learn a lot.. :)

###########################################################################################################################