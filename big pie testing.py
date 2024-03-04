#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import plotly.graph_objects as go

st.title('PsychoSim: LSD Dosage Simulator')
st.caption("This simulation is not intended for official medical use. It's meant to visually display different dosages of LSD based on recent studies' assumptions.")

# small bio about LSD and its peculiar origins
st.subheader('About LSD')
st.write("""
LSD, or Lysergic Acid Diethylamide, is a powerful hallucinogenic drug known for its psychological effects. 
It is considered a partial agonist at serotonin receptors, meaning it can both activate and block serotonin receptors, 
leading to its complex range of effects. LSD was first synthesized in 1938, and taken by the scientist who had done this
accidentally. Maybe you have heard stories of the original synthesis as a pleasant, lovely experience, where Albert Hofmann
rode his bicycle home in a beautiful intoxication? That is not quite what happened - Albert Hofmann did immediately proceed
home after the accidental taking of the drug, but was then plagued by dizziness, restlessness, an aversion to the daylight, a 
dream-like trance which left him seeing colors and images which were not truly there. A terrifying experience to say the least...(History.com)
""")

# adding dose response for antagonists vs agonists LSD is a partial agonist...
st.subheader('Dose Response for Antagonists vs Agonists')
st.write("""
LSD acts as a partial agonist at serotonin receptors, meaning it doesn't fully activate the receptor like an agonist or block it like an antagonist. 
This unique interaction contributes to the drug's diverse and variable effects, ranging from euphoria to profound existential experiences (which can end in existential crises...).
""")

# define the dosage ranges for effects with associated colors for clarity
dosage_ranges = {
   'Microdose': (0, 25, '#b2fab4'),
   'Positive Effects': (25, 100, '#fadadd'),
   'Ego Dissolution': (100, 200, '#d1c1f0'),
   'Anxiety Risk': (200, 300, '#ff6961'),
}

# move the slider to just before the dosage effect visualization 
dosage = st.slider('Select LSD dosage (µg)', 0, 300, 25)

# slider will also show effect category
category = None
for key, (min_dose, max_dose, color) in dosage_ranges.items():
   if min_dose <= dosage <= max_dose:
       category = f"{dosage} µg is considered '{key}', characterized by {color} color."
       break

st.write(category if category else "Please select a dosage.")

# creating the dosage ranges visualization
fig_doses = go.Figure()

# add ranges for dosage effects
for label, (min_dose, max_dose, color) in dosage_ranges.items():
   fig_doses.add_shape(type="rect", x0=min_dose, x1=max_dose, y0=0, y1=1, line=dict(color=color), fillcolor=color, opacity=0.5, line_width=0)

# add lines for effective and toxic doses
effective_dose = 50
toxic_dose = 250
fig_doses.add_trace(go.Scatter(x=[effective_dose, effective_dose], y=[0, 1], mode="lines", name="Effective Dose", line=dict(color="blue", dash="dash")))
fig_doses.add_trace(go.Scatter(x=[toxic_dose, toxic_dose], y=[0, 1], mode="lines", name="Toxic Dose", line=dict(color="black", dash="dash")))

# add a marker for the selected dosage
fig_doses.add_trace(go.Scatter(x=[dosage], y=[0.5], mode="markers", name="Selected Dosage", marker=dict(color="red", size=10)))

# update layout for doses graph
fig_doses.update_layout(
   title="LSD Dosage Ranges and Effects",
   xaxis_title="Dosage (µg)",
   yaxis=dict(showticklabels=False), # trying to minimize space used, cleaner look
   yaxis_title="Effect",
   showlegend=True,
   xaxis=dict(range=[0, 300])  #  x-axis should now cover full dosage range
)

# information regarding LSD when it is 'ok' and when it is definitely not ok
st.subheader('LSD as a Medicine Component v. a Lethal Component')
st.write("""
LSD is slowly heading toward becoming an FDA approved pharmaceutical, specifically for PTSD treatments. However, just because it is approaching 
legality in a medical context does not mean that it is safe to consume at every dosage, just like other drugs. The effective dose is something we use in pharmacology
to determine when a drug is at the threshold for positive effects with minimal negative effects, this is a very low dose for LSD. The toxic dose is not just the dose where
someone begins to experience negative side effects, though, it is the dose which is deadly to the user. Negative effects will appear far before the toxic dose, but usually this
is the dose we see when someone has overdosed from a pharmaceutical agent. All pharmaceuticals vary in their effective v. toxic dose ranges. 
""")

# display the doses figure in Streamlit
st.plotly_chart(fig_doses)

st.subheader('LSD Use Amongst Different Age Groups')
st.write("""
LSD is considered to be one of the more popular hallucinogens, that being said it has a relatively high prevalance amongst a variety of age groups, 
but is most popular in the age group of 18-25, and significantly falls off in use after age 25. The data that is being displayed in the following visuals is from 
the Results from the 2021 National Survey on Drug Use and Health.
""")

# data for the Plotly chart, now pink color used
age_groups = ['12 to 17', '18 to 25', '26 or Older']
percent_using_hallucinogens = [1.3, 7.1, 2.1]  #  percentages displayed for age 

# create the Plotly figure with pink 
fig = go.Figure([go.Bar(x=age_groups, y=percent_using_hallucinogens, marker_color='pink')])

# titles, axes, etc. 
fig.update_layout(
   title="Hallucinogen Use Among Different Age Groups in 2021",
   xaxis_title="Age Group",
   yaxis_title="Percentage (%) of People Using Hallucinogens",
   plot_bgcolor="white",
   yaxis=dict(range=[0, max(percent_using_hallucinogens) + 1])  # Ensures a bit of space above the highest bar for better visualization
)

# display this updated chart in your Streamlit app
st.plotly_chart(fig)


# In[ ]:




