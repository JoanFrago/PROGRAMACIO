def list_benefits():
    return["Gorka likes big", "Marc likes small", "Unai likes medium", "Anas doesn't like"]

def build_sentence(info):
    return(info +(" cars"))
def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))
        
name_the_benefits_of_functions()