
def remove_duplicates(value):
    output =[]
    for x in value:
        if x in output:
            pass
        else:
            output.append(x)
    result="".join(output)
    return result
    


print(remove_duplicates("11223445566666ababzzz@@@123#*#*"))
