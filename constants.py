PROMPT_TEMPLATE = \
"""<s>[INST] <<SYS>>
{system_prompt}
<</SYS>>

{user_message} [/INST]
"""


prompt = \
"""<s>[INST] <<SYS>>
Fill FORMAT using only information from TRANSCRIPT and nothing else.

FORMAT:
“<h4>History of Presentation</h4>
(use list tags and history of conversation from transcript should go here here if discussed)
<h4>Past medical history</h4>
(use list tags and patient's past medical history as discussed should go here if discussed)
<h4>Medication</h4>
(use list tags and medications the patient is on or had in past and allergy status should go here if discussed; every medication is a separate item in the list)
<h4>Social history</h4>
(use list tags and drinking, smoking habits, lifestyle, etc should go here if discussed)
<h4>Family history</h4>
(use list tags and family medical conditions history should go here here if discussed)
<h4>Examination</h4>
(use list tags and results of doctor's examination should go here if discussed)
<h4>Diagnosis</h4>
(use list tags and doctor's diagnosis should go here if discussed)
<h4>Plan</h4>
(use list tags and any tests to be ordered or medications to be prescribed should go here with exact dosage here if discussed)”
<</SYS>>
TRANSCRIPT:
"{transcript}" [/INST]
"""