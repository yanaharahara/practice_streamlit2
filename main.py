#音声認識ありかも(目の不自由な人に音声で混雑状況を伝える)
import streamlit as st
import datetime
import pandas as pd
import pytz
#import winsound
#import time
#9行目は写真挿入などの時に使うかも
#import streamlit.components.v1 as stc
from PIL import Image

if "hoge" not in st.session_state:
   st.session_state.hoge = 0


#バルーン
#st.balloons()

def color_background(x):
            color = ""
            if x["混雑度(MAXが100)"] >= 80:
                color = "background-color: #FF6666; color: #FFFFFF;"
            elif x["混雑度(MAXが100)"] <= 10:
                color = "background-color: #659AD2; color: #FFFFFF;"
            
            return [color for _ in x]


def english():
    #ロゴの挿入
    image = Image.open('app_logo.png')
    st.image(image,use_column_width=True)

    #st.title('混雑状況確認アプリ')

    st.write('First, please press the Enter / Exit button.')

    #checkbox?
    left_column,right_column = st.columns(2)
    left_button = left_column.button('Entry')
    right_button = right_column.button('Exit')

    if left_button:
        st.write('Welcome to INIAD')
        

    if right_button:
        st.write('We look forward to seeing you again.')


    latest_iteration = st.empty()
    bar = st.progress(0)

    if left_button:
        st.session_state.hoge += 1
        if st.session_state.hoge >= 30 and st.session_state.hoge <= 49:
            latest_iteration.text(f'Current number of people in the facility {st.session_state.hoge}')
            st.write('The number of people has increased slightly')
            bar.progress(st.session_state.hoge)
        if st.session_state.hoge >= 50 and st.session_state.hoge <= 79:
            latest_iteration.text(f'Current number of people in the facility {st.session_state.hoge}')
            st.write('Try to create as little congestion as possible in the building.')
            bar.progress(st.session_state.hoge)
        if st.session_state.hoge >= 80:
            latest_iteration.text(f'Current number of people in the facility {st.session_state.hoge}')
            st.write('The flow of people is increasing considerably.')
            bar.progress(st.session_state.hoge)
        if st.session_state.hoge <= 29:
            latest_iteration.text(f'Current number of people in the facility {st.session_state.hoge}')
            st.write('It is relatively empty.')
            bar.progress(st.session_state.hoge)


            
    if right_button:
        if st.session_state.hoge >= 1: 
            st.session_state.hoge -= 1
        latest_iteration.text(f'Current number of people in the facility {st.session_state.hoge}')
        bar.progress(st.session_state.hoge)

    #now = datetime.datetime.now()
    #st.write(now.strftime('現在の日時は、%Y年%m月%d日 %H:%M:%S'))
    now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
    st.write(now.strftime('The current date and time are %Y/%m/%d %H:%M:%S'))


    #時間ごとに混んでいる施設をアドバイス
    #時間ごとに表示するデータフレームを変える(if now.hour >= 12 みたいに)
    #dataframe or table
    if now.hour == 12:
        st.write('Currently, the cafeteria and Totyo tend to be crowded.')
        df = pd.DataFrame({
        'Place':['B:Lecture room','F:Totyo','C:INIAD Hall','E:Cafeteria','D:Presentation Hub','A:Media Center'],
        'Congestion (Max=100)':[10,100,30,100,60,10]
        })
        st.dataframe(df.style.apply(color_background,axis=1),width=10000,height=10000)

    elif now.hour >= 8 and now.hour <= 11:
        st.write('Currently, the presentation hub on the first floor tends to be crowded')
        df = pd.DataFrame({
        'Place':['C:Lecture room','D:Totyo','B:INIAD Hall','E:Cafeteria','F:Presentation Hub','A:Media Center'],
        'Congestion (Max=100)':[40,90,10,90,100,10]
        })
        st.dataframe(df.style.apply(color_background,axis=1),width=10000,height=10000)
        

    elif now.hour >= 13  and now.hour <= 17:
        st.write('At the moment, the cafeteria tends to be crowded,  \nbut Totyo is relatively empty..')
        df = pd.DataFrame({
        'Place':['C:Lecture room','D:Totyo','B:INIAD Hall','F:Cafeteria','E:Presentation Hub','A:Media Center'],
        'Congestion (Max=100)':[15,50,10,100,70,5]
        })
        st.dataframe(df.style.apply(color_background,axis=1),width=10000,height=10000)
        
    elif now.hour >= 18  and now.hour <= 19:
        st.write('The presentation hub on the first floor tends to be crowded at this time of day  \nThe other facilities are relatively empty.')
        df = pd.DataFrame({
        'Place':['C:Lecture room','D:Totyo','B:INIAD Hall','E:Cafeteria','F:Presentation Hub','A:Media Center'],
        'Congestion (Max=100)':[10,40,10,80,100,5]
        })
        st.dataframe(df.style.apply(color_background,axis=1),width=10000,height=10000)

    else:
        st.write('Currently, it is out of service hours. Entry hours are from 8:30am to 8:00pm on weekdays.')
        







    st.title('Inquire about congestion at INIAD')
    expander1 = st.expander('Which areas in INIAD are the most crowded?')
    expander1.write('It depends on the time of day, but basically the cafeteria will be the most likely place to be crowded.')
    expander2 = st.expander('What is the best time to go to Totyo?')
    expander2.write('Except for the period between 2nd and 3rd period, Totyo is basically empty. Aim for those times.')
    expander3 = st.expander('How to read the table?')
    expander3.write('The first column shows the location and the second column shows the congestion level of the location.  \nIf you click on the column name, you can also sort it, so it will be even easier to see it in a ranking format.')

    #リンクの設定(ここに建物のホームページのリンクを貼る)
    st.write('INIAD Website')
    st.markdown('<a href="https://www.iniad.org/">INIAD Website</a>',unsafe_allow_html=True)

def japanese():
    #ロゴの挿入
    image = Image.open('app_logo.png')
    st.image(image,use_column_width=True)

    #st.title('混雑状況確認アプリ')

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
        st.session_state.hoge += 1
        if st.session_state.hoge >= 30 and st.session_state.hoge <= 49:
            latest_iteration.text(f'現在の施設内の人数 {st.session_state.hoge}')
            st.write('人が若干増えてきました')
            bar.progress(st.session_state.hoge)
        if st.session_state.hoge >= 50 and st.session_state.hoge <= 79:
            latest_iteration.text(f'現在の施設内の人数 {st.session_state.hoge}')
            st.write('建物内で出来るだけ混雑を作らないようにしましょう')
            bar.progress(st.session_state.hoge)
        if st.session_state.hoge >= 80:
            latest_iteration.text(f'現在の施設内の人数 {st.session_state.hoge}')
            st.write('かなり人流が増えてきています')
            bar.progress(st.session_state.hoge)
        if st.session_state.hoge <= 29:
            latest_iteration.text(f'現在の施設内の人数 {st.session_state.hoge}')
            st.write('比較的空いています')
            bar.progress(st.session_state.hoge)


            
    if right_button:
        if st.session_state.hoge >= 1:
            st.session_state.hoge -= 1
        latest_iteration.text(f'現在の施設内の人数 {st.session_state.hoge}')
        bar.progress(st.session_state.hoge)

    #now = datetime.datetime.now()
    #st.write(now.strftime('現在の日時は、%Y年%m月%d日 %H:%M:%S'))
    now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
    st.write(now.strftime('現在の日時は、%Y年%m月%d日 %H:%M:%S'))


    #時間ごとに混んでいる施設をアドバイス
    #時間ごとに表示するデータフレームを変える(if now.hour >= 12 みたいに)
    #dataframe or table
    if now.hour == 12:
        st.write('現在の時間帯は食堂と糖朝が混雑する傾向にあります')
        df = pd.DataFrame({
        '場所':['B:講義室','F:糖朝','C:INIADホール','E:食堂','D:プレゼンテーションハブ','A:メディアセンター'],
        '混雑度(MAXが100)':[10,100,30,100,60,10]
        })
        st.dataframe(df.style.apply(color_background,axis=1),width=10000,height=10000)

    elif now.hour >= 8 and now.hour <= 11:
        st.write('現在の時間帯は1階のプレゼンテーションハブが混雑する傾向にあります')
        df = pd.DataFrame({
        '場所':['C:講義室','D:糖朝','B:INIADホール','E:食堂','F:プレゼンテーションハブ','A:メディアセンター'],
        '混雑度(MAXが100)':[40,90,10,90,100,10]
        })
        st.dataframe(df.style.apply(color_background,axis=1),width=10000,height=10000)

    elif now.hour >= 13  and now.hour <= 17:
        st.write('現在の時間帯は食堂が混雑する傾向にあります  \nまた、糖朝は比較的空いています')
        df = pd.DataFrame({
        '場所':['C:講義室','D:糖朝','B:INIADホール','F:食堂','E:プレゼンテーションハブ','A:メディアセンター'],
        '混雑度(MAXが100)':[15,50,10,100,70,5]
        })
        
        st.dataframe(df.style.apply(color_background,axis=1),width=10000,height=10000)
        #st.dataframe(df.style.highlight_max(axis=0,color="#FF6666").highlight_min(axis=0,color="#659AD2"),width=10000,height=10000)
        #color = "background-color: #FFFFFF; color: #000000;"
        
    elif now.hour >= 18  and now.hour <= 19:
        st.write('現在の時間帯は1階のプレゼンテーションハブが混雑する傾向にあります  \nまた、ほかの施設は比較的空いています')
        df = pd.DataFrame({
        '場所':['C:講義室','D:糖朝','B:INIADホール','E:食堂','F:プレゼンテーションハブ','A:メディアセンター'],
        '混雑度(MAXが100)':[10,40,10,80,100,5]
        })
        st.dataframe(df.style.apply(color_background,axis=1),width=10000,height=10000)

    else:
        st.write('現在は入構時間外になります  \n入構時間は平日8:30-20:00になります')
        







    st.title('INIADについての混雑状況のお問い合わせ')
    expander1 = st.expander('INIAD内でどの場所が一番混雑していますか？')
    expander1.write('時間帯にもよりますが基本的には食堂が一番混雑する可能性の高い場所になります')
    expander2 = st.expander('糖朝の空いている時間帯を教えてください')
    expander2.write('糖朝については2限と3限の間の時間帯以外は基本的に空いています。その時間帯を狙いましょう。')
    expander3 = st.expander('表の見方を教えてください')
    expander3.write('1列目が場所、2列目がその場所の混雑度を表しています。列名のところをクリックすると、ソートもできるのでランキング形式にしてみるとさらに見やすくなります。')

    #リンクの設定(ここに建物のホームページのリンクを貼る)
    st.write('iniadのホームページは下記のリンクから')
    st.markdown('<a href="https://www.iniad.org/">iniadホームページ</a>',unsafe_allow_html=True)



    #待ち時間の表示
    #import time
    #with st.spinner('Wait for it...'):
        #time.sleep(5)
    #st.success('Done!') 
    
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


lang = st.selectbox("言語を選択してください。please choose language",("日本語","English"))

#ボタンが押されたら
if lang == "日本語":
    japanese()
elif lang == "English":
    english()

else:
    japanese()


    


