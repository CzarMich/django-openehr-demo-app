"""
Views for our Django openEHR demo app
"""
from django.db import transaction
from django.forms import formset_factory
from django.shortcuts import render, redirect

from django_openehr_demo.forms import (
    AdmissionForm,
    AllergiesForm,
    ClinicalSynopsisForm,
    DemographicProfessionalForm,
    ProblemDiagnosisSummaryForm,
    ProblemsIssuesForm,
    ReasonForEncounterForm,
    RelevantContactForm,
)


def transfer_care(request):

    AdmissionFormset = formset_factory(AdmissionForm)
    AllergiesFormset = formset_factory(AllergiesForm)
    ClinicalSynopsisFormset = formset_factory(ClinicalSynopsisForm)
    DemographicProfessionalFormset = formset_factory(DemographicProfessionalForm)
    ProblemDiagnosisSummaryFormset = formset_factory(ProblemDiagnosisSummaryForm)
    ProblemsIssuesFormset = formset_factory(ProblemsIssuesForm)
    ReasonForEncounterFormSet = formset_factory(ReasonForEncounterForm)
    RelevantContactFormset = formset_factory(RelevantContactForm)

    if request.method == 'POST':
        admission_formset = AdmissionFormset(request.POST, request.FILES, prefix='admissions')
        allergies_formset = AllergiesFormset(request.POST, request.FILES, prefix='allergies')
        clinical_synopsis_formset = ClinicalSynopsisFormset(request.POST, request.FILES, prefix='clinsynopsis')
        demographic_professional_formset = DemographicProfessionalFormset(request.POST, request.FILES, prefix='demoprof')
        problem_diagnosis_formset = ProblemDiagnosisSummaryFormset(request.POST, request.FILES, prefix='probdiag')
        problems_issues_formset = ProblemsIssuesFormset(request.POST, request.FILES, prefix='probissue')
        relevant_contact_formset = RelevantContactFormset(request.POST, request.FILES, prefix='relevantcontacts')
        reason_for_encounter_formset = ReasonForEncounterFormSet(request.POST, request.FILES, prefix='reasonforenc')

        to_save = [
            admission_formset,
            allergies_formset,
            clinical_synopsis_formset,
            demographic_professional_formset,
            problem_diagnosis_formset,
            problems_issues_formset,
            relevant_contact_formset,
            reason_for_encounter_formset,
        ]


        if clinical_synopsis_formset.is_valid():
            with transaction.atomic():
                for form in clinical_synopsis_formset:
                    form.save()
                return redirect('/my-new-url/')
        else:
            pass # Something is invalid. If we just let the call to
        # render() below handle this, it will take the POSTed data
        # and display it in the form along with any error messages.

    else:
        admission_formset = AdmissionFormset(prefix='admissions')
        allergies_formset = AllergiesFormset(prefix='allergies')
        clinical_synopsis_formset = ClinicalSynopsisFormset(prefix='clinsynopsis')
        demographic_professional_formset = DemographicProfessionalFormset(prefix='demoprof')
        problem_diagnosis_formset = ProblemDiagnosisSummaryFormset(prefix='probdiag')
        problems_issues_formset = ProblemsIssuesFormset(prefix='probissue')
        reason_for_encounter_formset = ReasonForEncounterFormSet(prefix='reasonforenc')
        relevant_contact_formset = RelevantContactFormset(prefix='relevantcontacts')

    return render(request, 'transfer_care.html', {
        'admission_formset': admission_formset,
        'allergies_formset': allergies_formset,
        'clinical_synopsis_formset': clinical_synopsis_formset,
        'demographic_professional_formset': demographic_professional_formset,
        'problem_diagnosis_formset': problem_diagnosis_formset,
        'problems_issues_formset': problems_issues_formset,
        'reason_for_encounter_formset': reason_for_encounter_formset,
        'relevant_contact_formset': relevant_contact_formset,
    })
