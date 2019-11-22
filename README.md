# FAPIIS as a Service

The federal government maintains a database entitled "Federal Awardee Performance and Integrity Information System", which goes by the delightful acronym "FAPIIS". It's one of the three systems that Contracting Officers [need to look at](https://www.acquisition.gov/content/9104-6-federal-awardee-performance-and-integrity-information-system) when making an award decision for contracts above the simplified-acquistion threshold. It includes information about the following:

1. Terminations for Default
2. Terminations for Cause
3. Terminations for Material Failure to Comply
4. Non-Responsibility Determinations
5. Recipient Not Qualified Determinations
6. Defective Pricing Determinations
7. Administrative Agreements
8. DoD Determinations of Contractor Fault reported to FAPIIS by federal government personnel.
9. Subcontractor Payment Issues
10. Trafficking in Persons

Given that, a web service might be nice to have, right? Ok. Let's make one!

## Setup and Usage

I use [poetry](https://poetry.eustace.io/) to handle the dependencies and virtual environment.

```
git clone
cd fapiis-service
poetry install
poetry run python main.py
```

Once you're done, now you have a file called `fapiis.json`. Eventually, I'll build the Flask app that serves this data. But for now, it's just a JSON file.

## Roadmap

- Probably a REST API that allows for faceted search.
- Ideally, record-level information (i.e., get the PDFs and the other information), which would come from crawling the links and getting more detailed information.
