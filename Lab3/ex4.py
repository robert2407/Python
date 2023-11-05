def xml(tag, content, **elements):    # folosit ca sa tratam acel elem. ca un dictionar
    xml_element = f"<{tag}"         # string formatat, incep cu tagul

    for key, value in elements.items():     #transf dict in lista de tuple ca sa pot itera prin el
        xml_element += f' {key}="{value}"'

    xml_element += f">{content}</{tag}>"        #inchidem stringul formatat

    return xml_element

if __name__ == "__main__":
    result = xml("a", "Hello there", href="http://python.org", _class="my-link", id="someid")
    print(result)
