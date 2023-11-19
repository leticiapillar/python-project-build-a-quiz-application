# Example file for LinkedIn Learning Course "Python: Build a Quiz App" by Joe Marini
# QuizParser builds a quiz from a source file
import xml.sax
from quiz import *
from enum import Enum, unique


@unique
class QuizParserState(Enum):
    IDLE = 0
    PARSE_QUIZ = 1
    PARSE_DESCRIPTION = 2
    PARSE_QUESTION = 3
    PARSE_QUEST_TEXT = 4
    PARSE_ANSWER = 5


class QuizParser(xml.sax.ContentHandler):
    """
    The QuizParser class loads a particular quiz file, parses it, and returns
    a fully-built Quiz object that can then be presented to the user.
    """

    def __init__(self):
        self.new_quiz = Quiz()
        #TODO: properties for the parser state and current question and answer
        self._parse_state = QuizParserState.IDLE
        self._current_question = None
        self._current_answer = None

    def parse_quiz(self, quizpath):
        # load the file contents
        quiztext = ""
        with open(quizpath, "r") as quizfile:
            if quizfile.mode == "r":
                quiztext = quizfile.read()

        #TODO: parse the file
        xml.sax.parseString(quiztext, self)

        # return the finished quiz
        return self.new_quiz

    def startElement(self, tagname, attrs):
        # if tagname == "QuizML":
        #     self._parse_state = QuizParserState.PARSE_QUIZ
        #     self.new_quiz.name = attrs["name"]
        # #TODO: process the rest of the tags
        # elif tagname == "Description":
        #     self._parse_state = QuizParserState.PARSE_DESCRIPTION
        # elif tagname == "Question":
        #     self._parse_state = QuizParserState.PARSE_QUESTION
        #     if attrs["type"] == "multichoice":
        #         self._current_question = QuestionMC()
        #     elif attrs["type"] == "tf":
        #         self._current_question = QuestionTF()
        #     self._current_question.points = int(attrs["points"])
        #     self.new_quiz.total_points += self._current_question.points
        # elif tagname == "QuestionText":
        #     self._parse_state = QuizParserState.PARSE_QUEST_TEXT
        #     self._current_question.correct_answer = attrs["answer"]
        # elif tagname == "Answer":
        #     self._parse_state = QuizParserState.PARSE_ANSWER
        #     self._current_answer = Answer()
        #     self._current_answer.name = attrs["name"]
        
        match tagname:
            case "QuizML":
                self._parse_state = QuizParserState.PARSE_QUIZ
                self.new_quiz.name = attrs["name"]
            case "Description":
                self._parse_state = QuizParserState.PARSE_DESCRIPTION
            case "Question":
                self._parse_state = QuizParserState.PARSE_QUESTION
                if attrs["type"] == "multichoice":
                    self._current_question = QuestionMC()
                elif attrs["type"] == "tf":
                    self._current_question = QuestionTF()
                self._current_question.points = int(attrs["points"])
                self.new_quiz.total_points += self._current_question.points
            case "QuestionText":
                self._parse_state = QuizParserState.PARSE_QUEST_TEXT
                self._current_question.correct_answer = attrs["answer"]
            case "Answer":
                self._parse_state = QuizParserState.PARSE_ANSWER
                self._current_answer = Answer()
                self._current_answer.name = attrs["name"]


    def endElement(self, tagname):
        # if tagname == "QuizML":
        #     self._parse_state = QuizParserState.IDLE
        # #TODO: process the rest of the tags
        # elif tagname == "Description":
        #     self._parse_state = QuizParserState.PARSE_QUIZ
        # elif tagname == "Question":
        #     self._parse_state = QuizParserState.PARSE_QUIZ
        #     self.new_quiz.questions.append(self._current_question)
        # elif tagname == "QuestionText":
        #     self._parse_state = QuizParserState.PARSE_QUESTION
        # elif tagname == "Answer":
        #     self._parse_state = QuizParserState.PARSE_QUESTION
        #     self._current_question.answers.append(self._current_answer)
        
        match tagname:
            case "QuizML":
                self._parse_state = QuizParserState.IDLE
            case "Description":
                self._parse_state = QuizParserState.PARSE_QUIZ
            case "Question":
                self._parse_state = QuizParserState.PARSE_QUIZ
                self.new_quiz.questions.append(self._current_question)
            case "QuestionText":
                self._parse_state = QuizParserState.PARSE_QUESTION
            case "Answer":
                self._parse_state = QuizParserState.PARSE_QUESTION
                self._current_question.answers.append(self._current_answer)

    def characters(self, chars):
        #TODO: process the text content
        # if self._parse_state == QuizParserState.PARSE_DESCRIPTION:
        #     self.new_quiz.description += chars
        # elif self._parse_state == QuizParserState.PARSE_QUEST_TEXT:
        #     self._current_question.text += chars
        # elif self._parse_state == QuizParserState.PARSE_ANSWER:
        #     self._current_answer.text += chars
        
        match self._parse_state:
            case QuizParserState.PARSE_DESCRIPTION:
                self.new_quiz.description += chars
            case QuizParserState.PARSE_QUEST_TEXT:
                self._current_question.text += chars
            case QuizParserState.PARSE_ANSWER:
                self._current_answer.text += chars


if __name__ == "__main__":
    app = QuizParser()
    qz = app.parse_quiz("Quizzes/SampleQuiz.xml")
    print("Name of quiz       :", qz.name)
    print("Description of quiz:", qz.description)
    print("Total of questions :", len(qz.questions))
    print("Total of points    :", qz.total_points)
    print("List of questions  :")
    for i, q in enumerate(qz.questions):
        print(f"{i+1} - {q.text}")
