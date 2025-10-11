from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "mysecretkey2025"


majors_info = {
    "Computer Science": {"description": "Programming and algorithms.", "duration":"4 years", "difficulty":"High", "job_market":"Good", "salary":"$70k-$120k"},
    "Medicine": {"description": "Health and biology.", "duration":"7 years", "difficulty":"Very High", "job_market":"Excellent", "salary":"$60k-$150k"},
    "Engineering": {"description": "Math and science for solving problems.", "duration":"4-5 years", "difficulty":"High", "job_market":"Good", "salary":"$60k-$110k"},
    "Mathematics": {"description": "Numbers, logic, patterns.", "duration":"4 years", "difficulty":"Medium", "job_market":"Good", "salary":"$50k-$90k"},
    "Law": {"description": "Justice, critical thinking.", "duration":"4 years", "difficulty":"High", "job_market":"Good", "salary":"$50k-$100k"},
    "Literature": {"description": "Reading, writing, analyzing texts.", "duration":"4 years", "difficulty":"Medium", "job_market":"Average", "salary":"$40k-$70k"},
    "Biology": {"description": "Living organisms and genetics.", "duration":"4 years", "difficulty":"Medium", "job_market":"Good", "salary":"$45k-$80k"}
}


questions = {
    "Science": ["Do you enjoy biology?", "Do you enjoy chemistry?", "Do you like physics?", "Do you enjoy lab experiments?", "Do you enjoy studying human body?", "Do you like solving scientific problems?", "Do you enjoy environment studies?", "Do you enjoy earth science?", "Do you like medicine topics?", "Do you enjoy research?"],
    "Math": ["Do you enjoy solving math problems?", "Do you like programming?", "Do you enjoy algorithms?", "Do you enjoy logical puzzles?", "Do you like statistics?", "Do you enjoy geometry?", "Do you like trigonometry?", "Do you enjoy coding?", "Do you enjoy applied math?", "Do you like problem solving?"],
    "Humanities": ["Do you enjoy reading and writing?", "Do you like history?", "Do you enjoy literature?", "Do you like philosophy?", "Do you enjoy arts?", "Do you like social studies?", "Do you enjoy debates?", "Do you like psychology?", "Do you enjoy cultural studies?", "Do you like creative writing?"]
}


@app.route("/", methods=["GET","POST"])
def index():
    if request.method=="POST":
        username = request.form.get("username").strip()
        if username:
            session["username"] = username
            return redirect(url_for("track"))
    return render_template("index.html")

@app.route("/track", methods=["GET","POST"])
def track():
    username = session.get("username","User")
    if request.method=="POST":
        track_choice = request.form.get("track")
        if track_choice in questions:
            session["track"] = track_choice
            return redirect(url_for("quiz"))
    return render_template("track.html", username=username)

@app.route("/quiz", methods=["GET","POST"])
def quiz():
    username = session.get("username","User")
    track = session.get("track","Science")
    if request.method=="POST":
        answers = request.form.to_dict()
        try:
            score = sum(int(v) for v in answers.values())
        except:
            score = 0
        max_score = len(questions[track])*5
        match_percent = int(score/max_score*100)

        if track=="Science":
            major = "Medicine" if score>=30 else "Biology"
        elif track=="Math":
            major = "Computer Science" if score>=30 else "Engineering"
        else:
            major = "Law" if score>=30 else "Literature"

        session["major"] = major
        session["match"] = match_percent
        return redirect(url_for("results"))

    return render_template("quiz.html", username=username, track=track, questions=questions[track])

@app.route("/results")
def results():
    username = session.get("username","User")
    major = session.get("major","Unknown")
    match = session.get("match",0)
    return render_template("results.html", username=username, major=major, match=match)

@app.route("/compare", methods=["GET","POST"])
def compare():
    majors = list(majors_info.keys())
    result = None
    compare_data = None

    if request.method=="POST":
        m1 = request.form.get("major1")
        m2 = request.form.get("major2")
        try:
            s1 = int(request.form.get("score1",0))
            s2 = int(request.form.get("score2",0))
        except:
            s1=s2=0
        if m1==m2:
            result=f"Please select two different majors."
        else:
            compare_data = {
                m1: {**majors_info[m1], "match":s1},
                m2: {**majors_info[m2], "match":s2}
            }

    return render_template("compare.html", majors=majors, result=result, compare_data=compare_data)

@app.route("/roadmap")
def roadmap():
    roadmaps = {
        "Computer Science": ["Year1: Programming", "Year2: Projects", "Year3: Internship", "Year4: Job"],
        "Medicine": ["Year1: Biology", "Year2: Anatomy", "Year3: Internship", "Year4: Residency"],
        "Engineering": ["Year1: Basics", "Year2: Core Courses", "Year3: Projects", "Year4: Internship"],
        "Law": ["Year1: Intro", "Year2: Legal", "Year3: Internship", "Year4: Bar Exam Prep"]
    }
    return render_template("roadmap.html", roadmaps=roadmaps)

@app.route("/scholarship", methods=["GET","POST"])
def scholarship():
    result = None
    if request.method=="POST":
        try:
            gpa = float(request.form.get("gpa",0))
        except:
            gpa=0
        english = request.form.get("english","Beginner").lower()
        if gpa>=17 and english=="advanced":
            result="You are strong for scholarships."
        elif gpa>=14:
            result="You may try partial scholarships."
        else:
            result="Improve your GPA first."
    return render_template("scholarship.html", result=result)

if __name__=="__main__":
    app.run(debug=True)
