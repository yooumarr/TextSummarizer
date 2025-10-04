from langchain_core.prompts import PromptTemplate
from llm_model import llm 
from flask import Flask, render_template, request

app = Flask(__name__)

template = PromptTemplate.from_template("You are a helpful AI assistant. Please summarize {paragraph} in 3 sentences. Be creative in your response.")

llm_chain = template | llm

@app.route('/', methods=['GET','POST'])
def index():
    summary = ""
    if request.method == "POST":
        paragraph = request.form["paragraph"]
        if paragraph.strip():
            summary = llm_chain.invoke({"paragraph": paragraph})
    return render_template("index.html", summary=summary)

if __name__ == "__main__":
    app.run(debug=True)