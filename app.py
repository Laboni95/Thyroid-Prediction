from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("thyroid_model.pkl", "rb"))

@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")


@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":
        Age = int(request.form["age"])
        T3 = float(request.form["T3"])
        TT4 = float(request.form["TT4"])
        T4U = float(request.form["T4U"])
        FTI = float(request.form["FTI"])
        sex = request.form['sex']
        if (sex == "sex_M"):
            sex_M = 1
        else:
            sex_M = 0

        on_thyroxine = request.form['on_thyroxine']
        if (on_thyroxine == "on_thyroxine_t"):
            on_thyroxine_t = 1
        else:
            on_thyroxine_t = 0

        query_on_thyroxine = request.form['query_on_thyroxine']
        if (query_on_thyroxine == 'query_on_thyroxine_t'):
            query_on_thyroxine_t = 1
        else:
            query_on_thyroxine_t = 0

        on_antithyroid_medication = request.form["on_antithyroid_medication"]
        if (on_antithyroid_medication == 'on_antithyroid_medication_t'):
            on_antithyroid_medication_t = 1
        else:
            on_antithyroid_medication_t = 0

        sick = request.form['sick']
        if (sick == 'sick_t'):
            sick_t = 1
        else:
            sick_t = 0

        pregnant = request.form['pregnant']
        if (pregnant == 'pregnant_t'):
            pregnant_t = 1
        else:
            pregnant_t = 0

        thyroid_surgery = request.form['thyroid_surgery']
        if (thyroid_surgery == 'thyroid_surgery_t'):
            thyroid_surgery_t = 1
        else:
            thyroid_surgery_t = 0

        I131_treatment = request.form['I131_treatment']
        if (I131_treatment == 'I131_treatment_t'):
            I131_treatment_t = 1
        else:
            I131_treatment_t = 0

        query_hypothyroid = request.form['query_hypothyroid']
        if (query_hypothyroid == 'query_hypothyroid_t'):
            query_hypothyroid_t = 1
        else:
            query_hypothyroid_t = 0

        query_hyperthyroid = request.form['query_hyperthyroid']
        if (query_hyperthyroid == 'query_hyperthyroid_t'):
            query_hyperthyroid_t = 1
        else:
            query_hyperthyroid_t = 0

        lithium = request.form['lithium']
        if (lithium == 'lithium_t'):
            lithium_t = 1
        else:
            lithium_t = 0

        goitre = request.form['goitre']
        if(goitre == 'goitre_t'):
            goitre_t = 1
        else:
            goitre_t = 0

        tumor = request.form['tumor']
        if (tumor == 'tumor_t'):
            tumor_t = 1
        else:
            tumor_t = 0

        hypopituitary = request.form['hypopituitary']
        if (hypopituitary == 'hypopituitary_t'):

            hypopituitary_t =1
        else:
            hypopituitary_t = 0

        psych = request.form['psych']
        if (psych == 'psych_t'):
            psych_t = 1
        else:
            psych_t = 0

        referral_source = request.form['referral_source']
        if (referral_source == 'referral_source_SVHC'):
            referral_source_SVHC = 1
            referral_source_SVHD = 0
            referral_source_SVI = 0
            referral_source_other = 0
        elif (referral_source == 'referral_source_SVHD'):
            referral_source_SVHC = 0
            referral_source_SVHD = 1
            referral_source_SVI = 0
            referral_source_other = 0
        elif (referral_source == 'referral_source_SVI'):
            referral_source_SVHC = 0
            referral_source_SVHD = 0
            referral_source_SVI = 1
            referral_source_other = 0
        elif (referral_source == 'referral_source_other'):
            referral_source_SVHC = 0
            referral_source_SVHD = 0
            referral_source_SVI = 0
            referral_source_other = 1
        else:
            referral_source_SVHC = 0
            referral_source_SVHD = 0
            referral_source_SVI = 0
            referral_source_other = 0

        prediction = model.predict([[Age,
                                     T3,
                                     TT4,
                                     T4U,
                                     FTI,
                                     sex_M,
                                     on_thyroxine_t,
                                     query_on_thyroxine_t,
                                     on_antithyroid_medication_t,
                                     sick_t,
                                     pregnant_t,
                                     thyroid_surgery_t,
                                     I131_treatment_t,
                                     query_hypothyroid_t,
                                     query_hyperthyroid_t,
                                     lithium_t,
                                     goitre_t,
                                     tumor_t,
                                     hypopituitary_t,
                                     psych_t,
                                     referral_source_SVHC,
                                     referral_source_SVHD,
                                     referral_source_SVI,
                                     referral_source_other]])

    output = prediction[0]

    if output == 0:
        return render_template('home.html', prediction_text='Thyroid_Result : Compensated_Hypothyroid')
    elif output == 1:
        return render_template('home.html', prediction_text='Thyroid_Result : Negative')
    elif output == 2:
        return render_template('home.html', prediction_text= 'Thyroid_Result : Primary_Hypothyroid')
    else:
        return render_template('home.html', prediction_text='Thyroid_Result : Secondary_Hypothyroid')


if __name__ == '__main__':
    app.run(debug=True)






























