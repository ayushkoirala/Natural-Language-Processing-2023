from flask import Flask, render_template, request
from utils.general import load_lstm,generate   
from torchtext.data.utils import get_tokenizer
#Load GPU
import torch
device = torch.device('cpu')

tokenizer = get_tokenizer('spacy', language='en_core_web_sm')   
import torch
import torchtext

app = Flask(__name__)             # create an app instance


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/autocomplete', methods = ['GET','POST'])
def autocomplete():
    form = MyForm()
    code = False
    name = False
    print(form.validate_on_submit())
    if form.validate_on_submit():
        name = form.name.data 
        code = predict(prompt = name, temperature=0.5)
        form.name.data = ""
    return render_template("autocomplete.html",form=form,name =name, code=code)
# def generate_suggestions():
#     prompt = request.args.get('code', '')
#     print(prompt)

#     # real-----
   
#     try:
#         print("Here")
#         model,vocab_dict = load_lstm()
#         suggestions = [' '.join(generate(prompt.strip(), 30, 1, model, tokenizer, vocab_dict, device, seed=0))] 
#     except:
#         suggestions = []

#     # html_text put to tag id suggestions
#     suggestion_html = []
#     for suggestion in suggestions:
#         suggestion = suggestion.replace('\n', '<br>')
#         suggestion_html.append(f'<li class="list-group-item">{suggestion}</li>')
#     return {'suggestions': suggestion_html}


if __name__ == "__main__":        # on running python app.py
    app.run()    