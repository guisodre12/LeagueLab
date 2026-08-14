import streamlit as st

st.set_page_config(
    page_title="League Lab",
    page_icon="⚽",
    layout="wide"
)

st.title("League Lab")

# ─────────────────────────────────────────────
# Teams
# ─────────────────────────────────────────────

teams = [
    "Arsenal",
    "Aston Villa",
    "Bournemouth",
    "Brentford",
    "Brighton & Hove Albion",
    "Chelsea",
    "Coventry City",
    "Crystal Palace",
    "Everton",
    "Fulham",
    "Hull City",
    "Ipswich Town",
    "Leeds United",
    "Liverpool",
    "Manchester City",
    "Manchester United",
    "Newcastle United",
    "Nottingham Forest",
    "Sunderland",
    "Tottenham Hotspur"
]

team_names = {
    "ARS": "Arsenal",
    "AVL": "Aston Villa",
    "BOU": "Bournemouth",
    "BRE": "Brentford",
    "BHA": "Brighton & Hove Albion",
    "CHE": "Chelsea",
    "COV": "Coventry City",
    "CRY": "Crystal Palace",
    "EVE": "Everton",
    "FUL": "Fulham",
    "HUL": "Hull City",
    "IPS": "Ipswich Town",
    "LEE": "Leeds United",
    "LIV": "Liverpool",
    "MCI": "Manchester City",
    "UTD": "Manchester United",
    "NEW": "Newcastle United",
    "NFO": "Nottingham Forest",
    "SUN": "Sunderland",
    "TOT": "Tottenham Hotspur",
}

# ─────────────────────────────────────────────
# Matchday fixtures
# ─────────────────────────────────────────────

matchdays = {
    1: [
        ("TOT", "ARS"),
        ("MCI", "CHE"),
        ("UTD", "LIV"),
        ("NEW", "AVL"),
        ("EVE", "BRE"),
        ("BHA", "CRY"),
        ("LEE", "FUL"),
        ("NFO", "SUN"),
        ("BOU", "IPS"),
        ("COV", "HUL"),
    ],

    2: [
        ("ARS", "MCI"),
        ("CHE", "UTD"),
        ("LIV", "NEW"),
        ("AVL", "TOT"),
        ("BRE", "BHA"),
        ("CRY", "EVE"),
        ("FUL", "NFO"),
        ("SUN", "BOU"),
        ("IPS", "LEE"),
        ("HUL", "COV"),
    ],

    3: [
        ("MCI", "LIV"),
        ("UTD", "ARS"),
        ("NEW", "CHE"),
        ("TOT", "BRE"),
        ("AVL", "CRY"),
        ("EVE", "FUL"),
        ("BHA", "SUN"),
        ("LEE", "NFO"),
        ("BOU", "COV"),
        ("HUL", "IPS"),
    ],

    4: [
        ("ARS", "LIV"),
        ("MCI", "UTD"),
        ("CHE", "TOT"),
        ("NEW", "BRE"),
        ("CRY", "AVL"),
        ("FUL", "BHA"),
        ("SUN", "EVE"),
        ("NFO", "BOU"),
        ("LEE", "HUL"),
        ("IPS", "COV"),
    ],
}

# ─────────────────────────────────────────────
# Persistent state
# ─────────────────────────────────────────────

if "matchday" not in st.session_state:
    st.session_state.matchday = 1

if "results" not in st.session_state:
    st.session_state.results = {}


# ─────────────────────────────────────────────
# Matchday navigation
# ─────────────────────────────────────────────

previous, title, next_day = st.columns(
    [1, 4, 1],
    vertical_alignment="center"
)

with previous:
    if st.button(
        "←",
        use_container_width=True,
        disabled=st.session_state.matchday == 1
    ):
        st.session_state.matchday -= 1
        st.rerun()

with title:
    st.markdown(
        f"""
        <h3 style="text-align: center;">
            Matchday {st.session_state.matchday}
        </h3>
        """,
        unsafe_allow_html=True
    )

with next_day:
    if st.button(
        "→",
        use_container_width=True,
        disabled=st.session_state.matchday == len(matchdays)
    ):
        st.session_state.matchday += 1
        st.rerun()

selected_matchday = st.session_state.matchday
matches = matchdays[selected_matchday]


# ─────────────────────────────────────────────
# Fixtures
# ─────────────────────────────────────────────

fixtures_col, standings_col = st.columns(
    [1, 2.5],
    gap="large"
)

with fixtures_col:

    for i, (home, away) in enumerate(matches):

        match_id = f"md{selected_matchday}_{i}"

        team1, score1, x, score2, team2 = st.columns(
            [1.2, 1, 0.3, 1, 1.2],
            vertical_alignment="center"
        )

        # ───────── Home team ─────────

        with team1:
            st.markdown(
                f"""
                <p style="
                    text-align: right;
                    font-weight: 600;
                    margin: 0;
                ">
                    {home}
                </p>
                """,
                unsafe_allow_html=True
            )

        # ───────── Home score ─────────

        with score1:

            home_key = f"{match_id}_home"
            away_key = f"{match_id}_away"

            if home_key not in st.session_state:
                st.session_state[home_key] = ""

            if away_key not in st.session_state:
                st.session_state[away_key] = ""

            st.text_input(
                "Home score",
                key=home_key,
                label_visibility="collapsed",
                placeholder="0"
            )

        # ───────── X ─────────

        with x:
            st.markdown(
                """
                <p style="
                    text-align: center;
                    font-weight: 600;
                    margin: 0;
                ">
                    X
                </p>
                """,
                unsafe_allow_html=True
            )

        # ───────── Away score ─────────

        with score2:
            st.text_input(
                "Away score",
                key=away_key,
                label_visibility="collapsed",
                placeholder="0"
            )

        # ───────── Away team ─────────

        with team2:
            st.markdown(
                f"""
                <p style="
                    text-align: left;
                    font-weight: 600;
                    margin: 0;
                ">
                    {away}
                </p>
                """,
                unsafe_allow_html=True
            )


# ─────────────────────────────────────────────
# Save results
# ─────────────────────────────────────────────

for i, (home, away) in enumerate(matches):

    match_id = f"md{selected_matchday}_{i}"

    home_key = f"{match_id}_home"
    away_key = f"{match_id}_away"

    home_score = st.session_state.get(home_key, "")
    away_score = st.session_state.get(away_key, "")

    if home_score != "" and away_score != "":

        try:
            home_score = int(home_score)
            away_score = int(away_score)

            if home_score >= 0 and away_score >= 0:
                st.session_state.results[match_id] = (
                    home_score,
                    away_score
                )

        except ValueError:
            pass


# ─────────────────────────────────────────────
# Calculate standings
# ─────────────────────────────────────────────

standings = {
    team: {
        "P": 0,
        "W": 0,
        "D": 0,
        "L": 0,
        "GF": 0,
        "GA": 0,
        "GD": 0,
        "Pts": 0,
    }
    for team in teams
}


for matchday, fixtures in matchdays.items():

    for i, (home, away) in enumerate(fixtures):

        match_id = f"md{matchday}_{i}"

        if match_id not in st.session_state.results:
            continue

        home_score, away_score = st.session_state.results[match_id]

        home_team = team_names[home]
        away_team = team_names[away]

        # Matches played
        standings[home_team]["P"] += 1
        standings[away_team]["P"] += 1

        # Goals
        standings[home_team]["GF"] += home_score
        standings[home_team]["GA"] += away_score

        standings[away_team]["GF"] += away_score
        standings[away_team]["GA"] += home_score

        # Result
        if home_score > away_score:

            standings[home_team]["W"] += 1
            standings[away_team]["L"] += 1
            standings[home_team]["Pts"] += 3

        elif home_score < away_score:

            standings[away_team]["W"] += 1
            standings[home_team]["L"] += 1
            standings[away_team]["Pts"] += 3

        else:

            standings[home_team]["D"] += 1
            standings[away_team]["D"] += 1

            standings[home_team]["Pts"] += 1
            standings[away_team]["Pts"] += 1


# ─────────────────────────────────────────────
# Goal difference
# ─────────────────────────────────────────────

for team in teams:

    standings[team]["GD"] = (
        standings[team]["GF"]
        - standings[team]["GA"]
    )


# ─────────────────────────────────────────────
# Sort standings
# ─────────────────────────────────────────────

sorted_teams = sorted(
    teams,
    key=lambda team: (
        standings[team]["Pts"],
        standings[team]["GD"],
        standings[team]["GF"]
    ),
    reverse=True
)


# ─────────────────────────────────────────────
# Standings
# ─────────────────────────────────────────────

with standings_col:

    st.subheader("Standings")

    table = []

    for position, team in enumerate(
        sorted_teams,
        start=1
    ):

        data = standings[team]

        table.append({
            "#": position,
            "Team": team,
            "P": data["P"],
            "W": data["W"],
            "D": data["D"],
            "L": data["L"],
            "GF": data["GF"],
            "GA": data["GA"],
            "GD": data["GD"],
            "Pts": data["Pts"],
        })

    st.dataframe(
        table,
        hide_index=True,
        use_container_width=True,
        height=735,
        column_config={
            "#": st.column_config.NumberColumn(
                "#",
                width="small"
            ),
            "Team": st.column_config.TextColumn(
                "Team",
                width="large"
            ),
            "Pts": st.column_config.NumberColumn(
                "Pts",
                width="small"
            ),
        }
    )
