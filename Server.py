from flask import Flask, request, jsonify
import spacy
nlp = spacy.load("en_core_web_sm")

app = Flask(__name__)

@app.route('/process_string', methods=['POST'])
def process_string():

	if not request.json or 'input_string' not in request.json:
		return jsonify({"error": "Please provide a string with the 'input_string' key"}), 400

	input_string = request.json['input_string']
	doc = nlp(input_string)
	table = []
	for token in doc:

		table.append({"pos": token.pos_, "text": token.text , "dep": token.dep_ , "lemma": token.lemma_, "tag": token.tag_, "shape": token.shape_})

	return jsonify(table)

if __name__ == '__main__':
	app.run(debug=True, port=81)
