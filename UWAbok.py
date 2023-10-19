from rdflib import Graph, Namespace, RDF, RDFS, XSD, Literal
from pyshacl import validate
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

# Define subclass relationships
g.add((uwabok.Unit, RDFS.subClassOf, RDFS.Resource))
g.add((uwabok.Major, RDFS.subClassOf, RDFS.Resource))

# Define properties for Units
g.add((uwabok.hasUnitCode, RDF.type, RDF.Property))
g.add((uwabok.hasTitle, RDF.type, RDF.Property))
g.add((uwabok.hasLevel, RDF.type, RDF.Property))
g.add((uwabok.hasDescription, RDF.type, RDF.Property))
g.add((uwabok.hasOutcomes, RDF.type, RDF.Property))
g.add((uwabok.hasCreditPoints, RDF.type, RDF.Property))
g.add((uwabok.hasAssessments, RDF.type, RDF.Property))
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

# Define domain and range relationships
# For example, the following relationships assume that these properties apply to classes specified.
g.add((uwabok.hasUnitCode, RDFS.domain, uwabok.Unit))
g.add((uwabok.hasTitle, RDFS.domain, uwabok.Unit))
g.add((uwabok.hasLevel, RDFS.domain, uwabok.Unit))
g.add((uwabok.hasDescription, RDFS.domain, uwabok.Unit))
g.add((uwabok.hasOutcomes, RDFS.domain, uwabok.Unit))
g.add((uwabok.hasCreditPoints, RDFS.domain, uwabok.Unit))
g.add((uwabok.hasAssessments, RDFS.domain, uwabok.Unit))
g.add((uwabok.hasUnitPrereqText, RDFS.domain, uwabok.Unit))
g.add((uwabok.hasUnitPrereqCNF, RDFS.domain, uwabok.Unit))
g.add((uwabok.hasContactHours, RDFS.domain, uwabok.Unit))
g.add((uwabok.hasMajorCode, RDFS.domain, uwabok.Major))
g.add((uwabok.hasMajorTitle, RDFS.domain, uwabok.Major))
g.add((uwabok.hasMajorDescription, RDFS.domain, uwabok.Major))
g.add((uwabok.hasMajorOutcomes, RDFS.domain, uwabok.Major))
g.add((uwabok.hasMajorPrereqText, RDFS.domain, uwabok.Major))
g.add((uwabok.hasMajorUnits, RDFS.domain, uwabok.Major))
g.add((uwabok.hasMajorCourses, RDFS.domain, uwabok.Major))
g.add((uwabok.hasBridgingCourses, RDFS.domain, uwabok.Major))



# Define range relationships
g.add((uwabok.hasUnitCode, RDFS.range, XSD.string))
g.add((uwabok.hasTitle, RDFS.range, XSD.string))
g.add((uwabok.hasLevel, RDFS.range, XSD.string))
g.add((uwabok.hasDescription, RDFS.range, XSD.string))
g.add((uwabok.hasOutcomes, RDFS.range, XSD.string))
g.add((uwabok.hasCreditPoints, RDFS.range, XSD.integer))
g.add((uwabok.hasAssessments, RDFS.range, XSD.string))
g.add((uwabok.hasUnitPrereqText, RDFS.range, XSD.string))
g.add((uwabok.hasUnitPrereqCNF, RDFS.range, uwabok.Unit))
g.add((uwabok.hasContactHours, RDFS.range, XSD.integer))
g.add((uwabok.hasMajorCode, RDFS.range, XSD.string))
g.add((uwabok.hasMajorTitle, RDFS.range, XSD.string))
g.add((uwabok.hasMajorDescription, RDFS.range, XSD.string))
g.add((uwabok.hasMajorOutcomes, RDFS.range, XSD.string))
g.add((uwabok.hasMajorPrereqText, RDFS.range, XSD.string))
g.add((uwabok.hasMajorUnits, RDFS.range, uwabok.Unit))
g.add((uwabok.hasMajorCourses, RDFS.range, XSD.string))
g.add((uwabok.hasBridgingCourses, RDFS.range, XSD.string))


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
                g.add((unit_uri, uwabok.hasUnitPrereqCNF, prereq_unit_uri))
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

# Load the JSON data from your file
# Load the JSON data from your Majors file
with open('Majors.json', 'r') as json_file:
    majors_data = json.load(json_file)

# Iterate through the majors and add them to the RDF graph
for major_code, major_info in majors_data.items():
    major_uri = uwabok[major_code]

    # Add type information for the major
    g.add((major_uri, RDF.type, uwabok.Major))

    # Add properties and their values for the major
    g.add((major_uri, uwabok.hasMajorCode, Literal(major_info['code'])))
    g.add((major_uri, uwabok.hasMajorTitle, Literal(major_info['title'])))
    g.add((major_uri, uwabok.hasMajorDescription,
          Literal(major_info['description'])))

    # Outcomes as a list of literals
    for outcome in major_info['outcomes']:
        g.add((major_uri, uwabok.hasMajorOutcomes, Literal(outcome)))

    # Prerequisites for the major (assuming it's a text value)
    prerequisites_text = major_info.get('prerequisites', "")
    if prerequisites_text:
        g.add((major_uri, uwabok.hasMajorPrereqText, Literal(prerequisites_text)))

    # List of courses required for the major
    courses = major_info.get('courses', [])
    for course in courses:
        g.add((major_uri, uwabok.hasMajorCourses, Literal(course)))

    # List of bridging courses (if applicable)
    bridging_courses = major_info.get('bridging', [])
    for course in bridging_courses:
        g.add((major_uri, uwabok.hasBridgingCourses, Literal(course)))

    # List of units associated with the major
    units = major_info.get('units', [])
    for unit in units:
        # Assuming each unit is represented as a string, create URIs for the units if they don't already exist
        unit_uri = uwabok[unit]
        g.add((unit_uri, RDF.type, uwabok.Unit))
        # Create a relationship between the major and the unit
        g.add((major_uri, uwabok.hasMajorUnits, unit_uri))

# Add SHACL constraints
shacl_graph = Graph()
shacl_graph.parse("UWAbok_constraints.ttl", format="turtle")

# Validate the data graph against the SHACL constraints
conforms, results_graph, results_text = validate(g, shacl_graph=shacl_graph, data_graph_format="turtle", shacl_graph_format="turtle", inference="rdfs")

# Print validation results
print(results_text)
# Serialize the RDF graph to a file
g.serialize("uwaBOK.rdf")
