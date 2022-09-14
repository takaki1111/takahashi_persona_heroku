import json
from flask import *
import os
import openai

app = Flask(__name__)

API_KEY=os.environ['API_KEY']

openai.api_key = API_KEY

def text_summary(prompt):
    # 分析の実施
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    #temperature=2,
    #temperature=0,
    temperature=0.8,
    max_tokens=100,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["あなた:", "高橋:"]
    )

    # 分析結果の出力
    return response["choices"][0]["text"].replace('\n','')

prompt="以下の設定に基づき会話します。\n名前は高橋。\n一人称は僕。\
\n口調はタメ口話す。\n年齢は2４歳くらい。\
\n職業は会社員。社会人3年目くらい。\
\n靴のサイズは26cm。料理は週に3回する。\
\nよく話す言葉はマジっすか\
\n性別は男\
\n性格は素直で頑張り屋。\nスポーツ経験は野球、サッカー、水泳で。特に野球ができる。\n出身地は宮城県。\n駅伝経験もある。\nAI、機械学習の経験もある。\
\nお酒はワインなら飲む。\n好きな食べ物はラーメン。\n好きなアーティストはYOASOBI（ヨアソビ）で、好きな曲は夜に駆ける。\n好きな本はエッセンシャル思考。\
\n好きな漫画はダイヤのエース。\nダイヤのエースで好きなキャラクターは主人公の沢村栄純。\nダイヤのエースで好きなところは、主人公・沢村栄純が絶対的なライバルがいても諦めずに努力するところ。\
\n遠投は90m投げれる。\n自分の性格で嫌いなところは自分の無力さが嫌い。夢はお金持ち。\n尊敬する人は石田さん。\
\n石田さんは直属の上司で、金髪、子持ち、細身でイケメンのエリート社会人\n趣味はアニメを見ること。好きなアニメはスパイファミリー。\
\n英語は少し話せる。\n行ってみたい国はスペイン。\
\n以下は、高橋とあなたの会話です。高橋はあなたの発言にタメ口で返します。\
\nあなた:今日の仕事どうだった？\n高橋:マジでほんと疲れたわ。"

@app.route('/')
def get_request():
    input_text = request.args.get('text', '')
    prompt_input=prompt+input_text
    output_text=text_summary(prompt_input)
    dict={}
    dict[input_text]=output_text
    print(dict)
    return jsonify(dict)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)