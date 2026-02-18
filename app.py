from flask import Flask, render_template, request

app = Flask(__name__)

# ======================================
# CAREER FIELDS
# ======================================

career_data = {
    "Technology": {
        "jobs": [
            "Software Developer",
            "AI Engineer",
            "Data Scientist",
            "Cybersecurity Analyst",
            "Cloud Engineer"
        ]
    },
    "Medical": {
        "jobs": [
            "Doctor",
            "Dentist",
            "Nurse",
            "Pharmacist",
            "Physiotherapist"
        ]
    },
    "Business": {
        "jobs": [
            "Investment Banker",
            "Marketing Manager",
            "Business Analyst",
            "Entrepreneur",
            "Financial Analyst"
        ]
    },
    "Design": {
        "jobs": [
            "UI/UX Designer",
            "Graphic Designer",
            "Fashion Designer",
            "Animator",
            "Interior Designer"
        ]
    },
    "Law": {
        "jobs": [
            "Corporate Lawyer",
            "Criminal Lawyer",
            "Judge",
            "Legal Advisor"
        ]
    }
}

# ======================================
# GLOBAL UNIVERSITIES DATABASE
# ======================================

universities = {

    "United States": [
        {"name": "Harvard University", "type": "Private", "ielts": "7.5+", "sat": "1500+", "cost": "$55k-$75k/year"},
        {"name": "Stanford University", "type": "Private", "ielts": "7.0+", "sat": "1450+", "cost": "$55k-$75k/year"},
        {"name": "MIT", "type": "Private", "ielts": "7.0+", "sat": "1450+", "cost": "$50k-$75k/year"},
        {"name": "University of California, Berkeley", "type": "Public", "ielts": "7.0+", "sat": "1400+", "cost": "$30k-$45k/year"},
        {"name": "University of Michigan", "type": "Public", "ielts": "6.5+", "sat": "1350+", "cost": "$28k-$50k/year"},
    ],

    "United Kingdom": [
        {"name": "Oxford University", "type": "Public", "ielts": "7.0+", "cost": "$30k-$50k/year"},
        {"name": "Cambridge University", "type": "Public", "ielts": "7.0+", "cost": "$30k-$50k/year"},
        {"name": "Imperial College London", "type": "Public", "ielts": "6.5+", "cost": "$25k-$45k/year"},
        {"name": "University College London", "type": "Public", "ielts": "6.5+", "cost": "$25k-$40k/year"},
    ],

    "Canada": [
        {"name": "University of Toronto", "type": "Public", "ielts": "6.5+", "cost": "$25k-$40k/year"},
        {"name": "UBC", "type": "Public", "ielts": "6.5+", "cost": "$20k-$35k/year"},
        {"name": "McGill University", "type": "Public", "ielts": "6.5+", "cost": "$20k-$35k/year"},
    ],

    "Australia": [
        {"name": "University of Melbourne", "type": "Public", "ielts": "6.5+", "cost": "$30k-$45k/year"},
        {"name": "Australian National University", "type": "Public", "ielts": "6.5+", "cost": "$28k-$40k/year"},
    ],

    "Germany": [
        {"name": "Technical University of Munich", "type": "Public", "ielts": "6.5+", "cost": "Low / Almost Free"},
        {"name": "Heidelberg University", "type": "Public", "ielts": "6.5+", "cost": "Low / Almost Free"},
    ],

    "France": [
        {"name": "Sorbonne University", "type": "Public", "ielts": "6.5+", "cost": "$3k-$10k/year"},
        {"name": "HEC Paris", "type": "Private", "ielts": "7.0+", "cost": "$40k-$60k/year"},
    ],

    "Netherlands": [
        {"name": "University of Amsterdam", "type": "Public", "ielts": "6.5+", "cost": "$10k-$20k/year"},
        {"name": "Delft University of Technology", "type": "Public", "ielts": "6.5+", "cost": "$12k-$18k/year"},
    ],

    "Singapore": [
        {"name": "National University of Singapore", "type": "Public", "ielts": "6.5+", "cost": "$20k-$35k/year"},
        {"name": "Nanyang Technological University", "type": "Public", "ielts": "6.5+", "cost": "$20k-$35k/year"},
    ],

    "Japan": [
        {"name": "University of Tokyo", "type": "Public", "ielts": "6.5+", "cost": "$5k-$10k/year"},
        {"name": "Kyoto University", "type": "Public", "ielts": "6.5+", "cost": "$5k-$10k/year"},
    ],

    "South Korea": [
        {"name": "Seoul National University", "type": "Public", "ielts": "6.0+", "cost": "$5k-$15k/year"},
        {"name": "KAIST", "type": "Public", "ielts": "6.5+", "cost": "$8k-$20k/year"},
    ],

    "Switzerland": [
        {"name": "ETH Zurich", "type": "Public", "ielts": "7.0+", "cost": "$1k-$5k/year"},
        {"name": "EPFL", "type": "Public", "ielts": "6.5+", "cost": "$1k-$5k/year"},
    ],

    "Ireland": [
        {"name": "Trinity College Dublin", "type": "Public", "ielts": "6.5+", "cost": "$20k-$35k/year"},
    ],

    "Sweden": [
        {"name": "Lund University", "type": "Public", "ielts": "6.5+", "cost": "$10k-$20k/year"},
        {"name": "KTH Royal Institute of Technology", "type": "Public", "ielts": "6.5+", "cost": "$12k-$18k/year"},
    ],

    "India": [
        {"name": "IIT", "type": "Public", "exam": "JEE Advanced", "cost": "$2k-$5k/year"},
        {"name": "AIIMS", "type": "Public", "exam": "NEET", "cost": "$1k-$3k/year"},
        {"name": "BITS Pilani", "type": "Private", "exam": "BITSAT", "cost": "$4k-$8k/year"},
    ],
}

# ======================================
# ROUTES
# ======================================

@app.route("/")
def home():
    return render_template(
        "index.html",
        fields=career_data.keys(),
        countries=universities.keys()
    )


@app.route("/shortlist", methods=["POST"])
def shortlist():
    field = request.form["field"]
    path_type = request.form["path_type"]
    country = request.form.get("country")
    budget = request.form.get("budget")

    return render_template(
        "shortlist.html",
        field=field,
        path_type=path_type,
        jobs=career_data[field]["jobs"],
        country=country,
        budget=budget
    )


@app.route("/final", methods=["POST"])
def final():
    selected_jobs = request.form.getlist("jobs")
    country = request.form.get("country")
    budget = request.form.get("budget")
    path_type = request.form.get("path_type")

    return render_template(
        "final.html",
        jobs=selected_jobs,
        country=country,
        budget=budget,
        path_type=path_type,
        universities=universities.get(country, [])
    )


if __name__ == "__main__":
    app.run(debug=True)













