# #Shivam Saini

#  How we can Integrate Linkedin With LangChain(or we can say chatGpt, LLM Model)

# %%
# Linkedin Scrapping 

import requests
api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
api_key = 'YourAPIkey_of_Proxycurl'
header_dic = {'Authorization': 'Bearer ' + api_key}
def Linkedin_Scrape(url):
    params = {
    'url': url,
    'fallback_to_cache': 'on-error',
    'use_cache': 'if-present',
    'skills': 'include',
    'inferred_salary': 'include',
    'personal_email': 'include',
    'personal_contact_number': 'include',
    'twitter_profile_id': 'include',
    'facebook_profile_id': 'include',
    'github_profile_id': 'include',
    'extra': 'include',
    'headline' : 'include',
    'certification' : 'include' 
     }
    response = requests.get(api_endpoint,
                        params=params,
                        headers=header_dic)
    return response

# %%
Linkedin_Data = Linkedin_Scrape('https://www.linkedin.com/in/shivam199063/')

# %%
Linkedin_Data = Linkedin_Data.json()

# %%
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI

# %%
openapiKey = 'Api__Key_Of_OpenAi'

# %%
model = ChatOpenAI(
    model = 'gpt-3.5-turbo',
    temperature= 1,
    openai_api_key  = openapiKey

)

# %%
from langchain.chains import LLMChain

# %%
MyTemplate = """ {someoneinformation}
                Given is the someoneinformation about Linkedin Profile:
                1. Tell me summary about in one line.
                2. 2 unique point about him/her.
                3. tell me about him/her in  words.
"""

# %%
myPromptTEmplate = PromptTemplate(
    input_variables= ['someoneinformation'],
    template= MyTemplate
)

# %%
myinfo = myPromptTEmplate.format(someoneinformation = Linkedin_Data['summary'])

# %%
mychain = LLMChain(
    llm=model,
    prompt= myPromptTEmplate
)

# %%
print(mychain.run(someoneinformation = Linkedin_Data['summary']))


