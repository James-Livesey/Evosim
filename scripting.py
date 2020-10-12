inputsToProcess = []

def processScript(source):
    sourceFile = open(source, "r")
    sourceCode = sourceFile.read()
    
    sourceFile.close()

    parsedInputsToProcess = [""]
    inComment = False

    for character in sourceCode:
        if character == "#":
            inComment = True
        elif character == "\n":
            inComment = False

            parsedInputsToProcess.append("")
        elif inComment:
            pass
        elif character in [":", ",", ";"]:
            parsedInputsToProcess.append("")
        else:
            parsedInputsToProcess[-1] += character

    for inputText in parsedInputsToProcess:
        inputText = inputText.strip()

        if inputText != "":
            if inputText == "$":
                inputsToProcess.append("")
            else:
                inputsToProcess.append(inputText)