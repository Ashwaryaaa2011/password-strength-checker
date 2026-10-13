import streamlit as st
import re

# Page configuration
st.set_page_config(
    page_title="Password Strength Checker",
    page_icon="🔐",
    layout="centered"
)

# Application heading
st.title("🔐 Password Strength Checker")
st.write(
    "Check your password strength and get suggestions "
    "to make it more secure."
)
st.info("Use a sample password for testing. Do not enter your actual password.")

# Password input field
password = st.text_input(
    "Enter a sample password:",
    type="password",
    placeholder="Enter password here"
)

if password:
    # Check the five password criteria
    checks = {
        "At least 8 characters": len(password) >= 8,
        "At least one uppercase letter (A-Z)": bool(
            re.search(r"[A-Z]", password)
        ),
        "At least one lowercase letter (a-z)": bool(
            re.search(r"[a-z]", password)
        ),
        "At least one number (0-9)": bool(
            re.search(r"[0-9]", password)
        ),
        "At least one special character": bool(
            re.search(r"[^A-Za-z0-9]", password)
        )
    }

    # Calculate password score
    score = sum(checks.values())

    # Determine password strength
    if score <= 2:
        strength = "Weak"
        color = "red"
    elif score <= 4:
        strength = "Moderate"
        color = "orange"
    else:
        strength = "Strong"
        color = "green"

    # Display results
    st.subheader("📊 Password Strength Analysis")

    st.markdown(
        f"### Strength: :{color}[{strength}]"
    )
    st.metric("Password Strength Score", f"{score} / 5")

    # Visual progress bar
    st.progress(score / 5)

    # Checklist
    st.subheader("✅ Criteria Checklist")

    for criterion, passed in checks.items():
        if passed:
            st.success(f"✔ {criterion}")
        else:
            st.error(f"✘ {criterion}")

    # Suggestions for improvement
    st.subheader("💡 Suggestions for Improvement")

    suggestions = {
        "At least 8 characters":
            "Use at least 8 characters.",
        "At least one uppercase letter (A-Z)":
            "Add an uppercase letter, such as A or B.",
        "At least one lowercase letter (a-z)":
            "Add a lowercase letter, such as a or b.",
        "At least one number (0-9)":
            "Include a number, such as 3 or 7.",
        "At least one special character":
            "Include a special character, such as !, @, or #."
    }

    missing = [
        suggestions[criterion]
        for criterion, passed in checks.items()
        if not passed
    ]

    if missing:
        for suggestion in missing:
            st.write(f"- {suggestion}")
    else:
        st.success(
            "Excellent! Your sample password meets all "
            "five criteria."
        )

    # Final message
    if strength == "Weak":
        st.warning(
            "Your password is weak. Follow the suggestions above "
            "to improve it."
        )
    elif strength == "Moderate":
        st.info(
            "Your password has moderate strength. "
            "Improve the missing criteria to make it stronger."
        )
    else:
        st.success(
            "Your password meets all five criteria!"
        )

else:
    st.caption("Enter a sample password above to begin the analysis.")

# Sample test cases
with st.expander("🧪 Sample Passwords for Testing"):
    st.write("Try these examples (do not use real passwords):")
    st.code(
        "abc\n"
        "abcdefgh\n"
        "Abcdef12\n"
        "Abcdef12!"
    )
    st.caption(
        "These examples demonstrate different scores and strength levels."
    )
