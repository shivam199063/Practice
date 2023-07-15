
from langchain.llms import OpenAI
my_openai_key = "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"
mymodel = OpenAI(temperature=0 ,openai_api_key=my_openai_key)


from langchain import PromptTemplate

myprompt = PromptTemplate(
    template= "tell me top 2 {things} of india, which me only name of it.",
    input_variables=["things"]
)

# myprompt.format(things="food")

# output = mymodel( prompt=myprompt.format(things="animal"))

# print(output)


from langchain.chains import LLMChain


mychain = LLMChain(
    prompt=myprompt,
    llm=mymodel
)

print(mychain.run(things="food"))


