import sys

# Define the grade points dictionary once at the top level
grade_points = {
    "A1": 6, "B2": 5, "B3": 4,
    "C4": 3, "C5": 2, "C6": 1,
    "D7": 0, "E8": 0, "F9": 0
}

# Popular FUNAAB courses displayed to the user
popular_courses = [
    "Mechatronic Engineering",
    "Computer Science",
    "Mechanical Engineering",
    "Electrical and Electronics Engineering",
    "Civil Engineering",
    "Agricultural Engineering",
    "Biochemistry",
    "Microbiology",
    "Veterinary Medicine",
    "Food Science and Technology",
    "Biotechnology",
    "Public Health",
    "Cyber Security",
    "Data Science",
    "Software Engineering",
    "Accounting",
    "Business Administration",
    "Economics",
    "Statistics",
    "Environmental Management and Toxicology"
]

# FUNAAB courses used to check "Other Course"
funaab_courses = [
    "Agricultural Administration",
    "Agricultural Economics and Farm Management",
    "Agricultural Extension and Rural Development",
    "Animal Breeding and Genetics",
    "Animal Nutrition",
    "Animal Physiology",
    "Animal Production and Health",
    "Aquaculture and Fisheries Management",
    "Climate Science and Agricultural Meteorology",
    "Crop Protection",
    "Environmental Management and Toxicology",
    "Forest Resource Management",
    "Geology",
    "Horticulture",
    "Hydrology and Water Resources Management",
    "Pasture and Range Management",
    "Plant Breeding and Seed Technology",
    "Plant Physiology and Crop Production",
    "Soil Science and Land Management",
    "Water Resources Management and Agro-Meteorology",
    "Wildlife and Eco-Tourism Management",
    "Water, Sanitation and Hygiene",
    "Biochemistry",
    "Biotechnology",
    "Microbiology",
    "Public Health",
    "Pure and Applied Botany",
    "Pure and Applied Zoology",
    "Science Laboratory Technology",
    "Computer Science",
    "Cyber Security",
    "Data Science",
    "Information and Communication Technology",
    "Information Systems",
    "Information Technology",
    "Software Engineering",
    "Clothing and Textile Design",
    "Food Science and Technology",
    "Home Science and Management",
    "Hospitality and Tourism Management",
    "Nutrition and Dietetics",
    "Chemistry",
    "Geophysics",
    "Industrial Chemistry",
    "Mathematics",
    "Physics",
    "Statistics",
    "Agricultural Engineering",
    "Civil Engineering",
    "Electrical and Electronics Engineering",
    "Mechanical Engineering",
    "Mechatronic Engineering",
    "Veterinary Medicine",
    "Accounting",
    "Banking and Finance",
    "Business Administration",
    "Cooperative Studies",
    "Development Studies",
    "Economics",
    "Entrepreneurial Studies",
    "Library and Information Science"
]

# Human medical courses that FUNAAB does not offer
medical_courses = [
    "MEDICINE",
    "HUMAN MEDICINE",
    "MBBS",
    "NURSING",
    "NURSING SCIENCE",
    "PHARMACY",
    "DENTISTRY",
    "DENTAL SURGERY",
    "SURGERY",
    "SURGERY SCIENCE"
]

# Welcome message
print("\n=====================================================")
print("  WELCOME TO THE FUNAAB ADMISSION CALCULATOR")
print("=====================================================")
print("This program helps estimate your FUNAAB screening aggregate.")

while True:
    print("\n=====================================================")
    print("  FUNAAB Admission Screening Aggregate Calculator   ")
    print("=====================================================")
    print("1. Calculate Admission Screening Aggregate")
    print("2. About Calculator")
    print("3. Exit Program")

    choice = input("Select an option (1-3): ").strip()

    if choice == '3':
        print("\nThank you for using the FUNAAB Calculator. Goodbye!")
        break

    elif choice == '2':
        print("\n--- ABOUT THE CALCULATOR ---")
        print("This calculator estimates a student's FUNAAB")
        print("admission screening aggregate using:")
        print("• JAMB score")
        print("• O'Level sitting")
        print("• O'Level grades")
        print("• Course competitiveness")
        print("\n⚠️ This is an estimate and is not an official")
        print("FUNAAB admission decision.")

    elif choice == '1':
        print("\n--- Start New Application Screening Form ---")
        student_name = input("Enter your Full Name: ").strip().title()

        # Course selection
        while True:
            print("\n--- POPULAR FUNAAB COURSES ---")

            for number, course in enumerate(popular_courses, start=1):
                print(f"{number}. {course}")

            other_option = len(popular_courses) + 1
            print(f"{other_option}. Other Course")

            try:
                course_choice = int(
                    input(f"\nSelect your course (1-{other_option}): ")
                )

                # User selected one of the displayed courses
                if 1 <= course_choice <= len(popular_courses):
                    chosen_course = popular_courses[course_choice - 1].upper()
                    break

                # User selected Other Course
                elif course_choice == other_option:

                    other_course = input(
                        "Enter the name of your course: "
                    ).strip().upper()

                    # Check if the course is a human medical course
                    if any(
                        med_course in other_course
                        for med_course in medical_courses
                    ):
                        print("\n❌ Sorry, FUNAAB doesn't offer human medical courses.")
                        print("Please choose another course.")
                        continue

                    # Check if FUNAAB offers the course
                    if other_course in [
                        course.upper() for course in funaab_courses
                    ]:
                        chosen_course = other_course
                        print("\n✅ Course found! Continuing with your application...")
                        break

                    else:
                        print(
                            "\n❌ Sorry, FUNAAB doesn't offer such a course yet."
                        )
                        print("Please choose another course.")

                else:
                    print(
                        f"⚠️ Invalid choice! Please select a number "
                        f"from 1-{other_option}."
                    )

            except ValueError:
                print("⚠️ Error: Please enter a valid number.")

        # 1. Handle JAMB UTME Score Input (60% Weight)
        while True:
            try:
                jamb_score = int(input("Enter your JAMB score (0-400): "))

                if 0 <= jamb_score <= 400:

                    if jamb_score < 160:
                        print(
                            f"\n❌ Sorry {student_name}, you do not meet "
                            "the minimum FUNAAB cut-off mark of 160."
                        )
                        print("You are ineligible to apply.")
                        jamb_component = None
                        break

                    jamb_component = (jamb_score / 400) * 60
                    break

                print(
                    "⚠️ Invalid! JAMB score must be between 0 and 400."
                )

            except ValueError:
                print("⚠️ Error: Please enter a valid number.")

        if jamb_component is None:
            continue

        # 2. Handle O'Level Sitting Weight (10% Weight)
        while True:
            try:
                sittings = int(
                    input("How many O'level sittings? (1 or 2): ")
                )

                if sittings == 1:
                    sitting_component = 10
                    break

                elif sittings == 2:
                    sitting_component = 6
                    break

                print(
                    "⚠️ FUNAAB only accepts a maximum of 2 sittings."
                )

            except ValueError:
                print("⚠️ Error: Please enter 1 or 2.")

        # 3. Handle O'Level Subjects Grade Point System (30% Weight)
        core_subjects = [
            "English",
            "Mathematics",
            "Physics",
            "Chemistry",
            "Biology"
        ]

        total_olevel_points = 0
        student_grades = {}

        print(
            "\nEnter your grades for the 5 core subjects "
            "(e.g., A1, B3, C6):"
        )

        for subject in core_subjects:
            while True:
                grade = input(f"{subject} Grade: ").strip().upper()

                if grade in grade_points:
                    total_olevel_points += grade_points[grade]
                    student_grades[subject] = grade
                    break

                print(
                    "⚠️ Invalid Grade! Please type a valid WAEC "
                    "grade (e.g., A1, B2, C4, F9)."
                )

        # Display entered grades
        print("\n--- YOUR O'LEVEL GRADES ---")

        for subject in core_subjects:
            print(f"{subject}: {student_grades[subject]}")

        print(
            f"Total O'Level Points: "
            f"{total_olevel_points} / 30"
        )

        # 4. Compile the Final Aggregate
        final_aggregate = (
            jamb_component
            + sitting_component
            + total_olevel_points
        )

        # 5. Determine Competitive Course vs General Course
        competitive_courses = [
            "COMPUTER SCIENCE",
            "CYBER SECURITY",
            "DATA SCIENCE",
            "SOFTWARE ENGINEERING",
            "MECHANICAL ENGINEERING",
            "ELECTRICAL AND ELECTRONICS ENGINEERING",
            "CIVIL ENGINEERING",
            "MECHATRONIC ENGINEERING",
            "BIOCHEMISTRY",
            "MICROBIOLOGY",
            "VETERINARY MEDICINE"
        ]

        is_competitive = False

        for comp_course in competitive_courses:
            if comp_course in chosen_course:
                is_competitive = True
                break

        # 6. Evaluate Admission Probability
        if is_competitive:

            if final_aggregate >= 72:
                status = (
                    "🌟 HIGH CHANCE "
                    "(Very competitive score for this department!)"
                )

            elif final_aggregate >= 62:
                status = (
                    "⚖️ MEDIUM CHANCE "
                    "(On the borderline. Supplementary list possible.)"
                )

            else:
                status = (
                    "⚠️ LOW CHANCE "
                    "(Below safe merit targets for competitive courses.)"
                )

        else:

            if final_aggregate >= 60:
                status = (
                    "🌟 HIGH CHANCE "
                    "(Solid score for general admission guidelines.)"
                )

            elif final_aggregate >= 50:
                status = (
                    "⚖️ MEDIUM CHANCE "
                    "(Passable aggregate score.)"
                )

            else:
                status = (
                    "⚠️ LOW CHANCE "
                    "(Below average screening performance levels.)"
                )

        # 7. Output Report Sheet
        print("\n=============================================")
        print("          FUNAAB SCREENING REPORT CARD       ")
        print("=============================================")
        print(f"STUDENT NAME:   {student_name}")
        print(f"CHOSEN COURSE:  {chosen_course}")
        print(
            f"DEPARTMENT TYPE: "
            f"{'🔥 High-Competition Major' if is_competitive else '📁 Standard Major'}"
        )
        print("---------------------------------------------")
        print(
            f"JAMB Score Component (60%):     "
            f"{jamb_component:.2f} / 60.00"
        )
        print(
            f"O'Level Grades Component (30%): "
            f"{total_olevel_points:.2f} / 30.00"
        )
        print(
            f"Sitting Points Component (10%): "
            f"{sitting_component:.2f} / 10.00"
        )
        print("---------------------------------------------")
        print(
            f"FINAL COMPOSITE AGGREGATE:      "
            f"{final_aggregate:.2f}% / 100.00%"
        )
        print("---------------------------------------------")
        print(f"ADMISSION ASSESSMENT: {status}")
        print("=============================================")

        # Small motivational message
        if final_aggregate >= 70:
            print("🔥 Excellent aggregate! Keep up the good work!")

        elif final_aggregate >= 60:
            print("👍 Good aggregate! Keep working hard.")

        else:
            print("📚 Keep studying and improving your score!")

    else:
        print("⚠️ Invalid choice. Please select 1, 2 or 3.")
