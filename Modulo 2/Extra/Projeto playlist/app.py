import streamlit as st

generos= {
    "K-pop": {
        "Stray Kids":"https://www.youtube.com/watch?v=57n4dZAPxNY&list=RD57n4dZAPxNY&start_radio=1",
        "Twice":"https://www.youtube.com/watch?v=eHHQaoEW30Q&list=RDeHHQaoEW30Q&start_radio=1",
        "Enhypen":"https://www.youtube.com/watch?v=FPDYeRk2PO8&list=RDFPDYeRk2PO8&start_radio=1",
        "XLOV":"https://www.youtube.com/watch?v=NBZgirj_C2Y&list=RDNBZgirj_C2Y&start_radio=1"
    },
    "Pop" : {
        "Katseye":"https://www.youtube.com/watch?v=l9CZykYZkOQ&list=RDl9CZykYZkOQ&start_radio=1",
        "Ariana Grande":"https://www.youtube.com/watch?v=gl1aHhXnN1k&list=RDgl1aHhXnN1k&start_radio=1",
        "Sabrina Carpenter":"https://www.youtube.com/watch?v=aSugSGCC12I&list=RDaSugSGCC12I&start_radio=1",
        "One Direction":"https://www.youtube.com/watch?v=QJO3ROT-A4E&list=RDQJO3ROT-A4E&start_radio=1"
    },
    "MPB":{
        "ANAVITÓRIA":"https://www.youtube.com/watch?v=qkuRfK4Ye4U&list=RDqkuRfK4Ye4U&start_radio=1",
        "Melim":"https://www.youtube.com/watch?v=gxrwP81P2zQ&list=RDgxrwP81P2zQ&start_radio=1",
        "Vitor Kley":"https://www.youtube.com/watch?v=YVJijQIualA&list=RDYVJijQIualA&start_radio=1",
        "Jão":"https://www.youtube.com/watch?v=d9RM8viAKrw&list=RDd9RM8viAKrw&start_radio=1"
    },
    "Pagode":{
        "Seu Jorge":"https://www.youtube.com/watch?v=2GsBx_SmjOI&list=RD2GsBx_SmjOI&start_radio=1",
        "Mumuzinho":"https://www.youtube.com/watch?v=QdCd6L0uhcc&list=RDQdCd6L0uhcc&start_radio=1",
        "Dilsinho":"https://www.youtube.com/watch?v=a_rxi0ujVGI&list=RDa_rxi0ujVGI&start_radio=1",
        "Turma do Pagode":"https://www.youtube.com/watch?v=S_SXl-ETXRI&list=RDS_SXl-ETXRI&start_radio=1"

    }

}

#------------------------------------------SIDEBAR
st.sidebar.title("BiaBeats")
st.sidebar.image("gato.png")

genero= st.sidebar.selectbox("Escolha um gênero musical",generos.keys())

artista= st.sidebar.selectbox("Escolha um artista",generos[genero].keys())

#------------------------------------------BODY

st.title(artista)
st.markdown('---')

video,sobre=st.tabs(['Vídeo',"Sobre o Artista"])

with video:
    st.video(generos[genero][artista])

with sobre:
    if artista=="Stray Kids":
        st.markdown("""
        Stray Kids (em coreano: 스트레이 키즈; romaniz.: Seuteurei kijeu; comumente abreviado como SKZ) é um grupo masculino sul-coreano formado pela JYP Entertainment. É composto por oito integrantes: Bang Chan, Lee Know, Changbin, Hyunjin, Han, Felix, Seungmin e I.N. Por motivos pessoais não revelados, Woojin deixou o grupo em outubro de 2019. Stray Kids produz suas próprias gravações; a equipe principal de produção se chama 3Racha e consiste em Bang Chan, Changbin e Han, e os outros membros frequentemente participam da composição das músicas.
        """)
    elif artista =="Twice":
            st.markdown("""
        Twice (em coreano: 트와이스; romaniz.: Teuwaiseu; em japonês: トゥワイス; romaniz.: Tuwaisu) é um grupo feminino sul-coreano formado pela JYP Entertainment em 2015. O grupo é composto de nove integrantes: Nayeon, Jeongyeon, Momo, Sana, Jihyo, Mina, Dahyun, Chaeyoung e Tzuyu. Twice foi formado no reality show Sixteen (2015) e estreou em 20 de outubro de 2015, com o extended play (EP) The Story Begins.[3]
        """)
    elif artista =="Enhypen":
         st.markdown("""
        Enhypen (hangul: 엔하이픈; rr: Enhaipeun; em japonês: エンハイプン; Enhaipun; estilizado como ENHYPEN), é um boy-group sul-coreano formado pela empresa Belift Lab, empreendimento conjunto entre as empresas de entretenimento CJ ENM e HYBE Corporation.[3] Formado por meio do reality show de sobrevivência de 2020, I-Land, o grupo é composto por sete integrantes: Jungwon, Heeseung, Jay, Jake, Sunghoon, Sunoo e Ni-ki. Enhypen estreou em 30 de novembro de 2020, com o extended play (EP) Border: Day One.         
         """)
    elif artista =="XLOV":
         st.markdown("""
        XLOV (em coreano: 엑스러브; RR: Ekseureobeu) é um grupo masculino sul-coreano formado e gerenciado pela 257 Entertainment. O grupo é composto por quatro membros: Wumuti, Rui, Hyun e Haru. Eles estrearam em 7 de janeiro de 2025 com seu single álbum I'mma Be.
        """)
    elif artista =="Katseye":
         st.markdown("""
        Katseye (em inglês: Katseye; [ˈkætsaɪ]; ket-s-ai; estilizado em letras maiúsculas; traduzido para o português como Olho de Gato, referência à gema de mesmo nome) é um grupo feminino formado pela Hybe UMG e Geffen Records e baseado em Los Angeles. O grupo é composto por seis integrantes: Manon, Sophia, Daniela, Lara, Megan e Yoonchae. Com membros da Filipinas, Coreia do Sul, Suíça e Estados Unidos (com raízes ligadas diretamente a Venezuela, Cuba, Índia, Suécia, Singapura e China)[1][2][3], é comumente descrito como um grupo feminino global.[4][5]
        """)
    elif artista =="Ariana Grande":
         st.markdown("""
         Ariana Grande-Butera[2][3] (Boca Raton, 26 de junho de 1993)[4][5] é uma cantora, compositora e atriz norte-americana. Ao longo da carreira, tornou-se uma das cantoras mais ouvidas da história da música em streaming[6] e um dos nomes de maior relevância da música pop na atualidade.[
        """)
    elif artista =="Sabrina Carpenter":
         st.markdown("""
        Sabrina Annlynn Carpenter[1] (Quakertown, 11 de maio de 1999)[2] é uma cantora, compositora, produtora e atriz norte-americana.[3][4] Ganhou popularidade ao estrelar a série Girl Meets World (2014–2017), do Disney Channel, e posteriormente assinou com a Hollywood Records.[5][6][7] Ela lançou seu single de estreia "Can't Blame a Girl for Trying" em 2014, seguido pelos álbuns de estúdio Eyes Wide Open (2015), Evolution (2016), Singular: Act I (2018) e Singular: Act II (2019).
        """)
    elif artista =="One Direction":
         st.markdown("""
        One Direction , frequentemente abreviado para 1D , foi uma boy band pop anglo-irlandesa formada em Londres em 2010. O grupo era composto por Niall Horan , Liam Payne , Harry Styles , Louis Tomlinson e Zayn Malik (até sua saída em 2015). O grupo vendeu mais de 70 milhões de discos em todo o mundo, tornando-se uma das boy bands mais vendidas de todos os tempos, antes de entrar em hiato por tempo indeterminado em 2016.
        """)
    elif artista =="ANAVITÓRIA":
         st.markdown("""
        Anavitória é uma dupla de música folk-pop brasileira formado em 2014 em Araguaína, Tocantins pelas cantoras Ana Caetano e Vitória Falcão.[3]

        Alcançaram o sucesso na música popular brasileira com o lançamento de seu primeiro álbum de estúdio homônimo, Anavitória em 2016, aclamado pela critica e que recebeu a certificação de disco de diamante, vendendo mais de 300 mil cópias.
        """)