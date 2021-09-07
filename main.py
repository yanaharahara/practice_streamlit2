#音声認識ありかも(目の不自由な人に音声で混雑状況を伝える)
import streamlit as st
from datetime import datetime
import pandas as pd
import winsound
#import time
#7行目は写真挿入などの時に使うかも
#import streamlit.components.v1 as stc
while(True):
    i = 50
    break

st.title('混雑状況確認アプリ')

st.write('始めに入退室ボタンを押してください')

#checkbox?
left_column,right_column = st.columns(2)
left_button = left_column.button('入室')
right_button = right_column.button('退室')

if left_button:
    st.write('iniadへようこそ')
if right_button:
    st.write('またのご利用お待ちしております。')


latest_iteration = st.empty()
bar = st.progress(0)

if left_button:
    if i >= 30 and i <= 49:
        latest_iteration.text(f'現在の施設内の人数 {i+1}')
        st.write('人が若干増えてきました')
        bar.progress(i+1)
    if i >= 50 and i <= 79:
        latest_iteration.text(f'現在の施設内の人数 {i+1}')
        st.write('建物内で出来るだけ混雑を作らないようにしましょう')
        bar.progress(i+1)
    if i >= 80:
        latest_iteration.text(f'現在の施設内の人数 {i+1}')
        st.write('かなり人流が増えてきています')
        bar.progress(i+1)
    if i <= 29:
        latest_iteration.text(f'現在の施設内の人数 {i+1}')
        st.write('比較的空いています')
        bar.progress(i+1)


        
if right_button:
    i+=1
    latest_iteration.text(f'現在の施設内の人数 {i-1}')
    bar.progress(i-1)

#now = datetime.datetime.now()
#st.write(now.strftime('現在の日時は、%Y年%m月%d日 %H:%M:%S'))
now = datetime.today()
st.write(now.strftime('現在の日時は、%Y年%m月%d日 %H:%M:%S'))


#この施設の混雑度具合はアンケートを取る
#時間ごとに混んでいる施設をアドバイス
if now.hour != 12 and now.hour != 13:
    st.write('現在の時間帯は比較的どこの施設も空いています。')

if now.hour >= 12 and now.hour <= 13:
    st.write('この時間帯は普段だと、食堂が若干混んでいます') 

#ここもアンケートを取る(いまのところリアルタイムで混雑度収集は厳しそうだから)
#時間ごとに表示するデータフレームを変える(if now.hour >= 12 みたいに)
df = pd.DataFrame({
    '場所':['INIADホール','講義室','糖朝'],
    '混雑度(MAXが100)':[60,40,50]
})     

#dataframe or table
st.dataframe(df.style.highlight_max(axis=0),width=10000,height=10000)



st.title('INIADについての混雑状況のお問い合わせ')
expander1 = st.expander('INIAD内でどの場所が一番混雑していますか？')
expander1.write('INIADホール付近は授業の前後でたくさんの生徒が集まります。')
expander2 = st.expander('食堂のすいている時間帯を教えてください')
expander2.write('糖朝については2限と3限の間の時間帯以外は基本的に空いています。その時間帯を狙いましょう。')
expander3 = st.expander('表の見方を教えてください')
expander3.write('1列目が場所、2列目がその場所の混雑度を表しています。列名のところをクリックすると、ソートもできるのでランキング形式にしてみるとさらに見やすくなります。')

#リンクの設定
st.write('iniadのホームページは下記のリンクから')
st.markdown('<a href="https://www.iniad.org/">iniadホームページ</a>',unsafe_allow_html=True)

#音声の再生
#st.audio('音声ファイルの名前')

#音声の自動再生(この方法だとボタンを押す度に反応してしまう)
#import winsound
#winsound.PlaySound('音声ファイルの名前.wav', winsound.SND_FILENAME)

#音声の自動再生方法2
#from fabric.api import runs_once
#@runs_once
#def play():
    #winsound.PlaySound('新音声データ.wav', winsound.SND_FILENAME)
#def play2():
    #play()
#play2()





#stc.html('<img width="200" alt="test" src="https://cafe-mickey.com/coffee-life/wp-content/uploads/2021/02/image.gif">')





