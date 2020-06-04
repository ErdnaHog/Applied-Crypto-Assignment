from main import mainframe, font_family, my_file_path, button_colour
from subpages import clear_screen
from tkinter import Frame, Label, PhotoImage, Button, FLAT, IntVar, Radiobutton
from tkinter.messagebox import askyesno
from PIL import Image, ImageTk
import os  # * for file path
import random  # * for random question generation

# * Local Variables
questions = [
    "If we want to ensure the principle _____, the contents of a message must not be modified while transit.",
    "What is one of the characteristic of reference monitor ?",
    "What is one of the approach to implement a security model ?",
    "What is one of the key characteristics of a good security policy ?",
    "In ____ attacks, there is no modification to message contents",
]

answer_choice = [
    ["Confidentiality", "Authentication", "Integrity", "Access Control", ],
    ["Should always Invoke", "Should be big enough",
        "Should have strong processing power", "Should be compromised", ],
    ["Confidentiality", "Integrity", "Strong Security", "No Security", ],
    ["Confidentiality", "Functionality", "Integrity", "Access Control", ],
    ["Passive", "Active", "Both of the above", "None of the above", ],
]

correct_answers = [2, 0, 3, 1, 0]

indexes = []


class Quiz:
    def quiz_page():
        clear_screen(mainframe)

        # * Landing Page Frame
        landing_page_frame = Frame(mainframe, bg="#ffffff")
        landing_page_frame.grid(row=0, column=0)
        # * Loading images to make it look nicer
        img1 = ImageTk.PhotoImage(Image.open(os.path.join(
            my_file_path, "resources", "infosec.jpg")).resize((550, 366)))
        img2 = ImageTk.PhotoImage(Image.open(os.path.join(
            my_file_path, "resources", "img2.png")).resize((474, 150)))

        # * Label Title
        Label(landing_page_frame, text="Quiz", font=(
            font_family, 30, "bold"), background="#ffffff").grid(row=0, column=0, pady=5)
        # * Label image
        label_image = Label(landing_page_frame, image=img1,
                            background="#ffffff")
        label_image.image = img1
        label_image.grid(row=1, column=0, pady=15)
        # * Start Button
        start_button = Button(landing_page_frame, image=img2, background="#ffffff",
                              relief=FLAT, border=0, command=lambda: Quiz.startIsPressed(landing_page_frame))
        start_button.image = img2
        start_button.grid(row=2, column=0)

    def gen(num_questions):
        global indexes
        # ? changing value will change number of questions generated
        while len(indexes) < 5:
            x = random.randint(0, num_questions)
            if x in indexes:
                continue
            else:
                indexes.append(x)

    def start_quiz():
        global quiz_frame
        quiz_frame = Frame(mainframe, bg="#ffffff")
        quiz_frame.grid(row=0, column=0)

        # * 1 frame per question
        question1_frame = Frame(quiz_frame, bg="#ffffff")
        question2_frame = Frame(quiz_frame, bg="#ffffff")
        question3_frame = Frame(quiz_frame, bg="#ffffff")
        submit_button_frame = Frame(quiz_frame, bg="#ffffff")
        global result_frame, answer_frame_list
        result_frame = Frame(quiz_frame, bg="#ffffff")
        answer1_frame = Frame(quiz_frame, bg="#ffffff")
        answer2_frame = Frame(quiz_frame, bg="#ffffff")
        answer3_frame = Frame(quiz_frame, bg="#ffffff")
        answer_frame_list = [answer1_frame, answer2_frame, answer3_frame]

        question_frame_list = [question1_frame,
                               question2_frame, question3_frame]

        # * tkinter variables
        answer1 = IntVar()
        answer2 = IntVar()
        answer3 = IntVar()

        radio_variable_list = [answer1, answer2, answer3]

        for j in range(3):
            question_frame_list[j].grid(row=j, column=0, padx=20)
            radio_variable_list[j].set(-1)
            Label(
                question_frame_list[j],
                text=questions[indexes[j]],
                font=(font_family, 15),
                wraplength=750,
                background="#ffffff"
            ).grid(row=0, column=0, pady=10)

            for i in range(4):
                Radiobutton(
                    question_frame_list[j],
                    text=answer_choice[indexes[j]][i],
                    font=(font_family, 12),
                    value=i,
                    variable=radio_variable_list[j],
                    background="#ffffff"
                ).grid(row=i+1, column=0)

        submit_button_frame.grid(row=4, column=0, pady=10)

        Button(
            submit_button_frame,
            text="Submit",
            font=(font_family, 20),
            background=button_colour,
            command=lambda: Quiz.check_answer(
                radio_variable_list, submit_button_frame)
        ).grid(row=0, column=0)

    def check_answer(radio_variable_list, submit_button_frame):
        answered_all = True
        for var in radio_variable_list:
            if var.get() == -1:
                answered_all = False
                break
        if not answered_all:
            result = askyesno(title="Submit Answers",
                              message="Not all questions are answered. Do you want to proceed?")
        else:
            result = askyesno(title="Submit Answers",
                              message="Do you want to proceed?")

        if result:
            list_of_correct = []
            for i in range(len(radio_variable_list)):
                user_answer = radio_variable_list[i].get()
                correct_answer = correct_answers[indexes[i]]
                answer_frame = answer_frame_list[i]
                answer_frame.grid(row=i, column=1, padx=20)
                if user_answer == correct_answer:
                    list_of_correct.append("correct")
                    Label(answer_frame, text="Correct",
                          fg="green", font=(font_family, 12), background="#ffffff").grid(row=0, column=0)
                else:
                    list_of_correct.append("wrong")
                    correct_answer_word = answer_choice[indexes[i]
                                                        ][correct_answer]
                    Label(answer_frame, text="Incorrect",
                          fg="red", font=(font_family, 12), background="#ffffff").grid(row=0, column=0)
                    Label(answer_frame, text=f"Correct answer is: {correct_answer_word}", font=(
                        font_family, 12), background="#ffffff").grid(row=1, column=0)

            submit_button_frame.destroy()
            score = 0
            for correct in list_of_correct:
                if correct == "correct":
                    score += 1
            Quiz.show_result(score)

    def show_result(result):
        result_frame.grid(row=5, column=0, columnspan=2)
        Label(
            result_frame,
            text=f"Your result is {result}/3",
            font=(font_family, 20),
            background="#ffffff"
        ).grid(row=0, column=0, columnspan=2, pady=10)
        Button(result_frame, text="Main Page", font=(font_family, 20),
               background=button_colour, command=Quiz.quiz_page).grid(row=1, column=0, padx=5, pady=5)
        Button(result_frame, text="Try Again", font=(font_family, 20), background=button_colour,
               command=lambda: Quiz.startIsPressed(quiz_frame)).grid(row=1, column=1, padx=5, pady=5)

    def startIsPressed(landing_page_frame):
        landing_page_frame.destroy()
        Quiz.gen(len(questions)-1)
        Quiz.start_quiz()
