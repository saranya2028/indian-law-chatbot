# scripts/generate_lots_of_law_files.py
# Creates 60 law .txt templates in law_data/
from pathlib import Path

ROOT = Path(__file__).parent.parent
OUT = ROOT / "law_data"
OUT.mkdir(exist_ok=True)

entries = {
"ipc_120b_conspiracy.txt":
"""IPC Section 120B | Criminal conspiracy | source: https://www.indiacode.nic.in/
Whoever is a party to a criminal conspiracy to commit an offense shall be punished as a conspirator.
[Summary]
Criminal conspiracy covers agreements to commit offenses; conspirators can be punished even if the planned offense was not completed.
""",

"ipc_141_unlawful_assembly.txt":
"""IPC Section 141 | Unlawful assembly | source: https://www.indiacode.nic.in/
An assembly of five or more persons whose common object is to commit an offense, resist the execution of law, or commit mischief, etc. is an unlawful assembly.
[Summary]
Defines unlawful assembly and when group action is criminal.
""",

"ipc_147_rioting.txt":
"""IPC Section 147 | Rioting | source: https://www.indiacode.nic.in/
When force or violence is used by an unlawful assembly in prosecution of common object, members are guilty of rioting.
[Summary]
Rioting describes violent acts by groups; punishments vary with severity.
""",

"ipc_148_rioting_armed.txt":
"""IPC Section 148 | Rioting, armed with deadly weapon | source: https://www.indiacode.nic.in/
Rioting while being armed with deadly weapon increases punishment.
[Summary]
Being armed during rioting attracts higher penalties.
""",

"ipc_302_murder.txt":
"""IPC Section 302 | Punishment for murder | source: https://www.indiacode.nic.in/
Whoever commits murder shall be punished with death, or imprisonment for life, and shall also be liable to fine.
[Summary]
Defines punishment for murder and severity of sentences.
""",

"ipc_307_attempt_to_murder.txt":
"""IPC Section 307 | Attempt to murder | source: https://www.indiacode.nic.in/
Whoever does any act with such intention or knowledge and under such circumstances that, if they caused death, they would be guilty of murder, is guilty of attempt to murder.
[Summary]
Attempted murder carries heavy imprisonment even if death did not occur.
""",

"ipc_304_homicide_not_amounting_to_murder.txt":
"""IPC Section 304 | Culpable homicide not amounting to murder | source: https://www.indiacode.nic.in/
Punishment for culpable homicide that does not amount to murder depends on intent and circumstances.
[Summary]
Lesser degree of culpable homicide with reduced punishment compared to murder.
""",

"ipc_376_rape.txt":
"""IPC Section 376 | Punishment for rape | source: https://www.indiacode.nic.in/
Rape is punishable with rigorous imprisonment for a specified minimum term and may extend to life imprisonment under certain circumstances.
[Summary]
Defines punishment for rape and aggravating factors.
""",

"ipc_354a_sexual_harassment.txt":
"""IPC Section 354A | Sexual harassment | source: https://www.indiacode.nic.in/
Includes unwelcome physical contact, demands for sexual favors, or showing pornography against a woman's will.
[Summary]
Covers sexual harassment and related punishments.
""",

"ipc_354d_stalking.txt":
"""IPC Section 354D | Stalking | source: https://www.indiacode.nic.in/
Following a person or monitoring their electronic communication to cause fear or alarm is punishable as stalking.
[Summary]
Criminalizes stalking including electronic monitoring.
""",

"ipc_498a_cruelty_by_husband_relatives.txt":
"""IPC Section 498A | Cruelty to a woman by husband or relatives | source: https://www.indiacode.nic.in/
Subjecting a married woman to cruelty that may drive her to suicide or cause grave injury is punishable.
[Summary]
Domestic cruelty by husband/relatives is a non-bailable offence in many cases.
""",

"dowry_prohibition_act_3_offence.txt":
"""Dowry Prohibition Act | Dowry offences overview | source: https://www.indiacode.nic.in/
Giving or taking dowry is prohibited; demands and harassment related to dowry are punishable.
[Summary]
Covers dowry demands and related criminal and civil remedies.
""",

"protection_of_women_domestic_violence_act.txt":
"""Protection of Women from Domestic Violence Act | Remedies and protection orders | source: https://www.indiacode.nic.in/
Provides civil remedies, protection orders, and maintenance for victims of domestic violence.
[Summary]
Gives immediate protective relief (orders, residence rights) to victims.
""",

"crpc_154_fir.txt":
"""CrPC Section 154 | Information in cognizable cases (FIR) | source: https://www.indiacode.nic.in/
Every information relating to a cognizable offence, if given orally to an officer in charge of a police station, shall be reduced to writing and a copy given to the informant free of cost.
[Summary]
Procedure for lodging an FIR and police duties on receiving information.
""",

"crpc_156_investigation_by_police.txt":
"""CrPC Section 156 | Police investigation | source: https://www.indiacode.nic.in/
A police officer may, without the order of a Magistrate, investigate any cognizable case.
[Summary]
Police powers to investigate cognizable offenses.
""",

"crpc_57_procedure_after_arrest.txt":
"""CrPC Section 57 | Procedure after arrest (remand to custody) | source: https://www.indiacode.nic.in/
Procedure for producing arrested persons before Magistrate and remand decisions.
[Summary]
Describes custody and remand timelines and magistrate’s role.
""",

"crpc_41_arrest_without_warrant.txt":
"""CrPC Section 41 | Arrest without warrant | source: https://www.indiacode.nic.in/
Circumstances where police may arrest without warrant, and duties post-arrest.
[Summary]
When police can arrest without a warrant and required procedural safeguards.
""",

"evidence_act_32_dying_declaration.txt":
"""Evidence Act Section 32 | Dying declarations | source: https://www.indiacode.nic.in/
Statements made by a person as to the cause of their death are admissible under certain conditions.
[Summary]
Rules on admissibility and weight of dying declarations in trials.
""",

"ipc_420_cheating.txt":
"""IPC Section 420 | Cheating and dishonestly inducing delivery of property | source: https://www.indiacode.nic.in/
Whoever cheats and dishonestly induces the person deceived to deliver property shall be punished with imprisonment and fine.
[Summary]
Defines cheating and criminal consequences for fraudulent inducement.
""",

"neg_instruments_138_cheque_bounce.txt":
"""Negotiable Instruments Act Section 138 | Dishonour of cheque | source: https://www.indiacode.nic.in/
Drawer of cheque may face criminal liability when cheque bounces for insufficiency of funds.
[Summary]
Cheque bounce can have criminal penalties and civil remedies.
""",

"consumer_protection_act_complaints.txt":
"""Consumer Protection Act | Filing consumer complaints | source: https://www.indiacode.nic.in/
Consumers can file complaints in District, State, or National Commissions for defective goods and unfair trade practices.
[Summary]
Explains consumer complaints and compensation mechanisms.
""",

"it_act_66d_cheating_by_personation.txt":
"""IT Act Section 66D | Cheating by personation by use of communication device | source: https://www.indiacode.nic.in/
Cheating by impersonation using a computer resource or network is punishable.
[Summary]
Impersonation/fraud via digital means is an offense under IT Act.
""",

"it_act_67_obscene_electronic.txt":
"""IT Act Section 67 | Publishing or transmitting obscene material electronically | source: https://www.indiacode.nic.in/
Publishing or transmitting obscene content online is punishable with imprisonment and fine.
[Summary]
Regulates obscene material distributed electronically.
""",

"it_act_66e_violation_of_privacy.txt":
"""IT Act Section 66E | Violation of privacy (images) | source: https://www.indiacode.nic.in/
Intentionally capturing and transmitting private images without consent is punished.
[Summary]
Protects privacy against non-consensual capture and distribution.
""",

"ipc_499_defamation.txt":
"""IPC Section 499 | Defamation | source: https://www.indiacode.nic.in/
Whoever makes or publishes an imputation harming another's reputation is said to defame.
[Summary]
Defamation can be criminal or civil; exceptions include truth for public good.
""",

"ipc_500_punishment_defamation.txt":
"""IPC Section 500 | Punishment for defamation | source: https://www.indiacode.nic.in/
Punishment for defamation may include imprisonment up to two years, fine, or both.
[Summary]
Specifies penalties for defamation.
""",

"ipc_503_criminal_intimidation.txt":
"""IPC Section 503 | Criminal intimidation | source: https://www.indiacode.nic.in/
Threats of injury to person, reputation or property with intent to cause alarm are criminal.
[Summary]
Threats and intimidation may be prosecuted under this section.
""",

"ipc_506_punishment_intimidation.txt":
"""IPC Section 506 | Punishment for criminal intimidation | source: https://www.indiacode.nic.in/
Whoever commits criminal intimidation is punishable with imprisonment or fine.
[Summary]
Specifies punishments for intimidation and threatening acts.
""",

"ipc_504_intentional_insult.txt":
"""IPC Section 504 | Intentional insult with intent to provoke breach of peace | source: https://www.indiacode.nic.in/
Intentional insult intended to provoke breach of peace is punishable.
[Summary]
Covers insults that provoke violence or public disorder.
""",

"ipc_505_public_mischief.txt":
"""IPC Section 505 | Statements conducing to public mischief | source: https://www.indiacode.nic.in/
Statements likely to cause fear, alarm, or enmity among communities are punishable.
[Summary]
Applies to statements (including online) that can incite public disorder.
""",

"ipc_295_insult_religious_feelings.txt":
"""IPC Section 295 | Injuring or defiling place of worship or insulting religion | source: https://www.indiacode.nic.in/
Acts intended to insult religious feelings of any class are punishable.
[Summary]
Prohibits actions that outrage religious feelings.
""",

"ipc_295a_deliberate_and_malicious_intent.txt":
"""IPC Section 295A | Deliberate and malicious acts intended to outrage religious feelings | source: https://www.indiacode.nic.in/
Deliberate and malicious acts intended to outrage religious feelings are punished.
[Summary]
Targets deliberate attacks on religious harmony.
""",

"ipc_354c_image_sharing_privacy.txt":
"""IPC Section 354C | Voyeurism and non-consensual image sharing | source: https://www.indiacode.nic.in/
Capturing or sharing private acts or images without consent is punishable.
[Summary]
Addresses non-consensual photography and image dissemination.
""",

"ipc_509_insult_to_modesty.txt":
"""IPC Section 509 | Word, gesture or act intended to insult the modesty of a woman | source: https://www.indiacode.nic.in/
Insulting the modesty of a woman by words, gestures, or acts is an offense.
[Summary]
Covers insulting behavior targeting a woman's modesty.
""",

"posco_section_4_penalty.txt":
"""POCSO Section 4 | Penalty for penetrative sexual assault | source: https://www.indiacode.nic.in/
Punishment for penetrative sexual assault with minimum imprisonment and fines as specified.
[Summary]
Covers crimes involving children and strict punishments under POCSO.
""",

"juvenile_justice_rehabilitation.txt":
"""Juvenile Justice Act | Rehabilitation and social reintegration | source: https://www.indiacode.nic.in/
Provides procedures for juveniles in conflict with law, including rehabilitation, adoption of child protection measures.
[Summary]
Focuses on reformative measures for minors rather than punitive ones.
""",

"labour_payment_of_wages.txt":
"""Payment of Wages Act | Payment timelines and deductions | source: https://www.indiacode.nic.in/
Rules on timely payment of wages and permissible deductions under employment laws.
[Summary]
Protects workers’ wage rights and remedies for violation.
""",

"minimum_wages_act.txt":
"""Minimum Wages Act | Minimum wage protections | source: https://www.indiacode.nic.in/
Employers must pay at least the statutory minimum wage to workers in scheduled employments.
[Summary]
Defines minimum wage obligations and enforcement mechanisms.
""",

"motor_vehicles_compulsory_insurance.txt":
"""Motor Vehicles Act | Compulsory third-party insurance | source: https://www.indiacode.nic.in/
Owners must have at least third-party insurance for vehicles; compensation rules apply for accidents.
[Summary]
Ensures compensation mechanisms for victims of motor accidents.
""",

"motor_vehicles_accident_claims.txt":
"""Motor Vehicles Act | Claims Tribunal and compensation | source: https://www.indiacode.nic.in/
Procedures to claim compensation for motor accident victims via Motor Accidents Claims Tribunal.
[Summary]
Provides forum and procedure for accident compensation claims.
""",

"companies_act_insider_trading_note.txt":
"""Companies Act & Securities Laws | Insider trading overview | source: https://www.indiacode.nic.in/
Insider trading and securities fraud are regulated; penalties under SEBI and other statutes apply.
[Summary]
Regulation of insider trading under securities laws; corporate governance rules.
""",

"gst_compliance_returns.txt":
"""GST Act | Filing returns and compliance overview | source: https://www.indiacode.nic.in/
GST return filing timelines and penalties for non-compliance.
[Summary]
Explains reporting obligations under GST law.
""",

"ndps_possession_punishment.txt":
"""NDPS Act | Possession and punishment for narcotics | source: https://www.indiacode.nic.in/
Possession, trafficking, and production of narcotic substances are severely punished under NDPS Act.
[Summary]
Strict penalties for drug-related offenses; wide-ranging enforcement powers.
""",

"environmental_protection_penalties.txt":
"""Environment Protection Act | Penalties for violations | source: https://www.indiacode.nic.in/
Pollution control, regulatory powers and penalties for breaches under environmental law.
[Summary]
Covers penalties and remedial orders for environmental harm.
""",

"arbitration_act_overview.txt":
"""Arbitration and Conciliation Act | Arbitration overview | source: https://www.indiacode.nic.in/
Provides legal framework for arbitration, enforcement of awards, and interim measures.
[Summary]
Encourages out-of-court dispute resolution via arbitration with enforcement mechanisms.
""",

"family_law_divorce_overview.txt":
"""Marriage Laws | Divorce grounds overview (Hindu/Muslim/Indian law) | source: https://www.indiacode.nic.in/
Grounds for divorce vary by personal law; cruelty, adultery, desertion are common grounds.
[Summary]
Overview of divorce grounds and civil remedies depending on personal law.
""",

"maintenance_law_hindu.txt":
"""Hindu Marriage Act Section 24 | Maintenance pending suit | source: https://www.indiacode.nic.in/
Court may order maintenance for spouse/children during proceedings where necessary.
[Summary]
Covers interim maintenance and court powers to protect dependent spouses.
""",

"dowry_death_ipc_304b.txt":
"""IPC Section 304B | Dowry death | source: https://www.indiacode.nic.in/
Death of a woman within seven years of marriage due to dowry-related cruelty is a distinct offence with severe punishment.
[Summary]
Dowry death has specific presumption of dowry-related cruelty and high penalties.
""",

"rape_medical_exam_procedure.txt":
"""Medical & Evidence | Procedures for medical examination and forensic collection | source: https://www.indiacode.nic.in/
Guidelines exist for survivors' examination, evidence collection, and chain-of-custody for sexual assault cases.
[Summary]
Procedural safeguards for survivors and admissibility of forensic evidence.
""",

"workplace_posh_overview.txt":
"""POSH Act | Sexual harassment at workplace (Prevention of Sexual Harassment Act) | source: https://www.indiacode.nic.in/
Employers must provide internal complaint committees and processes to address workplace sexual harassment.
[Summary]
Employer obligations and internal remedies for workplace harassment.
""",

"service_law_rights_termination.txt":
"""Service Law | Termination and disciplinary procedures (public/private) | source: https://www.indiacode.nic.in/
Rules for lawful termination, disciplinary hearings and remedies for wrongful dismissal.
[Summary]
Procedure for fair disciplinary process and appeals in employment.
""",

"consumer_time_limits_warranty.txt":
"""Consumer Protection | Warranty and limitation for product claims | source: https://www.indiacode.nic.in/
Time limits and procedures for consumer claims, including warranty claims.
[Summary]
Covers timebars and remedies at consumer commissions.
""",

"landlord_tenant_eviction.txt":
"""Rent Control & Civil Procedure | Eviction grounds and procedure | source: https://www.indiacode.nic.in/
Eviction for non-payment of rent, use violations, and landlord remedies under relevant state laws.
[Summary]
Eviction requires statutory procedure; state-specific laws apply.
""",

"insurance_claims_overview.txt":
"""Insurance Act & Regulations | Claim procedures and policyholder rights | source: https://www.indiacode.nic.in/
Policy terms, claims process, and dispute resolution for insurance claims.
[Summary]
Explains claims filing and grievance redressal mechanisms.
""",

"trade_mark_copyright_overview.txt":
"""IPR | Trademark and Copyright basics | source: https://www.indiacode.nic.in/
Basics of registration, infringement, and remedies for IP rights (trademarks, copyright).
[Summary]
High-level overview of intellectual property protections and enforcement.
""",

"building_permit_local_laws.txt":
"""Municipal & Building Regulations | Building permits and local compliance | source: https://www.indiacode.nic.in/
Local municipal laws regulate construction, permits, and penalties for illegal construction.
[Summary]
Local compliance and remedy mechanisms for building law violations.
""",

"food_safety_laws_overview.txt":
"""Food Safety & Standards Act | Food safety regulation & penalties | source: https://www.indiacode.nic.in/
Regulatory framework for food safety, licensing, and penalties for adulteration.
[Summary]
Enforcement mechanisms for food safety violations.
""",

"medical_negligence_overview.txt":
"""Medical Negligence | Liability and remedies | source: https://www.indiacode.nic.in/
Patients can seek civil remedies for negligence and compensation via courts or consumer forums.
[Summary]
Medical negligence claims are civil in nature with potential compensation.
""",

"electricity_act_compliance.txt":
"""Electricity Act | Licensing and consumer protections | source: https://www.indiacode.nic.in/
Framework for electricity supply, licensing, and consumer grievance redressal.
[Summary]
Regulatory structure for power distribution and consumer rights.
""",

"income_tax_evasion_penalty.txt":
"""Income Tax Act | Evasion penalties & prosecution | source: https://www.indiacode.nic.in/
Penalties and prosecution provisions for tax evasion and fraud.
[Summary]
Covers penalties and criminal liability for tax offences.
""",

"foreign_exchange_regulations_overview.txt":
"""FEMA | Foreign Exchange Management Act overview | source: https://www.indiacode.nic.in/
Regulates foreign exchange dealings and penalties for contravention.
[Summary]
Controls on foreign exchange transactions and penalties for violations.
""",

"public_interest_disclosure_whistleblower.txt":
"""Whistleblower Protections | Public interest disclosures and protections | source: https://www.indiacode.nic.in/
Measures for reporting corruption or malpractice and protections for whistleblowers.
[Summary]
Mechanisms for reporting wrongdoing and safeguards for reporters.
""",

"electoral_offences_overview.txt":
"""Representation of People Act | Electoral offences overview | source: https://www.indiacode.nic.in/
Corrupt practices, illegal conduct in elections and associated penalties.
[Summary]
Covers offences around elections and corrupt practices.
""",

"police_misconduct_complaints.txt":
"""Police Complaints & Oversight | Redressal for police misconduct | source: https://www.indiacode.nic.in/
Mechanisms exist to file complaints against police misconduct; state police complaint authorities may apply.
[Summary]
Options to complain about police excesses or procedural lapses.
""",

"human_rights_commission_overview.txt":
"""Human Rights Act | National and State Human Rights Commissions | source: https://www.indiacode.nic.in/
Commissions receive complaints of human rights violations and recommend remedies.
[Summary]
Non-judicial redressal forums for rights violations.
""",

"land_registration_property_rights.txt":
"""Registration Act & Transfer of Property | Property transfer and registration requirements | source: https://www.indiacode.nic.in/
Procedural requirements to register property transfers and remedies for disputes.
[Summary]
Registration formalities and legal effect on property rights.
""",

"partition_law_family_property.txt":
"""Partition & Succession | Division of family property and succession rules | source: https://www.indiacode.nic.in/
Rules for partition, inheritance and succession depend on personal laws and statutes.
[Summary]
Explains partition procedure and inheritance basics.
""",

"contract_act_17_fraud.txt":
"""Indian Contract Act Section 17 | Fraud | source: https://www.indiacode.nic.in/
Fraud vitiates consent in contracts; misrepresentation or deceit may allow rescission and damages.
[Summary]
Contractual remedies for fraud, misrepresentation, and consent vitiation.
""",

"consumer_misrepresentation_unfair_trade.txt":
"""Consumer Protection | Unfair trade practices & misleading advertisements | source: https://www.indiacode.nic.in/
Regulates false advertising and unfair trade practices with penalties.
[Summary]
Consumer protection against misrepresentation in trade.
""",

"gst_penalties_nonfiling.txt":
"""GST Act | Penalties for non-filing and evasion | source: https://www.indiacode.nic.in/
Outlines penalties for late filing, evasion, and fraudulent claims.
[Summary]
Consequences for non-compliance with GST obligations.
""",

"banking_fraud_nego_instruments.txt":
"""Banking Offences | Fraud and negotiated instruments | source: https://www.indiacode.nic.in/
Banking frauds and offences have specific criminal sanctions and regulatory remedies.
[Summary]
Covers bank fraud and instrument misuse.
""",

"service_provider_liability_online_platforms.txt":
"""Platform Liability | Online intermediary liability (IT Act) | source: https://www.indiacode.nic.in/
Intermediary liability rules set out takedown and safe-harbour conditions for platforms.
[Summary]
Explains when platforms are protected from liability and when they must act on complaints.
""",

"arson_and_damage_property.txt":
"""IPC Sections on Arson & Mischief | Damage to property | source: https://www.indiacode.nic.in/
Willful damage to property and arson are punishable under IPC’s mischief and related sections.
[Summary]
Covers property damage offences and related penalties.
""",

"hate_speech_and_communal_violence.txt":
"""Public Order & Hate Speech | Provisions controlling hate speech and incitement | source: https://www.indiacode.nic.in/
Speech that incites communal hatred or violence can be prosecuted under various provisions.
[Summary]
Prohibits incitement to violence and communal discord.
""",

"privacy_data_protection_note.txt":
"""Privacy, Data Protection & Personal Data Rules | Overview | source: https://www.indiacode.nic.in/
While a comprehensive Data Protection law is evolving, IT Act rules and other statutes regulate personal data handling.
[Summary]
Explains current privacy protections and potential statutory remedies.
""",

"traffic_offences_speeding_drunk_driving.txt":
"""Motor Vehicles Act | Traffic offences overview | source: https://www.indiacode.nic.in/
Traffic rules, penalties for speeding, drunk driving, and vehicle offences including license suspensions.
[Summary]
Road safety offences and penalties for drivers.
""",

"marriage_annulment_voidable_marriage.txt":
"""Family Law | Annulment and voidable marriages overview | source: https://www.indiacode.nic.in/
Grounds for annulment and distinctions between void and voidable marriages under personal laws.
[Summary]
Explains annulment and legal consequences for parties.
""",

"employment_minimum_wages_and_overtime.txt":
"""Labour Law | Minimum wages and overtime obligations | source: https://www.indiacode.nic.in/
Employers must pay minimum wages and overtime where applicable; enforcement mechanisms exist.
[Summary]
Worker rights for pay and overtime, and enforcement options.
""",

"consumer_electronic_refund_returns.txt":
"""Consumer Remedies | Refunds, returns and defective goods | source: https://www.indiacode.nic.in/
Procedures for returning defective goods and claiming refunds under consumer laws.
[Summary]
Consumer rights for defective product remedies.
""",

"evidence_chain_of_custody_forensics.txt":
"""Evidence & Forensics | Chain of custody rules | source: https://www.indiacode.nic.in/
Disciplines for collecting, preserving and presenting forensic evidence in courts.
[Summary]
Importance of chain-of-custody for admissible forensic evidence.
""",

"criminal_procedure_bail_types.txt":
"""Bail Types & Procedure | Regular, anticipatory and interim bail overview | source: https://www.indiacode.nic.in/
Procedure and principles for granting bail including factors courts consider.
[Summary]
Explains different bail types and judicial considerations.
""",

"terrorism_laws_unlawful_activities.txt":
"""UAPA & Terrorism Laws | Unlawful Activities (Prevention) Act overview | source: https://www.indiacode.nic.in/
Severe provisions for terrorism-related offences with special procedure; stringent bail rules.
[Summary]
Covers anti-terror laws and special procedural provisions.
""",

"cybercrime_phishing_and_fraud.txt":
"""Cybercrime Overview | Phishing, fraud and identity theft | source: https://www.indiacode.nic.in/
Phishing, identity theft, unauthorized access and financial cybercrimes are prosecutable under IT Act and IPC.
[Summary]
Common cybercrime types and applicable laws for prosecution.
"""
}

# create files
for fname, content in entries.items():
    fp = OUT / fname
    if not fp.exists():
        fp.write_text(content, encoding='utf-8')
        print("created", fp.name)
    else:
        print("exists", fp.name)

print("Done. Created/checked", len(entries), "files in", OUT)
