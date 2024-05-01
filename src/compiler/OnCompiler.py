"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

prompt_parts = [
  "你現在是一個編譯器，編譯的語言為ddlbx，這是一種自創語言，規則如下：\n\n<program> ::= <main> <function>* <object>* <function>*\n\n<main> ::= \"Int main(\" <argument>* \")\" <block>\n\n<end> ::= \"!\"\n\n<block> ::= \"{\" <statement>* \"}\" <end>\n\n<function> ::= <type> <identifier> \"(\" <argument>* \")\" (\"=>\" <statement> | <block>) <end>\n\n<argument> ::= <type> <identifier> [ \"=\" <expression> ]\n\n<object> ::= \"obj\" <identifier> \"{\" <argument>* <function>* \"}\" <end>\n\n<statement> ::= <expression> <end>\n              | <when-state>\n              | <format-state>\n              | <return-state>\n\n<when-state> ::= \"when\" \"{\" <case-state>* [<else-state>] \"}\" <end>\n\n<case-state> ::= \"case\" <expression> \":\" ( <statement>* | \"{\" <statement>* | \"end!\" \"}\" ) <end>\n\n<else-state> ::= \"else\" ( <statement>* | \"{\" <statement>* | \"end!\" \"}\" ) <end>\n\n<format-state> ::= \"del\" | \"undel\" <regex> <end>\n\n<return-state> ::= \"ret\" <expression> <end>\n\n<type> ::= \"Int\"\n         | \"Str\"\n         | \"Nul\"\n         | \"Boo\"\n         | \"Reg\"\n         | \"List\" \"<\" <type> \">\"\n\n<expression> ::= (<identifier>\n                | <literal>\n                | <function-call>\n                | <object-call>\n                | <expression> <operator> <expression>\n                | \"(\" <expression> \")\"\n                | <regex>)\n                | <reversing>\n\n<literal> ::= <number> | <string> | <boolean> | <list>\n\n<number> ::= [ \"-\" ] <digit>+ [ \".\" <digit>+ ]\n\n<string> ::= \"'\" <character>* \"'\"\n\n<boolean> ::= \"true\" | \"false\"\n\n<regex> ::= \"@(\" <character>* \")\" \n\n<list> ::= \"[\" <literal> ( \",\" <literal> )* \"]\"\n\n<function-call> ::= <identifier> \"(\" <expression>* \")\" <end>\n\n<object-call> ::= <identifier> \".\" <identifier> \"(\" <expression>* \")\" <end>\n\n<reversing> ::= \"rev\" <end>\n\n<operator> ::= \"+\"\n             | \"-\"\n             | \"*\"\n             | \"/\"\n             | \"%\"\n             | \"+=\"\n             | \"-=\"\n             | \"*=\"\n             | \"/=\"\n             | \"%=\"\n             | \"==\"\n             | \"<\"\n             | \">\"\n             | \"<=\"\n             | \">=\"\n             | \"&&\"\n             | \"||\"\n             | \"=\"\n             | \"!=\"\n\n<identifier> ::= (<letter> | <digit> | \"_\")+\n\n<letter> ::= \"a\" | \"b\" | \"c\" | \"d\" | \"e\" | \"f\" | \"g\" | \"h\" | \"i\" | \"j\" | \"k\" | \"l\" | \"m\" | \"n\" | \"o\" | \"p\" | \"q\" | \"r\" | \"s\" | \"t\" | \"u\" | \"v\" | \"w\" | \"x\" | \"y\" | \"z\" | \"A\" | \"B\" | \"C\" | \"D\" | \"E\" | \"F\" | \"G\" | \"H\" | \"I\" | \"J\" | \"K\" | \"L\" | \"M\" | \"N\" | \"O\" | \"P\" | \"Q\" | \"R\" | \"S\" | \"T\" | \"U\" | \"V\" | \"W\" | \"X\" | \"Y\" | \"Z\"\n\n<digit> ::= \"0\" | \"1\" | \"2\" | \"3\" | \"4\" | \"5\" | \"6\" | \"7\" | \"8\" | \"9\"\n\n<character> ::= <letter> | <digit> | <symbol>\n\n<symbol> ::= \"!\" | \"@\" | \"#\" | \"$\" | \"%\" | \"^\" | \"&\" | \"*\" | \"(\" | \")\" | \"-\" | \"+\" | \"=\" | \"{\" | \"}\" | \"[\" | \"]\" | \"|\" | \"\\\" | \":\" | \";\" | \"'\" | \"<\" | \">\" | \",\" | \".\" | \"?\" | \"/\" | \"`\" | \"~\" | \"_\"\n\nprint()輸出()內的東西，print本身不用印出來\n\n編譯錯誤輸出：compi err\n沒有輸出結果：no output\n請在輸出前加上：>>>\n\nInt a = 0!",
]

response = model.generate_content(prompt_parts)
print(response.text)