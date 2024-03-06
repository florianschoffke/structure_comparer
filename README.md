# KBV and ePA Medication Profile Comparison

## Overview
This document provides a summary of the differences between the KBV E-Rezept profiles and the ePA Medication profile, as identified by the compare.py script. Additionally, a remark field is generated and adjusted to give advice for the mapping process.


## Hosted Results
The results of the comparison can be viewed directly through these hosted links:
- [KBV_PR_FOR_Organization in OrganizationDirectory](https://svensommer.github.io/structure_comparer/projects/erp/docs/OrganizationDirectory.html)
- [KBV_PR_FOR_Practitioner in PractitionerDirectory](https://svensommer.github.io/structure_comparer/projects/erp/docs/PractitionerDirectory.html)
- [KBV_PR_ERP_Prescription in EPAMedicationRequest](https://svensommer.github.io/structure_comparer/projects/erp/docs/EPAMedicationRequest.html)
- [KBV_PR_ERP_Medication_Compounding, KBV_PR_ERP_Medication_FreeText, KBV_PR_ERP_Medication_Ingredient, KBV_PR_ERP_Medication_PZN in EPAMedication](https://svensommer.github.io/structure_comparer/projects/erp/docs/EPAMedication.html)

## Web-App

This project provides a web app to configure the mapping between different profiles for different projects.

### Backend

Start the backend service from the repository root

```bash
python server.py --project-dir projects/<name>
```

The started service is available at `localhost:5000`. The OpenAPI specification is available with the route `/spec`.

#### REST Client

The service can be tested using a request collection in `rest/requests.http`. This file uses the extension _Rest Client_ (`humao.rest-client`).

Specify the `host` for the requests in setting like

```json
"rest-client.environmentVariables": {
    "local": {
        "host": "localhost:5000"
    }
}
```

A request can be performed by clicking _Send Request_ above the corresponding request.

### Frontend

TODO
