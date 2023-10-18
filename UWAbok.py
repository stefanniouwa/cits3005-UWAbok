from rdflib import Graph, Namespace, RDF, RDFS, XSD, Literal
import json

# Create an RDF Graph
g = Graph()

# Define your namespace
uwabok = Namespace("http://example.org/uwabok#")

# Bind it to the graph
g.bind("uwabok", uwabok)

# Define RDF Classes
g.add((uwabok.Unit, RDF.type, RDFS.Class))
g.add((uwabok.Major, RDF.type, RDFS.Class))
g.add((uwabok.Assessment, RDF.type, RDFS.Class))
g.add((uwabok.Prerequisite, RDF.type, RDFS.Class))

g.add((uwabok.UnitPrereq, RDF.type, RDFS.Class))
g.add((uwabok.MajorPrereq, RDF.type, RDFS.Class))


# Define subclass relationships
g.add((uwabok.Unit, RDFS.subClassOf, RDFS.Resource))
g.add((uwabok.Major, RDFS.subClassOf, RDFS.Resource))
g.add((uwabok.Assessment, RDFS.subClassOf, RDFS.Resource))
g.add((uwabok.Prerequisite, RDFS.subClassOf, RDFS.Resource))
g.add((uwabok.UnitPrereq, RDFS.subClassOf, uwabok.Prerequisite))
g.add((uwabok.MajorPrereq, RDFS.subClassOf, uwabok.Prerequisite))

# Define properties for Units
g.add((uwabok.hasUnitCode, RDF.type, RDF.Property))
g.add((uwabok.hasTitle, RDF.type, RDF.Property))
g.add((uwabok.hasLevel, RDF.type, RDF.Property))
g.add((uwabok.hasDescription, RDF.type, RDF.Property))
g.add((uwabok.hasOutcomes, RDF.type, RDF.Property))
g.add((uwabok.hasCreditPoints, RDF.type, RDF.Property))
g.add((uwabok.hasAssessments, RDF.type, RDF.Property))
g.add((uwabok.hasPrerequisites, RDF.type, RDF.Property))
g.add((uwabok.hasUnitPrereqText, RDF.type, RDF.Property))
g.add((uwabok.hasUnitPrereqCNF, RDF.type, RDF.Property))
g.add((uwabok.hasContactHours, RDF.type, RDF.Property))

# Define properties for Majors
g.add((uwabok.hasMajorCode, RDF.type, RDF.Property))
g.add((uwabok.hasMajorTitle, RDF.type, RDF.Property))
g.add((uwabok.hasMajorDescription, RDF.type, RDF.Property))
g.add((uwabok.hasMajorOutcomes, RDF.type, RDF.Property))
g.add((uwabok.hasMajorPrereqText, RDF.type, RDF.Property))
g.add((uwabok.hasMajorUnits, RDF.type, RDF.Property))
g.add((uwabok.hasMajorCourses, RDF.type, RDF.Property))
g.add((uwabok.hasBridgingCourses, RDF.type, RDF.Property))

# Define properties for Assessments
g.add((uwabok.hasProjectAssessment, RDF.type, RDF.Property))
g.add((uwabok.hasExamAssessment, RDF.type, RDF.Property))
g.add((uwabok.hasReportAssessment, RDF.type, RDF.Property))
g.add((uwabok.hasPresentationAssessment, RDF.type, RDF.Property))
g.add((uwabok.hasOtherAssessments, RDF.type, RDF.Property))


# Define domain and range relationships
# For example, the following relationships assume that these properties apply to classes specified.
g.add((uwabok.hasUnitCode, RDFS.domain, uwabok.Unit))
g.add((uwabok.hasTitle, RDFS.domain, uwabok.Unit))
g.add((uwabok.hasLevel, RDFS.domain, uwabok.Unit))
g.add((uwabok.hasDescription, RDFS.domain, uwabok.Unit))
g.add((uwabok.hasOutcomes, RDFS.domain, uwabok.Unit))
g.add((uwabok.hasCreditPoints, RDFS.domain, uwabok.Unit))
g.add((uwabok.hasAssessments, RDFS.domain, uwabok.Unit))
g.add((uwabok.hasPrerequisites, RDFS.domain, uwabok.Unit))
g.add((uwabok.hasUnitPrereqText, RDFS.domain, uwabok.UnitPrereq))
g.add((uwabok.hasUnitPrereqCNF, RDFS.domain, uwabok.UnitPrereq))
g.add((uwabok.hasMajorCode, RDFS.domain, uwabok.Major))
g.add((uwabok.hasMajorTitle, RDFS.domain, uwabok.Major))
g.add((uwabok.hasMajorDescription, RDFS.domain, uwabok.Major))
g.add((uwabok.hasMajorOutcomes, RDFS.domain, uwabok.Major))
g.add((uwabok.hasMajorPrereqText, RDFS.domain, uwabok.MajorPrereq))
g.add((uwabok.hasMajorUnits, RDFS.domain, uwabok.Major))
g.add((uwabok.hasMajorCourses, RDFS.domain, uwabok.Major))
g.add((uwabok.hasBridgingCourses, RDFS.domain, uwabok.Major))
g.add((uwabok.hasProjectAssessment, RDFS.domain, uwabok.Assessment))


# Define range relationships
g.add((uwabok.hasUnitCode, RDFS.range, XSD.string))
g.add((uwabok.hasTitle, RDFS.range, XSD.string))
g.add((uwabok.hasLevel, RDFS.range, XSD.string))
g.add((uwabok.hasDescription, RDFS.range, XSD.string))
g.add((uwabok.hasOutcomes, RDFS.range, XSD.string))
g.add((uwabok.hasCreditPoints, RDFS.range, XSD.integer))
g.add((uwabok.hasAssessments, RDFS.range, uwabok.Assessment))
g.add((uwabok.hasPrerequisites, RDFS.range, uwabok.Prerequisite))
g.add((uwabok.hasUnitPrereqText, RDFS.range, XSD.string))
g.add((uwabok.hasUnitPrereqCNF, RDFS.range, uwabok.Unit))
g.add((uwabok.hasMajorCode, RDFS.range, XSD.string))
g.add((uwabok.hasMajorTitle, RDFS.range, XSD.string))
g.add((uwabok.hasMajorDescription, RDFS.range, XSD.string))
g.add((uwabok.hasMajorOutcomes, RDFS.range, XSD.string))
g.add((uwabok.hasMajorPrereqText, RDFS.range, XSD.string))
g.add((uwabok.hasMajorUnits, RDFS.range, uwabok.Unit))
g.add((uwabok.hasMajorCourses, RDFS.range, XSD.string))
g.add((uwabok.hasBridgingCourses, RDFS.range, XSD.string))
g.add((uwabok.hasProjectAssessment, RDFS.range, XSD.string))


# This is 2 examples of Units from units.json
# "DENT6870": {
#     "code": "DENT6870",
#     "title": "Oral Pathology Theory I Part 1",
#     "school": "Dental School",
#     "board_of_examiners": "06 - Health",
#     "delivery_mode": "",
#     "level": "6",
#     "description": "This is the first-year theory unit in Oral Pathology in the Doctor of Clinical DentiXSD.string
#y course. The unit is taken over two semesters and parts 1 and 2 must be completed to fulfil the requirements of the unit. Topics are covered via seminars and literature reviews, at a basic level during the early stages of the course and with increasing complexity throughout the course. The material covered depends on the needs of the individual student, the work previously performed in the course, the clinical needs of patients being treated by the student, and the relevance to current literature in oral medicine.",
#     "credit": "6",
#     "offering": {},
#     "outcomes": [
#         " evaluate, synthesise and apply the literature and diagnostic techniques relevant to generall and oral pathology.",
#         " demonXSD.string
#ate advanced problem solving and diagnostic skills",
#         " demonXSD.string
#ate an in-depth knowledge of oral pathology through discussion, interpretation and evaluation in written and oral presentations",
#         " interpret original research",
#         " define and demonXSD.string
#ate the responsibility of being a practitioner in oral pathology",
#         " provide clinical leadership",
#         " use effective communication skills with colleagues, patients and the broader community."
#     ],
#     "assessment": [
#         " oral exam ",
#         " case Based ",
#         " written examination"
#     ],
#     "prerequisites_text": "a Bachelor of Dental Science of this University or equivalent.a Pass in the primary examinations of the Royal AuXSD.string
#alasian College of Dental Surgeons or equivalent.and at least two years' full-time equivalent experience in general dental practice",
#     "prerequisites_cnf": [],
#     "contact": {
#         "seminars": "4"
#     },
#     "note": "Students are required to be registered with the Dental Board of AuXSD.string
#alia for the duration of the Doctor of Clinical DentiXSD.string
#y (90840)."
# },
# "DENT6871": {
#     "code": "DENT6871",
#     "title": "Oral Pathology Theory I Part 2",
#     "school": "Dental School",
#     "board_of_examiners": "06 - Health",
#     "delivery_mode": "",
#     "level": "6",
#     "description": "This is the first-year theory unit in Oral Pathology in the Doctor of Clinical DentiXSD.string
#y course. The unit is taken over two semesters and parts 1 and 2 must be completed to fulfill the requirements of the unit. Topics are covered via seminars, literature reviews, journal clubs, clinic-pathologic conferences, and clinical laboratory sessions, at a basic level during the early stages of the course and with increasing complexity throughout the course. This course will focus on the fundamentals of general pathology, and oral pathology.",
#     "credit": "6",
#     "offering": {},
#     "outcomes": [
#         " evaluate, synthesise and apply the literature relevant to oral pathology and biology",
#         " demonXSD.string
#ate advanced problem solving and diagnostic skills",
#         " demonXSD.string
#ate an in-depth knowledge of oral pathology through discussion, interpretation and evaluation in written and oral presentations",
#         " interpret original research",
#         " define and demonXSD.string
#ate the responsibility of being a practitioner in oral pathology",
#         " provide clinical leadership",
#         " use effective communication skills with colleagues, patients and the broader community."
#     ],
#     "assessment": [
#         " oral exam ",
#         " case based ",
#         " written examination"
#     ],
#     "prerequisites_text": "a Bachelor of Dental Science of this University or equivalent.a Pass in the primary examinations of the Royal AuXSD.string
#alasian College of Dental Surgeons or equivalent.and at least two years' full-time equivalent experience in general dental practice",
#     "prerequisites_cnf": [],
#     "contact": {
#         "lectures/seminars": "6"
#     },
#     "note": "Students are required to be registered with the Dental Board of AuXSD.string
#alia for the duration of the Doctor of Clinical DentiXSD.string
#y (90840)."
# },

# i am going to load the json file and then iterate through the units and add them to the graph
# Load the JSON data from your file
with open('Units.json', 'r') as json_file:
    units_data = json.load(json_file)

# Iterate through the units and add them to the RDF graph
for unit_code, unit_info in units_data.items():
    unit_uri = uwabok[unit_code]

    # Add type information for the unit
    g.add((unit_uri, RDF.type, uwabok.Unit))

    # Add properties and their values
    g.add((unit_uri, uwabok.hasUnitCode, Literal(unit_info['code'])))
    g.add((unit_uri, uwabok.hasTitle, Literal(unit_info['title'])))
    g.add((unit_uri, uwabok.hasLevel, Literal(unit_info['level'], datatype=XSD.integer)))
    g.add((unit_uri, uwabok.hasDescription, Literal(unit_info['description'])))

    # Outcomes as a list of literals
    for outcome in unit_info['outcomes']:
        g.add((unit_uri, uwabok.hasOutcomes, Literal(outcome)))

    g.add((unit_uri, uwabok.hasCreditPoints, Literal(unit_info['credit'], datatype=XSD.integer)))

    # Assessments as a list of literals
    for assessment in unit_info['assessment']:
        g.add((unit_uri, uwabok.hasAssessments, Literal(assessment)))

   # Prerequisites text
    prerequisite_text = unit_info['prerequisites_text']
    if prerequisite_text:
        g.add((unit_uri, uwabok.hasUnitPrereqText, Literal(prerequisite_text)))

    # Prerequisites cnf
    for prerequisite_cnf in unit_info['prerequisites_cnf']:
        for prerequisite_unit in prerequisite_cnf:
            if prerequisite_unit:
                # Create a URI for the prerequisite unit (if it's not an empty string)
                prereq_unit_uri = uwabok[prerequisite_unit]
                g.add((unit_uri, uwabok.hasPrerequisites, prereq_unit_uri))
                g.add((prereq_unit_uri, RDF.type, uwabok.Unit))

# Add additional subclass, subproperty, domain, and range relationships as needed
    # Contact Hours
    contact_hours = unit_info.get('contact', {})  # Get the contact hours data

    # Calculate the total contact hours
    total_contact_hours = 0
    for contact_type, hours in contact_hours.items():
        try:
            total_contact_hours += int(hours)
        except ValueError:
            pass  # Handle non-integer values gracefully

    g.add((unit_uri, uwabok.hasContactHours, Literal(total_contact_hours, datatype=XSD.integer)))

# Serialize the RDF graph to a file
g.serialize("uwaBOK.rdf")
