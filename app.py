import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from datetime import datetime
from html import escape

# ============================================================
# SKILLPATH AI — PREMIUM CAREER INTELLIGENCE PLATFORM
# ============================================================

st.set_page_config(
    page_title="SkillPath AI | Career Intelligence",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CAREER DATABASE
# ============================================================

CAREERS = {
    "Software Developer": {
        "category": "Technology",
        "icon": "⌘",
        "description": "Build websites, applications, and software products.",
        "interests": ["Technology", "Problem Solving", "Building Things"],
        "skills": ["Programming", "Logical Thinking", "Problem Solving"],
        "learn": ["Python fundamentals", "HTML, CSS and JavaScript", "Git and GitHub", "Databases", "Build real projects"],
        "projects": ["Portfolio website", "Task management app", "Student management system"],
        "resources": ["freeCodeCamp", "CS50", "MDN Web Docs"],
        "duration": "6–12 months"
    },
    "AI / Machine Learning Engineer": {
        "category": "Technology",
        "icon": "✳",
        "description": "Create intelligent systems that learn from data.",
        "interests": ["Technology", "Research", "Mathematics"],
        "skills": ["Programming", "Mathematics", "Analytical Thinking"],
        "learn": ["Python", "NumPy and Pandas", "Statistics", "Machine learning", "Model deployment"],
        "projects": ["Movie recommendation system", "Image classifier", "Prediction dashboard"],
        "resources": ["Kaggle Learn", "Google Machine Learning Crash Course", "scikit-learn documentation"],
        "duration": "8–14 months"
    },
    "Data Analyst": {
        "category": "Business & Technology",
        "icon": "▥",
        "description": "Transform data into useful business insights.",
        "interests": ["Business", "Mathematics", "Problem Solving"],
        "skills": ["Analytical Thinking", "Mathematics", "Research"],
        "learn": ["Excel", "SQL", "Python basics", "Power BI", "Data storytelling"],
        "projects": ["Sales dashboard", "Student performance analysis", "Market research report"],
        "resources": ["Kaggle Learn", "Microsoft Learn", "SQLBolt"],
        "duration": "4–8 months"
    },
    "Cybersecurity Analyst": {
        "category": "Technology",
        "icon": "⬡",
        "description": "Protect computer systems and information.",
        "interests": ["Technology", "Problem Solving", "Research"],
        "skills": ["Logical Thinking", "Problem Solving", "Analytical Thinking"],
        "learn": ["Networking fundamentals", "Linux", "Security basics", "Threat analysis", "Security labs"],
        "projects": ["Security awareness campaign", "Network monitoring lab", "Password strength checker"],
        "resources": ["Cisco Skills for All", "TryHackMe beginner paths", "OWASP"],
        "duration": "6–12 months"
    },
    "UI/UX Designer": {
        "category": "Design & Creative",
        "icon": "◈",
        "description": "Design beautiful and useful digital experiences.",
        "interests": ["Design", "Creativity", "Technology"],
        "skills": ["Creativity", "Visual Design", "Communication"],
        "learn": ["Design principles", "Figma", "User research", "Wireframing", "Prototyping"],
        "projects": ["Mobile app redesign", "Website prototype", "Design system"],
        "resources": ["Figma Learn", "Google UX Design resources", "Nielsen Norman Group"],
        "duration": "4–8 months"
    },
    "Digital Marketer": {
        "category": "Business & Creative",
        "icon": "↗",
        "description": "Help brands connect with audiences through digital media.",
        "interests": ["Business", "Creativity", "Communication"],
        "skills": ["Communication", "Creativity", "Writing"],
        "learn": ["Marketing fundamentals", "SEO", "Social media strategy", "Analytics", "Campaign planning"],
        "projects": ["Brand campaign", "Content calendar", "Marketing performance dashboard"],
        "resources": ["Google Skillshop", "HubSpot Academy", "Meta Blueprint"],
        "duration": "3–6 months"
    },
    "Healthcare Professional": {
        "category": "Healthcare",
        "icon": "✚",
        "description": "Support people's health and wellbeing through clinical care.",
        "interests": ["Healthcare", "Helping People", "Science"],
        "skills": ["Empathy", "Communication", "Research"],
        "learn": ["Explore healthcare professions", "Understand admission requirements", "Study relevant sciences", "Complete required accredited education", "Obtain required registration"],
        "projects": ["Health awareness presentation", "Community wellness research", "First-aid awareness project"],
        "resources": ["Official university admissions", "Relevant professional councils", "WHO learning resources"],
        "duration": "Depends on qualification"
    },
    "Teacher / Educator": {
        "category": "Education",
        "icon": "✎",
        "description": "Help learners understand, grow, and develop new skills.",
        "interests": ["Education", "Helping People", "Communication"],
        "skills": ["Communication", "Empathy", "Leadership"],
        "learn": ["Choose a subject", "Develop teaching skills", "Understand required qualifications", "Create lesson plans", "Gain teaching experience"],
        "projects": ["Interactive lesson plan", "Educational video", "Learning activity kit"],
        "resources": ["DIKSHA", "SWAYAM", "Official teacher education guidelines"],
        "duration": "Depends on qualification"
    },
    "Environmental Scientist": {
        "category": "Science & Environment",
        "icon": "✺",
        "description": "Study environmental problems and develop sustainable solutions.",
        "interests": ["Science", "Nature", "Research"],
        "skills": ["Research", "Analytical Thinking", "Problem Solving"],
        "learn": ["Environmental science basics", "Research methods", "Data collection", "GIS introduction", "Field experience"],
        "projects": ["Local water-quality study", "Waste audit", "Environmental data dashboard"],
        "resources": ["SWAYAM", "UNEP educational resources", "University open courses"],
        "duration": "Depends on qualification"
    },
    "Business Analyst": {
        "category": "Business",
        "icon": "▤",
        "description": "Improve business processes using research and data.",
        "interests": ["Business", "Problem Solving", "Communication"],
        "skills": ["Analytical Thinking", "Communication", "Problem Solving"],
        "learn": ["Business fundamentals", "Excel and SQL", "Requirements gathering", "Process mapping", "Dashboard creation"],
        "projects": ["Business process improvement", "Customer survey", "Operations dashboard"],
        "resources": ["Microsoft Learn", "Coursera audit courses", "SWAYAM"],
        "duration": "4–8 months"
    },
    "Content Creator": {
        "category": "Media & Creative",
        "icon": "✦",
        "description": "Create videos, stories, and digital content for audiences.",
        "interests": ["Creativity", "Communication", "Design"],
        "skills": ["Creativity", "Writing", "Visual Design"],
        "learn": ["Storytelling", "Content planning", "Video editing", "Audience research", "Analytics"],
        "projects": ["Short-video series", "Content portfolio", "Personal brand"],
        "resources": ["YouTube Creator Academy", "Canva Design School", "Meta creator resources"],
        "duration": "2–6 months"
    },
    "Lawyer": {
        "category": "Law & Public Service",
        "icon": "⚖",
        "description": "Study legal issues and represent or advise people.",
        "interests": ["Law", "Helping People", "Research"],
        "skills": ["Communication", "Research", "Writing"],
        "learn": ["Explore legal careers", "Understand law admission pathways", "Complete recognized legal education", "Develop legal research skills", "Meet professional enrollment requirements"],
        "projects": ["Legal awareness poster", "Case study review", "Mock debate"],
        "resources": ["Official law university websites", "Bar Council information", "Government legal education portals"],
        "duration": "Depends on qualification"
    }
}

INTERESTS = sorted({
    item
    for career in CAREERS.values()
    for item in career["interests"]
})

SKILLS = sorted({
    item
    for career in CAREERS.values()
    for item in career["skills"]
})

PAGES = [
    "Overview",
    "Explore Careers",
    "Discover My Path",
    "Career Dashboard",
    "My Roadmap",
    "Resources"
]

# ============================================================
# SESSION STATE
# ============================================================

if "current_page" not in st.session_state:
    st.session_state.current_page = "Overview"

if "profile" not in st.session_state:
    st.session_state.profile = None

if "matches" not in st.session_state:
    st.session_state.matches = []

if "selected_career" not in st.session_state:
    st.session_state.selected_career = None


def navigate(destination):
    st.session_state.current_page = destination
    st.rerun()


# ============================================================
# PREMIUM STYLING
# ============================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');

:root {
    --background: #0c0618;
    --surface: #170c2b;
    --surface2: #201136;
    --border: rgba(211,177,255,0.16);
    --text: #f7f2ff;
    --muted: #b9a9d0;
    --pink: #f38bd5;
    --purple: #9c6bff;
    --blue: #5cbbff;
}

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

.stApp {
    background:
        radial-gradient(ellipse at 88% 5%, rgba(115,54,194,0.22), transparent 35%),
        radial-gradient(ellipse at 20% 75%, rgba(70,45,160,0.14), transparent 35%),
        #0c0618;
    color: var(--text);
}

.block-container {
    max-width: 1330px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

h1, h2, h3 {
    font-family: 'Manrope', sans-serif !important;
    color: #fff !important;
    letter-spacing: -0.035em;
}

p, label {
    color: #e4d8f4;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #150b29 0%, #0c0719 100%);
    border-right: 1px solid rgba(210,177,255,0.14);
}

[data-testid="stSidebar"] .block-container {
    padding-top: 2rem;
}

[data-testid="stSidebar"] button {
    width: 100%;
    text-align: left;
}

[data-testid="stSidebar"] .stButton > button {
    background: transparent;
    color: #cdbce6;
    border: 1px solid transparent;
    border-radius: 12px;
    padding: 0.75rem;
}

[data-testid="stSidebar"] .stButton > button:hover {
    background: rgba(160,112,255,0.16);
    border-color: rgba(190,145,255,0.25);
    color: white;
}

.stButton > button[kind="primary"] {
    background: linear-gradient(100deg, #7958ff, #b55cf6, #ed78c2);
    color: white;
    border: none;
    border-radius: 12px;
    font-weight: 700;
    padding: 0.72rem 1.2rem;
    box-shadow: 0 8px 25px rgba(140,76,245,0.22);
}

.stButton > button[kind="secondary"] {
    background: rgba(170,128,245,0.11);
    color: #f4eaff;
    border: 1px solid rgba(191,149,255,0.24);
    border-radius: 12px;
}

.stButton > button:hover {
    filter: brightness(1.12);
}

div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div,
div[data-baseweb="textarea"] {
    background: #201435 !important;
    border-color: rgba(193,150,255,0.22) !important;
    color: white !important;
    border-radius: 12px !important;
}

input, textarea {
    color: white !important;
}

[data-testid="stMetric"] {
    background: rgba(255,255,255,0.035);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 18px;
}

[data-testid="stMetricValue"] {
    color: white;
}

[data-testid="stProgressBar"] > div > div {
    background: linear-gradient(90deg, #7c62ff, #e978c7);
}

[data-testid="stExpander"] {
    background: rgba(255,255,255,0.035);
    border: 1px solid var(--border);
    border-radius: 14px;
}

hr {
    border-color: rgba(190,160,255,0.15);
}

.brand {
    font-family: 'Manrope', sans-serif;
    font-size: 1.7rem;
    font-weight: 800;
    color: #fff;
    letter-spacing: -0.05em;
}

.brand span {
    background: linear-gradient(90deg, #b48aff, #f59cd5);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.eyebrow {
    color: #c9a6ff;
    font-size: 0.72rem;
    font-weight: 800;
    letter-spacing: 0.19em;
    text-transform: uppercase;
    margin-bottom: 12px;
}

.hero {
    background:
        radial-gradient(circle at 80% 30%, rgba(197,85,244,0.25), transparent 38%),
        radial-gradient(circle at 20% 85%, rgba(91,94,246,0.18), transparent 45%),
        linear-gradient(135deg, #1c1037 0%, #10091e 65%, #170a29 100%);
    border: 1px solid rgba(206,162,255,0.25);
    border-radius: 26px;
    padding: 50px 45px;
    margin-bottom: 24px;
    box-shadow: 0 25px 75px rgba(0,0,0,0.22);
    position: relative;
    overflow: hidden;
}

.hero::after {
    content: "✧";
    position: absolute;
    right: 7%;
    top: 6%;
    font-size: 180px;
    color: rgba(201,145,255,0.09);
    pointer-events: none;
}

.hero h1 {
    font-size: clamp(2.8rem, 5vw, 5rem);
    font-weight: 800;
    line-height: 1.09;
    margin: 12px 0 20px;
}

.gradient {
    background: linear-gradient(90deg, #b88bff, #ff9fd6, #8ecfff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero-copy {
    font-size: 1.05rem;
    line-height: 1.85;
    max-width: 650px;
    color: #d5c8e8;
}

.pill {
    display: inline-block;
    padding: 8px 13px;
    border-radius: 999px;
    background: rgba(186,142,255,0.11);
    border: 1px solid rgba(204,160,255,0.24);
    color: #eadcff;
    margin: 5px 7px 5px 0;
    font-size: 0.83rem;
}

.panel {
    background: linear-gradient(145deg, rgba(43,24,74,0.82), rgba(20,12,38,0.92));
    border: 1px solid rgba(204,161,255,0.18);
    border-radius: 20px;
    padding: 25px;
    margin-bottom: 16px;
    min-height: 170px;
    box-shadow: 0 14px 35px rgba(0,0,0,0.12);
}

.panel h3 {
    font-size: 1.15rem;
    margin: 8px 0;
}

.panel p {
    color: #bdafd1;
    font-size: 0.92rem;
    line-height: 1.7;
}

.panel-icon {
    font-size: 1.9rem;
    color: #c49bff;
}

.stat-number {
    font-size: 2.1rem;
    font-weight: 800;
    color: #fff;
}

.stat-label {
    color: #b6a6cc;
    font-size: 0.84rem;
}

.section-title {
    font-size: 1.7rem;
    font-weight: 800;
    margin: 25px 0 8px;
}

.muted {
    color: #bbaed0;
    font-size: 0.94rem;
}

.career-category {
    color: #c5a1ff;
    font-size: 0.68rem;
    font-weight: 800;
    letter-spacing: 0.15em;
    text-transform: uppercase;
}

.score {
    font-size: 2.2rem;
    font-weight: 800;
    background: linear-gradient(90deg, #ae87ff, #ef90d7);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.roadmap-step {
    border-left: 3px solid #a47cff;
    background: rgba(167,111,255,0.075);
    border-radius: 0 14px 14px 0;
    padding: 18px 22px;
    margin: 12px 0;
}

.roadmap-step h4 {
    color: white;
    margin: 0 0 7px;
}

.roadmap-step p {
    color: #c9b9df;
    margin: 0;
}

.footer {
    color: #88799f;
    text-align: center;
    font-size: 0.8rem;
    margin-top: 40px;
    padding-top: 18px;
    border-top: 1px solid rgba(200,160,255,0.12);
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# HTML RENDERING HELPER
# IMPORTANT: st.html() prevents raw HTML appearing as text
# ============================================================

def show_html(content):
    st.html(content)


def panel(title, description, icon="✦", category=None):
    category_html = (
        f'<div class="career-category">{escape(category)}</div>'
        if category else ""
    )

    show_html(f"""
    <div class="panel">
        <div class="panel-icon">{icon}</div>
        {category_html}
        <h3>{escape(title)}</h3>
        <p>{escape(description)}</p>
    </div>
    """)


def heading(title, subtitle=None):
    st.markdown(f"## {title}")

    if subtitle:
        st.caption(subtitle)


# ============================================================
# MATCHING ENGINE
# ============================================================

def calculate_matches(profile):
    results = []

    user_interests = set(profile["interests"])
    user_skills = set(profile["skills"])
    goal = profile["goal"].lower()

    for name, career in CAREERS.items():
        career_interests = set(career["interests"])
        career_skills = set(career["skills"])

        interest_overlap = len(user_interests & career_interests)
        skill_overlap = len(user_skills & career_skills)

        interest_score = (
            interest_overlap / len(career_interests)
        ) * 55

        skill_score = (
            skill_overlap / len(career_skills)
        ) * 35

        goal_score = 0

        searchable_text = (
            name + " " +
            career["category"] + " " +
            career["description"]
        ).lower()

        if goal.strip():
            goal_words = [
                word for word in goal.split()
                if len(word) > 3
            ]

            if any(word in searchable_text for word in goal_words):
                goal_score = 10

        total = round(
            interest_score + skill_score + goal_score
        )

        results.append({
            "name": name,
            "score": total,
            "interest_matches": list(
                user_interests & career_interests
            ),
            "skill_matches": list(
                user_skills & career_skills
            ),
            "missing_skills": list(
                career_skills - user_skills
            )
        })

    return sorted(
        results,
        key=lambda x: x["score"],
        reverse=True
    )


# ============================================================
# SIDEBAR NAVIGATION
# NO RADIO-WIDGET SESSION STATE CONFLICT
# ============================================================

with st.sidebar:

    show_html("""
    <div style="margin-bottom:35px;">
        <div class="brand">✦ SkillPath <span>AI</span></div>
        <div class="eyebrow" style="margin-top:8px;">
            CAREER INTELLIGENCE
        </div>
    </div>
    """)

    st.caption("WORKSPACE")

    for page_name in PAGES:
        icons = {
            "Overview": "◈",
            "Explore Careers": "▦",
            "Discover My Path": "✧",
            "Career Dashboard": "◉",
            "My Roadmap": "↗",
            "Resources": "▤"
        }

        label = f"{icons[page_name]}  {page_name}"

        if st.button(
            label,
            key=f"nav_{page_name}",
            use_container_width=True,
            type=(
                "primary"
                if st.session_state.current_page == page_name
                else "secondary"
            )
        ):
            navigate(page_name)

    st.markdown("---")

    show_html("""
    <div class="panel">
        <div class="eyebrow">YOUR NEXT CHAPTER</div>
        <h3>Start where you are.</h3>
        <p>You don't need a perfect plan.
        You need a useful next step.</p>
    </div>
    """)

    if st.session_state.profile:
        st.success("✓ Career profile completed")
    else:
        st.caption("Create your profile to unlock recommendations.")


# ============================================================
# MAIN CONTENT
# ============================================================

page = st.session_state.current_page


# ============================================================
# PAGE 1 — OVERVIEW
# ============================================================

if page == "Overview":

    show_html("""
    <div class="hero">
        <div class="eyebrow">✦ YOUR PERSONAL CAREER COMPASS</div>

        <h1>
            Build a future<br>
            <span class="gradient">that fits you.</span>
        </h1>

        <p class="hero-copy">
            Discover career possibilities, understand the skills
            that matter, and transform uncertainty into a
            personalised plan for your next chapter.
        </p>

        <div style="margin-top:24px;">
            <span class="pill">✦ Career discovery</span>
            <span class="pill">◈ Skill-gap insights</span>
            <span class="pill">◎ Personalised roadmaps</span>
        </div>
    </div>
    """)

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button(
            "✦ Discover My Career",
            type="primary",
            use_container_width=True
        ):
            navigate("Discover My Path")

    with col2:
        if st.button(
            "◈ Explore Careers",
            use_container_width=True
        ):
            navigate("Explore Careers")

    with col3:
        if st.button(
            "↗ Build My Roadmap",
            use_container_width=True
        ):
            navigate("My Roadmap")

    st.write("")

    heading(
        "Your career journey",
        "Three steps to move from uncertainty to action."
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        panel(
            "01 — Discover",
            "Explore your strengths, interests and career possibilities.",
            "◇"
        )

    with c2:
        panel(
            "02 — Develop",
            "Understand your skill gaps and build relevant abilities.",
            "✳"
        )

    with c3:
        panel(
            "03 — Move Forward",
            "Follow your personalised roadmap and take action.",
            "↗"
        )

    heading(
        "Your intelligence workspace",
        "Everything you need to plan your career."
    )

    a, b, c = st.columns(3)

    with a:
        panel(
            "Career Explorer",
            "Browse opportunities across technology, business, science, design and more.",
            "▦"
        )

        if st.button(
            "Open Explorer →",
            key="home_explore",
            use_container_width=True
        ):
            navigate("Explore Careers")

    with b:
        panel(
            "Career Dashboard",
            "Visualise career matches and understand your strengths.",
            "◉"
        )

        if st.button(
            "Open Dashboard →",
            key="home_dashboard",
            use_container_width=True
        ):
            navigate("Career Dashboard")

    with c:
        panel(
            "Personal Roadmap",
            "Turn career recommendations into a structured action plan.",
            "↗"
        )

        if st.button(
            "Open Roadmap →",
            key="home_roadmap",
            use_container_width=True
        ):
            navigate("My Roadmap")

    st.write("")

    m1, m2, m3, m4 = st.columns(4)

    with m1:
        st.metric("Career paths", len(CAREERS))

    with m2:
        st.metric(
            "Career fields",
            len(set(
                career["category"]
                for career in CAREERS.values()
            ))
        )

    with m3:
        st.metric("Roadmap stages", 5)

    with m4:
        st.metric("Your journey", "Personalised")


# ============================================================
# PAGE 2 — EXPLORE CAREERS
# ============================================================

elif page == "Explore Careers":

    show_html("""
    <div class="eyebrow">CAREER EXPLORER</div>
    <h1>Explore a world of
    <span class="gradient">possibilities.</span></h1>
    <p class="muted">
    You don't have to have everything figured out before you start.
    </p>
    """)

    search = st.text_input(
        "Search careers",
        placeholder="Try design, technology, healthcare..."
    )

    categories = ["All Fields"] + sorted(
        set(career["category"] for career in CAREERS.values())
    )

    selected_category = st.selectbox(
        "Filter by field",
        categories
    )

    filtered = []

    for name, career in CAREERS.items():

        text = (
            name + " " +
            career["category"] + " " +
            career["description"]
        ).lower()

        matches_search = search.lower() in text

        matches_category = (
            selected_category == "All Fields"
            or career["category"] == selected_category
        )

        if matches_search and matches_category:
            filtered.append((name, career))

    st.caption(f"{len(filtered)} career paths available")

    for index in range(0, len(filtered), 3):

        columns = st.columns(3)

        for offset, column in enumerate(columns):

            position = index + offset

            if position >= len(filtered):
                continue

            name, career = filtered[position]

            with column:

                panel(
                    name,
                    career["description"],
                    career["icon"],
                    career["category"]
                )

                if st.button(
                    f"Explore {name} →",
                    key=f"career_{name}",
                    use_container_width=True
                ):
                    st.session_state.selected_career = name
                    navigate("My Roadmap")


# ============================================================
# PAGE 3 — DISCOVER MY PATH
# ============================================================

elif page == "Discover My Path":

    show_html("""
    <div class="eyebrow">PERSONALISED CAREER DISCOVERY</div>
    <h1>Let's find your
    <span class="gradient">direction.</span></h1>
    <p class="muted">
    Share a little about yourself to discover suitable career paths.
    </p>
    """)

    with st.form("career_profile_form"):

        left, right = st.columns(2)

        with left:

            name = st.text_input(
                "Your name",
                value=(
                    st.session_state.profile["name"]
                    if st.session_state.profile else ""
                ),
                placeholder="Enter your name"
            )

            stage = st.selectbox(
                "Your current stage",
                [
                    "School student",
                    "College student",
                    "Graduate",
                    "Working professional",
                    "Career changer",
                    "Exploring options"
                ]
            )

        with right:

            field = st.text_input(
                "Your academic or professional field",
                placeholder="e.g. Computer Science, Commerce, Arts"
            )

            goal = st.text_input(
                "Your career goal (optional)",
                placeholder="e.g. Build technology that helps people"
            )

        interests = st.multiselect(
            "What are you interested in?",
            INTERESTS,
            placeholder="Choose your interests"
        )

        skills = st.multiselect(
            "Which skills or strengths describe you?",
            SKILLS,
            placeholder="Choose your current strengths"
        )

        submitted = st.form_submit_button(
            "✦ Discover My Career Matches",
            type="primary",
            use_container_width=True
        )

    if submitted:

        if not interests:
            st.warning("Please select at least one interest.")

        else:

            profile = {
                "name": name.strip() or "Explorer",
                "stage": stage,
                "field": field,
                "goal": goal,
                "interests": interests,
                "skills": skills
            }

            st.session_state.profile = profile

            st.session_state.matches = calculate_matches(
                profile
            )

            st.session_state.selected_career = (
                st.session_state.matches[0]["name"]
            )

            st.success("Your career matches are ready!")

    if st.session_state.matches:

        heading(
            "Your top career matches",
            "Indicative scores based on selected interests and skills."
        )

        for match in st.session_state.matches[:3]:

            career = CAREERS[match["name"]]

            col1, col2 = st.columns([4, 1])

            with col1:

                panel(
                    match["name"],
                    career["description"],
                    career["icon"],
                    career["category"]
                )

            with col2:

                show_html(f"""
                <div class="panel">
                    <div class="eyebrow">MATCH</div>
                    <div class="score">{match["score"]}%</div>
                </div>
                """)

                if st.button(
                    "View Roadmap →",
                    key=f"match_{match['name']}",
                    use_container_width=True
                ):
                    st.session_state.selected_career = match["name"]
                    navigate("My Roadmap")

        if st.button(
            "View My Career Dashboard →",
            type="primary"
        ):
            navigate("Career Dashboard")


# ============================================================
# PAGE 4 — CAREER DASHBOARD
# ============================================================

elif page == "Career Dashboard":

    show_html("""
    <div class="eyebrow">CAREER INTELLIGENCE DASHBOARD</div>
    <h1>Your career.
    <span class="gradient">Your insights.</span></h1>
    <p class="muted">
    Understand your career matches and discover your next steps.
    </p>
    """)

    if not st.session_state.matches:

        st.info(
            "Complete your career profile to unlock your dashboard."
        )

        if st.button(
            "Create My Profile →",
            type="primary"
        ):
            navigate("Discover My Path")

    else:

        profile = st.session_state.profile
        matches = st.session_state.matches

        st.subheader(
            f"Welcome, {profile['name']} ✦"
        )

        top = matches[0]

        m1, m2, m3, m4 = st.columns(4)

        with m1:
            st.metric("Top match", f"{top['score']}%")

        with m2:
            st.metric("Careers analysed", len(matches))

        with m3:
            st.metric("Your interests", len(profile["interests"]))

        with m4:
            st.metric("Current strengths", len(profile["skills"]))

        st.write("")

        left, right = st.columns([1.5, 1])

        with left:

            st.subheader("Career Match Analysis")

            top_matches = matches[:6]

            fig = go.Figure()

            fig.add_trace(go.Bar(
                x=[m["score"] for m in top_matches][::-1],
                y=[m["name"] for m in top_matches][::-1],
                orientation="h",
                marker=dict(
                    color=[
                        "#855fff",
                        "#9469ff",
                        "#a477ff",
                        "#b786f5",
                        "#c894ec",
                        "#d6a1e8"
                    ][::-1]
                ),
                text=[
                    f"{m['score']}%"
                    for m in top_matches
                ][::-1],
                textposition="outside"
            ))

            fig.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font=dict(color="#e6d8f7"),
                height=400,
                margin=dict(l=5, r=35, t=20, b=20),
                xaxis=dict(
                    range=[0, 110],
                    showgrid=True,
                    gridcolor="rgba(255,255,255,0.07)"
                ),
                yaxis=dict(showgrid=False)
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        with right:

            st.subheader("Career Match Overview")

            fig2 = go.Figure(
                data=[
                    go.Pie(
                        labels=[
                            "Matched indicators",
                            "Other indicators"
                        ],
                        values=[
                            top["score"],
                            100 - top["score"]
                        ],
                        hole=0.78,
                        marker=dict(
                            colors=["#a475ff", "#241637"]
                        ),
                        textinfo="none"
                    )
                ]
            )

            fig2.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                font=dict(color="white"),
                height=350,
                margin=dict(l=0, r=0, t=0, b=0),
                showlegend=False,
                annotations=[
                    dict(
                        text=f"{top['score']}%",
                        x=0.5,
                        y=0.5,
                        font=dict(
                            size=38,
                            color="white"
                        ),
                        showarrow=False
                    )
                ]
            )

            st.plotly_chart(
                fig2,
                use_container_width=True
            )

        heading("Skill Gap Analysis")

        chosen = st.selectbox(
            "Choose a career to analyse",
            [m["name"] for m in matches]
        )

        chosen_match = next(
            m for m in matches
            if m["name"] == chosen
        )

        career = CAREERS[chosen]

        required = career["skills"]

        current = set(profile["skills"])

        for skill in required:

            achieved = skill in current

            st.write(
                f"{'✓' if achieved else '○'} {skill}"
            )

            st.progress(
                100 if achieved else 0
            )

        st.info(
            "Match percentages are indicative rule-based scores, "
            "not predictions of career success."
        )

        if st.button(
            "Generate Roadmap →",
            type="primary"
        ):
            st.session_state.selected_career = chosen
            navigate("My Roadmap")


# ============================================================
# PAGE 5 — MY ROADMAP
# ============================================================

elif page == "My Roadmap":

    show_html("""
    <div class="eyebrow">PERSONALISED LEARNING JOURNEY</div>
    <h1>From ambition
    <span class="gradient">to action.</span></h1>
    <p class="muted">
    A clear, practical learning path for your chosen career.
    </p>
    """)

    names = list(CAREERS.keys())

    default = st.session_state.selected_career

    default_index = (
        names.index(default)
        if default in names
        else 0
    )

    chosen = st.selectbox(
        "Select your career path",
        names,
        index=default_index
    )

    st.session_state.selected_career = chosen

    career = CAREERS[chosen]

    show_html(f"""
    <div class="panel">
        <div class="eyebrow">{escape(career['category'])}</div>
        <div class="panel-icon">{career['icon']}</div>
        <h2>{escape(chosen)}</h2>
        <p>{escape(career['description'])}</p>
        <span class="pill">
            Estimated exploration and learning:
            {escape(career['duration'])}
        </span>
    </div>
    """)

    heading(
        "Your 5-stage roadmap",
        "A structured pathway from foundations to real-world experience."
    )

    stages = [
        (
            "01 — Explore the Foundations",
            f"Understand the role and its core concepts. Start with {career['learn'][0]}."
        ),
        (
            "02 — Build Essential Skills",
            f"Focus on {career['learn'][1]} and {career['learn'][2]}."
        ),
        (
            "03 — Develop Practical Knowledge",
            f"Learn {career['learn'][3]}."
        ),
        (
            "04 — Create Real Projects",
            f"Build: {career['projects'][0]} and {career['projects'][1]}."
        ),
        (
            "05 — Prepare for Opportunities",
            f"Work on {career['learn'][4]}, document your work, and explore relevant internships or entry pathways."
        )
    ]

    for title, description in stages:

        show_html(f"""
        <div class="roadmap-step">
            <h4>{escape(title)}</h4>
            <p>{escape(description)}</p>
        </div>
        """)

    heading("Suggested Portfolio Projects")

    c1, c2, c3 = st.columns(3)

    for col, project in zip(c1, career["projects"]):

        with col:
            panel(
                project,
                "Build this project to develop practical experience.",
                "✦"
            )

    heading("Learning Resources")

    for resource in career["resources"]:
        st.write(f"✧ {resource}")

    if chosen in ["Lawyer", "Healthcare Professional", "Teacher / Educator"]:
        st.warning(
            "This career may require accredited education, "
            "specific qualifications, licensing, or professional "
            "registration. Verify the current requirements "
            "with the relevant official authority."
        )

    # Downloadable report without external PDF libraries
    report = f"""
SKILLPATH AI — CAREER ROADMAP REPORT

Generated: {datetime.now().strftime('%d %B %Y')}

CAREER: {chosen}
FIELD: {career['category']}

ABOUT THIS CAREER
{career['description']}

ESTIMATED LEARNING PERIOD
{career['duration']}

YOUR ROADMAP

"""

    for title, description in stages:
        report += f"{title}\n{description}\n\n"

    report += "\nSUGGESTED PROJECTS\n"

    for project in career["projects"]:
        report += f"- {project}\n"

    report += "\nLEARNING RESOURCES\n"

    for resource in career["resources"]:
        report += f"- {resource}\n"

    report += (
        "\nNote: This is an educational career guidance prototype. "
        "Career matches are indicative and professional "
        "requirements should be verified independently.\n"
    )

    st.download_button(
        "↓ Download My Career Report",
        data=report,
        file_name="SkillPath_AI_Career_Roadmap.txt",
        mime="text/plain",
        type="primary",
        use_container_width=True
    )


# ============================================================
# PAGE 6 — RESOURCES
# ============================================================

elif page == "Resources":

    show_html("""
    <div class="eyebrow">LEARNING RESOURCE LIBRARY</div>
    <h1>Keep learning.
    <span class="gradient">Keep growing.</span></h1>
    <p class="muted">
    Explore platforms and tools to support your career journey.
    </p>
    """)

    resources = [
        (
            "Programming & Development",
            "freeCodeCamp, CS50, MDN Web Docs",
            "⌘"
        ),
        (
            "AI & Data Science",
            "Kaggle Learn, Google ML Crash Course, Microsoft Learn",
            "✳"
        ),
        (
            "Design & Creativity",
            "Figma Learn, Canva Design School",
            "◈"
        ),
        (
            "Business & Marketing",
            "HubSpot Academy, Google Skillshop",
            "↗"
        ),
        (
            "Academic Learning",
            "SWAYAM, NPTEL, DIKSHA",
            "▤"
        ),
        (
            "Career Preparation",
            "LinkedIn Learning resources, GitHub, portfolio projects",
            "✦"
        )
    ]

    for index in range(0, len(resources), 3):

        columns = st.columns(3)

        for offset, col in enumerate(columns):

            position = index + offset

            if position >= len(resources):
                continue

            title, description, icon = resources[position]

            with col:
                panel(
                    title,
                    description,
                    icon
                )

    st.info(
        "Some learning platforms offer both free and paid content. "
        "Check their current terms and availability."
    )


# ============================================================
# FOOTER
# ============================================================

show_html("""
<div class="footer">
    ✦ SkillPath AI — Career Intelligence Platform
    <br>
    Discover • Develop • Move Forward
    <br><br>
    Academic project prototype | Built with Python & Streamlit
</div>
""")