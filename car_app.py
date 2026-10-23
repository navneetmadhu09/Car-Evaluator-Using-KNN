import streamlit as st
import pickle
import html

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="Car Evaluator",
    page_icon="🚘",
    layout="wide"
)

# --------------------------------------------------
# CUSTOM DARK THEME
# --------------------------------------------------
st.markdown("""
<style>
.stApp {
    background-color: #0b1120;
    color: #f8fafc;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Header */
.hero {
    background: linear-gradient(135deg, #172554, #111827);
    border: 1px solid #334155;
    border-radius: 18px;
    padding: 25px;
    margin-bottom: 20px;
}

.hero h1 {
    color: #ffffff;
    font-size: 38px;
    font-weight: 800;
}

.hero p {
    color: #d1d5db;
    font-size: 16px;
    line-height: 1.7;
}

/* Headings and text */
h2, h3 {
    color: #f8fafc !important;
}

.stMarkdown p {
    color: #e2e8f0;
}

/* Input labels */
div[data-testid="stWidgetLabel"] p {
    color: #f8fafc !important;
    font-weight: 600;
}

/* Select boxes */
div[data-baseweb="select"] > div {
    background-color: #1e293b;
    border-color: #475569;
    color: #ffffff;
}

/* Radio labels */
div[data-testid="stRadio"] label {
    color: #f8fafc !important;
}

/* Form */
div[data-testid="stForm"] {
    background-color: #111827;
    border: 1px solid #334155;
    border-radius: 18px;
    padding: 24px;
}

/* Predict button */
div[data-testid="stFormSubmitButton"] button {
    width: 100%;
    min-height: 50px;
    background-color: #dc2626;
    color: #ffffff;
    border: none;
    border-radius: 12px;
    font-size: 17px;
    font-weight: 700;
}

div[data-testid="stFormSubmitButton"] button:hover {
    background-color: #b91c1c;
    color: #ffffff;
}

/* Prediction result panel */
.result-panel {
    background-color: #111827;
    border: 1px solid #475569;
    border-radius: 16px;
    padding: 24px;
    margin-top: 15px;
}

.result-good {
    color: #86efac;
    font-size: 26px;
    font-weight: 800;
}

.result-acceptable {
    color: #fde68a;
    font-size: 26px;
    font-weight: 800;
}

.result-bad {
    color: #fca5a5;
    font-size: 26px;
    font-weight: 800;
}

.result-message {
    color: #e2e8f0;
    font-size: 16px;
    margin-top: 10px;
}

/* Footer */
.footer {
    color: #94a3b8;
    text-align: center;
    padding-top: 25px;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)


# --------------------------------------------------
# LOAD SAVED MODEL FILES
# --------------------------------------------------
@st.cache_resource
def load_models():

    with open("carmodel.sav", "rb") as f:
        knn = pickle.load(f)

    with open("carscaler.sav", "rb") as f:
        scalar = pickle.load(f)

    with open("carlabel.sav", "rb") as f:
        label = pickle.load(f)

    return knn, scalar, label


# --------------------------------------------------
# MAIN APPLICATION
# --------------------------------------------------
def main():

    # Header and car image
    col1, col2 = st.columns([1.5, 1])

    with col1:
        st.markdown("""
        <div class="hero">
            <h1>🚘 CAR EVALUATOR</h1>
            <p>
                Evaluate a car based on its buying price,
                maintenance cost, number of doors,
                seating capacity, luggage space and safety.
            </p>
            <p>
                🏷️ Price &nbsp; | &nbsp; 🔧 Maintenance
                &nbsp; | &nbsp; 👥 Capacity
                &nbsp; | &nbsp; 🛡️ Safety
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.image(
            "https://images.unsplash.com/photo-1492144534655-ae79c964c9d7",
            use_container_width=True
        )

    st.divider()

    st.markdown("## ⚙️ Enter Car Details")
    st.caption(
        "Choose the car features below and click Evaluate Car."
    )

    # --------------------------------------------------
    # INPUT FORM
    # --------------------------------------------------
    with st.form("car_form"):

        st.markdown("### 💰 Price and Maintenance")

        col1, col2 = st.columns(2)

        with col1:
            bp = st.selectbox(
                "Buying Price",
                ["Low", "Med", "High", "Very High"]
            )

        with col2:
            main_cost = st.selectbox(
                "Maintenance Cost",
                ["Low", "Med", "High", "Very High"]
            )

        st.divider()
        st.markdown("### 🚗 Car Specifications")

        col3, col4 = st.columns(2)

        with col3:
            door = st.radio(
                "Number of Doors",
                ["2", "3", "4", "5_or_more"],
                horizontal=True
            )

        with col4:
            persons = st.radio(
                "Seating Capacity",
                ["2", "4", "more"],
                horizontal=True
            )

        col5, col6 = st.columns(2)

        with col5:
            lug_boot = st.radio(
                "Luggage Boot Size",
                ["small", "med", "big"],
                horizontal=True
            )

        with col6:
            safety = st.radio(
                "Safety Level",
                ["low", "med", "high"],
                horizontal=True
            )

        predict = st.form_submit_button("🔍 Evaluate Car")

    # --------------------------------------------------
    # ENCODE INPUTS
    # Preserving your original encoding logic
    # --------------------------------------------------
    if bp == "Low":
        buying = 1
    elif bp == "Med":
        buying = 2
    elif bp == "High":
        buying = 0
    else:
        buying = 3

    if main_cost == "Low":
        m = 1
    elif main_cost == "Med":
        m = 2
    elif main_cost == "High":
        m = 0
    else:
        m = 3

    if door == "2":
        d = 2
    elif door == "3":
        d = 3
    elif door == "4":
        d = 4
    else:
        d = 5

    if persons == "2":
        per = 2
    elif persons == "4":
        per = 4
    else:
        per = 5

    if lug_boot == "big":
        lug = 0
    elif lug_boot == "med":
        lug = 1
    else:
        lug = 2

    if safety == "high":
        saf = 0
    elif safety == "low":
        saf = 1
    else:
        saf = 2

    features = [buying, m, d, per, lug, saf]

    # --------------------------------------------------
    # PREDICTION
    # --------------------------------------------------
    if predict:

        try:
            knn, scalar, label = load_models()

            scaled_features = scalar.transform([features])
            result = knn.predict(scaled_features)

            # Preserve your original target encoder reference
            prediction = label[4].inverse_transform(result)[0]

            st.divider()
            st.markdown("## 📊 Evaluation Result")

            if prediction == "vgood":
                result_text = "🌟 VERY GOOD"
                result_class = "result-good"
                message = "This car is highly recommended."

            elif prediction == "good":
                result_text = "✅ GOOD"
                result_class = "result-good"
                message = "This car is a good choice."

            elif prediction == "acc":
                result_text = "👍 ACCEPTABLE"
                result_class = "result-acceptable"
                message = "This car may be suitable."

            elif prediction == "unacc":
                result_text = "⚠️ UNACCEPTABLE"
                result_class = "result-bad"
                message = "Consider evaluating another car."

            else:
                result_text = str(prediction)
                result_class = "result-acceptable"
                message = "The model returned this category."

            st.markdown(
                f"""
                <div class="result-panel">
                    <div class="{result_class}">
                        {html.escape(str(result_text))}
                    </div>
                    <div class="result-message">
                        {html.escape(message)}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

        except FileNotFoundError:
            st.error(
                "Model files not found. Keep carmodel.sav, "
                "carscaler.sav and carlabel.sav in the same "
                "folder as car_app.py."
            )

        except (IndexError, AttributeError, TypeError, ValueError) as e:
            st.error(
                f"Prediction processing failed: {e}. "
                "Check the saved model, scaler and label encoder."
            )

        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")

    # --------------------------------------------------
    # FOOTER
    # --------------------------------------------------
    st.divider()

    st.markdown("""
    <div class="footer">
        🚘 Car Evaluator | Machine Learning Project using KNN
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
