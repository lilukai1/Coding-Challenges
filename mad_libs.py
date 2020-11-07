# MadLibs - Practice Input and Output
#
# Template:
#    I enjoy practice! I find it helps me to __(verb)__ better.
#    Without practice, my __(noun)__ would probably not even work.
#    My code is getting more __(adjective)__ every single day!


# TODO: Prompt the user for parts of speech and store them in variables



# TODO: Output the template to the screen with the blanks filled out with what the user stated

template = "I enjoy practice! I find it helps me to __(verb)__ better.  Without practice, my __(noun)__ would probably not even work.  My code is getting more __(adjective)__ every single day!"
    
template_list = template.split(" ")
finished_mad_lib = ""

for word in template_list :
    if word.startswith("_"):
        word = word.strip("_")
        word = word.strip(")")
        word = word.strip("(")

        replacement = input(f"Please give me a {word}:")
        word = replacement
    finished_mad_lib += word + " "

print(finished_mad_lib)