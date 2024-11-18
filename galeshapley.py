def nrmp_matching(applicants_preferences, hospitals_preferences, hospital_slots):
    # Initialize all applicants as free and track their proposals
    free_applicants = list(applicants_preferences.keys())
    engaged_pairs = {hospital: [] for hospital in hospitals_preferences}  # List to handle multiple slots

    # Track proposals made by each applicant
    proposals = {applicant: [] for applicant in applicants_preferences}

    while free_applicants:
        applicant = free_applicants[0]  # Pick the first free applicant
        applicant_prefers = applicants_preferences[applicant]

        # Find the highest-ranked hospital they have not yet applied to
        for hospital in applicant_prefers:
            if hospital not in proposals[applicant]:
                proposals[applicant].append(hospital)

                # If hospital has a free slot, engage them
                if len(engaged_pairs[hospital]) < hospital_slots[hospital]:
                    engaged_pairs[hospital].append(applicant)
                    free_applicants.remove(applicant)
                    break
                else:
                    # hospital is full; check if it prefers this new applicant
                    hospital_prefers = hospitals_preferences[hospital]
                    current_applicants = engaged_pairs[hospital]

                    # Find the least preferred applicant currently matched to this hospital
                    worst_applicant = max(current_applicants, key=lambda x: hospital_prefers.index(x))

                    # If the new applicant is preferred over the worst current applicant, switch them
                    if hospital_prefers.index(applicant) < hospital_prefers.index(worst_applicant):
                        engaged_pairs[hospital].remove(worst_applicant)
                        engaged_pairs[hospital].append(applicant)
                        free_applicants.append(worst_applicant)
                        free_applicants.remove(applicant)
                        break

    return engaged_pairs
