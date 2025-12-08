# scripts/generate_cyber_defamation_files.py
from pathlib import Path

ROOT = Path(__file__).parent.parent
OUT = ROOT / "law_data"
OUT.mkdir(exist_ok=True)

entries = {
"ipc_499_defamation.txt":
"""IPC Section 499 | Defamation | source: https://www.indiacode.nic.in/
Whoever, by words either spoken or intended to be read, or by signs or by visible representations, makes or publishes any imputation concerning any person, intending to harm, or knowing or having reason to believe that such imputation will harm, the reputation of such person, is said to commit defamation.

Exception: Truth for public good and fair comments on public conduct are exceptions; see full legal text for details.

[Summary]
Defamation concerns publication or spoken words that harm someone's reputation. Remedies: criminal or civil action.

""",

"ipc_500_punishment_defamation.txt":
"""IPC Section 500 | Punishment for defamation | source: https://www.indiacode.nic.in/
Whoever defames another shall be punished with simple imprisonment for a term which may extend to two years, or with fine, or with both.

[Summary]
Punishment for defamation may include imprisonment up to two years, fine, or both.

""",

"ipc_504_intentional_insult.txt":
"""IPC Section 504 | Intentional insult with intent to provoke breach of peace | source: https://www.indiacode.nic.in/
Whoever intentionally insults, and thereby gives provocation to any person, intending or knowing it to be likely that such provocation will cause him to break the public peace, is punishable.

[Summary]
Intentional insults that provoke breach of the peace are punishable.

""",

"ipc_505_statements_public_mischief.txt":
"""IPC Section 505 | Statements conducing to public mischief | source: https://www.indiacode.nic.in/
Whoever makes, publishes, or circulates any statement, rumor or report with intent to cause, or which is likely to cause, any officer, soldier, sailor or airman to mutiny or disorderly conduct, or to encourage animosity among communities, shall be punished.

[Summary]
Publishing certain statements that cause public alarm, enmity, or danger is punishable.

""",

"ipc_507_anonymous_threat.txt":
"""IPC Section 507 | Criminal intimidation by anonymous communication | source: https://www.indiacode.nic.in/
Whoever commits the offense of criminal intimidation by anonymous communication shall be punished as provided in the Code, potentially with imprisonment.

[Summary]
Making threats anonymously (e.g., anonymous messages) is punishable under this section.

""",

"ipc_507a_stalking_online_offences.txt":
"""IPC (companion) | Stalking & harassment (relevant provisions) | source: https://www.indiacode.nic.in/
Various provisions address stalking and harassment; online stalking which induces fear or alarm may be covered by criminal intimidation, causing hurt, or other specific provisions.

[Summary]
Online stalking/harassment can be prosecuted under stalking, intimidation, or related IPC sections depending on facts.

""",

"it_act_66_d_cheating_by_impersonation.txt":
"""IT Act Section 66D | Cheating by personation by using computer resources | source: https://www.indiacode.nic.in/
Whoever cheats or dishonestly induces any person by personation using a computer or network shall be punished with imprisonment or fine.

[Summary]
Using electronic means to impersonate or cheat is an offense under the IT Act.

""",

"it_act_67_obscene_material.txt":
"""IT Act Section 67 | Publishing or transmitting obscene material in electronic form | source: https://www.indiacode.nic.in/
Whoever publishes or transmits obscene material in electronic form shall be punished with imprisonment up to three years and a fine for first conviction; higher for subsequent convictions.

[Summary]
Transmitting obscene/explicit material electronically is punishable.

""",

"it_act_66e_violation_of_privacy.txt":
"""IT Act Section 66E | Violation of privacy (covering capturing/distributing images) | source: https://www.indiacode.nic.in/
Whoever intentionally captures, publishes or transmits images of a private area of a person without consent shall be punished.

[Summary]
Capturing and sharing private images without consent is an offence under IT Act.

""",

"it_act_67b_cyberstalking.txt":
"""IT Act (related) | Cyberstalking and online harassment (interpretive summary) | source: https://www.indiacode.nic.in/
The IT Act and IPC provisions together address persistent online harassment, repeated unwanted messages, threats and cyberstalking.

[Summary]
Repeated unwanted communications and harassment can be prosecuted using IT Act and IPC provisions.

""",

"ipc_354d_stalking.txt":
"""IPC Section 354D | Stalking | source: https://www.indiacode.nic.in/
Whoever follows a woman and monitors the use by a woman of the internet, email or any other form of electronic communication, commits the offense of stalking.

[Summary]
Stalking (including electronic monitoring) is a punishable offense.

""",

"negotiable_instruments_cheque_bounce.txt":
"""Negotiable Instruments Act Section 138 | Dishonour of cheque for insufficiency, etc. | source: https://www.indiacode.nic.in/
Where a cheque drawn by a person for payment of any debt or other liability is returned due to insufficient funds, the drawer may be punishable.

[Summary]
Cheque bounce has criminal remedies under Section 138; included for financial harassment contexts.

""",

"ipc_503_criminal_intimidation.txt":
"""IPC Section 503 | Criminal intimidation | source: https://www.indiacode.nic.in/
Whoever threatens another with injury to person, reputation or property, or to cause alarm, is guilty of criminal intimidation.

[Summary]
Threats of harm to person or reputation are punishable.

""",

"ipc_505_part2_public_mischief_social_media.txt":
"""IPC Section 505(2) | Statements creating fear or alarm to public | source: https://www.indiacode.nic.in/
Statements made with intent to cause fear or alarm among public, or incite violence, may be punished under clause (2).

[Summary]
Social media posts that incite public disorder or fear may fall under this provision.

""",

"ipc_354a_sexual_harassment_online.txt":
"""IPC Section 354A | Sexual harassment | source: https://www.indiacode.nic.in/
Sexual harassment includes unwelcome physical contact, advances, or remarks; in some contexts online sexual harassment may be covered.

[Summary]
Online sexual harassment can be treated as sexual harassment depending on facts.

""",

"consumer_protection_online_defamation.txt":
"""Consumer Protection & Related Remedies | Online defamation & complaints | source: https://www.indiacode.nic.in/
Complaints about online services, defamation via platforms, and related consumer issues can be filed with appropriate commissions; separate criminal remedy may apply.

[Summary]
Victims may have regulatory/consumer options in addition to criminal remedies.

""",

"privacy_rights_transmission_of_data.txt":
"""Privacy & Data Protection (interpretation) | Unauthorized transmission of personal data | source: https://www.indiacode.nic.in/
Unauthorized sharing of sensitive personal data may be actionable under IT Act rules and privacy frameworks.

[Summary]
Sharing personal data without consent may violate privacy rules and IT Act provisions.

""",

"ipc_292_obscene_publication.txt":
"""IPC Section 292 | Sale, distribution of obscene material | source: https://www.indiacode.nic.in/
The sale or distribution of obscene material (including electronic distribution) is prohibited and punishable.

[Summary]
Obscene publications distributed online can be prosecuted under IPC.

""",

"ipc_354c_sexual_harrassment_image_sharing.txt":
"""IPC Section 354C | Voyeurism & non-consensual image sharing | source: https://www.indiacode.nic.in/
Capturing a person’s private acts or sharing private images without consent is punishable.

[Summary]
Non-consensual image-sharing or voyeurism attracts criminal penalties.

""",

"it_act_66a_history_note.txt":
"""IT Act - Section 66A Note | (Struck down by Supreme Court - S. 66A) | source: https://www.indiacode.nic.in/
Note: Section 66A (which criminalized sending offensive messages) was struck down by the Supreme Court; however, other provisions and IPC sections remain applicable for online misuse.

[Summary]
66A is no longer in force; rely on IPC/IT Act provisions currently operative.

""",

"ipc_509_word_or_gesture_intent_to_outrage.txt":
"""IPC Section 509 | Word, gesture or act intended to insult the modesty of a woman | source: https://www.indiacode.nic.in/
Whoever intends to insult the modesty of a woman by word or gesture shall be punished.

[Summary]
Offensive words/gestures intended to insult a woman's modesty are punishable.

"""
}

for fname, content in entries.items():
    fp = OUT / fname
    if not fp.exists():
        fp.write_text(content, encoding='utf-8')
        print("created", fp.name)
    else:
        print("exists", fp.name)

print("Done. Created/checked", len(entries), "files in", OUT)
