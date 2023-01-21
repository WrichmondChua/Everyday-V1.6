# The script of the game goes in this file
# Declare characters used by this game. The color argument colorizes the
# name of the character.
# Blue colour for male characters and for general characters and Pink colour for female characters.
#0040ff- Blue
#ff00ff- Pink
default scoreL1SHS= 0
default scoreL2SHS= 0
default scoreL3SHS= 0

default scoreL1College = 0
default scoreL2College = 0
default scoreL3College = 0

default scorepopquiz= 0

default L1SHSProgress = 0
default L2SHSProgress = 0
default L3SHSProgress = 0

default L1CollegeProgress = 0
default L2CollegeProgress = 0
default L3CollegeProgress = 0

#shs and college pop quiz
define Wrichmond= Character("Wrichmond", color= "#0040ff")
define mrpopquiz= Character("Mr.Pop Quiz", color= "#0040ff")

#images for Pop Quiz
image MrPopQuiz= im.Scale("Characters/Mr.PopQuiz.png", 650,820)

#shs
define martin = Character("Martin", color= "#0040ff")
define matthew = Character("Matthew", color= "#0040ff")
define allen = Character ("Allen", color= "#0040ff")
define teachermarites= Character("Teacher Marites", color= "#ff00ff")
define teacherkaren= Character("Teacher Karen", color= "#ff00ff")
define elevenA= Character ("11-A Students", color= "#0040ff")
define player = Character("[playername]", color= "#0040ff")

#college
define adrian= Character("Adrian", color= "#0040ff")
define christian= Character("Christian", color= "#0040ff")
define mark= Character("Mark", color= "#0040ff")
define teacherluna= Character("Teacher Luna", color= "#ff00ff")
define teacherraul= Character("Teacher Raul", color= "#0040ff")

#shs
image Martin = im.Scale("Characters/Martin.png", 650, 820)
image MatthewSweat = im.Scale("Characters/Matthew Sweat.png", 650, 820)
image Matthew= im.Scale("Characters/Matthew.png", 650,820)
image Allen= im.Scale("Characters/Allen.png", 650, 820)
image Wrichmond= im.Scale("Characters/Wrichmond.png", 650,820)
image TeacherMarites= im.Scale("Characters/TeacherMarites.png", 850,900)
image TeacherKaren= im.Scale("Characters/TeacherKaren.png", 850,900)

#college
image Adrian= im.Scale("Characters/Adrian.png", 650,820)
image Christian= im.Scale("Characters/Christian.png", 650,820)
image Mark= im.Scale("Characters/Mark.png", 650,820)
image TeacherLuna= im.Scale("Characters/TeacherLuna.png", 850,900)
image TeacherRaul= im.Scale("Characters/TeacherRaul.png", 650,820)

#QuizSHS
define Question1SHS= Character("Question 1")
define Question2SHS= Character("Question 2")
define Question3SHS= Character("Question 3")
define Question4SHS= Character("Question 4")
define Question5SHS= Character("Question 5")
define Question6SHS= Character("Question 6")
define Question7SHS= Character("Question 7")
define Question8SHS= Character("Question 8")
define Question9SHS= Character("Question 9")
define Question10SHS= Character("Question 10")

#QuizCollege
define Question1College= Character("Question 1")
define Question2College= Character("Question 2")
define Question3College= Character("Question 3")
define Question4College= Character("Question 4")
define Question5College= Character("Question 5")
define Question6College= Character("Question 6")
define Question7College= Character("Question 7")
define Question8College= Character("Question 8")
define Question9College= Character("Question 9")
define Question10College= Character("Question 10")
#
image campus = im.Scale("Places/campus2.jpg",1280,720)
image hallway = im.Scale("Places/hallway.jpg",1280,720)
image cr= im.Scale("Places/cr.jpg", 1280,720)
image cafeteria= im.Scale("Places/cafeteria.jpg", 1280,720)
image ClassroomSHS= im.Scale("Places/classroomshs.png", 1280,720)
image HouseProtag= im.Scale("Places/HouseProtag.png", 1280, 720)
image LivingRoom= im.Scale("Places/LivingRoom.jpg", 1280,720)
image Bedroom= im.Scale ("Places/Bedroom.jpg", 1280,720)
image BlackBG= im.Scale("Backgrounds/black.jpg", 1280,720)
image FoamMattress= im.Scale("FoamMattress.png", 1280,720)
image TheEnd= "The End.jpg"
image chalkboard= im.Scale("Backgrounds/Chalkboard.jpg", 1280,720)
image locked= "gallery0.jpg"
image colorcode= "ColorCode.jpg"
#
image L1SHS= "SHSLessons/L1SHS.png"
image L1SHS2= "SHSLessons/L1SHS2.png"
image L1SHS3= "SHSLessons/L1SHS3.png"
image L1SHS4= "SHSLessons/L1SHS4.png"
image L1SHS5= "SHSLessons/L1SHS5.png"
image L1SHS6= "SHSLessons/L1SHS6.png"
image L1SHS7= "SHSLessons/L1SHS7.png"
image L1SHS8= "SHSLessons/L1SHS8.png"
image L1SHS9= "SHSLessons/L1SHS9.png"
image L1SHS10= "SHSLessons/L1SHS10.png"
image L1SHS11= "SHSLessons/L1SHS11.png"
image L2SHS= "SHSLessons/L2SHS.jpg"
image L2SHS2= "SHSLessons/L2SHS2.png"
image L2SHS3= "SHSLessons/L2SHS3.png"
image L2SHS4= "SHSLessons/L2SHS4.png"
image L2SHS5= "SHSLessons/L2SHS5.png"
image L2SHS6= "SHSLessons/L2SHS6.png"
image L2SHS7= "SHSLessons/L2SHS7.png"
image L2SHS8= "SHSLessons/L2SHS8.png"
image L2SHS9= "SHSLessons/L2SHS9.png"
image L2SHS10= "SHSLessons/L2SHS10.png"
image L3SHS= "SHSLessons/L3SHS.jpg"
image L3SHS2= "SHSLessons/L3SHS2.png"
image L3SHS3= "SHSLessons/L3SHS3.png"
image L3SHS4= "SHSLessons/L3SHS4.png"
image L3SHS5= "SHSLessons/L3SHS5.png"
image L3SHS6= "SHSLessons/L3SHS6.png"
image L3SHS7= "SHSLessons/L3SHS7.png"
image L3SHS8= "SHSLessons/L3SHS8.png"
image L3SHS9= "SHSLessons/L3SHS9.png"
image L3SHS10= "SHSLessons/L3SHS10.png"
image Mechanics1= "Mechanics1.png"
image Mechanics2= "Mechanics2.png"
#
image L1College= "CollegeLessons/L1College.png"
image L1College2= "CollegeLessons/L1College2.png"
image L1College3= "CollegeLessons/L1College3.png"
image L1College4= "CollegeLessons/L1College4.png"
image L1College5= "CollegeLessons/L1College5.png"
image L1College6= "CollegeLessons/L1College6.png"
image L1College7= "CollegeLessons/L1College7.png"
image L1College8= "CollegeLessons/L1College8.png"
image L1College9= "CollegeLessons/L1College9.png"
image L1College10= "CollegeLessons/L1College10.png"
image L1College11= "CollegeLessons/L1College11.png"
image L2College= "CollegeLessons/L2College.png"
image L2College2= "CollegeLessons/L2College2.png"
image L2College3= "CollegeLessons/L2College3.png"
image L2College4= "CollegeLessons/L2College4.png"
image L3College= "CollegeLessons/L3College.png"
image L3College2= "CollegeLessons/L3College2.png"
image L3College3= "CollegeLessons/L3College3.png"
image L3College4= "CollegeLessons/L3College4.png"


# The game starts here.
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 1.0
    on hide:
        linear 0.5 alpha 0
    # This is to fade the bar in and out, and is only required once in your script

init: ### just setting variables in advance so there are no undefined variable problems
    $ timer_range = 0
    $ timer_jump = 0
    $ time = 0

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01),
    false=[Hide('countdown'), Jump(timer_jump)])
        ### ^this code decreases variable time by 0.01 until time hits 0, at which point, the game jumps to label timer_jump (timer_jump is another variable that will be defined later)

    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve
        # ^This is the timer bar.

label start:

    "Before the game starts, we would like to show you the color code that can help you access the lessons
    for both Senior High School and College easily."

    show ColorCode

    window hide

    pause

    hide ColorCode

    "Thank you for seeing the color code. Have fun playing!"

    #This is for inputting the player name of your choice
    python:
        playername=renpy.input("Please enter the protagonist's name: ", length=32)
        playername=playername.strip()

    #Player name by default if the player entered the game w/o inputting a playern name.
        if not playername:
            playername= "Default"


    #Grade or year level

    menu:
        "Choose your difficulty"

        "Senior High School":
            jump popquizshsprompt
        "College":
            jump popquizcollegeprompt

    return

    label popquizshsprompt:
        menu:
            "Do you want to have a pop quiz first before proceeding to the game?"

            "Yes":
                jump popquizshs
            "Skip pop quiz":
                jump shs

    label popquizshs:

            show chalkboard

            show MrPopQuiz

            mrpopquiz "In this pop quiz, you will answer 5 questions. Whether you answered all of the questions or not,
            the game will proceed so good luck and have fun."

            hide MrPopQuiz

            jump Question1PopQuizSHS

    return

    label Question1PopQuizSHS:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question1popquizshs_slow'      ### set where you want to jump once the timer runs out


        Question1SHS "Who is not a poet?"
        jump q1popquizshs
    return

    label q1popquizshs:

        show screen countdown                          ### call and start the timer

        menu:

            "A. William Shakespeare":
                call popquizwronganswershs1
            "B. Oscar Wilde":
                call popquizwronganswershs1
            "C. Rudyard Kipling":
                call popquizwronganswershs1
            "D. Peter Griffin":
                call popquizcorrectanswershs1

    return

    label popquizwronganswershs1:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}D. Peter Griffin{/b}.
        You may now proceed to Question no. 2."
        $ scorepopquiz +=0
        stop sound
        stop music
        jump Question2PopQuizSHS

    return

    label popquizcorrectanswershs1:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 2."
        $ scorepopquiz +=1
        stop sound
        stop music
        jump Question2PopQuizSHS
    return

    label question1popquizshs_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}D. Peter Griffin{/b}.
        You may now proceed to Question no. 2."
        $ scorepopquiz +=0
        stop sound
        stop music
        jump Question2PopQuizSHS
    return


    label Question2PopQuizSHS:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question2popquizshs_slow'                    ### set where you want to jump once the timer runs out


        Question2SHS "Which of the following is a pronoun?"
        jump q2popquizshs
    return

    label q2popquizshs:

        show screen countdown                          ### call and start the timer

        menu:

            "A. He":
                call popquizcorrectanswershs2
            "B. Was":
                call popquizwronganswershs2
            "C. Below":
                call popquizwronganswershs2
            "D. Under":
                call popquizwronganswershs2

    return


    label popquizwronganswershs2:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. He{/b}.
        You may now proceed to Question no. 3."
        $ scorepopquiz +=0
        stop sound
        stop music
        jump Question3PopQuizSHS

    return

    label popquizcorrectanswershs2:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 3."
        $ scorepopquiz +=1
        stop sound
        stop music
        jump Question3PopQuizSHS
    return

    label question2popquizshs_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}A. He{/b}. You may now proceed to Question no. 3."
        $ scorepopquiz +=0
        stop sound
        stop music
        jump Question3PopQuizSHS
    return


    label Question3PopQuizSHS:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question3popquizshs_slow'                    ### set where you want to jump once the timer runs out


        Question3SHS "What is the past tense of leave?"
        jump q3popquizshs
    return

    label q3popquizshs:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Leaved":
                call popquizwronganswershs3
            "B. Lived":
                call popquizwronganswershs3
            "C. Left":
                call popquizcorrectanswershs3
            "D. Leaves":
                call popquizwronganswershs3

    return

    label popquizwronganswershs3:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}C. Left{/b}.
        You may now proceed to Question no. 4."
        $ scorepopquiz +=0
        stop sound
        stop music
        jump Question4PopQuizSHS

    return

    label popquizcorrectanswershs3:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 4."
        $ scorepopquiz +=1
        stop sound
        stop music
        jump Question4PopQuizSHS
    return

    label question3popquizshs_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}C. Left{/b}. You may now proceed to Question no. 4."
        $ scorepopquiz +=0
        stop sound
        stop music
        jump Question4PopQuizSHS
    return


    label Question4PopQuizSHS:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question4popquizshs_slow'                    ### set where you want to jump once the timer runs out


        Question4SHS "A noun that serves as the name to a specific place, person, or thing."
        jump q4popquizshs
    return

    label q4popquizshs:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Common Noun":
                call popquizwronganswershs4
            "B. Proper Noun":
                call popquizcorrectanswershs4
            "C. Verb":
                call popquizwronganswershs4
            "D. Pronoun":
                call popquizwronganswershs4

    return

    label popquizwronganswershs4:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}B. Proper Noun{/b}.
        You may now proceed to Question no. 5."
        $ scorepopquiz +=0
        stop sound
        stop music
        jump Question5PopQuizSHS

    return

    label popquizcorrectanswershs4:
    hide screen countdown
    play sound "audio/Correct Answer sfx.mp3"
    "Your answer is correct! You may now proceed to Question no. 5."
    $ scorepopquiz +=1
    stop sound
    stop music
    jump Question5PopQuizSHS

    return

    label question4popquizshs_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}B. Proper Noun{/b}.
        You may now proceed to Question no. 5."
        $ scorepopquiz +=0
        stop sound
        stop music
        jump Question5PopQuizSHS
    return


    label Question5PopQuizSHS:
        $ time =10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question5popquizshs_slow'                    ### set where you want to jump once the timer runs out


        Question5SHS "Who wrote the poem and/or Anglican Hymn All Things Bright and Beautiful?"
        jump q5popquizshs
    return

    label q5popquizshs:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Emily Dickenson":
                call popquizwronganswershs5
            "B. Charlie Chaplin":
                call popquizwronganswershs5
            "C. Dr. Seuss":
                call popquizwronganswershs5
            "D. Cecil Frances Alexander":
                call popquizcorrectanswershs5

    return


    label popquizcorrectanswershs5:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! And this is the end of the pop quiz, let us now see the results."
        $ scorepopquiz +=1
        stop sound
        stop music
        jump ResultsPopQuizSHS

    return

    label popquizwronganswershs5:
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}D. Cecil Frances Alexander{/b}.
        And this is the end of the pop quiz, let us now see the results."
        $ scorepopquiz +=0
        stop sound
        stop music
        jump ResultsPopQuizSHS
    return

    label question5popquizshs_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}D. Cecil Frances Alexander{/b}.
        And this is the end of the pop quiz, let us now see the results."
        $ scorepopquiz +=0
        stop sound
        stop music
        jump ResultsPopQuizSHS
    return

    label ResultsPopQuizSHS:
        "Congratulations, player. Out of 5 questions, you answered {b}[scorepopquiz]{/b} questions. Enjoy playing
        the rest of the game. Good luck and have fun!"

        hide screen countdown

        jump shs

    return

#####For College English Pop Quiz######

    label popquizcollegeprompt:
        menu:
            "Would you like to have a pop quiz first before proceeding to the game?"

            "Yes":
                jump popquizcollege
            "Skip pop quiz":
                jump college

    label popquizcollege:

            show chalkboard

            show MrPopQuiz

            mrpopquiz "In this pop quiz, you will answer 5 questions. Whether you answered all of the questions or not,
            the game will proceed so good luck and have fun."

            hide MrPopQuiz

            jump Question1PopQuizCollege

    return

    label Question1PopQuizCollege:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question1popquizcollege_slow'                    ### set where you want to jump once the timer runs out


        Question1College "Complete this sentence:
            \nI am having dinner with ______ tonight."
        jump q1popquizcollege

    label q1popquizcollege:

        show screen countdown                          ### call and start the timer

        menu:

            "A. he":
                call popquizwronganswercollege1
            "B. they":
                call popquizwronganswercollege1
            "C. his":
                call popquizwronganswercollege1
            "D. him":
                call popquizcorrectanswercollege1

    return


    label popquizwronganswercollege1:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}D. him{/b}. You may now proceed to Question no. 2."
        $ scorepopquiz +=0
        stop sound
        stop music
        jump Question2PopQuizCollege
    return


    label popquizcorrectanswercollege1:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 2."
        $ scorepopquiz +=1
        stop sound
        stop music
        jump Question2PopQuizCollege
    return

    label question1popquizcollege_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}D. him{/b}. You may now proceed to Question no. 2."
        $ scorepopquiz +=0
        stop sound
        stop music
        jump Question2PopQuizCollege
    return


    label Question2PopQuizCollege:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question2popquizcollege_slow'                    ### set where you want to jump once the timer runs out


        Question2SHS "{u}What do you like?{/u}
        \nThis question can be used to ask about hobbies, likes, and dislikes in general."
        jump q2popquizcollege

    label q2popquizcollege:

        show screen countdown                          ### call and start the timer

        menu:

            "A. True":
                call popquizcorrectanswercollege2
            "B. False":
                call popquizwronganswercollege2
            "C. Maybe":
                call popquizwronganswercollege2
            "D. No Idea":
                call popquizwronganswercollege2

    return


    label popquizcorrectanswercollege2:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 3."
        $ scorepopquiz +=1
        stop sound
        stop music
        jump Question3PopQuizCollege
    return


    label popquizwronganswercollege2:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. True{/b}. You may now proceed to Question no. 3."
        $ scorepopquiz +=0
        stop sound
        stop music
        jump Question3PopQuizCollege

    return

    label question2popquizcollege_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}A. True{/b}. You may now proceed to Question no. 3."
        $ scorepopquiz +=0
        stop sound
        stop music
        jump Question3PopQuizCollege
    return


    label Question3PopQuizCollege:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question3popquizshs_slow'                    ### set where you want to jump once the timer runs out


        Question3SHS "Elizabeth Bennet is the protagonist of which Jane Austen novel?"
        jump q3popquizcollege

    label q3popquizcollege:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Little Women":
                call popquizwronganswercollege3
            "B. Lord of the Rings":
                call popquizwronganswercollege3
            "C. Pride and Prejudice":
                call popquizcorrectanswercollege3
            "D. Twilight":
                call popquizwronganswercollege3

    return


    label popquizwronganswercollege3:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}C. Pride and Prejudice{/b}. You may now proceed to Question no. 4."
        $ scorepopquiz +=0
        stop sound
        stop music
        jump Question4PopQuizCollege
    return


    label popquizcorrectanswercollege3:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 4."
        $ scorepopquiz +=1
        stop sound
        stop music
        jump Question4PopQuizCollege

    return

    label question3popquizcollege_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}C. Pride and Prejudice{/b}.
        You may now proceed to Question no. 4."
        $ scorepopquiz +=0
        stop sound
        stop music
        jump Question4PopQuizCollege
    return


    label Question4PopQuizCollege:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question4popquizcollege_slow'                    ### set where you want to jump once the timer runs out


        Question4College "What is the name of the Bible's fifth book in Old Testament?"
        jump q4popquizcollege

    label q4popquizcollege:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Genesis":
                call popquizwronganswercollege4
            "B. Deuteronomy":
                call popquizcorrectanswercollege4
            "C. Revelation":
                call popquizwronganswercollege4
            "D. Psalm":
                call popquizwronganswercollege4
    return


    label popquizwronganswercollege4:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}B. Deuteronomy{/b}. You may now proceed to Question no. 5."
        $ scorepopquiz +=0
        stop sound
        stop music
        jump Question5PopQuizCollege
    return

    label popquizcorrectanswercollege4:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 5."
        $ scorepopquiz +=1
        stop sound
        stop music
        jump Question5PopQuizCollege
    return

    label question4popquizcollege_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}B. Deuteronomy{/b}. You may now proceed to Question no. 4."
        $ scorepopquiz +=0
        stop sound
        stop music
        jump Question5PopQuizCollege
    return


    label Question5PopQuizCollege:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question5popquizcollege_slow'                    ### set where you want to jump once the timer runs out


        Question5SHS "What is the meaning of the phrase ‘Mein Kampf’ in Hitler’s
        autobiography of the same name?"
        jump q5popquizcollege

    label q5popquizcollege:

        show screen countdown                          ### call and start the timer

        menu:

            "A. My Life":
                call popquizwronganswercollege5
            "B. My House":
                call popquizwronganswercollege5
            "C. My Money":
                call popquizwronganswercollege5
            "D. My Struggle":
                call popquizcorrectanswercollege5

    return


    label popquizwronganswercollege5:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}D. My Struggle{/b}.
        And this is the end of the pop quiz, let us now see the results."
        $ scorepopquiz +=0
        stop sound
        stop music
        jump ResultsPopQuizCollege
    return

    label popquizcorrectanswercollege5:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! And this is the end of the pop quiz, let us
        now see the results."
        $ scorepopquiz +=1
        stop sound
        stop music
        jump ResultsPopQuizCollege
    return

    label question5popquizcollege_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}D. My Struggle{/b}.
        And this is the end of the pop quiz, let us now see the results."
        $ scorepopquiz +=0
        stop sound
        stop music
        jump ResultsPopQuizCollege
    return

    label ResultsPopQuizCollege:
        "Congratulations, player. Out of 5 questions, you answered {b}[scorepopquiz]{/b} questions. Enjoy playing
        the rest of the game. Good luck and have fun!"

        hide screen countdown

        jump college

    return


    label shs:

        #So this will tackle the scenario of SHS once you chose SHS as your difficulty.

        $renpy.music.play("audio/The 126ers - End Of Summer Instrumental Extended.mp3", loop=True)
        scene campus

        "There are four friends named Martin, Matthew, Allen, and [playername]. They went to school together today.
        All of them are grade 11 Senior High School students at Belridge Senior High School and they belong to 11-A class."

        stop music

        $renpy.sound.play("audio/Japanese School Bell.mp3", loop=True)

        "(The bell rings)"

        "All students of Belridge Senior High School. Please come to your respective classrooms.
        Your classes will start in 10 minutes."

        stop sound

        play music "audio/The 126ers - End Of Summer Instrumental Extended.mp3"

        show Allen

        allen "Oh, man. We're gonna be late. What are we going to do?"

        hide Allen

        menu:

            "What are they going to do?"

            "Go to the classroom early":
                jump classroom
            "Go to the cafeteria":
                jump cafeteria
            "Go to the comfort room":
                jump CR


        label classroom:

            show Martin

            martin "Alright, guys, let's race our way to the classroom as fast as we can."

            hide Martin

            $renpy.sound.play("audio/Running.mp3", loop=True)

            "The four of them began running all the way to their classroom."

            hide campus

            show hallway

            $renpy.sound.play("audio/Running.mp3", loop=True)

            allen "Look, we're almost there. Let's keep running."

            "They kept running all the way to their classroom."

            stop sound

            "And finally, they made it."

            hide hallway

            stop music

            show black

            play sound "audio/Door Open and Door Close.mp3"

            "(Door opens and closes)"

            stop sound

            hide black

            jump classroomSHS

        return

    label cafeteria:

        player "Since we have 10 minutes before the class starts, would you guys like to accompany me in buying food?"

        show Matthew

        matthew "Hell no!"

        hide Matthew

        show Martin

        martin "You are not a child anymore, man. You can already take care of yourself."

        hide Martin

        show Allen

        allen "It's a no for me."

        hide Allen

        player "Oh, come on! Are you guys really my friends?! Alright, I'll treat you all at the cafeteria,
        but please, let's
        go to the cafeteria together."

        "And they all agreed to go to the cafeteria together."

        hide campus

        show cafeteria

        "After they went to the cafeteria to buy food, they went out and hurriedly went to the classroom."

        hide cafeteria

        show hallway

        $renpy.sound.play("audio/Running.mp3", loop=True)

        allen "Look, we're almost there. Let's keep running."

        "They kept running all the way to their classroom."

        stop sound

        "And finally, they made it."

        hide hallway

        stop music

        show black

        play sound "audio/Door Open and Door Close.mp3"

        "(Door opens and closes)"

        stop sound

        hide black

        jump classroomSHS

    return

    label CR:

        "Suddenly, [playername] felt the nature's call."

        player "I need to go to the comfort room. Please wait for me."

        show Allen

        allen "[playername], we're not going to wait for you in the comfort room. We will accompany you instead.
        That's what friends are for, right?"

        hide Allen

        player "Alright then. Let's go."

        "And they went to the comfort room."

        hide campus2

        stop music

        $renpy.sound.play("audio/toilet music.mp3", loop=True)

        show cr

        "[playername] has to stay inside the cubicle toilet a bit longer while
        Matthew, Allen, and Martin will wait for him in the comfort room."

        show Martin

        martin "I think [playername] will take a while in answering the nature's call."

        hide Martin

        show Matthew

        matthew "Well, it seems like [playername] ate a lot of breakfast a while ago before going to school."

        hide Matthew

        show Allen

        allen "Can't blame [playername] about that though if that's the sole reason why. We should wait a little
        bit longer."

        hide Allen

        "After a long time of waiting, [playername] was able to finish answering the call of the nature. [playername] wore his
        pants and his belt on."

        $renpy.sound.play("audio/toilet flush.mp3", loop=True)

        "([playername] flushes the toilet)"

        stop sound

        $renpy.music.play("audio/The 126ers - End Of Summer Instrumental Extended.mp3", loop=True)

        "And [playername] went out of the toilet cubicle."

        player "Phew! I feel relieved, guys. Thank you for waiting for me to finish taking a dump."

        show Martin

        martin "No problem, man."

        hide Martin

        "(Martin checked the time on his phone)"

        show Martin

        martin "It's already 7:55. We should hurry to the classroom now!"

        hide Martin

        show Allen

        allen "Sir, yes, sir!"

        hide Allen

        "And they went out of the comfort room to go to their classroom."

        hide cr

        show hallway

        $renpy.sound.play("audio/Running.mp3", loop=True)

        allen "Look, we're almost there. Let's keep running."

        "They kept running all the way to their classroom."

        stop sound

        "And finally, they made it."

        hide hallway

        stop music

        show black

        play sound "audio/Door Open and Door Close.mp3"

        "(Door opens and closes)"

        stop sound

        hide black

        jump classroomSHS

    return

    label classroomSHS:

        show classroomshs

        $renpy.music.play("audio/The 126ers - End Of Summer Instrumental Extended.mp3", loop=True)

        show MatthewSweat

        matthew "Phew! That was tiring."

        hide MatthewSweat

        "Matthew wiped his sweat with his handkerchief and he checked the time on his wristwatch afterwards."

        show Matthew

        matthew "Good thing, we're not yet late. Our class will start at 8:00, but the time is 7:53."

        matthew "So we have seven minutes before the start of our class."

        hide Matthew

        player "Anyway, we should take our seats now."

        show Allen

        allen "Right, we should do that."

        hide Allen

        "[playername], Matthew, Allen, and Martin took their respective seats. At 8:00, their English teacher
    came inside the classroom. She walked towards her table and put down her things.
    Afterwards, she walked in front of the table and started greeting the class."

        show TeacherMarites

        teachermarites "Good morning, 11-A students."

        hide TeacherMarites

        elevenA "Good morning, teacher."

        show TeacherMarites

        teachermarites "I have an announcement to tell so please listen carefully."

        teachermarites "Since we were able to finish our lessons for this week, we won't have an English class
    today. However, we will have a quiz about those lessons tomorrow."

        hide TeacherMarites

        player "Huh??!!!! But, teacher, we only finished discussing those English lessons yesterday."

        show TeacherMarites

        teachermarites "Oh, come on, Mr. [playername]. I've decided to test your knowledge through your tomorrow's quiz
    because I want to see whether all of you learned anything from this class or not."

        teachermarites "Anyway, I will dismiss you early now so you can use your
    free time to study your lessons or to do something else. See you tomorrow, class."

        hide TeacherMarites

        elevenA "See you tomorrow, teacher."

        "Teacher Marites left the classroom immediately. Afterwards, the students left the classroom as well except for
    [playername], Martin, Matthew, and Allen."

        player "Yo! Do you like to study English with me in my house for our quiz tomorrow later after school?"

        show Matthew

        matthew "Sure thing, man. That would be nice."

        hide Matthew

        show Martin

        martin "Besides, studying is not complete without free food, right, [playername]?"

        hide Martin

        show Allen

        allen "Martin, here you go again with your desire to eat food. I think there's a dragon in your stomach, man."

        hide Allen

        show Martin

        martin "Shut it, Allen. I just want to eat while studying. I cannot gain knowledge without food, bro."

        hide Martin

        player "Alright then. It's decided. Don't forget it, okay?"

        "They spent the entire vacant time playing Dark Legends together while waiting for the vacant time to end."

        "At 1:00 p.m., the vacant time was over so their classmates went back to the classroom."

        "A few seconds later, Teacher Karen went inside the classroom and it's time for the entire class to endure
        her boring Math class."

        elevenA "Good afternoon, Teacher Karen."

        show TeacherKaren

        teacherkaren "Good afternoon, students. Our new lesson for today is about algebra."

        hide TeacherKaren

        show Matthew

        matthew "Here we go again."

        hide Matthew

        "They have to endure the boredom until 2:30 p.m. I hope they will be okay throughout the lesson."

        "They went to school so they have to listen to the teacher because that is their responsibility as a student
        no matter how boring the class is."

        stop music

        $renpy.sound.play("audio/Japanese School Bell.mp3", loop=True)

        "At 2:30 p.m., the bell rang again."

        stop sound

        $renpy.music.play("audio/The 126ers - End Of Summer Instrumental Extended.mp3", loop=True)

        show TeacherKaren

        teacherkaren "Okay, class. You may now dismiss. Goodbye, class."

        hide TeacherKaren

        elevenA "Goodbye, teacher."

        "Teacher Karen and the students of 11-A left the classroom."

        hide classroomshs

        jump campusSHS

    return

    label campusSHS:

        show campus

        player "Finally, school's over."

        show Matthew

        matthew "Yeah, it's already over. We were able to endure the boredom of her class this afternoon."

        hide Matthew

        player "Good thing I can finally go home and play video games for the rest of the day."

        show Martin

        martin "Wait, what? I thought we're going to study for our English quiz tomorrow at your house, remember?"

        hide Martin

        show Matthew

        matthew "Yeah, he's right. Studying for tomorrow's quiz comes first before video games, man."

        hide Matthew

        player "Oh, my bad. We're supposed to study English when we get to my house. But, Martin, I am sure you like
    eating better than studying."

        show Martin

        martin "Give me a break, [playername]. Studying gets better when there's food so deal with it!"

        hide Martin

        player "Relax, Martin, relax. I'm just joking around here, man. Anyway, let's go to my house."

        "And they began walking to [playername]'s home."

        hide campus

        jump shslessons

    return

    label shslessons:

        $renpy.music.play("audio/More Feels.mp3", loop=True)

        show HouseProtag

        "After 10 minutes of walking, they were able to make it to [playername]'s house."

        show Martin

        martin "And so we finally made it, everyone. So, [playername], are your parents around?"

        hide Martin

        player "No, they're not here. They went out of town for work, but they will be back after 3 days."

        show Matthew

        matthew "So when did they leave?"

        hide Matthew

        player "They left early in the morning before I went to school."

        show Matthew

        matthew "Oh, I see."

        hide Matthew

        player "Anyway, let's go inside my house."

        "[playername] took the house keys in the backpack and unlocked the door to their house.
        After unlocking the door, they went inside the house."

        hide HouseProtag

        show black

        stop music

        play sound "audio/Door Open and Door Close.mp3"

        "(Door opens and closes)"

        stop sound

        hide black

        $renpy.music.play("audio/More Feels.mp3", loop=True)

        show LivingRoom

        "So this is what the [playername]'s living room looks like."

        "To be honest, this living room looks beautiful in the eyes despite that it is
        simple as the way it is. Well, I can say that I do believe that simplicity is beauty."

        show Allen

        allen "It was quite a tiring day today. Forcing ourselves to study for tomorrow's quiz at this point
        is not effective."

        hide Allen

        show Martin

        martin "Allen's right. It will be better for us to take a rest first before eating and studying."

        hide Martin

        player "Yeah, that is really a good idea, Allen. We better go to my bedroom and start resting."

        "They all went to [playername]'s bedroom to rest and Matthew closed the door."

        hide LivingRoom

        show Bedroom

        player "So as usual, I still use the same bed so only 2 people can sleep in my bed,
        but Martin and I can get the foam mattress in the storage room. Matthew, don't close the door after
        we leave."

        "[playername] opened the door again."

        show Matthew

        matthew "Alright then. We'll just wait here as usual."

        hide Matthew

        "[playername] and Martin left the bedroom to get the foam mattress in the storage room.
        While Allen and Matthew, on the other hand, started having a conversation."

        show Allen

        allen "Matthew, to be honest, I doubt I will be able to pass our English quiz tomorrow.
        That is because I think it is very hard for me to learn our English lessons.
        This is ironic for me as someone who can speak English fluently."

        hide Allen

        show Matthew

        matthew "Allen, I know that it must have been hard for you to learn that subject, but I believe in you.
        I believe that you can do it uh... I mean, you can pass the tomorrow's quiz."

        matthew "Whether you're good at something or not, what matters the most is that you put your effort in doing
        your best."

        matthew "In fact, there is nothing wrong in trying until you succeed."

        matthew "That is because in school, you're not going to study one thing."

        matthew "You will be studying a lot of things and you have to do your best even if the results may turn out well
        or not because what matters the most is that you tried to persevere enough to make an effort in doing your best
        in everything that you do regardless of how important a certain task is."

        matthew "In my case, I wasn't really good at English before, but my teacher told me to keep trying to put a lot of
        effort in learning it"

        matthew "so in the end,
        I was able to improve my skills in English even though there will always be a room for me to make mistakes
        because my English is still not perfect after all."

        hide Matthew

        "Well, that reminds me of one of my junior high school teachers because she used to tell this kind of advice in our
        class before and I still remember and live with this advice of hers until now."

        "To be honest, that advice helped me to persevere in life whether in studies or in other things. Thanks, teacher.
        \n-Wrichmond"

        show Allen

        allen "Wow, that's good to hear, man. It is good to know that I have learned a lot of things from you.
        What I've learned from you today made me realize and understand the importance of putting effort into something."

        allen "Well anyway, thanks for the advice, man."

        hide Allen

        show Matthew

        matthew "No problem, man."

        hide Matthew

        "[playername] and Martin went back to the bedroom with the foam mattress."

        show Bedroom

        show FoamMattress

        window hide

        pause

        hide FoamMattress

        show Allen

        allen "Finally, they're here with the foam mattress."

        hide Allen

        "[playername] and Martin put down the foam mattress."

        player "And since we have the foam mattress here, we can now finally rest for an hour."

        "And so they decided to take a rest for an hour. Matthew and Allen slept on the foam mattress while [playername]
        and Martin slept on [playername]'s bed."

        stop music

        show black

        "After resting for an hour, they woke up and stretched their body."

        hide black

        $renpy.music.play("audio/More Feels.mp3", loop=True)

        show Bedroom

        player "(yawns)"

        martin "(yawns)"

        allen "(yawns)"

        matthew "(yawns)"

        show Allen

        allen "Alright, listen up. I have to say something."

        hide Allen

        player "What is it, Allen?"

        show Allen

        allen "Ok so here's the deal: we will eat together at Rowan's Diner after school.
        Regardless of the scores that we get, always remember that what matters the most is that we did our best
        on that day."

        hide Allen

        show Matthew

        matthew "Oh, well, I can't deny that Allen's idea is indeed a great idea. He is smart as Albert Einstein, man so
        I agree with him here."

        hide Matthew

        show Martin

        martin "Same."

        hide Martin

        player "Me too."

        show Matthew

        matthew "That's good to hear, guys. So what are we waiting for? Let's study!!!!!!"

        hide Matthew

        jump study

    label study:

        show Bedroom

        "Okay so you have finally decided to study, [playername]. In that case,
        I will be providing you the images of the lessons that you
        need to learn. Good luck and happy studying!"

        jump studychoicesSHS

    return

    label studychoicesSHS:

        hide black

        $renpy.music.play("audio/More Feels.mp3", loop=True)

        show Bedroom

        menu:
            "Which of the following lessons would you like to study?"

            "Lesson 1: Fundamental Considerations on Text Production and Consumption":
                jump L1SHS

            "Lesson 2: Note Taking":
                jump L2SHS

            "Lesson 3: The Citation, Reaction Paper, Review, and Critique":
                jump L3SHS

    return

    label L1SHS:

        stop music

        $renpy.music.play("audio/Good Friends- Yasper.mp3", loop=True)

        hide Bedroom

        show screen gameUISHS

        $L1SHSProgress = 0

        show L1SHS

        window hide

        pause

        hide L1SHS

        $L1SHSProgress += 9

        show L1SHS2

        window hide

        pause

        hide L1SHS2

        $L1SHSProgress += 9

        show L1SHS3

        window hide

        pause

        hide L1SHS3

        $L1SHSProgress += 9

        show L1SHS4

        window hide

        pause

        hide L1SHS4

        $L1SHSProgress += 9

        show L1SHS5

        window hide

        pause

        hide L1SHS5

        $L1SHSProgress += 9

        show L1SHS6

        window hide

        pause

        hide L1SHS6

        $L1SHSProgress += 9

        show L1SHS7

        window hide

        pause

        hide L1SHS7

        $L1SHSProgress += 9

        show L1SHS8

        window hide

        pause

        hide L1SHS8

        $L1SHSProgress += 9

        show L1SHS9

        window hide

        pause

        hide L1SHS9

        $L1SHSProgress += 9

        show L1SHS10

        window hide

        pause

        hide L1SHS10

        $L1SHSProgress += 19

        show L1SHS11

        window hide

        pause

        hide L1SHS11

        stop music

        show black

        hide screen gameUISHS

        "You have finally finished reading the lesson. You will now proceed to the quiz part."

        jump quizdaySHS1

    return

    label L2SHS:

        stop music

        $renpy.music.play("audio/Glimlip - S h e.mp3", loop=True)

        hide Bedroom

        show screen gameUISHS2

        $L2SHSProgress = 0

        show L2SHS

        window hide

        pause

        hide L2SHS

        $L2SHSProgress += 10

        show L2SHS2

        window hide

        pause

        hide L2SHS2

        $L2SHSProgress += 10

        show L2SHS3

        window hide

        pause

        hide L2SHS3

        $L2SHSProgress += 10

        show L2SHS4

        window hide

        pause

        hide L2SHS4

        $L2SHSProgress += 10

        show L2SHS5

        window hide

        pause

        hide L2SHS5

        $L2SHSProgress += 10

        show L2SHS6

        window hide

        pause

        hide L2SHS6

        $L2SHSProgress += 10

        show L2SHS7

        window hide

        pause

        hide L2SHS7

        $L2SHSProgress += 10

        show L2SHS8

        window hide

        pause

        hide L2SHS8

        $L2SHSProgress += 10

        show L2SHS9

        window hide

        pause

        hide L2SHS9

        $L2SHSProgress += 20

        show L2SHS10

        window hide

        pause

        hide L2SHS10

        stop music

        show black

        hide screen gameUISHS2

        "You have finally finished reading the lesson. You will now proceed to the quiz part."

        jump quizdaySHS2

    return

    label L3SHS:

        stop music

        $renpy.music.play("audio/DLJ - Deep Sleep ft. TABAL.mp3", loop=True)

        hide Bedroom

        show screen gameUISHS3

        $L3SHSProgress = 0

        show L3SHS

        window hide

        pause

        hide L3SHS

        $L3SHSProgress += 10

        show L3SHS2

        window hide

        pause

        hide L3SHS2

        $L3SHSProgress += 10

        show L3SHS3

        window hide

        pause

        hide L3SHS3

        $L3SHSProgress += 10

        show L3SHS4

        window hide

        pause

        hide L3SHS4

        $L3SHSProgress += 10

        show L3SHS5

        window hide

        pause

        hide L3SHS5

        $L3SHSProgress += 10

        show L3SHS6

        window hide

        pause

        hide L3SHS6

        $L3SHSProgress += 10

        show L3SHS7

        window hide

        pause

        hide L3SHS7

        $L3SHSProgress += 10

        show L3SHS8

        window hide

        pause

        hide L3SHS8

        $L3SHSProgress += 10

        show L3SHS9

        window hide

        pause

        hide L3SHS9

        $L3SHSProgress += 20

        show L3SHS10

        window hide

        pause

        hide L3SHS10

        stop music

        show black

        hide screen gameUISHS3

        "You have finally finished reading the lesson. You will now proceed to the quiz part."

        jump quizdaySHS3

    return

    label quizdaySHS1:

        $renpy.music.play("audio/The 126ers - End Of Summer Instrumental Extended.mp3", loop=True)

        show classroomshs

        show TeacherMarites

        teachermarites "Good morning, students. Today is your quiz day. Once I gave the quiz sheets to all of you,
        you may now start answering the questions provided. Do your best and good luck."

        hide TeacherMarites

        "Teacher Marites gave the quiz sheets to the students."

        "Okay, player. I will present to you the mechanics of this game so please read and follow the
        mechanics of this game. Thank you."

        hide classroomshs

        show Mechanics1

        window hide

        pause

        hide Mechanics1

        show Mechanics2

        window hide

        pause

        hide Mechanics2

        show classroomshs

        show TeacherMarites

        teachermarites "Okay, you may now start answering."

        hide TeacherMarites

        "Since you are about to take the quiz, you won't hear any background music until the end of the quiz."

        "That is because usually, when you take your in school, you have to take it quietly."

        stop music

        jump Question1SHSL1

    label Question1SHSL1:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question1shs_slow'                    ### set where you want to jump once the timer runs out


        Question1SHS "These are words and phrases that you can use in your text in order to guide the reader along."
        jump q1shs
    return

    label q1shs:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Academic Writing":
                jump L1wronganswershs1
            "B. Formal Writing":
                jump L1wronganswershs1
            "C. Signposts":
                jump L1correctanswershs1
            "D. Academic Language":
                jump L1wronganswershs1

    return


    label L1wronganswershs1:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}C. Signposts{/b}. You may now proceed to Question no. 2."
        $ scoreL1SHS +=0
        stop sound
        stop music
        jump Question2SHS
    return

    label L1correctanswershs1:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 2."
        $ scoreL1SHS +=0
        stop sound
        stop music
        jump Question2SHS

    return

    label question1shs_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}C. Signposts{/b}.
        You may now proceed to Question no. 2."
        $ scoreL1SHS +=0
        stop sound
        stop music
        jump Question2SHS
    return


    label Question2SHS:
        hide screen countdown
        $ time = 10                                   ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question2shs_slow'                    ### set where you want to jump once the timer runs out

        Question2SHS "The verbs are made central as they denote action."
        jump q2shs
    return

    label q2shs:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Nominalization":
                jump L1correctanswershs2
            "B. Passivization":
                jump L1wronganswershs2
            "C. Explicitness":
                jump L1wronganswershs2
            "D. Objectivity":
                jump L1wronganswershs2

    return

    label L1correctanswershs2:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 3."
        $ scoreL1SHS +=1
        stop sound
        stop music
        jump Question3SHS
    return

    label L1wronganswershs2:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. Nominalization{/b}.
        You may now proceed to Question no. 3."
        $ scoreL1SHS +=0
        stop sound
        stop music
        jump Question3SHS
    return

    label question2shs_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}A. Nominalization{/b}.
        You may now proceed to Question no. 3."
        $ scoreL1SHS +=0
        stop sound
        stop music
        jump Question3SHS
    return


    label Question3SHS:
        hide screen countdown
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                            ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question3shs_slow'                    ### set where you want to jump once the timer runs out

        Question3SHS "Which of the following is true about Academic Writing?"
        jump q3shs
    return

    label q3shs:

        show screen countdown                          ### call and start the timer


        menu:

            "A. It requires considerable effort to construct meaningful sentences,
            paragraphs, and arguments that make the text easy to comprehend.":
                jump L1wronganswershs3
            "B. It reflects your dignified stance in writing as a member of the academic community.":
                jump L1wronganswershs3
            "C. It is used to avoid redundancy.":
                jump L1wronganswershs3
            "D. It is based on research and not on the writer’s own opinion about a given topic.":
                jump L1correctanswershs3

    return

    label L1correctanswershs3:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 4."
        $ scoreL1SHS +=1
        stop sound
        stop music
        jump Question4SHS
    return

    label L1wronganswershs3:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}D. It is based on research and not on the writer’s own opinion
        about a given topic.{/b} You may now proceed to Question no. 4."
        $ scoreL1SHS +=0
        stop sound
        stop music
        jump Question4SHS
    return

    label question3shs_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}D. It is based on research and not on the writer’s own opinion
        about a given topic.{/b}
        You may now proceed to Question no. 4."
        $ scoreL1SHS +=0
        stop sound
        stop music
        jump Question4SHS
        stop music
    return



    label Question4SHS:
        hide screen countdown
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                             ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question4shs_slow'                    ### set where you want to jump once the timer runs out

        Question4SHS "In combining ideas effectively, you will need to avoid redundancy."
        jump q4shs
    return

    label q4shs:

        show screen countdown                          ### call and start the timer


        menu:

            "A. Structure":
                jump L1correctanswershs4
            "B. Formality":
                jump L1wronganswershs4
            "C. Objectivity":
                jump L1wronganswershs4
            "D. Explicitiness":
                jump L1wronganswershs4

    return

    label L1wronganswershs4:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. Structure{/b}. You may now proceed to Question no. 5."
        $ scoreL1SHS +=0
        stop sound
        stop music
        jump Question5SHS
    return

    label L1correctanswershs4:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 5."
        $ scoreL1SHS +=1
        stop sound
        stop music
        jump Question5SHS
    return

    label L1question4shs_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}A. Structure{/b}.
        You may now proceed to Question no. 5."
        $ scoreL1SHS +=0
        stop sound
        stop music
        jump Question5SHS
    return

    label Question5SHS:
        hide screen countdown
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question5shs_slow'                    ### set where you want to jump once the timer runs out

        Question5SHS "Reflects your dignified stance in writing as a member of the academic community."
        jump q5shs
    return

    label q5shs:

        show screen countdown                          ### call and start the timer


        menu:

            "A. Structure":
                jump L1wronganswershs5
            "B. Formality":
                jump L1correctanswershs5
            "C. Objectivity":
                jump L1wronganswershs5
            "D. Explicitness":
                jump L1wronganswershs5

    return

    label L1wronganswershs5:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}B. Formality{/b}. You may now proceed to Question no. 6."
        $ scoreL1SHS +=0
        stop sound
        stop music
        jump Question6SHS
    return

    label L1correctanswershs5:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 6."
        $ scoreL1SHS +=1
        stop sound
        stop music
        jump Question6SHS
    return

    label question5shs_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}B. Formality{/b}.
        You may now proceed to Question no. 6."
        $ scoreL1SHS +=0
        stop sound
        stop music
        jump Question6SHS
    return



    label Question6SHS:
        hide screen countdown
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question6shs_slow'                    ### set where you want to jump once the timer runs out

        Question6SHS "It refers to the impersonal and certain level of distance."
        jump q6shs
    return

    label q6shs:

        show screen countdown                          ### call and start the timer


        menu:

            "A. Structure":
                jump L1wronganswershs6
            "B. Formality":
                jump L1wronganswershs6
            "C. Objectivity":
                jump L1correctanswershs6
            "D. Explicitness":
                jump L1wronganswershs6

    return

    label L1wronganswershs6:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}C. Objectivity{/b}.
        You may now proceed to Question no. 7."
        $ scoreL1SHS +=0
        stop sound
        stop music
        jump Question7SHS
    return

    label L1correctanswershs6:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 7."
        $ scoreL1SHS +=1
        stop sound
        stop music
        jump Question7SHS
    return

    label question6shs_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}C. Objectivity{/b}.
        You may now proceed to Question no. 7."
        $ scoreL1SHS +=0
        stop sound
        stop music
        jump Question7SHS
    return

    label Question7SHS:
        hide screen countdown
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question7shs_slow'                    ### set where you want to jump once the timer runs out

        Question7SHS "It uses signposts to allow readers to trace the relationships in the parts of a study."
        jump q7shs
    return

    label q7shs:

        show screen countdown                          ### call and start the timer


        menu:

            "A. Structure":
                jump L1wronganswershs7
            "B. Formality":
                jump L1wronganswershs7
            "C. Objectivity":
                jump L1wronganswershs7
            "D. Explicitness":
                jump L1correctanswershs7

    return

    label L1correctanswershs7:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 8."
        $ scoreL1SHS +=1
        stop sound
        stop music
        jump Question8SHS
    return

    label L1wronganswershs7:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}D. Explicitness{/b}. You may now proceed to Question no. 8."
        $ scoreL1SHS +=0
        stop sound
        stop music
        jump Question8SHS
    return

    label question7shs_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}D. Explicitness{/b}.
        You may now proceed to Question no. 8."
        $ scoreL1SHS +=0
        stop sound
        stop music
        jump Question8SHS
    return

    label Question8SHS:
        hide screen countdown
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question8shs_slow'                    ### set where you want to jump once the timer runs out

        Question8SHS "To avoid sweeping generalization."
        jump q8shs
    return

    label q8shs:

        show screen countdown                          ### call and start the timer


        menu:

            "A. Caution":
                jump L1correctanswershs8
            "B. Cactus":
                jump L1wronganswershs8
            "C. Caught":
                jump L1wronganswershs8
            "D. Call":
                jump L1wronganswershs8

    return

    label L1wronganswershs8:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. Caution{/b}.
        You may now proceed to Question no. 9."
        $ scoreL1SHS +=0
        stop sound
        stop music
        jump Question9SHS
    return

    label L1correctanswershs8:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 9."
        $ scoreL1SHS +=1
        stop sound
        stop music
        jump Question9SHS
    return

    label question8shs_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}A. Caution{/b}.
        You may now proceed to Question no. 9."
        $ scoreL1SHS +=0
        stop sound
        stop music
        jump Question9SHS
    return

    label Question9SHS:
        hide screen countdown
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                             ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question9shs_slow'                    ### set where you want to jump once the timer runs out

        Question9SHS "It has a unique set of rules: it should be explicit,
        formal and factual as well as objective and analytical in nature."
        jump q9shs
    return

    label q9shs:

        show screen countdown                          ### call and start the timer


        menu:

            "A. Formal Writing":
                jump L1wronganswershs9
            "B. Academic Writing":
                jump L1wronganswershs9
            "C. Academic Language":
                jump L1correctanswershs9
            "D. Structure":
                jump L1wronganswershs9

    return

    label L1wronganswershs9:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}C. Academic Language{/b}.
        You may now proceed to Question no. 10."
        $ scoreL1SHS +=0
        stop sound
        stop music
        jump Question10SHS
    return

    label L1correctanswershs9:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 10."
        $ scoreL1SHS +=1
        stop sound
        stop music
        jump Question10SHS
    return

    label question9shs_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}C. Academic Language{/b}.
        You may now proceed to Question no. 10."
        $ scoreL1SHS +=0
        stop sound
        stop music
        jump Question10SHS
    return



    label Question10SHS:
        hide screen countdown
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question10shs_slow'                    ### set where you want to jump once the timer runs out

        Question10SHS "The results of the action are highlighted."
        jump q10shs
    return

    label q10shs:

        show screen countdown                          ### call and start the timer


        menu:

            "A. Nominalization":
                jump L1wronganswershs10
            "B. Passivization":
                jump L1correctanswershs10
            "C. Explicitiness":
                jump L1wronganswershs10
            "D. Objectivity":
                jump L1wronganswershs10

    return

    label L1wronganswershs10:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}B. Passivization{/b}. And this is the end of the quiz, let us
        now see the results."
        $ scoreL1SHS +=0
        stop sound
        stop music
        jump ResultsSHS1
    return

    label L1correctanswershs10:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! And this is the end of the quiz, let us
        now see the results."
        $ scoreL1SHS +=1
        stop sound
        stop music
        jump ResultsSHS1
    return

    label question10shs_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}B. Passivization{/b}.
        And this is the end of the quiz, let us
        now see the results."
        $ scoreL1SHS +=0
        stop sound
        stop music
        jump ResultsSHS1
    return


    label ResultsSHS1:
        show classroomshs

        if scoreL1SHS == 0:
            "Out of 10 questions, [playername] have answered {b}[scoreL1SHS]{/b}(0 percent) questions.
            Unfortunately, you have failed this quiz. Please study the lesson again."

            hide classroomshs

            jump L1SHS

        if scoreL1SHS == 1:
            "Out of 10 questions, [playername] have answered {b}[scoreL1SHS]{/b}(10 percent) questions.
            Unfortunately, you have failed this quiz. Please study the lesson again."

            hide classroomshs

            jump L1SHS

        if scoreL1SHS == 2:
            "Out of 10 questions, [playername] have answered {b}[scoreL1SHS]{/b}(20 percent) questions.
            Unfortunately, you have failed this quiz. Please study the lesson again."

            hide classroomshs

            jump L1SHS

        if scoreL1SHS == 3:
            "Out of 10 questions, [playername] have answered {b}[scoreL1SHS]{/b}(30 percent) questions.
            Unfortunately, you have failed this quiz. Please study the lesson again."

            hide classroomshs

            jump L1SHS

        if scoreL1SHS == 4:
            "Out of 10 questions, [playername] have answered {b}[scoreL1SHS]{/b}(40 percent) questions.
            Unfortunately, you have failed this quiz. Please study the lesson again."

            hide classroomshs

            jump L1SHS

        if scoreL1SHS == 5:
            "Out of 10 questions, [playername] answered {b}[scoreL1SHS]{/b} (50 percent)
            questions. Congratulations, [playername]. You passed in this quiz. Great job!"

            hide classroomshs

            jump EndingSHS

        if scoreL1SHS == 6:
            "Out of 10 questions, [playername] answered {b}[scoreL1SHS]{/b} (60 percent)
            questions. Congratulations, [playername]. You passed in this quiz. Great job!"

            hide classroomshs

            jump EndingSHS

        if scoreL1SHS == 7:
            "Out of 10 questions, [playername] answered {b}[scoreL1SHS]{/b} (70 percent)
            questions. Congratulations, [playername]. You passed in this quiz. Great job!"

            hide classroomshs

            jump EndingSHS

        if scoreL1SHS == 8:
            "Out of 10 questions, [playername] answered {b}[scoreL1SHS]{/b} (80 percent)
            questions. Congratulations, [playername]. You passed in this quiz. Great job!"

            hide classroomshs

            jump EndingSHS

        if scoreL1SHS == 9:
            "Out of 10 questions, [playername] answered {b}[scoreL1SHS]{/b} (90 percent)
            questions. Congratulations, [playername]. You passed in this quiz. Great job!"

            hide classroomshs

            jump EndingSHS


        if scoreL1SHS == 10:
            "Out of 10 questions, [playername] answered {b}[scoreL1SHS]{/b} (100 percent)
            questions. Congratulations, [playername]. You passed in this quiz. Great job!"

            hide classroomshs

            jump EndingSHS


    return

    label quizdaySHS2:

        $renpy.music.play("audio/The 126ers - End Of Summer Instrumental Extended.mp3", loop=True)

        show classroomshs

        show TeacherMarites

        teachermarites "Good morning, students. Today is your quiz day. Once I gave the quiz sheets to all of you,
        you may now start answering the questions provided. Do your best and good luck."

        hide TeacherMarites

        "Teacher Marites gave the quiz sheets to the students."

        "Okay, player. I will present to you the mechanics of this game so please read and follow the
        mechanics of this game. Thank you."

        hide classroomshs

        show Mechanics1

        window hide

        pause

        hide Mechanics1

        show Mechanics2

        window hide

        pause

        hide Mechanics2

        show classroomshs

        show TeacherMarites

        teachermarites "Okay, you may now start answering."

        hide TeacherMarites

        "Since you are about to take the quiz, you won't hear any background music until the end of the quiz."

        "That is because usually, when you take your in school, you have to take it quietly."

        stop music

        jump Question1SHSL2

    label Question1SHSL2:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question1shs_slowL2'                    ### set where you want to jump once the timer runs out


        Question1SHS "In note-taking, it is one of the simplest and most common ways to take notes.
        Points and keywords are written down in a hierarchical structure."
        jump q1shs2
    return

    label q1shs2:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Charting":
                jump L2wronganswershs1
            "B. Outlining":
                jump L2correctanswershs1
            "C. Mapping":
                jump L2wronganswershs1
            "D. Plagiarism":
                jump L2wronganswershs1

    return


    label L2wronganswershs1:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}B. Outlining{/b}. You may now proceed to Question no. 2."
        $ scoreL2SHS +=0
        stop sound
        stop music
        jump Question2SHSL2
    return

    label L2correctanswershs1:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 2."
        $ scoreL2SHS +=1
        stop sound
        stop music
        jump Question2SHSL2

    return

    label question1shs_slowL2:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}B. Outlining{/b}.
        You may now proceed to Question no. 2."
        $ scoreL2SHS +=0
        stop sound
        stop music
        jump Question2SHSL2
    return

    label Question2SHSL2:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question2shs_slowL2'                    ### set where you want to jump once the timer runs out


        Question2SHS "For visual thinkers, it might help to take notes using a mind map, or simply “_______.”"
        jump q2shs2
    return

    label q2shs2:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Charting":
                jump L2wronganswershs2
            "B. Outlining":
                jump L2wronganswershs2
            "C. Mapping":
                jump L2correctanswershs2
            "D. Plagiarism":
                jump L2wronganswershs2

    return


    label L2wronganswershs2:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}C. Mapping{/b}. You may now proceed to Question no. 3."
        $ scoreL2SHS +=0
        stop sound
        stop music
        jump Question3SHSL2
    return

    label L2correctanswershs2:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 3."
        $ scoreL2SHS +=1
        stop sound
        stop music
        jump Question3SHSL2

    return

    label question2shs_slowL2:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}C. Mapping{/b}.
        You may now proceed to Question no. 3."
        $ scoreL2SHS +=0
        stop sound
        stop music
        jump Question3SHSL2
    return

    label Question3SHSL2:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question3shs_slowL2'                    ### set where you want to jump once the timer runs out


        Question3SHS "It is a particular type of note-taking that works best when multiple topics
        are discussed simultaneously, as with comparisons, or when one topic is dissected into multiple parts."
        jump q3shs2
    return

    label q3shs2:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Charting":
                jump L2correctanswershs3
            "B. Outlining":
                jump L2wronganswershs3
            "C. Mapping":
                jump L2wronganswershs3
            "D. Plagiarism":
                jump L2wronganswershs3

    return


    label L2wronganswershs3:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. Charting{/b}. You may now proceed to Question no. 4."
        $ scoreL2SHS +=0
        stop sound
        stop music
        jump Question4SHSL2
    return

    label L2correctanswershs3:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 4."
        $ scoreL2SHS +=1
        stop sound
        stop music
        jump Question4SHSL2

    return

    label question3shs_slowL2:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}A. Charting{/b}.
        You may now proceed to Question no. 4."
        $ scoreL2SHS +=0
        stop sound
        stop music
        jump Question4SHSL2
    return


    label Question4SHSL2:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question4shs_slowL2'                    ### set where you want to jump once the timer runs out


        Question4SHS "Who popularized the Cornell Notes or Cornell Notes System?"
        jump q4shs2
    return

    label q4shs2:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Walter Pauk":
                jump L2correctanswershs4
            "B. James Sunderland":
                jump L2wronganswershs4
            "C. Heather Mason":
                jump L2wronganswershs4
            "D. Harry Mason":
                jump L2wronganswershs4

    return


    label L2wronganswershs4:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. Walter Pauk{/b}. You may now proceed to Question no. 5."
        $ scoreL2SHS +=0
        stop sound
        stop music
        jump Question5SHSL2
    return

    label L2correctanswershs4:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 5."
        $ scoreL2SHS +=1
        stop sound
        stop music
        jump Question5SHSL2

    return

    label question4shs_slowL2:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}A. Walter Pauk{/b}.
        You may now proceed to Question no. 5."
        $ scoreL2SHS +=0
        stop sound
        stop music
        jump Question5SHSL2
    return

    label Question5SHSL2:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question5shs_slow2'                    ### set where you want to jump once the timer runs out


        Question5SHS "What does SQ4R as a method of note-taking stands for?"
        jump q5shs2
    return

    label q5shs2:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Survey, Quality, Realism, Recitation, Reliable, Review":
                jump L2wronganswershs5
            "B. Service, Quality, Read, Recital, Review, Respectful":
                jump L2wronganswershs5
            "C. Salmon, Queen, Rider, Rangers, Reload, Rendering":
                jump L2wronganswershs5
            "D. Survey, Questions, Read, Recite, Relate, Review":
                jump L2correctanswershs5

    return


    label L2wronganswershs5:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}D. Survey, Questions, Read, Recite, Relate, Review{/b}.
        You may now proceed to Question no. 6."
        $ scoreL2SHS +=0
        stop sound
        stop music
        jump Question6SHSL2
    return

    label L2correctanswershs5:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 6."
        $ scoreL2SHS +=1
        stop sound
        stop music
        jump Question6SHSL2
    return

    label question5shs_slowL2:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}D. Survey, Questions,
        Read, Recite, Relate, Review{/b}. You may now proceed to Question no. 6."
        $ scoreL2SHS +=0
        stop sound
        stop music
        jump Question6SHSL2
    return

    label Question6SHSL2:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question6shs_slow2'                    ### set where you want to jump once the timer runs out


        Question6SHS "Take about three to five minutes to skim or “survey” the reading, writing down all the major headings,
        subheadings, topics, and other key points."
        jump q6shs2
    return

    label q6shs2:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Survey ":
                jump L2correctanswershs6
            "B. Read ":
                jump L2wronganswershs6
            "C. Recite":
                jump L2wronganswershs6
            "D. Read":
                jump L2wronganswershs6

    return


    label L2wronganswershs6:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. Survey{/b}.
        You may now proceed to Question no. 6."
        $ scoreL2SHS +=0
        stop sound
        stop music
        jump Question7SHSL2
    return

    label L2correctanswershs6:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 7."
        $ scoreL2SHS +=1
        stop sound
        stop music
        jump Question7SHSL2
    return

    label question6shs_slowL2:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}A. Survey{/b}.
        You may now proceed to Question no. 7."
        $ scoreL2SHS +=0
        stop sound
        stop music
        jump Question7SHSL2
    return

    label Question7SHSL2:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question7shs_slow2'                    ### set where you want to jump once the timer runs out


        Question7SHS "Based on what you saw while surveying, write down any broad questions you have about the text."
        jump q7shs2
    return

    label q7shs2:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Survey ":
                jump L2wronganswershs7
            "B. Question":
                jump L2correctanswershs7
            "C. Recite":
                jump L2wronganswershs7
            "D. Relate":
                jump L2wronganswershs7

    return


    label L2wronganswershs7:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}B. Question{/b}. You may now proceed to Question no. 8."
        $ scoreL2SHS +=0
        stop sound
        stop music
        jump Question8SHSL2
    return

    label L2correctanswershs7:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 8."
        $ scoreL2SHS +=1
        stop sound
        stop music
        jump Question8SHSL2

    return

    label question8shs_slowL2:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}B. Question{/b}.
        You may now proceed to Question no. 8."
        $ scoreL2SHS +=0
        stop sound
        stop music
        jump Question8SHSL2
    return

    label Question8SHSL2:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question8shs_slow2'                    ### set where you want to jump once the timer runs out


        Question8SHS "Now, actually read the text, section by section, keeping an eye out
        for the answers to your questions from the previous step."
        jump q8shs2
    return

    label q8shs2:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Survey ":
                jump L2wronganswershs8
            "B. Question":
                jump L2wronganswershs8
            "C. Read":
                jump L2correctanswershs8
            "D. Relate":
                jump L2wronganswershs8

    return


    label L2wronganswershs8:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}C. Read{/b}. You may now proceed to Question no. 9."
        $ scoreL2SHS +=0
        stop sound
        stop music
        jump Question9SHSL2
    return

    label L2correctanswershs8:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 9."
        $ scoreL2SHS +=1
        stop sound
        stop music
        jump Question9SHSL2

    return

    label question8shs_slow2:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}C. Read{/b}.
        You may now proceed to Question no. 9."
        $ scoreL2SHS +=0
        stop sound
        stop music
        jump Question9SHSL2
    return

    label Question9SHSL2:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question9shs_slow2'                    ### set where you want to jump once the timer runs out


        Question9SHS "After each section, write down all major ideas, keywords,
        and concepts—in other words, take notes. Again, answer the questions you posed in the second step as best you can."
        jump q9shs2
    return

    label q9shs2:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Survey ":
                jump L2wronganswershs9
            "B. Question":
                jump L2wronganswershs9
            "C. Read":
                jump L2wronganswershs9
            "D. Recite":
                jump L2correctanswershs9

    return


    label L2wronganswershs9:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}D. Recite{/b}. You may now proceed to Question no. 10."
        $ scoreL2SHS +=0
        stop sound
        stop music
        jump Question10SHSL2
    return

    label L2correctanswershs9:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 10."
        $ scoreL2SHS +=1
        stop sound
        stop music
        jump Question10SHSL2

    return

    label question9shs_slowL2:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}D. Recite{/b}.
        You may now proceed to Question no. 10."
        $ scoreL2SHS +=0
        stop sound
        stop music
        jump Question10SHSL2
    return

    label Question10SHSL2:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question10shs_slow2'                    ### set where you want to jump once the timer runs out


        Question10SHS "It involves reading with a purpose in order to grasp definitions and meanings, understand debates, and identify and interpret evidence."
        jump q10shs2
    return

    label q10shs2:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Active reading":
                jump L2correctanswershs10
            "B. Inactive reading":
                jump L2wronganswershs10
            "C. Passive reading":
                jump L2wronganswershs10
            "D. Backread":
                jump L2wronganswershs10

    return


    label L2wronganswershs10:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. Active reading{/b}. And this is the end of the quiz, let us
        now see the results."
        $ scoreL2SHS +=0
        stop sound
        stop music
        jump ResultsSHS2
    return

    label L2correctanswershs10:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! And this is the end of the quiz, let us now see the results."
        $ scoreL2SHS +=1
        stop sound
        stop music
        jump ResultsSHS2

    return

    label question10shs_slow2:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}A. Active reading{/b}.
        And this is the end of the quiz, let us now see the results."
        $ scoreL2SHS +=0
        stop sound
        stop music
        jump ResultsSHS2
    return

    label ResultsSHS2:
        show classroomshs

        if scoreL2SHS == 0:
            "Out of 10 questions, [playername] have answered {b}[scoreL2SHS]{/b}(0 percent) questions.
            Unfortunately, you have failed this quiz. Please study the lesson again."

            hide classroomshs

            jump L2SHS

        if scoreL2SHS == 1:
            "Out of 10 questions, [playername] have answered {b}[scoreL2SHS]{/b}(10 percent) questions.
            Unfortunately, you have failed this quiz. Please study the lesson again."

            hide classroomshs

            jump L2SHS

        if scoreL2SHS == 2:
            "Out of 10 questions, [playername] have answered {b}[scoreL2SHS]{/b}(20 percent) questions.
            Unfortunately, you have failed this quiz. Please study the lesson again."

            hide classroomshs

            jump L2SHS

        if scoreL2SHS == 3:
            "Out of 10 questions, [playername] have answered {b}[scoreL2SHS]{/b}(30 percent) questions.
            Unfortunately, you have failed this quiz. Please study the lesson again."

            hide classroomshs

            jump L2SHS

        if scoreL2SHS == 4:
            "Out of 10 questions, [playername] have answered {b}[scoreL2SHS]{/b}(40 percent) questions.
            Unfortunately, you have failed this quiz. Please study the lesson again."

            hide classroomshs

            jump L2SHS

        if scoreL2SHS == 5:
            "Out of 10 questions, [playername] answered {b}[scoreL2SHS]{/b} (50 percent)
            questions. Congratulations, [playername]. You passed in this quiz. Great job!"

            hide classroomshs

            jump EndingSHS

        if scoreL2SHS == 6:
            "Out of 10 questions, [playername] answered {b}[scoreL2SHS]{/b} (60 percent)
            questions. Congratulations, [playername]. You passed in this quiz. Great job!"

            hide classroomshs

            jump EndingSHS

        if scoreL2SHS == 7:
            "Out of 10 questions, [playername] answered {b}[scoreL2SHS]{/b} (70 percent)
            questions. Congratulations, [playername]. You passed in this quiz. Great job!"

            hide classroomshs

            jump EndingSHS

        if scoreL2SHS == 8:
            "Out of 10 questions, [playername] answered {b}[scoreL2SHS]{/b} (80 percent)
            questions. Congratulations, [playername]. You passed in this quiz. Great job!"

            hide classroomshs

            jump EndingSHS

        if scoreL2SHS == 9:
            "Out of 10 questions, [playername] answered {b}[scoreL2SHS]{/b} (90 percent)
            questions. Congratulations, [playername]. You passed in this quiz. Great job!"

            hide classroomshs

            jump EndingSHS


        if scoreL2SHS == 10:
            "Out of 10 questions, [playername] answered {b}[scoreL2SHS]{/b} (100 percent)
            questions. Congratulations, [playername]. You passed in this quiz. Great job!"

            hide classroomshs

            jump EndingSHS

    return

    label quizdaySHS3:

        $renpy.music.play("audio/The 126ers - End Of Summer Instrumental Extended.mp3", loop=True)

        show classroomshs

        show TeacherMarites

        teachermarites "Good morning, students. Today is your quiz day. Once I gave the quiz sheets to all of you,
        you may now start answering the questions provided. Do your best and good luck."

        hide TeacherMarites

        "Teacher Marites gave the quiz sheets to the students."

        "Okay, player. I will present to you the mechanics of this game so please read and follow the
        mechanics of this game. Thank you."

        hide classroomshs

        show Mechanics1

        window hide

        pause

        hide Mechanics1

        show Mechanics2

        window hide

        pause

        hide Mechanics2

        show classroomshs

        show TeacherMarites

        teachermarites "Okay, you may now start answering."

        hide TeacherMarites

        "Since you are about to take the quiz, you won't hear any background music until the end of the quiz."

        "That is because usually, when you take your in school, you have to take it quietly."

        stop music

        jump Question1SHSL3

    label Question1SHSL3:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question1shs_slowL3'                    ### set where you want to jump once the timer runs out


        Question1SHS "Involves reading with a purpose in order to grasp definitions and
        meanings,understand debates, and identify and interpret evidence."
        jump q1shs3
    return

    label q1shs3:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Active reading":
                jump L3correctanswershs1
            "B. Inactive reading":
                jump L3wronganswershs1
            "C. Passive reading":
                jump L3wronganswershs1
            "D. Backread":
                jump L3wronganswershs1

    return


    label L3wronganswershs1:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. Active reading{/b}. You may now proceed to Question no. 2."
        $ scoreL3SHS +=0
        stop sound
        stop music
        jump Question2SHSL3
    return

    label L3correctanswershs1:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 2."
        $ scoreL3SHS +=1
        stop sound
        stop music
        jump Question2SHSL3

    return

    label question1shs_slowL3:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}A. Active reading{/b}.
        You may now proceed to Question no. 2."
        $ scoreL1SHS +=0
        stop sound
        stop music
        jump Question2SHSL3
    return

    label Question2SHSL3:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question2shs_slowL3'                    ### set where you want to jump once the timer runs out


        Question2SHS "Usually consists of just a page number in the page’s top-right corner."
        jump q2shs3
    return

    label q2shs3:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Cover header":
                jump L3wronganswershs2
            "B. Page header":
                jump L3correctanswershs2
            "C. Back header":
                jump L3wronganswershs2
            "D. Title header":
                jump L3wronganswershs2

    return


    label L3wronganswershs2:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}B. Page header{/b}. You may now proceed to Question no. 3."
        $ scoreL3SHS +=0
        stop sound
        stop music
        jump Question3SHSL3
    return

    label L3correctanswershs2:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 3."
        $ scoreL3SHS +=1
        stop sound
        stop music
        jump Question3SHSL3
    return

    label question2shs_slowL3:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}B. Page header{/b}.
        You may now proceed to Question no. 3."
        $ scoreL3SHS +=0
        stop sound
        stop music
        jump Question3SHSL3
    return

    label Question3SHSL3:
            $ time = 10                                     ### set variable time to 3
            $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
            $ timer_jump = 'question3shs_slow3'                    ### set where you want to jump once the timer runs out


            Question3SHS "How many APA headings level are possible.?"
            jump q3shs3
    return

    label q3shs3:

            show screen countdown                          ### call and start the timer

            menu:

                "A. 2":
                    jump L3wronganswershs3
                "B. 3":
                    jump L3wronganswershs3
                "C. 4":
                    jump L3wronganswershs3
                "D. 5":
                    jump L3correctanswershs3

    return

    label L3wronganswershs3:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}D. 5{/b}. You may now proceed to Question no. 4."
        $ scoreL3SHS +=0
        stop sound
        stop music
        jump Question4SHSL3
    return

    label L3correctanswershs3:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 4."
        $ scoreL3SHS +=1
        stop sound
        stop music
        jump Question4SHSL3
    return

    label question3shs_slowL3:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}D. 5{/b}.
        You may now proceed to Question no. 4."
        $ scoreL1SHS +=0
        stop sound
        stop music
        jump Question4SHSL3
    return

    label Question4SHSL3:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question4shs_slow3'                    ### set where you want to jump once the timer runs out


        Question4SHS "Heading level 1 is used for main sections such as “_______” or “_______”."
        jump q4shs3
    return

    label q4shs3:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Methods or Results":
                jump L3correctanswershs4
            "B. Critic or Results":
                jump L3wronganswershs4
            "C. Summary or Results":
                jump L3wronganswershs4
            "D. Title or Results":
                jump L3wronganswershs4

    return

    label L3wronganswershs4:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. Methods or Results{/b}. You may now proceed to Question no. 5."
        $ scoreL3SHS +=0
        stop sound
        stop music
        jump Question5SHSL3
    return

    label L3correctanswershs4:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 5."
        $ scoreL3SHS +=1
        stop sound
        stop music
        jump Question5SHSL3
    return

    label question4shs_slowL3:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}A. Methods or Results{/b}.
        You may now proceed to Question no. 5."
        $ scoreL1SHS +=0
        stop sound
        stop music
        jump Question5SHSL3
    return

    label Question5SHSL3:
            $ time = 10                                     ### set variable time to 3
            $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
            $ timer_jump = 'question5shs_slow3'                    ### set where you want to jump once the timer runs out


            Question5SHS "Heading levels 2 to 5 are used for __________."
            jump q5shs3
    return

    label q5shs3:
        show screen countdown                          ### call and start the timer

        menu:
            "A. Subtitle":
                jump L3wronganswershs5
            "B. Substitution":
                jump L3wronganswershs5
            "C. Subheading":
                jump L3correctanswershs5
            "D. Heading":
                jump L3wronganswershs5

    return


    label L3wronganswershs5:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}C. Subheading{/b}. You may now proceed to Question no. 6."
        $ scoreL3SHS +=0
        stop sound
        stop music
        jump Question6SHSL3
    return

    label L3correctanswershs5:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 6."
        $ scoreL3SHS +=1
        stop sound
        stop music
        jump Question6SHSL3

    return

    label question5shs_slowL3:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}C. Subheading{/b}.
        You may now proceed to Question no. 6."
        $ scoreL1SHS +=0
        stop sound
        stop music
        jump Question6SHSL3
    return

    label Question6SHSL3:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question6shs_slow3'                    ### set where you want to jump once the timer runs out


        Question6SHS "This is the first page of an APA Style paper. There are different guidelines for student and professional papers.
        Both versions include the paper title and author’s name and affiliation."
        jump q6shs3
    return

    label q6shs3:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Title page":
                jump L3correctanswershs6
            "B. First page":
                jump L3wronganswershs6
            "C. Top page":
                jump L3wronganswershs6
            "D. Front page":
                jump L3wronganswershs6

    return


    label L3wronganswershs6:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. Title page{/b}. You may now proceed to Question no. 7."
        $ scoreL3SHS +=0
        stop sound
        stop music
        jump Question7SHSL3
    return

    label L3correctanswershs6:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 7."
        $ scoreL3SHS +=1
        stop sound
        stop music
        jump Question7SHSL3

    return

    label question6shs_slowL3:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}A. Title page{/b}.
        You may now proceed to Question no. 7."
        $ scoreL1SHS +=0
        stop sound
        stop music
        jump Question7SHSL3
    return

    label Question7SHSL3:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question7shs_slow3'                    ### set where you want to jump once the timer runs out


        Question7SHS "A 150–250 word summary of your paper,
        usually required in professional papers, but it’s rare to include one in student papers."
        jump q7shs3
    return

    label q7shs3:

            show screen countdown                          ### call and start the timer

            menu:

                "A. Construct":
                    jump L3wronganswershs7
                "B. Abstract":
                    jump L3correctanswershs7
                "C. Title Page":
                    jump L3wronganswershs7
                "D. Active reading":
                    jump L3wronganswershs7

    return

    label L3wronganswershs7:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}B. Abstract{/b}. You may now proceed to Question no. 8."
        $ scoreL3SHS +=0
        stop sound
        stop music
        jump Question8SHSL3
    return

    label L3correctanswershs7:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 8."
        $ scoreL3SHS +=1
        stop sound
        stop music
        jump Question8SHSL3
    return

    label question7shs_slowL3:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}B. Abstract{/b}.
        You may now proceed to Question no. 8."
        $ scoreL1SHS +=0
        stop sound
        stop music
        jump Question8SHSL3
    return

    label Question8SHSL3:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question8shs_slow3'                    ### set where you want to jump once the timer runs out


        Question8SHS "APA Style does not provide guidelines for formatting the ____________.
        It’s also not a required paper element in either professional or student papers."
        jump q8shs3
    return

    label q8shs3:
        show screen countdown                          ### call and start the timer

        menu:
            "A. Title page":
                jump L3wronganswershs8
            "B. Abstract":
                jump L3wronganswershs8
            "C. Table of contents":
                jump L3correctanswershs8
            "D. Cover page":
                jump L3wronganswershs8

    return

    label L3wronganswershs8:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}C. Table of contents{/b}.
        You may now proceed to Question no. 9."
        $ scoreL3SHS +=0
        stop sound
        stop music
        jump Question9SHSL3
    return

    label L3correctanswershs8:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 9."
        $ scoreL3SHS +=1
        stop sound
        stop music
        jump Question9SHSL3
    return

    label question8shs_slowL3:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}C. Table of contents{/b}.
        You may now proceed to Question no. 9."
        $ scoreL1SHS +=0
        stop sound
        stop music
        jump Question9SHSL3
    return


    label Question9SHSL3:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question9shs_slow3'                    ### set where you want to jump once the timer runs out


        Question9SHS "When you’re writing a reaction about what
        you have seen or experienced, that would be classified as _____________________."
        jump q9shs3
    return

    label q9shs3:
        show screen countdown                          ### call and start the timer

        menu:
            "A. Tissue Paper":
                call L3wronganswershs9
            "B. Review Paper":
                call L3wronganswershs9
            "C. Reaction paper":
                call L3correctanswershs9
            "D. I have no idea":
                call L3wronganswershs9

    return


    label L3wronganswershs9:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}C. Reaction paper{/b}. You may now proceed to Question no. 10."
        $ scoreL3SHS +=0
        stop sound
        stop music
        jump Question10SHSL3
    return

    label L3correctanswershs9:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 10."
        $ scoreL3SHS +=1
        stop sound
        stop music
        jump Question10SHSL3

    return

    label question9shs_slowL3:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}C. Reaction paper{/b}.
        You may now proceed to Question no. 9."
        $ scoreL1SHS +=0
        stop sound
        stop music
        jump Question10SHSL3
    return

    label Question10SHSL3:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question10shs_slow3'                    ### set where you want to jump once the timer runs out


        Question10SHS "When you’re writing a reaction about what
        you have seen or experienced, that would be classified as _____________________"
        jump q10shs3
    return

    label q10shs3:
        show screen countdown                          ### call and start the timer

        menu:
            "A. Scratch Paper":
                jump L3wronganswershs10
            "B. Bond Paper":
                jump L3wronganswershs10
            "C. Review Paper":
                jump L3correctanswershs10
            "D. One whole sheet of paper":
                jump L3wronganswershs10

    return

    label L3wronganswershs10:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}C. Review Paper{/b}. And this is the end of the quiz, let us
        now see the results."
        $ scoreL1SHS +=0
        stop sound
        stop music
        jump ResultsSHS3
    return

    label L3correctanswershs10:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! And this is the end of the quiz, let us
        now see the results."
        $ scoreL3SHS +=1
        stop sound
        stop music
        jump ResultsSHS3
    return

    label question10shs_slowL3:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}C. Review Paper{/b}.
        You may now proceed to Question no. 10."
        $ scoreL1SHS +=0
        stop sound
        stop music
        jump ResultsSHS3
    return

    label ResultsSHS3:
        show classroomshs

        if scoreL3SHS == 0:
            "Out of 10 questions, [playername] have answered {b}[scoreL3SHS]{/b}(0 percent) questions.
            Unfortunately, you have failed this quiz. Please study the lesson again."

            hide classroomshs

            jump L3SHS

        if scoreL3SHS == 1:
            "Out of 10 questions, [playername] have answered {b}[scoreL3SHS]{/b}(10 percent) questions.
            Unfortunately, you have failed this quiz. Please study the lesson again."

            hide classroomshs

            jump L3SHS

        if scoreL3SHS == 2:
            "Out of 10 questions, [playername] have answered {b}[scoreL3SHS]{/b}(20 percent) questions.
            Unfortunately, you have failed this quiz. Please study the lesson again."

            hide classroomshs

            jump L3SHS

        if scoreL3SHS == 3:
            "Out of 10 questions, [playername] have answered {b}[scoreL3SHS]{/b}(30 percent) questions.
            Unfortunately, you have failed this quiz. Please study the lesson again."

            hide classroomshs

            jump L3SHS

        if scoreL3SHS == 4:
            "Out of 10 questions, [playername] have answered {b}[scoreL3SHS]{/b}(40 percent) questions.
            Unfortunately, you have failed this quiz. Please study the lesson again."

            hide classroomshs

            jump L3SHS

        if scoreL3SHS == 5:
            "Out of 10 questions, [playername] answered {b}[scoreL3SHS]{/b} (50 percent)
            questions. Congratulations, [playername]. You passed in this quiz. Great job!"

            hide classroomshs

            jump EndingSHS

        if scoreL3SHS == 6:
            "Out of 10 questions, [playername] answered {b}[scoreL3SHS]{/b} (60 percent)
            questions. Congratulations, [playername]. You passed in this quiz. Great job!"

            hide classroomshs

            jump EndingSHS

        if scoreL3SHS == 7:
            "Out of 10 questions, [playername] answered {b}[scoreL3SHS]{/b} (70 percent)
            questions. Congratulations, [playername]. You passed in this quiz. Great job!"

            hide classroomshs

            jump EndingSHS

        if scoreL3SHS == 8:
            "Out of 10 questions, [playername] answered {b}[scoreL3SHS]{/b} (80 percent)
            questions. Congratulations, [playername]. You passed in this quiz. Great job!"

            hide classroomshs

            jump EndingSHS

        if scoreL3SHS == 9:
            "Out of 10 questions, [playername] answered {b}[scoreL3SHS]{/b} (90 percent)
            questions. Congratulations, [playername]. You passed in this quiz. Great job!"

            hide classroomshs

            jump EndingSHS


        if scoreL3SHS == 10:
            "Out of 10 questions, [playername] answered {b}[scoreL3SHS]{/b} (100 percent)
            questions. Congratulations, [playername]. You passed in this quiz. Great job!"

            hide classroomshs

            jump EndingSHS


    label EndingSHS:
        $renpy.music.play("audio/The 126ers - End Of Summer Instrumental Extended.mp3", loop=True)

        show classroomshs

        show TeacherMarites

        teachermarites "The quiz is over. You may now pass your paper."

        hide Teacher Marites

        "A few minutes later."

        show TeacherMarites

        teachermarites "Congratulations to all of you
        in this class for doing their best for today's quiz. Let's give ourselves a round of applause."

        hide TeacherMarites

        "The students gave theirselves a round of applause."

        show Matthew

        matthew "Yeah! We did it."

        hide Matthew

        playername "That's right. Our time spent in studying for this quiz has finally paid off."

        show Matthew

        matthew "Anyway, we'll talk more about it later."

        hide Matthew

        show Martin

        martin "Alright, then. For now, let us celebrate our own victory."

        hide Martin

        show TeacherMarites

        teachermarites "And so our class ends today. See you tomorrow."

        hide TeacherMarites

        "Teacher Marites left the classroom."

        "After a few hours, their school has finally ended."

        hide classroomshs

        show campus

        show Matthew

        matthew "Before we head to the diner, I forgot to tell you something."

        hide Matthew

        show Allen

        allen "What is it, Matthew?"

        hide Allen

        show Matthew

        matthew "Well, I forgot to tell you that since I made the agreement yesterday, I will be the one to treat
        you all there."

        hide Matthew

        show Martin

        martin "That's a good idea, Matthew! Your timing is perfect because actually..."

        martin "I don't have enough money to eat at the diner so I will accept your treat."

        hide Martin

        show Matthew

        matthew "Don't worry, man. I got this."

        hide Matthew

        show Allen

        allen "Anyway, thank you for giving me a wonderful advice when I was at my lowest yesterday."

        hide Allen

        show Matthew

        matthew "You're welcome, man. That's what friends are for."

        matthew "So what are we waiting for? Let's go!"

        hide Matthew

        "And they went to the diner to have fun eating the best food and drinking the best drink."

        hide campus

        show black

        "Before the game ends, we would like to give our big thanks to sir Gerald for being the best thesis adviser
        that we ever had. He has always been there for us when we need him the most when it comes to advice or guide,
        testing our game, and many more."

        "We wish him all the best. Our respect is big for him."

        "We would also like to give our big thanks in advance to those who will play this game and to those who will
        support us in developing this game because if not because of your support, we won't be able to develop this game
        with our own heart and soul."

        "Until then, goodbye."

        hide black

        show TheEnd

        window hide

        pause

        hide TheEnd

    return


###############################################################################

    label college:
        #So this will tackle the scenario of College once you chose College as your difficulty.

        $renpy.music.play("audio/The 126ers - End Of Summer Instrumental Extended.mp3", loop=True)
        scene campus

        "There are four friends named Adrian, Mark, Christian, and [playername]. They went to school together today.
        All of them are grade 11 Senior High School students at Belridge Senior High School and they belong to 11-A class."

        stop music

        $renpy.sound.play("audio/Japanese School Bell.mp3", loop=True)

        "(The bell rang)"

        "All students of Belridge Senior High School. Please come to your respective classrooms.
        Your classes will start in 10 minutes."

        stop sound

        play music "audio/The 126ers - End Of Summer Instrumental Extended.mp3"

        show Adrian

        adrian "Oh, man. We're gonna be late. What are we going to do?"

        hide Adrian

        menu:

            "What are they going to do?"

            "Go to the classroom early":
                jump classroom2
            "Go to the cafeteria":
                jump cafeteria2
            "Go to the comfort room":
                jump CR2

    label classroom2:
        show Mark

        mark "Alright guys, let's race our way to the classroom as fast as we can."

        hide Mark

        $renpy.sound.play("audio/Running.mp3", loop=True)

        "The four of them began running all the way to their classroom."

        hide campus

        show hallway

        $renpy.sound.play("audio/Running.mp3", loop=True)

        christian "Look, we're almost there. Let's keep running."

        "They kept running all the way to their classroom."

        stop sound

        "And finally, they made it."

        hide hallway

        stop music

        show black

        play sound "audio/Door Open and Door Close.mp3"

        "(Door opens and closes)"

        stop sound

        hide black

        jump classroomCollege

        jump campusCollege


    label cafeteria2:
        player "Since we have 10 minutes before the class starts, would you guys like to accompany me in buying food?"

        show Christian

        christian "Hell no!"

        hide Christian

        show Mark

        mark "You are not a child anymore, man. You can already take care of yourself."

        hide Mark

        show Adrian

        adrian "It's a no for me."

        hide Adrian

        player "Oh, come on! Are you guys really my friends?! Alright, I'll treat you all at the cafeteria,
        but please, let's
        go to the cafeteria together."

        "And they all agreed to go to the cafeteria together."

        hide campus

        show cafeteria

        "After they went to the cafeteria to buy food, they went out and hurriedly went to the classroom."

        hide cafeteria

        show hallway

        $renpy.sound.play("audio/Running.mp3", loop=True)

        christian "Look, we're almost there. Let's keep running."

        "They kept running all the way to their classroom."

        stop sound

        "And finally, they made it."

        hide hallway

        stop music

        show black

        play sound "audio/Door Open and Door Close.mp3"

        "(Door opens and closes)"

        stop sound

        hide black

        jump classroomCollege

        jump campusCollege

    return

    label CR2:
        "Suddenly, [playername] felt the nature's call."

        player "I need to go to the comfort room. Please wait for me."

        show Adrian

        adrian "[playername], we're not going to wait for you in the comfort room. We will accompany you instead.
        That's what friends are for, right?"

        hide adrian

        player "Alright, then. Let's go."

        "And they went to the comfort room."

        hide campus2

        stop music

        $renpy.sound.play("audio/toilet music.mp3", loop=True)

        show cr

        "[playername] has to stay inside the cubicle toilet a bit longer while
        Matthew, Allen, and Martin will wait for him in the comfort room."

        show Mark

        mark "I think [playername] will take a while in answering the nature's call."

        hide Mark

        show Christian

        christian "Well, it seems like [playername] ate a lot of breakfast a while ago before going to school."

        hide Christian

        show Adrian

        adrian "Can't blame [playername] about that though if that's the sole reason why. We should wait a little
        bit longer."

        hide Adrian

        "After a long time of waiting, [playername] was able to finish answering the call of the nature.
        [playername] wore his pants and his belt on."

        $renpy.sound.play("audio/toilet flush.mp3", loop=True)

        "([playername] flushes the toilet)"

        stop sound

        $renpy.music.play("audio/The 126ers - End Of Summer Instrumental Extended.mp3", loop=True)

        "And [playername] went out of the toilet cubicle."

        player "Phew! I feel relieved, guys. Thank you for waiting for me to finish taking a dump."

        show Mark

        mark "No problem, man."

        hide Mark

        "(Mark checked the time on his phone)"

        show Mark

        mark "It's already 7:55. We should hurry to the classroom now!"

        hide Mark

        show Christian

        christian "Sir, yes, sir!"

        hide Christian

        "And they went out of the comfort room to go to their classroom."

        hide cr

        show hallway

        $renpy.sound.play("audio/Running.mp3", loop=True)

        christian "Look, we're almost there. Let's keep running."

        "They kept running all the way to their classroom."

        stop sound

        "And finally, they made it."

        hide hallway

        stop music

        show black

        play sound "audio/Door Open and Door Close.mp3"

        "(Door opens and closes)"

        stop sound

        hide black

        jump classroomCollege

    return

    label classroomCollege:
        show classroomshs

        $renpy.music.play("audio/The 126ers - End Of Summer Instrumental Extended.mp3", loop=True)

        show Adrian

        adrian "Phew! That was tiring."

        hide Adrian

        "Adrian wiped his sweat with his handkerchief and he checked the time on his wristwatch afterwards."

        show Adrian

        adrian "Good thing, we're not yet late. Our class will start at 8:00, but the time is 7:53."

        adrian "So we have seven minutes before the start of our class."

        hide Adrian

        player "Anyway, we should take our seats now."

        show Christian

        christian "Right, we should do that."

        hide Christian

        "[playername], Adrian, Mark, and Christian took their respective seats. At 8:00, their English teacher
    came inside the classroom. She walked towards her table and put down her things.
    Afterwards, she walked in front of the table and started greeting the class."

        show TeacherLuna

        teacherluna "Good morning, 11-A students."

        hide TeacherLuna

        elevenA "Good morning, teacher."

        show TeacherLuna

        teacherluna "I have an announcement to tell so please listen carefully."

        teacherluna "Since we were able to finish our lessons for this week, we won't have an English class
    today. However, we will have a quiz about those lessons tomorrow."

        hide TeacherLuna

        player "Huh??!!!! But, teacher, we only finished discussing those English lessons yesterday."

        show TeacherLuna

        teacherluna "Oh, come on, Mr. [playername]. I've decided to test your knowledge through your tomorrow's quiz
        because I want to see whether all of you learned anything from this class or not."

        teacherluna  "Anyway, I will dismiss you early now so you can use your
        free time to study your lessons or to do something else. See you tomorrow, class."

        hide TeacherLuna

        elevenA "See you tomorrow, teacher."

        "Teacher Luna left the classroom immediately. Afterwards, the students left the classroom as well except for
    [playername], Adrian, Mark, and Christian."

        player "Yo! Do you like to study English with me in my house for our quiz tomorrow later after school?"

        show Mark

        mark "Sure thing, man. That would be nice."

        hide Mark

        show Adrian

        adrian "Besides, studying is not complete without free food, right, [playername]?"

        hide Adrian

        show Christian

        christian "Adrian, here you go again with your desire to eat food. I think there's a dragon in your stomach, man."

        hide Christian

        show Adrian

        adrian "Shut it, Allen. I just want to eat while studying. I cannot gain knowledge without food, bro."

        hide Adrian

        player "Alright, then. It's decided. Don't forget it, okay?"

        "They spent the entire vacant time playing Dark Legends together while waiting for the vacant time to end."

        "At 1:00 p.m., the vacant time was over so their classmates went back to the classroom."

        "A few seconds later, Teacher Raul went inside the classroom and it's time for the entire class to endure
        her boring Math class."

        elevenA "Good afternoon, Teacher Raul."

        show TeacherRaul

        teacherraul "Good afternoon, students. Our new lesson for today is about algebra."

        hide TeacherRaul

        show Mark

        mark "Here we go again."

        hide Mark

        "They have to endure the boredom until 2:30 p.m. I hope they will be okay throughout the lesson."

        "They went to school so they have to listen to the teacher because that is their responsibility as a student
        no matter how boring the class is."

        stop music

        $renpy.sound.play("audio/Japanese School Bell.mp3", loop=True)

        "At 2:30 p.m., the bell rang again."

        stop sound

        $renpy.music.play("audio/The 126ers - End Of Summer Instrumental Extended.mp3", loop=True)

        show TeacherRaul

        teacherraul "Okay, class. You may now dismiss. Goodbye, class."

        hide TeacherRaul

        elevenA "Goodbye, teacher."

        "Teacher Raul and the students of 11-A left the classroom."

        hide classroomshs

        jump campusCollege


    label campusCollege:
        show campus

        player "Finally, school's over."

        show Mark

        mark "Yeah, it's already over. We were able to endure the boredom of her class this afternoon."

        hide Mark

        player "Good thing I can finally go home and play video games for the rest of the day."

        show Adrian

        adrian "Wait, what? I thought we're going to study for our English quiz tomorrow at your house, remember?"

        hide Adrian

        show Mark

        mark "Yeah, he's right. Studying for tomorrow's quiz comes first before video games, man."

        hide Mark

        player "Oh, my bad. We're supposed to study English when we get to my house. But, Adrian, I am sure you like
    eating better than studying."

        show Adrian

        adrian "Give me a break, [playername]. Studying gets better when there's food so deal with it!"

        hide Adrian

        player "Relax, Martin, relax. I'm just joking around here, man. Anyway, let's go to my house."

        "And they began walking to [playername]'s home."

        hide campus

        jump Collegelessons

    return

    label Collegelessons:
        $renpy.music.play("audio/More Feels.mp3", loop=True)

        show HouseProtag

        "After 10 minutes of walking, they were able to make it to [playername]'s house."

        show Adrian

        adrian "And so we finally made it, everyone. So, [playername], are your parents around?"

        hide Adrian

        player "No, they're not here. They went out of town for work, but they will be back after 3 days."

        show Mark

        mark "So when did they leave?"

        hide Mark

        player "They left early in the morning before I went to school."

        show Mark

        mark "Oh, I see."

        hide Mark

        player "Anyway, let's go inside my house."

        "[playername] took the house keys in the backpack and unlocked the door to their house.
        After unlocking the door, they went inside the house."

        hide HouseProtag

        show black

        stop music

        play sound "audio/Door Open and Door Close.mp3"

        "(Door opens and closes)"

        stop sound

        hide black

        $renpy.music.play("audio/More Feels.mp3", loop=True)

        show LivingRoom

        "So this is what the [playername]'s living room looks like."

        "To be honest, this living room looks beautiful in the eyes despite that it is
        simple as the way it is. Well, I can say that I do believe that simplicity is beauty."

        show Christian

        christian "It was quite a tiring day today. Forcing ourselves to study for tomorrow's quiz at this point
        is not effective."

        hide Christian

        show Adrian

        adrian "Christian's right. It will be better for us to take a rest first before eating and studying."

        hide Adrian

        player "Yeah, that is really a good idea, Christian. We better go to my bedroom and start resting."

        "They all went to [playername]'s bedroom to rest and Mark closed the door."

        hide LivingRoom

        show Bedroom

        player "So as usual, I still use the same bed so only 2 people can sleep in my bed,
        but Adrian and I can get the foam mattress in the storage room. Mark, don't close the door after
        we leave."

        "[playername] opened the door again."

        show Adrian

        adrian "Alright then. We'll just wait here as usual."

        hide Adrian

        "[playername] and Adrian left the bedroom to get the foam mattress in the storage room.
        While Christian and Mark, on the other hand, started having a conversation."

        show Mark

        mark "Christian, to be honest, I doubt I will be able to pass our English quiz tomorrow.
        That is because I think it is very hard for me to learn our English lessons.
        This is ironic for me as someone who can speak English fluently."

        hide Mark

        show Christian

        christian "Mark, I know that it must have been hard for you to learn that subject, but I believe in you.
        I believe that you can do it uh... I mean, you can pass the tomorrow's quiz."

        christian "Whether you're good at something or not, what matters the most is that you put your effort in doing
        your best."

        christian "In fact, there is nothing wrong in trying until you succeed."

        christian "That is because in school, you're not going to study one thing."

        christian "You will be studying a lot of things and you have to do your best even if the results may turn out well
        or not because what matters the most is that you tried to persevere enough to make an effort in doing your best
        in everything that you do regardless of how important a certain task is."

        christian "In my case, I wasn't really good at English before, but my teacher told me to keep trying to put a lot of
        effort in learning it"

        christian "so in the end,
        I was able to improve my skills in English even though there will always be a room for me to make mistakes
        because my English is still not perfect after all."

        hide Christian

        "Well, that reminds me of one of my junior high school teachers because she used to tell this kind of advice in our
        class before and I still remember and live with this advice of hers until now."

        "To be honest, that advice helped me to persevere in life whether in studies or in other things. Thanks, teacher.
        \n-Wrichmond"

        show Mark

        mark "Wow, that's good to hear, man. It is good to know that I have learned a lot of things from you.
        What I've learned from you today made me realize and understand the importance of putting effort into something."

        mark "Well, anyway. Thanks for the advice, man."

        hide Mark

        show Christian

        christian "No problem, man."

        hide Christian

        "And [playername] and Adrian went back to the bedroom with the foam mattress."

        show Bedroom

        show FoamMattress

        window hide

        pause

        hide FoamMattress

        show Christian

        christian "Finally, they're here with the foam mattress."

        hide Christian

        "[playername] and Adrian put down the foam mattress."

        player "And since we have the foam mattress here, we can now finally rest for an hour."

        "And so they decided to take a rest for an hour. Matthew and Allen slept on the foam mattress while [playername]
        and Martin slept on [playername]'s bed."

        stop music

        show black

        "After resting for an hour, they woke up and stretched their body."

        hide black

        $renpy.music.play("audio/More Feels.mp3", loop=True)

        show Bedroom

        player "(yawns)"

        adrian "(yawns)"

        mark "(yawns)"

        christian "(yawns)"

        show Christian

        christian "Alright, listen up. I have to say something."

        hide Christian

        player "What is it, Christian?"

        show Christian

        christian "Ok so here's the deal: we will eat together at Rowan's Diner after school.
        Regardless of the scores that we get, always remember that what matters the most is that we did our best
        on that day."

        hide Christian

        show Adrian

        adrian "Oh, well, I can't deny that Christian's idea is indeed a great idea. He is smart as Albert Einstein, man so
        I agree with him here."

        hide Adrian

        show Mark

        mark "Same."

        hide Mark

        player "Me too."

        show Christian

        christian "That's good to hear, guys. So what are we waiting for? Let's study!!!!!!"

        hide Christian

        "Okay, player. Before you proceed to the quiz day of [playername], Adrian, Mark, and Christian, I want you
        to help [playername] to get the best score possible for tomorrow's quiz. The [playername]'s fate
        for tomorrow's quiz is in your hands now so you better learn the lessons right away, ok?"

        jump study2

    return

    label study2:

        show Bedroom

        "Okay so you have finally decided to study, player. In that case,
        I will be providing you the images of the lessons that you
        need to learn. Good luck and happy studying!"

        jump studychoicesCollege

    return

    label studychoicesCollege:

        hide black

        show Bedroom

        $renpy.music.play("audio/More Feels.mp3", loop=True)

        menu:
            "Which of the following lessons should you study?"

            "Lesson 1: Concept Paper":
                jump L1College

            "Lesson 2: Position Paper (Part 1)":
                jump L2College

            "Lesson 3: Position Paper (Part 2)":
                jump L3College

    return

    label L1College:
        stop music

        $renpy.music.play("audio/Good Friends- Yasper.mp3", loop=True)

        hide Bedroom

        show screen gameUICollege

        $L1CollegeProgress = 0

        show L1College

        window hide

        pause

        hide L1College

        $L1CollegeProgress += 9


        show L1College2

        window hide

        pause

        hide L1College2

        $L1CollegeProgress += 9


        show L1College3

        window hide

        pause

        hide L1College3

        $L1CollegeProgress += 9


        show L1College4

        window hide

        pause

        hide L1College4

        $L1CollegeProgress += 9


        show L1College5

        window hide

        pause

        hide L1College5

        $L1CollegeProgress += 9


        show L1College6

        window hide

        pause

        hide L1College6

        $L1CollegeProgress += 9


        show L1College7

        window hide

        pause

        hide L1College7

        $L1CollegeProgress += 9


        show L1College8

        window hide

        pause

        hide L1College8

        $L1CollegeProgress += 9


        show L1College9

        window hide

        pause

        hide L1College9

        $L1CollegeProgress += 9


        show L1College10

        window hide

        pause

        hide L1College10

        $L1CollegeProgress += 19


        show L1College11

        window hide

        pause

        hide L1College11

        stop music

        show black

        hide screen gameUICollege

        "You have finally finished reading the lesson. You will now proceed to the quiz part."

        jump quizdayCollege1

    return

    label quizdayCollege1:

        $renpy.music.play("audio/The 126ers - End Of Summer Instrumental Extended.mp3", loop=True)

        show classroomshs

        show TeacherMarites

        teachermarites "Good morning, students. Today is your quiz day. Once I gave the quiz sheets to all of you,
        you may now start answering the questions provided. Do your best and good luck."

        hide TeacherMarites

        "Teacher Marites gave the quiz sheets to the students."

        "Okay, player. I will present to you the mechanics of this game so please read and follow the
        mechanics of this game. Thank you."

        hide classroomshs

        show Mechanics1

        window hide

        pause

        hide Mechanics1

        show Mechanics2

        window hide

        pause

        hide Mechanics2

        show classroomshs

        show TeacherMarites

        teachermarites "Okay, you may now start answering."

        hide TeacherMarites

        "Since you are about to take the quiz, you won't hear any background music until the end of the quiz."

        "That is because usually, when you take your in school, you have to take it quietly."

        stop music

        jump Question1CollegeL1

    label Question1CollegeL1:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question1college_slow'                    ### set where you want to jump once the timer runs out


        Question1College "What are the 5 parts of a concept paper? "
        jump q1college
    return

    label q1college:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Earth, Fire, Water, Air, and Lightning":
                jump L1wronganswerCollege1
            "B. Apple, Lemon, Grapes, and Orange":
                jump L1wronganswerCollege1
            "C. Project Vision, Project Scope, Project Targets, Timeline and Milestones and Project Management":
                jump L1correctanswerCollege1
            "D. The sender, the receiver, the message, the channel and feedback":
                jump L1wronganswerCollege1

    return

    label L1wronganswerCollege1:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}C. Project Vision, Project Scope, Project Targets,
        Timeline and Milestones and Project Management{/b}. You may now proceed to Question no. 2."
        $ scoreL1College +=0
        stop sound
        stop music
        jump Question2CollegeL1
    return

    label L1correctanswerCollege1:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 2."
        $ scoreL1College +=1
        stop sound
        stop music
        jump Question2CollegeL1

    return

    label question1college_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}C. Project Vision, Project Scope, Project Targets,
        Timeline and Milestones and Project Management{/b}. You may now proceed to Question no. 2."
        $ scoreL1College +=0
        stop sound
        stop music
        jump Question2CollegeL1
    return

    label Question2CollegeL1:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question2college_slow'                    ### set where you want to jump once the timer runs out


        Question2College "Project scope is not part of concept paper."
        jump q2college
    return

    label q2college:

        show screen countdown                          ### call and start the timer

        menu:

            "A. True":
                jump L1wronganswerCollege2
            "B. False":
                jump L1correctanswerCollege2
            "C. Maybe":
                jump L1wronganswerCollege2
            "D. None of the Above":
                jump L1wronganswerCollege2

    return


    label L1wronganswerCollege2:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}B. False{/b}.
        You may now proceed to Question no. 3."
        $ scoreL1College +=0
        stop sound
        stop music
        jump Question3CollegeL1
    return

    label L1correctanswerCollege2:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 3."
        $ scoreL1College +=1
        stop sound
        stop music
        jump Question3CollegeL1

    return

    label question2college_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}B. False{/b}.
        You may now proceed to Question no. 3."
        $ scoreL1College +=0
        stop sound
        stop music
        jump Question3CollegeL1
    return

    label Question3CollegeL1:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question3college_slow'                    ### set where you want to jump once the timer runs out


        Question3College "It is the secondhand information obtained from reading books, watching news, videos,
        the internet, and other already documented material."
        jump q3college
    return

    label q3college:

        show screen countdown                          ### call and start the timer

        menu:

            "A. First data":
                jump L1wronganswerCollege3
            "B. Secondary data":
                jump L1correctanswerCollege3
            "C. Third Data":
                jump L1wronganswerCollege3
            "D. Fourth Data":
                jump L1wronganswerCollege3

    return


    label L1wronganswerCollege3:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}B. Secondary Data{/b}.
        You may now proceed to Question no. 4."
        $ scoreL1College +=0
        stop sound
        stop music
        jump Question4CollegeL1
    return

    label L1correctanswerCollege3:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 4."
        $ scoreL1College +=1
        stop sound
        stop music
        jump Question4CollegeL1
    return

    label question3college_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}B. False{/b}.
        You may now proceed to Question no. 3."
        $ scoreL1College +=0
        stop sound
        stop music
        jump Question4CollegeL1
    return

    label Question4CollegeL1:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question4college_slow'                    ### set where you want to jump once the timer runs out


        Question4College "Timeline and milestones is part of Concept paper."
        jump q4college
    return

    label q4college:

        show screen countdown                          ### call and start the timer

        menu:

            "A. True":
                jump L1correctanswerCollege4
            "B. False":
                jump L1wronganswerCollege4
            "C. Maybe":
                jump L1wronganswerCollege4
            "D. None of the Above":
                jump L1wronganswerCollege4

    return

    label L1wronganswerCollege4:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. True{/b}.
        You may now proceed to Question no. 5."
        $ scoreL1College +=0
        stop sound
        stop music
        jump Question5CollegeL1
    return

    label L1correctanswerCollege4:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 5."
        $ scoreL1College +=1
        stop sound
        stop music
        jump Question5CollegeL1

    return

    label question4college_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}A. True{/b}.
        You may now proceed to Question no. 5."
        $ scoreL1College +=0
        stop sound
        stop music
        jump Question5CollegeL1
    return

    label Question5CollegeL1:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question5college_slow'                    ### set where you want to jump once the timer runs out


        Question5College "Which of the following are the characteristics of a good concept paper?"
        jump q5college
    return

    label q5college:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Agreeableness, and Neuroticism":
                jump L1wronganswerCollege5
            "B. Beliefs":
                jump L1wronganswerCollege5
            "C. Cooperation":
                jump L1wronganswerCollege5
            "D. A clear description of the topic":
                jump L1correctanswerCollege5

    return

    label L1wronganswerCollege5:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}D. A clear description of the topic{/b}.
        You may now proceed to Question no. 6."
        $ scoreL1College +=0
        stop sound
        stop music
        jump Question6CollegeL1
    return

    label L1correctanswerCollege5:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 6."
        $ scoreL1College +=1
        stop sound
        stop music
        jump Question6CollegeL1
    return

    label question5college_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}D. A clear description of the topic{/b}.
        You may now proceed to Question no. 6."
        $ scoreL1College +=0
        stop sound
        stop music
        jump Question6CollegeL1
    return

    label Question6CollegeL1:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question6college_slow'                    ### set where you want to jump once the timer runs out


        Question6College "Timeline and milestones is part of the 5 parts of a concept paper?"
        jump q6college
    return

    label q6college:

        show screen countdown                          ### call and start the timer

        menu:

            "A. True":
                jump L1correctanswerCollege6
            "B. False":
                jump L1wronganswerCollege6
            "C. Maybe":
                jump L1wronganswerCollege6
            "D. None of the Above":
                jump L1wronganswerCollege6

    return

    label L1wronganswerCollege6:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. True{/b}.
        You may now proceed to Question no. 7."
        $ scoreL1College +=0
        stop sound
        stop music
        jump Question7CollegeL1
    return

    label L1correctanswerCollege6:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 7."
        $ scoreL1College +=1
        stop sound
        stop music
        jump Question7CollegeL1
    return

    label question6college_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}A. True{/b}.
        You may now proceed to Question no. 7."
        $ scoreL1College +=0
        stop sound
        stop music
        jump Question7CollegeL1
    return

    label Question7CollegeL1:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question7college_slow'                    ### set where you want to jump once the timer runs out


        Question7College "The part of the Concept Paper that covers
        personnel allocation and synchronizes efforts across different functions."
        jump q7college
    return

    label q7college:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Project Management":
                jump L1correctanswerCollege7
            "B. Time Scale Projects":
                jump L1wronganswerCollege7
            "C. Research Projects":
                jump L1wronganswerCollege7
            "D. Project Proposal":
                jump L1wronganswerCollege7

    return

    label L1wronganswerCollege7:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. Project Management{/b}.
        You may now proceed to Question no. 8."
        $ scoreL1College +=0
        stop sound
        stop music
        jump Question8CollegeL1
    return

    label L1correctanswerCollege7:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 8."
        $ scoreL1College +=1
        stop sound
        stop music
        jump Question8CollegeL1
    return

    label question7college_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}A. Project Management{/b}.
        You may now proceed to Question no. 8."
        $ scoreL1College +=0
        stop sound
        stop music
        jump Question8CollegeL1
    return

    ##later

    label Question8CollegeL1:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question8college_slow'                    ### set where you want to jump once the timer runs out


        Question8College "The Concept Paper should next define the __________, the specific flow of activities involved,
        the organizational boundaries as well as the end-to-end processes."
        jump q8college
    return

    label q8college:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Concept Scope":
                jump L1wronganswerCollege8
            "B. Reaction Scope":
                jump L1wronganswerCollege8
            "C. Review Scope":
                jump L1wronganswerCollege8
            "D. Project scope":
                jump L1correctanswerCollege8

    return

    label L1wronganswerCollege8:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}D. Project Scope{/b}.
        You may now proceed to Question no. 9."
        $ scoreL1College +=0
        stop sound
        stop music
        jump Question9CollegeL1
    return

    label L1correctanswerCollege8:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 9."
        $ scoreL1College +=1
        stop sound
        stop music
        jump Question9CollegeL1
    return

    label question8college_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}D. Project Scope{/b}.
        You may now proceed to Question no. 9."
        $ scoreL1College +=0
        stop sound
        stop music
        jump Question9CollegeL1
    return

    label Question9CollegeL1:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question9college_slow'                    ### set where you want to jump once the timer runs out


        Question9College "What is the most important part of a concept paper?"
        jump q9college
    return

    label q9college:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Supporting Documentation":
                jump L1correctanswerCollege9
            "B. Time Scale Projects":
                jump L1wronganswerCollege9
            "C. Research Projects":
                jump L1wronganswerCollege9
            "D. Project Proposal":
                jump L1wronganswerCollege9

    return

    label L1wronganswerCollege9:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. Supporting Documentation{/b}.
        You may now proceed to Question no. 10."
        $ scoreL1College +=0
        stop sound
        stop music
        jump Question10CollegeL1
    return

    label L1correctanswerCollege9:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 10."
        $ scoreL1College +=1
        stop sound
        stop music
        jump Question10CollegeL1
    return

    label question9college_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}A. Supporting Documentation{/b}.
        You may now proceed to Question no. 10."
        $ scoreL1College +=0
        stop sound
        stop music
        jump Question10CollegeL1
    return

    label Question10CollegeL1:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question10college_slow'                    ### set where you want to jump once the timer runs out


        Question10College "A brief paper that outlines the important
        components of a research or project before it is carried out."
        jump q10college
    return

    label q10college:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Concept paper":
                jump L1correctanswerCollege10
            "B. Position Paper ":
                jump L1wronganswerCollege10
            "C. Review Paper":
                jump L1wronganswerCollege10
            "D. None of the Above":
                jump L1wronganswerCollege10

    return

    label L1wronganswerCollege10:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. Concept Paper{/b}.
         And this is the end of the quiz, let us now see the results."
        $ scoreL1College +=0
        stop sound
        stop music
        jump ResultsCollege1
    return

    label L1correctanswerCollege10:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 10.
        And this is the end of the quiz, let us now see the results."
        $ scoreL1College +=1
        stop sound
        stop music
        jump ResultsCollege1
    return

    label question10college_slow:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}A. Concept Paper{/b}.
        And this is the end of the quiz, let us now see the results."
        $ scoreL1College +=0
        stop sound
        stop music
        jump ResultsCollege1
    return

    label ResultsCollege1:
        show classroomshs

        if scoreL1College == 0:
            "Out of 10 questions, [playername] have answered {b}[scoreL1College]{/b}(0 percent) questions.
            Unfortunately, you have failed this quiz. Please study the lesson again."

            hide classroomshs

            jump L1College

        if scoreL1College == 1:
            "Out of 10 questions, [playername] have answered {b}[scoreL1College]{/b}(10 percent) questions.
            Unfortunately, you have failed this quiz. Please study the lesson again."

            hide classroomshs

            jump L1College

        if scoreL1College == 2:
            "Out of 10 questions, [playername] have answered {b}[scoreL1College]{/b}(20 percent) questions.
            Unfortunately, you have failed this quiz. Please study the lesson again."

            hide classroomshs

            jump L1College

        if scoreL1College == 3:
            "Out of 10 questions, [playername] have answered {b}[scoreL1College]{/b}(30 percent) questions.
            Unfortunately, you have failed this quiz. Please study the lesson again."

            hide classroomshs

            jump L1College

        if scoreL1College == 4:
            "Out of 10 questions, [playername] have answered {b}[scoreL1College]{/b}(40 percent) questions.
            Unfortunately, you have failed this quiz. Please study the lesson again."

            hide classroomshs

            jump L1College

        if scoreL1College == 5:
            "Out of 10 questions, [playername] answered {b}[scoreL1College]{/b} (50 percent)
            questions. Congratulations, [playername]. You passed in this quiz. Great job!"

            hide classroomshs

            jump EndingCollege

        if scoreL1College == 6:
            "Out of 10 questions, [playername] answered {b}[scoreL1College]{/b} (60 percent)
            questions. Congratulations, [playername]. You passed in this quiz. Great job!"

            hide classroomshs

            jump EndingCollege

        if scoreL1College == 7:
            "Out of 10 questions, [playername] answered {b}[scoreL1College]{/b} (70 percent)
            questions. Congratulations, [playername]. You passed in this quiz. Great job!"

            hide classroomshs

            jump EndingCollege

        if scoreL1College == 8:
            "Out of 10 questions, [playername] answered {b}[scoreL1College]{/b} (80 percent)
            questions. Congratulations, [playername]. You passed in this quiz. Great job!"

            hide classroomshs

            jump EndingCollege

        if scoreL1College == 9:
            "Out of 10 questions, [playername] answered {b}[scoreL1College]{/b} (90 percent)
            questions. Congratulations, [playername]. You passed in this quiz. Great job!"

            hide classroomshs

            jump EndingCollege


        if scoreL1College == 10:
            "Out of 10 questions, [playername] answered {b}[scoreL1College]{/b} (100 percent)
            questions. Congratulations, [playername]. You passed in this quiz. Great job!"

            hide classroomshs

            jump EndingCollege

    label L2College:
        stop music

        $renpy.music.play("audio/Glimlip - S h e.mp3", loop=True)

        hide Bedroom

        show screen gameUICollege2

        $L2CollegeProgress = 0

        show L2College

        window hide

        pause

        hide L2College

        $L2CollegeProgress += 20


        show L2College2

        window hide

        pause

        hide L2College2

        $L2CollegeProgress += 20


        show L2College3

        window hide

        pause

        hide L2College3

        $L2CollegeProgress += 60


        show L2College4

        window hide

        pause

        hide L2College4

        $L2CollegeProgress

        stop music

        show black

        hide screen gameUICollege2

        "You have finally finished reading the lesson. You will now proceed to the quiz part."

        jump quizdayCollege2


    return

    label quizdayCollege2:

        $renpy.music.play("audio/The 126ers - End Of Summer Instrumental Extended.mp3", loop=True)

        show classroomshs

        show TeacherLuna

        teacherluna "Good morning, students. Today is your quiz day. Once I gave the quiz sheets to all of you,
        you may now start answering the questions provided. Do your best and good luck."

        hide TeacherLuna

        "Teacher Luna gave the quiz sheets to the students."

        "Okay, player. I will present to you the mechanics of this game so please read and follow the
        mechanics of this game. Thank you."

        hide classroomshs

        show Mechanics1

        window hide

        pause

        hide Mechanics1

        show Mechanics2

        window hide

        pause

        hide Mechanics2

        show classroomshs

        show TeacherLuna

        teacherluna "Okay, you may now start answering."

        hide TeacherLuna

        "Since you are about to take the quiz, you won't hear any background music until the end of the quiz."

        "That is because usually, when you take your in school, you have to take it quietly."

        stop music

    jump Question1CollegeL2

    return

    label Question1CollegeL2:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question1college_slowL2'                    ### set where you want to jump once the timer runs out


        Question1College "A good _________  will not only provide facts but also make proposals for resolutions."
        jump q1collegeL2
    return

    label q1collegeL2:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Concept Paper":
                jump L2wronganswercollege1
            "B. Position Paper":
                jump L2correctanswercollege1
            "C. Reaction Paper":
                jump L2wronganswercollege1
            "D. None of the above":
                jump L2wronganswercollege1

    return

    label L2correctanswercollege1:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 2."
        $ scoreL2College +=1
        stop sound
        stop music
        jump Question2CollegeL2
    return

    label L2wronganswercollege1:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}B. Position Paper{/b}. You may now proceed to Question no. 2."
        $ scoreL2College +=0
        stop sound
        stop music
        jump Question2CollegeL2
    return

    label question1college_slowL2:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}B. Position Paper{/b}. You may now proceed to Question no. 2."
        $ scoreL2College +=0
        stop sound
        stop music
        jump Question2CollegeL2
    return

    label Question2CollegeL2:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question2college_slowL2'                    ### set where you want to jump once the timer runs out


        Question2College "What are the three main elements of a position paper?."
        jump q2collegeL2
    return

    label q2collegeL2:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Knowledge and Skills about the field, Communication and Relationship Skills":
                jump L2wronganswercollege2
            "B. Quality of Instruction, Beliefs, and Professional behaviors":
                jump L2wronganswercollege2
            "C. Introduction, Body, and  Conclusion ":
                jump L2correctanswercollege2
            "D. None of the above":
                jump L2wronganswercollege2

    return

    label L2correctanswercollege2:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 2."
        $ scoreL2College +=1
        stop sound
        stop music
        jump Question3CollegeL2
    return

    label L2wronganswercollege2:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}C. Introduction, Body, and Conclusion{/b}.
        You may now proceed to Question no. 3."
        $ scoreL2College +=0
        stop sound
        stop music
        jump Question3CollegeL2
    return

    label question2college_slowL2:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is The correct answer is {b}C. Introduction, Body,
        and Conclusion{/b}. You may now proceed to Question no. 3."
        $ scoreL2College +=0
        stop sound
        stop music
        jump Question3CollegeL2
    return

    label Question3CollegeL2:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question3college_slowL2'                    ### set where you want to jump once the timer runs out


        Question3College "The part of the position paper that introduce your topic and end with your thesis statement."
        jump q3collegeL2
    return

    label q3collegeL2:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Introduction ":
                jump L2correctanswercollege3
            "B. Conclusion":
                jump L2wronganswercollege3
            "C. The body of the paper":
                jump L2wronganswercollege3
            "D. None of the above":
                jump L2wronganswercollege3

    return

    label L2correctanswercollege3:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 4."
        $ scoreL2College +=1
        stop sound
        stop music
        jump Question4CollegeL2
    return

    label L2wronganswercollege3:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. Introduction{/b}. You may now proceed to Question no. 4."
        $ scoreL2College +=0
        stop sound
        stop music
        jump Question4CollegeL2
    return

    label question3college_slowL2:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}A. Introduction{/b}.
        You may now proceed to Question no. 4."
        $ scoreL2College +=0
        stop sound
        stop music
        jump Question4CollegeL2
    return

    label Question4CollegeL2:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question4college_slowL2'                    ### set where you want to jump once the timer runs out


        Question4College "Identifies the issue that will be discussed and states the author's position on the issue introduction.
        a proposed study is about, why it is being undertaken, and how it will be carried out."
        jump q4collegeL2
    return

    label q4collegeL2:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Conclusions":
                jump L2wronganswercollege4
            "B. Introduction ":
                jump L2correctanswercollege4
            "C. The body of the paper":
                jump L2wronganswercollege4
            "D. None of the above":
                jump L2wronganswercollege4

    return

    label L2correctanswercollege4:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 5."
        $ scoreL2College +=1
        stop sound
        stop music
        jump Question5CollegeL2
    return

    label L2wronganswercollege4:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}B. Introduction {/b}. You may now proceed to Question no. 5."
        $ scoreL2College +=0
        stop sound
        stop music
        jump Question5CollegeL2
    return

    label question4college_slowL2:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}B. Introduction {/b}.
        You may now proceed to Question no. 5."
        $ scoreL2College +=0
        stop sound
        stop music
        jump Question5CollegeL2
    return

    label Question5CollegeL2:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question5college_slowL2'                    ### set where you want to jump once the timer runs out


        Question5College "A _______, restating the key points and, where applicable, suggesting resolutions to the issue.
        a proposed study is about, why it is being undertaken, and how it will be carried out."
        jump q5collegeL2
    return

    label q5collegeL2:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Introduction":
                jump L2wronganswercollege5
            "B. The body of the paper":
                jump L2wronganswercollege5
            "C. Conclusion":
                jump L2correctanswercollege5
            "D. None of the above":
                jump L2wronganswercollege5

    return

    label L2correctanswercollege5:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 6."
        $ scoreL2College +=1
        stop sound
        stop music
        jump Question6CollegeL2
    return

    label L2wronganswercollege5:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}C. Conclusion{/b}. You may now proceed to Question no. 6."
        $ scoreL2College +=0
        stop sound
        stop music
        jump Question6CollegeL2
    return

    label question5college_slowL2:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}C. Conclusion{/b}.
        You may now proceed to Question no. 6."
        $ scoreL2College +=0
        stop sound
        stop music
        jump Question6CollegeL2
    return

    label Question6CollegeL2:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question6college_slowL2'                    ### set where you want to jump once the timer runs out


        Question6College "It contains the central argument and can be further broken up into three unique sections."
        jump q6collegeL2
    return

    label q6collegeL2:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Introduction":
                jump L2correctanswercollege6
            "B. The body of the paper ":
                jump L2correctanswercollege6
            "C. Conclusion":
                jump L2wronganswercollege6
            "D. None of the above":
                jump L2wronganswercollege6

    return

    label L2correctanswercollege6:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 7."
        $ scoreL2College +=1
        stop sound
        stop music
        jump Question7CollegeL2
    return

    label L2wronganswercollege6:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}B. The body of the paper{/b}.
        You may now proceed to Question no. 7."
        $ scoreL2College +=0
        stop sound
        stop music
        jump Question7CollegeL2
    return

    label question6college_slowL2:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}B. The body of the paper{/b}.
        You may now proceed to Question no. 7."
        $ scoreL2College +=0
        stop sound
        stop music
        jump Question7CollegeL2
    return

    label Question7CollegeL2:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question7college_slowL2'                    ### set where you want to jump once the timer runs out


        Question7College "What is the first step to start writing a position paper?."
        jump q7collegeL2
    return

    label q7collegeL2:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Introduction":
                jump L2wronganswercollege7
            "B. Conclusions  ":
                jump L2wronganswercollege7
            "C. Selecting a Topic ":
                jump L2correctanswercollege7
            "D. The Body of the paper":
                jump L2wronganswercollege7

    return

    label L2correctanswercollege7:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 8."
        $ scoreL2College +=1
        stop sound
        stop music
        jump Question8CollegeL2
    return

    label L2wronganswercollege7:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}C. Selecting a Topic{/b}.
        You may now proceed to Question no. 8."
        $ scoreL2College +=0
        stop sound
        stop music
        jump Question8CollegeL2
    return

    label question7college_slowL2:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}C. Selecting a Topic{/b}.
        You may now proceed to Question no. 8."
        $ scoreL2College +=0
        stop sound
        stop music
        jump Question8CollegeL2
    return

    label Question8CollegeL2:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question8college_slowL2'                    ### set where you want to jump once the timer runs out


        Question8College "Position paper has _________ Main Elements.
        a proposed study is about, why it is being undertaken, and how it will be carried out."
        jump q8collegeL2
    return

    label q8collegeL2:

        show screen countdown                          ### call and start the timer

        menu:

            "A. One (1)":
                jump L2wronganswercollege8
            "B. Two (2)":
                jump L2wronganswercollege8
            "C. Three (3)":
                jump L2correctanswercollege8
            "D. Four (4)":
                jump L2wronganswercollege8

    return

    label L2correctanswercollege8:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 9."
        $ scoreL2College +=1
        stop sound
        stop music
        jump Question9CollegeL2
    return

    label L2wronganswercollege8:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}C. Three (3){/b}. You may now proceed to Question no. 9."
        $ scoreL2College +=0
        stop sound
        stop music
        jump Question9CollegeL2
    return

    label question8college_slowL2:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}C. Three (3){/b}.
        You may now proceed to Question no. 9."
        $ scoreL2College +=0
        stop sound
        stop music
        jump Question9CollegeL2
    return

    label Question9CollegeL2:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question9college_slowL2'                    ### set where you want to jump once the timer runs out


        Question9College "Introduction is part of position paper."
        jump q9collegeL2
    return

    label q9collegeL2:

        show screen countdown                          ### call and start the timer

        menu:

            "A. True ":
                jump L2correctanswercollege9
            "B. False ":
                jump L2wronganswercollege9
            "C. Maybe":
                jump L2wronganswercollege9
            "D. None of the Above":
                jump L2wronganswercollege9

    return

    label L2correctanswercollege9:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 10."
        $ scoreL2College +=1
        stop sound
        stop music
        jump Question10CollegeL2
    return

    label L2wronganswercollege9:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. True{/b}. You may now proceed to Question no. 10."
        $ scoreL2College +=0
        stop sound
        stop music
        jump Question10CollegeL2
    return

    label question9college_slowL2:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}A. True{/b}. You may now proceed to Question no. 10."
        $ scoreL2College +=0
        stop sound
        stop music
        jump Question10CollegeL2
    return

    label Question10CollegeL2:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question10college_slowL2'                    ### set where you want to jump once the timer runs out


        Question10College "What is the name of Lesson 2?"
        jump q10collegeL2
    return

    label q10collegeL2:

        show screen countdown                          ### call and start the timer

        menu:

            "A. Reaction Paper ":
                jump L2wronganswercollege10
            "B. Review Paper":
                jump L2wronganswercollege10
            "C. Note Taking":
                jump L2wronganswercollege10
            "D. Position Paper (Part 1).":
                jump L2correctanswercollege10

    return

    label L2correctanswercollege10:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! And this is the end of the quiz, let us
        now see the results."
        $ scoreL2College +=1
        stop sound
        stop music
        jump ResultsCollege2
    return

    label L2wronganswercollege10:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}D. Position Paper (Part 1){/b}.
        And this is the end of the quiz, let us now see the results."
        $ scoreL2College +=0
        stop sound
        stop music
        jump ResultsCollege2
    return

    label question1college_slow2:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}D. Position Paper (Part 1){/b}.
        And this is the end of the quiz, let us now see the results."
        $ scoreL2College +=0
        stop sound
        stop music
        jump ResultsCollege2
    return

    label ResultsCollege2:
        show classroomshs

        if scoreL2College == 0:
            "Out of 10 questions, [playername] have answered {b}[scoreL2College]{/b}(0 percent) questions.
            Unfortunately, you have failed this quiz. Please study the lesson again."

            hide classroomshs

            jump L2College

        if scoreL2College == 1:
            "Out of 10 questions, [playername] have answered {b}[scoreL2College]{/b}(10 percent) questions.
            Unfortunately, you have failed this quiz. Please study the lesson again."

            hide classroomshs

            jump L2College

        if scoreL2College == 2:
            "Out of 10 questions, [playername] have answered {b}[scoreL2College]{/b}(20 percent) questions.
            Unfortunately, you have failed this quiz. Please study the lesson again."

            hide classroomshs

            jump L2College

        if scoreL2College == 3:
            "Out of 10 questions, [playername] have answered {b}[scoreL2College]{/b}(30 percent) questions.
            Unfortunately, you have failed this quiz. Please study the lesson again."

            hide classroomshs

            jump L2College

        if scoreL2College == 4:
            "Out of 10 questions, [playername] have answered {b}[scoreL2College]{/b}(40 percent) questions.
            Unfortunately, you have failed this quiz. Please study the lesson again."

            hide classroomshs

            jump L2College

        if scoreL2College == 5:
            "Out of 10 questions, [playername] answered {b}[scoreL2College]{/b} (50 percent)
            questions. Congratulations, [playername]. You passed in this quiz. Great job!"

            hide classroomshs

            jump EndingCollege

        if scoreL2College == 6:
            "Out of 10 questions, [playername] answered {b}[scoreL2College]{/b} (60 percent)
            questions. Congratulations, [playername]. You passed in this quiz. Great job!"

            hide classroomshs

            jump EndingCollege

        if scoreL2College == 7:
            "Out of 10 questions, [playername] answered {b}[scoreL2College]{/b} (70 percent)
            questions. Congratulations, [playername]. You passed in this quiz. Great job!"

            hide classroomshs

            jump EndingCollege

        if scoreL2College == 8:
            "Out of 10 questions, [playername] answered {b}[scoreL2College]{/b} (80 percent)
            questions. Congratulations, [playername]. You passed in this quiz. Great job!"

            hide classroomshs

            jump EndingCollege

        if scoreL2College == 9:
            "Out of 10 questions, [playername] answered {b}[scoreL2College]{/b} (90 percent)
            questions. Congratulations, [playername]. You passed in this quiz. Great job!"

            hide classroomshs

            jump EndingCollege


        if scoreL2College == 10:
            "Out of 10 questions, [playername] answered {b}[scoreL2College]{/b} (100 percent)
            questions. Congratulations, [playername]. You passed in this quiz. Great job!"

            hide classroomshs

            jump EndingCollege

    label L3College:
        stop music

        $renpy.music.play("audio/DLJ - Deep Sleep ft. TABAL.mp3", loop=True)

        hide Bedroom

        show screen gameUICollege3

        $L3CollegeProgress = 0

        show L3College

        window hide

        pause

        hide L3College

        $L3CollegeProgress += 20


        show L3College2

        window hide

        pause

        hide L3College2

        $L3CollegeProgress += 20


        show L3College3

        window hide

        pause

        hide L3College3

        $L3CollegeProgress += 60


        show L3College4

        window hide

        pause

        hide L3College4

        stop music

        show black

        hide screen gameUICollege3

        "You have finally finished reading the lesson. You will now proceed to the quiz part."

        jump quizdayCollege3

    return

    label quizdayCollege3:

        $renpy.music.play("audio/The 126ers - End Of Summer Instrumental Extended.mp3", loop=True)

        show classroomshs

        show TeacherLuna

        teacherluna "Good morning, students. Today is your quiz day. Once I gave the quiz sheets to all of you,
        you may now start answering the questions provided. Do your best and good luck."

        hide TeacherLuna

        "Teacher Luna gave the quiz sheets to the students."

        "Okay, player. I will present to you the mechanics of this game so please read and follow the
        mechanics of this game. Thank you."

        hide classroomshs

        show Mechanics1

        window hide

        pause

        hide Mechanics1

        show Mechanics2

        window hide

        pause

        hide Mechanics2

        show classroomshs

        show TeacherLuna

        teacherluna "Okay, you may now start answering."

        hide TeacherLuna

        "Since you are about to take the quiz, you won't hear any background music until the end of the quiz."

        "That is because usually, when you take your in school, you have to take it quietly."

        stop music

    jump Question1CollegeL3

    label Question1CollegeL3:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question1college_slowL3'                    ### set where you want to jump once the timer runs out


        Question1College "To take a side on a subject, you should first establish the_____ of a topic that interests you."
        jump q1collegeL3
    return

    label q1collegeL3:

        show screen countdown                          ### call and start the time

        menu:
            "A. Arguability":
                call L3correctanswercollege1
            "B. Controversy":
                call L3wronganswercollege1
            "C. Advocating":
                call L3wronganswercollege1
            "D. Distinctive":
                call L3wronganswercollege1
    return

    label L3wronganswercollege1:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}A. Arguability{/b}.
        You may now proceed to Question no. 2."
        $ scoreL3College +=0
        stop sound
        stop music
        jump Question2CollegeL3
    return

    label L3correctanswercollege1:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! And this is the end of the quiz, let us
        now see the results. You may now proceed to Question no. 2."
        $ scoreL3College +=1
        stop sound
        stop music
        jump Question2CollegeL3
    return

    label question1college_slowL3:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}A. Arguability{/b}.
        You may now proceed to Question no. 2."
        $ scoreL3College +=0
        stop sound
        stop music
        jump Question2CollegeL3
    return

    label Question2CollegeL3:
        $ time = 10                                     ### set variable time to 3
        $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
        $ timer_jump = 'question2college_slowL3'                    ### set where you want to jump once the timer runs out


        Question2College " It is a real issue, with genuine ____ and uncertainty."
        jump q2collegeL3
    return

    label q2collegeL3:

        show screen countdown                          ### call and start the timer

        menu:
            "A. Arguability":
                call L3wronganswercollege2
            "B. Controversy":
                call L3correctanswercollege2
            "C. Advocating":
                call L3wronganswercollege2
            "D. Distinctive":
                call L3wronganswercollege2
    return


    label L3wronganswercollege2:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}B. Controversy{/b}.
        You may now proceed to Question no. 3."
        $ scoreL3College +=0
        stop sound
        stop music
        jump Question3CollegeL3
    return

    label L3correctanswercollege2:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 3."
        $ scoreL3College +=1
        stop sound
        stop music
        jump Question3CollegeL3

    return

    label question2college_slowL3:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}B. Controversy{/b}.
        You may now proceed to Question no. 3."
        $ scoreL3College +=0
        stop sound
        stop music
        jump Question3CollegeL3
    return

    label Question3CollegeL3:
            $ time = 10                                     ### set variable time to 3
            $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
            $ timer_jump = 'question3college_slowL3'                    ### set where you want to jump once the timer runs out


            Question3College "Which of the following does not teach you how to write a conclusion
            for a position paper?"
            jump q3collegeL3
    return

    label q3collegeL3:

        show screen countdown                          ### call and start the timer

        menu:

                "A. Restate your topic and why it is important":
                    call L3wronganswercollege3
                "B. Restate your thesis/claim":
                    call L3wronganswercollege3
                "C. Address opposing viewpoints and explain why readers should align with your
                position":
                    call L3wronganswercollege3
                "D. Create a Reaction Paper on your Position Paper":
                    call L3correctanswercollege3

        return

    label L3wronganswercollege3:
            hide screen countdown
            play sound "audio/Wrong Answer sfx.mp3"
            "Your answer is incorrect. The correct answer is {b}D. Create a Reaction Paper on your Position Paper{/b}.
            You may now proceed to Question no. 4."
            $ scoreL3College +=0
            stop sound
            stop music
            jump Question4CollegeL3
    return

    label L3correctanswercollege3:
            hide screen countdown
            play sound "audio/Correct Answer sfx.mp3"
            "Your answer is correct! You may now proceed to Question no. 4."
            $ scoreL3College +=1
            stop sound
            stop music
            jump Question4CollegeL3
    return

    label question3college_slowL3:
            play sound "audio/Time Distortion sfx.mp3"
            "Unfortunately, you ran out of time. The correct answer is {b}D. Create a Reaction Paper on
            your Position Paper{/b}. You may now proceed to Question no. 4."
            $ scoreL3College +=0
            stop sound
            stop music
            jump Question4CollegeL3
    return

    label Question4CollegeL3:
            $ time = 10                                     ### set variable time to 3
            $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
            $ timer_jump = 'question4college_slowL3'                    ### set where you want to jump once the timer runs out


            Question4College "The goal of the position paper is to convince the audience
            that your opinion is valid and defensible."
            jump q4collegeL3
    return

    label q4collegeL3:

        show screen countdown                          ### call and start the timer
        menu:

                "A. True":
                    call L3correctanswercollege4
                "B. False":
                    call L3wronganswercollege4
                "C. Maybe":
                    call L3wronganswercollege4
                "D. No Idea":
                    call L3wronganswercollege4

        return

    label L3wronganswercollege4:
            hide screen countdown
            play sound "audio/Wrong Answer sfx.mp3"
            "Your answer is incorrect. The correct answer is {b}A. True{/b}.
            You may now proceed to Question no. 5."
            $ scoreL3College +=0
            stop sound
            stop music
            jump Question5CollegeL3
    return

    label L3correctanswercollege4:
            hide screen countdown
            play sound "audio/Correct Answer sfx.mp3"
            "Your answer is correct! You may now proceed to Question no. 5."
            $ scoreL3College +=1
            stop sound
            stop music
            jump Question5CollegeL3
    return

    label question4college_slowL3:
            play sound "audio/Time Distortion sfx.mp3"
            "Unfortunately, you ran out of time. The correct answer is {b}A. True{/b}.
            You may now proceed to Question no. 5."
            $ scoreL3College +=0
            stop sound
            stop music
            jump Question5CollegeL3
    return

    label Question5CollegeL3:
            $ time = 10                                     ### set variable time to 3
            $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
            $ timer_jump = 'question5college_slowL3'                    ### set where you want to jump once the timer runs out


            Question5College "Which of the following does not teach you how to write a conclusion
            for a position paper?"
            jump q5collegeL3
    return

    label q5collegeL3:

        show screen countdown                          ### call and start the timer

        menu:
            "A. Restate your topic and why it is important":
                call L3wronganswercollege5
            "B. Restate your thesis/claim":
                call L3wronganswercollege5
            "C. Address opposing viewpoints and explain why readers should align with your
                position":
                call L3wronganswercollege5
            "D. Create a Reaction Paper on your Position Paper":
                call L3correctanswercollege5

        return

    label L3wronganswercollege5:
            hide screen countdown
            play sound "audio/Wrong Answer sfx.mp3"
            "Your answer is incorrect. The correct answer is {b}D. Create a Reaction Paper on your Position Paper{/b}.
            You may now proceed to Question no. 6."
            $ scoreL3College +=0
            stop sound
            stop music
            jump Question6CollegeL3
    return

    label L3correctanswercollege5:
            hide screen countdown
            play sound "audio/Correct Answer sfx.mp3"
            "Your answer is correct! You may now proceed to Question no. 6."
            $ scoreL3College +=1
            stop sound
            stop music
            jump Question6CollegeL3
    return

    label question5college_slowL5:
            play sound "audio/Time Distortion sfx.mp3"
            "Unfortunately, you ran out of time. The correct answer is {b}D. Create a Reaction Paper on your Position Paper{/b}.
            You may now proceed to Question no. 6."
            $ scoreL3College +=0
            stop sound
            stop music
            jump Question6CollegeL3
    return

    label Question6CollegeL3:
            $ time = 10                                     ### set variable time to 3
            $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
            $ timer_jump = 'question6college_slowL3'                    ### set where you want to jump once the timer runs out


            Question6College "The goal of the position paper is to convince the audience
            that your opinion is valid and defensible."
            jump q6collegeL3
    return

    label q6collegeL3:

        show screen countdown                          ### call and start the timer

        menu:
            "A. True":
                call L3correctanswercollege6
            "B. False":
                call L3wronganswercollege6
            "C. Maybe":
                call L3wronganswercollege6
            "D. No Idea":
                call L3wronganswercollege6

        return

    label L3wronganswercollege6:
            hide screen countdown
            play sound "audio/Wrong Answer sfx.mp3"
            "Your answer is incorrect. The correct answer is {b}A. True{/b}.
            You may now proceed to Question no. 7."
            $ scoreL3College +=0
            stop sound
            stop music
            jump Question7CollegeL3
    return

    label L3correctanswercollege6:
            hide screen countdown
            play sound "audio/Correct Answer sfx.mp3"
            "Your answer is correct! You may now proceed to Question no. 7."
            $ scoreL3College +=1
            stop sound
            stop music
            jump Question7CollegeL3

    return

    label question6college_slowL3:
            play sound "audio/Time Distortion sfx.mp3"
            "Unfortunately, you ran out of time. The correct answer is {b}A. True{/b}.
            You may now proceed to Question no. 7."
            $ scoreL3College +=0
            stop sound
            stop music
            jump Question7CollegeL3

    return

    label Question7CollegeL3:
                $ time = 10                                     ### set variable time to 3
                $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
                $ timer_jump = 'question7college_slowL3'                    ### set where you want to jump once the timer runs out


                Question7College "Your job is to take two side of the argument and
                persuade your audience that you have well-founded knowledge of the topic being presented."
                jump q7collegeL3
    return

    label q7collegeL3:

        show screen countdown                          ### call and start the timer

        menu:
            "A. True":
                call L3wronganswercollege7
            "B. False":
                call L3correctanswercollege7
            "C. Maybe":
                call L3wronganswercollege7
            "D. No Idea":
                call L3wronganswercollege7

    return

    label L3wronganswercollege7:
        hide screen countdown
        play sound "audio/Wrong Answer sfx.mp3"
        "Your answer is incorrect. The correct answer is {b}B. False{/b}.
        You may now proceed to Question no. 8."
        $ scoreL3College +=0
        stop sound
        stop music
        jump Question8CollegeL3

    return

    label L3correctanswercollege7:
        hide screen countdown
        play sound "audio/Correct Answer sfx.mp3"
        "Your answer is correct! You may now proceed to Question no. 8."
        $ scoreL3College +=1
        stop sound
        stop music
        jump Question8CollegeL3

    return

    label question7college_slowL3:
        play sound "audio/Time Distortion sfx.mp3"
        "Unfortunately, you ran out of time. The correct answer is {b}B. False{/b}.
        You may now proceed to Question no. 8."
        $ scoreL3College +=0
        stop sound
        stop music
        jump Question8CollegeL3

    return

    label Question8CollegeL3:
         $ time = 10                                     ### set variable time to 3
         $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
         $ timer_jump = 'question8college_slowL3'                    ### set where you want to jump once the timer runs out

         Question8College "It is important to support your argument with evidence to ensure the validity of your claim."
         jump q8collegeL3

    return

    label q8collegeL3:

        show screen countdown                          ### call and start the timer

        menu:
            "A. True":
                call L3correctanswercollege8
            "B. False":
                call L3wronganswercollege8
            "C. Maybe":
                call L3wronganswercollege8
            "D. No Idea":
                call L3wronganswercollege8

    return

    label L3wronganswercollege8:
                hide screen countdown
                play sound "audio/Wrong Answer sfx.mp3"
                "Your answer is incorrect. The correct answer is {b}A. True{/b}.
                You may now proceed to Question no. 9."
                $ scoreL3College +=0
                stop sound
                stop music
                jump Question9CollegeL3
    return

    label L3correctanswercollege8:
                hide screen countdown
                play sound "audio/Correct Answer sfx.mp3"
                "Your answer is correct! You may now proceed to Question no. 9."
                $ scoreL3College +=1
                stop sound
                stop music
                jump Question9CollegeL3
    return

    label question8college_slowL3:
                play sound "audio/Time Distortion sfx.mp3"
                "Unfortunately, you ran out of time. The correct answer is {b}A. True{/b}.
                You may now proceed to Question no. 9."
                $ scoreL3College +=0
                stop sound
                stop music
                jump Question9CollegeL3
    return

    label Question9CollegeL3:
         $ time = 10                                     ### set variable time to 3
         $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
         $ timer_jump = 'question9college_slowL3'                    ### set where you want to jump once the timer runs out

         Question9College "It is very not important to ensure that you are addressing all sides of the issue and presenting
         it in a manner that is easy for you audience to understand."
         jump q9collegeL3

    return

    label q9collegeL3:

        show screen countdown                          ### call and start the timer

        menu:
            "A. True":
                call L3wronganswercollege9
            "B. False":
                call L3correctanswercollege9
            "C. Maybe":
                call L3wronganswercollege9
            "D. No Idea":
                call L3wronganswercollege9

    return

    label L3wronganswercollege9:
                hide screen countdown
                play sound "audio/Wrong Answer sfx.mp3"
                "Your answer is incorrect. The correct answer is {b}B. False{/b}.
                You may now proceed to Question no. 10."
                $ scoreL3College +=0
                stop sound
                stop music
                jump Question10CollegeL3
    return

    label L3correctanswercollege9:
                hide screen countdown
                play sound "audio/Correct Answer sfx.mp3"
                "Your answer is correct! You may now proceed to Question no. 10."
                $ scoreL3College +=1
                stop sound
                stop music
                jump Question10CollegeL3
    return

    label question9college_slowL3:
                play sound "audio/Time Distortion sfx.mp3"
                "Unfortunately, you ran out of time. The correct answer is {b}B. False{/b}.
                You may now proceed to Question no. 10."
                $ scoreL3College +=0
                stop sound
                stop music
                jump Question10CollegeL3
    return

    label Question10CollegeL3:
         $ time = 10                                     ### set variable time to 3
         $ timer_range = 10                              ### set variable timer_range to 3 (this is for purposes of showing a bar)
         $ timer_jump = 'question10college_slowL3'                    ### set where you want to jump once the timer runs out

         Question10College "The goal of a position paper is not to convince the audience that your opinion
         is valid and defensible."
         jump q10collegeL3

    return

    label q10collegeL3:

        show screen countdown                          ### call and start the timer

        menu:
            "A. True":
                call L3wronganswercollege10
            "B. False":
                call L3correctanswercollege10
            "C. Maybe":
                call L3wronganswercollege10
            "D. No Idea":
                call L3wronganswercollege10

    return

    label L3wronganswercollege10:
                hide screen countdown
                play sound "audio/Wrong Answer sfx.mp3"
                "Your answer is incorrect. The correct answer is {b}B. False{/b}.
                And this is the end of the quiz, let us now see the results."
                $ scoreL3College +=0
                stop sound
                stop music
                jump ResultsCollege3
    return

    label L3correctanswercollege10:
                hide screen countdown
                play sound "audio/Correct Answer sfx.mp3"
                "Your answer is correct! And this is the end of the quiz, let us
                now see the results."
                $ scoreL3College +=1
                stop sound
                stop music
                jump ResultsCollege3
    return

    label question10college_slowL3:
                play sound "audio/Time Distortion sfx.mp3"
                "Unfortunately, you ran out of time. The correct answer is {b}B. False{/b}.
                And this is the end of the quiz, let us now see the results."
                $ scoreL3College +=0
                stop sound
                stop music
                jump ResultsCollege3
    return

    label ResultsCollege3:
        show classroomshs

        if scoreL3College == 0:
            "Out of 10 questions, [playername] have answered {b}[scoreL3College]{/b}(0 percent) questions.
            Unfortunately, you have failed this quiz. Please study the lesson again."

            hide classroomshs

            jump L3College

        if scoreL3College == 1:
            "Out of 10 questions, [playername] have answered {b}[scoreL3College]{/b}(10 percent) questions.
            Unfortunately, you have failed this quiz. Please study the lesson again."

            hide classroomshs

            jump L3College

        if scoreL3College== 2:
            "Out of 10 questions, [playername] have answered {b}[scoreL3College]{/b}(20 percent) questions.
            Unfortunately, you have failed this quiz. Please study the lesson again."

            hide classroomshs

            jump L3College

        if scoreL3College == 3:
            "Out of 10 questions, [playername] have answered {b}[scoreL3College]{/b}(30 percent) questions.
            Unfortunately, you have failed this quiz. Please study the lesson again."

            hide classroomshs

            jump L3College

        if scoreL3College == 4:
            "Out of 10 questions, [playername] have answered {b}[scoreL3College]{/b}(40 percent) questions.
            Unfortunately, you have failed this quiz. Please study the lesson again."

            hide classroomshs

            jump L3College

        if scoreL3College == 5:
            "Out of 10 questions, [playername] answered {b}[scoreL3College]{/b} (50 percent)
            questions. Congratulations, [playername]. You passed in this quiz. Great job!"

            hide classroomshs

            jump EndingCollege

        if scoreL3College == 6:
            "Out of 10 questions, [playername] answered {b}[scoreL3College]{/b} (60 percent)
            questions. Congratulations, [playername]. You passed in this quiz. Great job!"

            hide classroomshs

            jump EndingCollege

        if scoreL3College == 7:
            "Out of 10 questions, [playername] answered {b}[scoreL3College]{/b} (70 percent)
            questions. Congratulations, [playername]. You passed in this quiz. Great job!"

            hide classroomshs

            jump EndingCollege

        if scoreL3College == 8:
            "Out of 10 questions, [playername] answered {b}[scoreL3College]{/b} (80 percent)
            questions. Congratulations, [playername]. You passed in this quiz. Great job!"

            hide classroomshs

            jump EndingCollege

        if scoreL3College == 9:
            "Out of 10 questions, [playername] answered {b}[scoreL3College]{/b} (90 percent)
            questions. Congratulations, [playername]. You passed in this quiz. Great job!"

            hide classroomshs

            jump EndingCollege


        if scoreL3College == 10:
            "Out of 10 questions, [playername] answered {b}[scoreL3College]{/b} (100 percent)
            questions. Congratulations, [playername]. You passed in this quiz. Great job!"

            hide classroomshs

            jump EndingCollege

    label EndingCollege:
        $renpy.music.play("audio/The 126ers - End Of Summer Instrumental Extended.mp3", loop=True)

        show classroomshs

        show TeacherLuna

        teacherluna "The quiz is over. You may now pass your paper."

        hide TeacherLuna

        "The students put their paper on the teacher's table. Afterwards, they returned to their seats and waited for
        the quiz results."

        "A few minutes later."

        show TeacherLuna

        teacherluna "Congratulations to all of you
        in this class for doing their best for today's quiz. Let's give ourselves a round of applause."

        hide TeacherLuna

        "The students gave theirselves a round of applause."

        show Mark

        mark "Yeah! We did it."

        hide Mark

        playername "That's right. Our time spent in studying for this quiz has finally paid off."

        show Mark

        mark "Anyway, we'll talk more about it later."

        hide Mark

        show Adrian

        adrian "Alright, then. For now, let us celebrate our own victory."

        hide Adrian

        show TeacherLuna

        teacherluna "And so our class ends today. See you tomorrow."

        hide TeacherLuna

        "Teacher Luna left the classroom."

        "After a few hours, their school has finally ended."

        hide classroomshs

        show campus

        show Mark

        mark "Before we head to the diner, I forgot to tell you something."

        hide Mark

        show Christian

        christian "What is it, Matthew?"

        hide Christian

        show Mark

        mark "Well, I forgot to tell you that since I made the agreement yesterday, I will be the one to treat
        you all there."

        hide Mark

        show Adrian

        adrian "That's a good idea, Mark! Your timing is perfect because actually..."

        adrian "I don't have enough money to eat at the diner so I will accept your treat."

        hide Adrian

        show Mark

        mark "Don't worry, man. I got this."

        hide Mark

        show Christian

        christian "Anyway, thank you for giving me a wonderful advice when I was at my lowest yesterday."

        hide Christian

        show Mark

        mark "You're welcome, man. That's what friends are for."

        mark "So what are we waiting for? Let's go!"

        hide Mark

        "And they went to the diner to have fun eating the best food and drinking the best drink."

        hide campus

        show black

        "Before the game ends, we would like to give our big thanks to sir Gerald for being the best thesis adviser
        that we ever had. He has always been there for us when we need him the most when it comes to advice or guide,
        testing our game, and many more."

        "We wish him all the best. Our respect is big for him."

        "We would also like to give our big thanks in advance to those who will play this game and to those who will
        support us in developing this game because if not because of your support, we won't be able to develop this game
        with our own heart and soul."

        "Until then, goodbye."

        hide black

        show TheEnd

        window hide

        pause

        hide TheEnd

    return
